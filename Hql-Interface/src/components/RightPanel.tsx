import { useEffect } from 'react'
import { useAppDispatch, useAppState } from '../state/store'
import { DetectionsSidebar } from './DetectionsSidebar'
import { RowInspector } from './RowInspector'

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
        <aside className="w-96 shrink-0 border-l border-gruvbox-light-bg2 dark:border-gruvbox-dark-bg2">
          <RowInspector row={row} onClose={() => dispatch({ type: 'closeInspector' })} />
        </aside>
      )
    }
  }

  return (
    <aside className="w-72 shrink-0 border-l border-gruvbox-light-bg2 dark:border-gruvbox-dark-bg2">
      <DetectionsSidebar />
    </aside>
  )
}
