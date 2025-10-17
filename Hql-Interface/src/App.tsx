import { useState } from 'react';
import { useTheme } from './hooks/useTheme';
import { ThemeToggle } from './components/ThemeToggle';
import { QueryEditor } from './components/QueryEditor';
import { ResultsTable } from './components/ResultsTable';
import { SchemaExplorer } from './components/SchemaExplorer';
import { DetectionsSidebar } from './components/DetectionsSidebar';
import type { QueryResult } from './types';

function App() {
  const { theme } = useTheme();
  const [results, setResults] = useState<QueryResult | null>(null);
  const [showSchema, setShowSchema] = useState(true);
  const [showDetections, setShowDetections] = useState(true);

  return (
    <div className="h-screen flex flex-col">
      {/* Header */}
      <header className="flex items-center justify-between px-6 py-3 border-b border-gruvbox-light-bg2 dark:border-gruvbox-dark-bg2 bg-gruvbox-light-bg1 dark:bg-gruvbox-dark-bg1">
        <div className="flex items-center gap-4">
          <h1 className="text-xl font-bold">HQL Interface</h1>
          <div className="flex gap-2">
            <button
              onClick={() => setShowSchema(!showSchema)}
              className={`text-sm btn px-3 py-1 ${showSchema ? 'btn-primary' : ''}`}
            >
              Schema
            </button>
            <button
              onClick={() => setShowDetections(!showDetections)}
              className={`text-sm btn px-3 py-1 ${showDetections ? 'btn-primary' : ''}`}
            >
              Detections
            </button>
          </div>
        </div>
        <ThemeToggle />
      </header>

      {/* Main Content */}
      <div className="flex-1 flex overflow-hidden">
        {/* Left Sidebar - Schema */}
        {showSchema && <SchemaExplorer />}

        {/* Center - Editor and Results */}
        <div className="flex-1 flex flex-col overflow-hidden">
          {/* Query Editor */}
          <div className="h-1/2 border-b border-gruvbox-light-bg2 dark:border-gruvbox-dark-bg2">
            <QueryEditor onResultsChange={setResults} theme={theme} />
          </div>

          {/* Results Table */}
          <div className="h-1/2">
            <ResultsTable results={results} />
          </div>
        </div>

        {/* Right Sidebar - Detections */}
        {showDetections && <DetectionsSidebar />}
      </div>
    </div>
  );
}

export default App;
