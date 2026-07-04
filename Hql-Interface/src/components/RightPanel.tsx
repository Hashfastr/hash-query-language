import { useEffect, useRef, useState, type ReactNode } from 'react'
import { useAppDispatch, useAppState } from '../state/store'
import { DetectionsSidebar } from './DetectionsSidebar'
import { RowInspector } from './RowInspector'

const MIN_WIDTH = 220

// Panel widths are stored under their own localStorage keys, per mode
// (inspector vs detections), NOT inside the versioned persist.ts blob:
// a persistence schema bump shouldn't reset someone's panel layout.
function loadWidth(key: string, fallback: number): number {
  const v = Number(localStorage.getItem(key))
  return Number.isFinite(v) && v >= MIN_WIDTH ? v : fallback
}

function ResizablePanel({
  storageKey,
  defaultWidth,
  children,
}: {
  storageKey: string
  defaultWidth: number
  children: ReactNode
}) {
  const [width, setWidth] = useState(() => loadWidth(storageKey, defaultWidth))
  const widthRef = useRef(width)
  widthRef.current = width

  // Re-read when switching between panel modes (different storageKey)
  useEffect(() => {
    setWidth(loadWidth(storageKey, defaultWidth))
  }, [storageKey, defaultWidth])

  const startDrag = (e: React.PointerEvent<HTMLDivElement>) => {
    e.preventDefault()
    const handle = e.currentTarget
    const startX = e.clientX
    const startW = widthRef.current
    handle.setPointerCapture(e.pointerId)

    const clamp = (w: number) =>
      Math.min(Math.max(w, MIN_WIDTH), Math.round(window.innerWidth * 0.7))

    const move = (ev: PointerEvent) => setWidth(clamp(startW + startX - ev.clientX))
    const up = () => {
      handle.removeEventListener('pointermove', move)
      localStorage.setItem(storageKey, String(widthRef.current))
    }
    handle.addEventListener('pointermove', move)
    handle.addEventListener('pointerup', up, { once: true })
  }

  return (
    <aside
      style={{ width }}
      className="relative flex shrink-0 border-l border-gruvbox-light-bg2 dark:border-gruvbox-dark-bg2"
    >
      <div
        onPointerDown={startDrag}
        title="Drag to resize"
        className="absolute inset-y-0 -left-1 z-10 w-2 cursor-col-resize hover:bg-gruvbox-light-bg3/50 dark:hover:bg-gruvbox-dark-bg3/50"
      />
      <div className="min-w-0 flex-1 overflow-hidden">{children}</div>
    </aside>
  )
}

export function RightPanel() {
  const state = useAppState()
  const dispatch = useAppDispatch()
  const { rightPanel } = state

  useEffect(() => {
    if (rightPanel.mode !== 'row') return
    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'Escape') dispatch({ type: 'closeInspector' })
    }
    window.addEventListener('keydown', onKey)
    return () => window.removeEventListener('keydown', onKey)
  }, [rightPanel.mode, dispatch])

  if (state.sidebarCollapsed) return null

  if (rightPanel.mode === 'row') {
    const tab = state.tabs.find((t) => t.id === rightPanel.tabId)
    const row = tab?.run.results?.data[rightPanel.table]?.[rightPanel.rowIndex]
    if (row !== undefined) {
      return (
        <ResizablePanel storageKey="hql-interface:inspector-width" defaultWidth={384}>
          <RowInspector row={row} onClose={() => dispatch({ type: 'closeInspector' })} />
        </ResizablePanel>
      )
    }
  }

  return (
    <ResizablePanel storageKey="hql-interface:detections-width" defaultWidth={288}>
      <DetectionsSidebar />
    </ResizablePanel>
  )
}
