import { useEffect, type ReactNode } from 'react'
import { useDragResize } from '../hooks/useDragResize'
import { useAppDispatch, useAppState } from '../state/store'
import { DetectionsSidebar } from './DetectionsSidebar'
import { RowInspector } from './RowInspector'

// Width is remembered per mode (inspector vs detections) so a wide breakout
// doesn't force a wide detections list.
function ResizablePanel({
  storageKey,
  defaultWidth,
  children,
}: {
  storageKey: string
  defaultWidth: number
  children: ReactNode
}) {
  const { size, startDrag } = useDragResize({
    storageKey,
    defaultSize: defaultWidth,
    min: 220,
    max: () => Math.round(window.innerWidth * 0.7),
    axis: 'x',
    direction: -1, // panel sits on the right; dragging left grows it
  })

  return (
    <aside
      style={{ width: size }}
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
