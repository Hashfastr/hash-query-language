import { useEffect } from 'react'
import { Editor } from './components/Editor'
import { ResultsPane } from './components/ResultsPane'
import { RightPanel } from './components/RightPanel'
import { TopBar } from './components/TopBar'
import { useRunner } from './hooks/useRunner'
import { persist } from './lib/persist'
import { useActiveTab, useAppDispatch, useAppState, useIsRunning } from './state/store'

export default function App() {
  const state = useAppState()
  const tab = useActiveTab()
  const dispatch = useAppDispatch()
  const isRunning = useIsRunning()
  const { run } = useRunner()

  useEffect(() => {
    persist(state)
  }, [state])

  return (
    <div className="flex h-full flex-col bg-gruvbox-light-bg0 text-gruvbox-light-fg dark:bg-gruvbox-dark-bg0 dark:text-gruvbox-dark-fg">
      <TopBar />
      <div className="flex min-h-0 flex-1">
        <main className="flex min-w-0 flex-1 flex-col">
          <div className="h-1/2 min-h-[120px]">
            <Editor
              tabId={tab.id}
              value={tab.query}
              isDark={state.theme === 'dark'}
              onChange={(query) => dispatch({ type: 'setQuery', tabId: tab.id, query })}
              onRun={() => {
                if (!isRunning && tab.query.trim()) void run(tab.id, tab.query)
              }}
            />
          </div>
          <div className="min-h-0 flex-1 border-t border-gruvbox-light-bg2 dark:border-gruvbox-dark-bg2">
            <ResultsPane />
          </div>
        </main>
        <RightPanel />
      </div>
    </div>
  )
}
