import type { AppState } from '../types'

// Bump the version suffix (and the Persisted.version check) on any shape
// change — stale blobs are discarded, not migrated, which is fine because
// only tab titles/queries and cosmetics live here. Results are intentionally
// never persisted: they can be megabytes and go stale the moment data moves.
const KEY = 'hql-interface:v1'

export interface Persisted {
  version: 1
  theme: 'dark' | 'light'
  sidebarCollapsed: boolean
  activeTabId: string
  tabs: { id: string; title: string; query: string }[]
}

export function loadPersisted(): Persisted | null {
  try {
    const raw = localStorage.getItem(KEY)
    if (!raw) return null
    const parsed = JSON.parse(raw) as Persisted
    if (parsed.version !== 1) return null
    return parsed
  } catch {
    return null
  }
}

let timer: ReturnType<typeof setTimeout> | undefined

/** Debounced write; results are intentionally never persisted. */
export function persist(state: AppState): void {
  clearTimeout(timer)
  timer = setTimeout(() => {
    const data: Persisted = {
      version: 1,
      theme: state.theme,
      sidebarCollapsed: state.sidebarCollapsed,
      activeTabId: state.activeTabId,
      tabs: state.tabs.map((t) => ({ id: t.id, title: t.title, query: t.query })),
    }
    try {
      localStorage.setItem(KEY, JSON.stringify(data))
    } catch {
      // storage full or unavailable; nothing sensible to do
    }
  }, 500)
}
