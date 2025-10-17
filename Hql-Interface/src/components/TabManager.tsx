import { useState, useEffect, forwardRef, useImperativeHandle } from 'react';
import { QueryEditor } from './QueryEditor';
import { ResultsTable } from './ResultsTable';
import type { QueryResult, Theme } from '../types';

interface Tab {
  id: string;
  name: string;
  query: string;
  results: QueryResult | null;
}

interface TabManagerProps {
  theme: Theme;
  onDetectionSaved?: () => void;
}

const TABS_STORAGE_KEY = 'hql-tabs';
const ACTIVE_TAB_KEY = 'hql-active-tab';

export interface TabManagerHandle {
  loadDetectionIntoActiveTab: (query: string) => void;
}

export const TabManager = forwardRef<TabManagerHandle, TabManagerProps>(({ theme, onDetectionSaved }, ref) => {
  const [tabs, setTabs] = useState<Tab[]>(() => {
    try {
      const saved = localStorage.getItem(TABS_STORAGE_KEY);
      if (saved) {
        const parsed = JSON.parse(saved);
        return parsed.length > 0 ? parsed : [{ id: '1', name: 'Query 1', query: '', results: null }];
      }
    } catch (err) {
      console.error('Failed to load tabs:', err);
    }
    return [{ id: '1', name: 'Query 1', query: '', results: null }];
  });

  const [activeTabId, setActiveTabId] = useState<string>(() => {
    try {
      const saved = localStorage.getItem(ACTIVE_TAB_KEY);
      return saved || tabs[0]?.id || '1';
    } catch {
      return tabs[0]?.id || '1';
    }
  });

  // Save tabs to localStorage whenever they change
  useEffect(() => {
    try {
      localStorage.setItem(TABS_STORAGE_KEY, JSON.stringify(tabs));
    } catch (err) {
      console.error('Failed to save tabs:', err);
    }
  }, [tabs]);

  // Save active tab
  useEffect(() => {
    try {
      localStorage.setItem(ACTIVE_TAB_KEY, activeTabId);
    } catch (err) {
      console.error('Failed to save active tab:', err);
    }
  }, [activeTabId]);

  const activeTab = tabs.find(t => t.id === activeTabId) || tabs[0];

  const addTab = () => {
    const newId = Date.now().toString();
    const newTab: Tab = {
      id: newId,
      name: `Query ${tabs.length + 1}`,
      query: '',
      results: null,
    };
    setTabs([...tabs, newTab]);
    setActiveTabId(newId);
  };

  const closeTab = (tabId: string) => {
    if (tabs.length === 1) return; // Don't close the last tab

    const newTabs = tabs.filter(t => t.id !== tabId);
    setTabs(newTabs);

    // If closing active tab, switch to another
    if (activeTabId === tabId) {
      const tabIndex = tabs.findIndex(t => t.id === tabId);
      const newActiveIndex = tabIndex > 0 ? tabIndex - 1 : 0;
      setActiveTabId(newTabs[newActiveIndex].id);
    }
  };

  const updateTabQuery = (tabId: string, query: string) => {
    setTabs(tabs.map(t => t.id === tabId ? { ...t, query } : t));
  };

  const updateTabResults = (tabId: string, results: QueryResult | null) => {
    setTabs(tabs.map(t => t.id === tabId ? { ...t, results } : t));
  };

  const renameTab = (tabId: string, name: string) => {
    setTabs(tabs.map(t => t.id === tabId ? { ...t, name } : t));
  };

  // Expose method to load detection into active tab
  useImperativeHandle(ref, () => ({
    loadDetectionIntoActiveTab: (query: string) => {
      // Use setTabs with functional update to avoid stale closure
      setTabs(currentTabs => {
        return currentTabs.map(t =>
          t.id === activeTabId
            ? { ...t, query, results: null }
            : t
        );
      });
    },
  }), [activeTabId]);

  return (
    <div className="flex flex-col h-full">
      {/* Tab Bar */}
      <div className="flex items-center border-b border-gruvbox-light-bg2 dark:border-gruvbox-dark-bg2 bg-gruvbox-light-bg1 dark:bg-gruvbox-dark-bg1">
        <div className="flex-1 flex overflow-x-auto">
          {tabs.map((tab) => (
            <div
              key={tab.id}
              className={`group flex items-center gap-2 px-4 py-2 border-r border-gruvbox-light-bg2 dark:border-gruvbox-dark-bg2 cursor-pointer min-w-0 ${
                activeTabId === tab.id
                  ? 'bg-gruvbox-light-bg dark:bg-gruvbox-dark-bg'
                  : 'hover:bg-gruvbox-light-bg2 dark:hover:bg-gruvbox-dark-bg2'
              }`}
              onClick={() => setActiveTabId(tab.id)}
            >
              <input
                type="text"
                value={tab.name}
                onChange={(e) => renameTab(tab.id, e.target.value)}
                onClick={(e) => e.stopPropagation()}
                className="bg-transparent border-none outline-none text-sm min-w-0 flex-1"
                style={{ width: `${Math.max(tab.name.length * 8, 60)}px` }}
              />
              {tabs.length > 1 && (
                <button
                  onClick={(e) => {
                    e.stopPropagation();
                    closeTab(tab.id);
                  }}
                  className="opacity-0 group-hover:opacity-100 text-gruvbox-light-gray dark:text-gruvbox-dark-gray hover:text-gruvbox-light-red dark:hover:text-gruvbox-dark-red"
                  title="Close tab"
                >
                  ×
                </button>
              )}
            </div>
          ))}
        </div>
        <button
          onClick={addTab}
          className="px-4 py-2 hover:bg-gruvbox-light-bg2 dark:hover:bg-gruvbox-dark-bg2"
          title="New tab"
        >
          +
        </button>
      </div>

      {/* Active Tab Content */}
      {activeTab && (
        <div className="flex-1 flex flex-col overflow-hidden">
          {/* Query Editor */}
          <div className="h-1/2 border-b border-gruvbox-light-bg2 dark:border-gruvbox-dark-bg2">
            <QueryEditor
              query={activeTab.query}
              onQueryChange={(query) => updateTabQuery(activeTab.id, query)}
              onResultsChange={(results) => updateTabResults(activeTab.id, results)}
              onDetectionSaved={onDetectionSaved}
              theme={theme}
            />
          </div>

          {/* Results Table */}
          <div className="h-1/2">
            <ResultsTable results={activeTab.results} />
          </div>
        </div>
      )}
    </div>
  );
});
