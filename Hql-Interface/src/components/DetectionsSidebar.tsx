import { useEffect, useState } from 'react'
import { useDetections } from '../hooks/useDetections'
import { useAppDispatch, useAppState } from '../state/store'
import * as api from '../services/api'

const levelColor: Record<string, string> = {
  critical: 'text-gruvbox-light-red dark:text-gruvbox-dark-red',
  high: 'text-gruvbox-light-orange dark:text-gruvbox-dark-orange',
  medium: 'text-gruvbox-light-yellow dark:text-gruvbox-dark-yellow',
  low: 'text-gruvbox-light-aqua dark:text-gruvbox-dark-aqua',
}

export function DetectionsSidebar() {
  const { detections } = useAppState()
  const dispatch = useAppDispatch()
  const { reload } = useDetections()
  const [filter, setFilter] = useState('')

  useEffect(() => {
    void reload()
  }, [reload])

  const open = async (id: string | undefined, title: string | undefined) => {
    if (!id) return
    try {
      const det = await api.getDetection(id)
      dispatch({ type: 'addTab', query: det.hql, title: title ?? id })
    } catch {
      // detection body unavailable; nothing to open
    }
  }

  const q = filter.toLowerCase()
  const items = detections.items.filter(
    (d) =>
      !q ||
      d.title?.toLowerCase().includes(q) ||
      d.description?.toLowerCase().includes(q) ||
      d.author?.toLowerCase().includes(q),
  )

  return (
    <div className="flex h-full flex-col">
      <div className="flex items-center gap-1 border-b border-gruvbox-light-bg2 dark:border-gruvbox-dark-bg2 px-2 py-1">
        <span className="text-sm font-semibold">Detections</span>
        <span className="text-xs text-gruvbox-light-gray dark:text-gruvbox-dark-gray">
          {detections.items.length}
        </span>
        <div className="flex-1" />
        <button className="btn" title="Refresh" onClick={() => void reload()}>
          ↻
        </button>
      </div>
      <input
        className="mx-2 my-1 rounded bg-gruvbox-light-bg1 dark:bg-gruvbox-dark-bg1 px-2 py-1 text-sm outline-none"
        placeholder="Filter…"
        value={filter}
        onChange={(e) => setFilter(e.target.value)}
      />
      <div className="min-h-0 flex-1 overflow-y-auto">
        {detections.status === 'error' && (
          <p className="p-2 text-sm text-gruvbox-light-red dark:text-gruvbox-dark-red">
            {detections.error}
          </p>
        )}
        {detections.status === 'ready' && items.length === 0 && (
          <p className="p-2 text-sm text-gruvbox-light-gray dark:text-gruvbox-dark-gray">
            No detections
          </p>
        )}
        {items.map((d, i) => (
          <button
            key={d.id ?? i}
            className="block w-full border-b border-gruvbox-light-bg1 dark:border-gruvbox-dark-bg1 px-2 py-2 text-left hover:bg-gruvbox-light-bg1 dark:hover:bg-gruvbox-dark-bg1"
            title="Open in a new tab"
            onClick={() => void open(d.id, d.title)}
          >
            <div className="flex items-center gap-1 text-sm">
              <span className="truncate font-medium">{d.title ?? d.id ?? 'untitled'}</span>
              {d.level && (
                <span className={`ml-auto text-xs ${levelColor[d.level] ?? ''}`}>{d.level}</span>
              )}
            </div>
            {d.description && (
              <p className="mt-0.5 line-clamp-2 text-xs text-gruvbox-light-gray dark:text-gruvbox-dark-gray">
                {d.description}
              </p>
            )}
            <div className="mt-0.5 flex gap-2 text-xs text-gruvbox-light-fg3 dark:text-gruvbox-dark-fg3">
              {d.status && <span>{d.status}</span>}
              {d.schedule && <span className="font-mono">{d.schedule}</span>}
            </div>
          </button>
        ))}
      </div>
    </div>
  )
}
