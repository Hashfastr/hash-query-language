import { useState } from 'react'
import { useAppDispatch, useAppState } from '../state/store'

export function QueryTabs() {
  const { tabs, activeTabId } = useAppState()
  const dispatch = useAppDispatch()
  const [editingId, setEditingId] = useState<string | null>(null)

  return (
    <div className="flex items-center gap-1 overflow-x-auto min-w-0">
      {tabs.map((tab) => {
        const active = tab.id === activeTabId
        return (
          <div
            key={tab.id}
            className={`group flex items-center gap-1 px-2 py-1 rounded-t text-sm cursor-pointer whitespace-nowrap border-b-2 ${
              active
                ? 'border-gruvbox-light-orange dark:border-gruvbox-dark-orange bg-gruvbox-light-bg1 dark:bg-gruvbox-dark-bg1'
                : 'border-transparent hover:bg-gruvbox-light-bg1 dark:hover:bg-gruvbox-dark-bg1'
            }`}
            onClick={() => dispatch({ type: 'setActiveTab', tabId: tab.id })}
            onDoubleClick={() => setEditingId(tab.id)}
          >
            {editingId === tab.id ? (
              <input
                autoFocus
                className="w-24 bg-transparent outline-none border-b border-gruvbox-light-gray dark:border-gruvbox-dark-gray"
                defaultValue={tab.title}
                onBlur={(e) => {
                  const title = e.target.value.trim()
                  if (title) dispatch({ type: 'renameTab', tabId: tab.id, title })
                  setEditingId(null)
                }}
                onKeyDown={(e) => {
                  if (e.key === 'Enter') e.currentTarget.blur()
                  if (e.key === 'Escape') setEditingId(null)
                }}
              />
            ) : (
              <span>{tab.title}</span>
            )}
            {tab.run.status === 'running' && (
              <span className="text-gruvbox-light-yellow dark:text-gruvbox-dark-yellow">●</span>
            )}
            {tabs.length > 1 && (
              <button
                className="opacity-0 group-hover:opacity-100 hover:text-gruvbox-light-red dark:hover:text-gruvbox-dark-red"
                onClick={(e) => {
                  e.stopPropagation()
                  dispatch({ type: 'closeTab', tabId: tab.id })
                }}
                title="Close tab"
              >
                ×
              </button>
            )}
          </div>
        )
      })}
      <button
        className="px-2 py-1 text-sm rounded hover:bg-gruvbox-light-bg1 dark:hover:bg-gruvbox-dark-bg1"
        onClick={() => dispatch({ type: 'addTab' })}
        title="New tab"
      >
        +
      </button>
    </div>
  )
}
