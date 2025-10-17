import { useState } from 'react';
import Editor from '@monaco-editor/react';
import { api, ApiError } from '../services/api';
import type { QueryResult } from '../types';

interface QueryEditorProps {
  onResultsChange: (results: QueryResult | null) => void;
  theme: 'light' | 'dark';
}

export function QueryEditor({ onResultsChange, theme }: QueryEditorProps) {
  const [query, setQuery] = useState('');
  const [isExecuting, setIsExecuting] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [saveMode, setSaveMode] = useState(false);
  const [saveForm, setSaveForm] = useState({
    title: '',
    description: '',
    author: '',
    schedule: '0 * * * *',
    status: 'enabled',
  });

  // Flatten nested objects one level deep with dot notation
  const flattenRow = (row: Record<string, any>): Record<string, any> => {
    const flattened: Record<string, any> = {};

    for (const [key, value] of Object.entries(row)) {
      // Check if value is a plain object (not null, not array, not Date, etc.)
      if (
        value !== null &&
        value !== undefined &&
        typeof value === 'object' &&
        !Array.isArray(value) &&
        Object.prototype.toString.call(value) === '[object Object]'
      ) {
        // Flatten one level: event.category, event.severity, etc.
        for (const [nestedKey, nestedValue] of Object.entries(value)) {
          flattened[`${key}.${nestedKey}`] = nestedValue;
        }
      } else {
        // Keep primitive values and arrays as-is
        flattened[key] = value;
      }
    }

    return flattened;
  };

  const executeQuery = async () => {
    if (!query.trim()) {
      setError('Please enter a query');
      return;
    }

    setIsExecuting(true);
    setError(null);
    onResultsChange(null);

    try {
      const startTime = performance.now();
      const response = await api.executeQuery(query, false);

      if (!response.id) {
        setError('No run ID returned');
        setIsExecuting(false);
        return;
      }

      // Poll for results
      const run = await api.pollRunUntilComplete(response.id);
      const endTime = performance.now();

      if (run.failed) {
        const errorMsg = run.str_out || 'Query execution failed';
        setError(errorMsg);
        setIsExecuting(false);
        return;
      }

      // Extract data from the results object
      let resultData: Record<string, any>[] = [];

      if (run.results?.data) {
        // Check if data is already an array
        if (Array.isArray(run.results.data)) {
          resultData = run.results.data;
        } else {
          // Data is keyed by table name, extract the first table's data
          const tableNames = Object.keys(run.results.data);
          if (tableNames.length > 0) {
            const firstTable = tableNames[0];
            const tableData = run.results.data[firstTable];
            if (Array.isArray(tableData)) {
              resultData = tableData;
            }
          }
        }
      }

      if (resultData.length > 0) {
        // Debug logging
        console.log('Raw resultData:', resultData);

        // Flatten nested objects one level deep
        const flattenedData = resultData.map(row => flattenRow(row));

        console.log('Flattened data:', flattenedData);

        const columns = Object.keys(flattenedData[0]);

        onResultsChange({
          columns,
          data: flattenedData,
          duration: run.duration || (endTime - startTime) / 1000,
          rowCount: flattenedData.length,
        });
      } else {
        onResultsChange({
          columns: [],
          data: [],
          duration: run.duration || (endTime - startTime) / 1000,
          rowCount: 0,
        });
      }
    } catch (err) {
      if (err instanceof ApiError) {
        setError(`API Error: ${err.message}`);
      } else if (err instanceof Error) {
        setError(err.message);
      } else {
        setError('An unknown error occurred');
      }
    } finally {
      setIsExecuting(false);
    }
  };

  const saveDetection = async () => {
    if (!query.trim()) {
      setError('Please enter a query');
      return;
    }

    if (!saveForm.title || !saveForm.author) {
      setError('Title and author are required');
      return;
    }

    try {
      await api.saveDetection({
        hql: query,
        ...saveForm,
      });
      setSaveMode(false);
      setSaveForm({
        title: '',
        description: '',
        author: '',
        schedule: '0 * * * *',
        status: 'enabled',
      });
      setError(null);
      alert('Detection saved successfully');
    } catch (err) {
      if (err instanceof ApiError) {
        setError(`Failed to save: ${err.message}`);
      } else if (err instanceof Error) {
        setError(err.message);
      }
    }
  };

  return (
    <div className="flex flex-col h-full">
      <div className="flex items-center justify-between p-4 border-b border-gruvbox-light-bg2 dark:border-gruvbox-dark-bg2">
        <h2 className="text-lg font-bold">Query Editor</h2>
        <div className="flex gap-2">
          <button
            onClick={executeQuery}
            disabled={isExecuting}
            className="btn-success"
          >
            {isExecuting ? 'Executing...' : 'Run Query'}
          </button>
          <button
            onClick={() => setSaveMode(!saveMode)}
            className="btn-primary"
          >
            {saveMode ? 'Cancel Save' : 'Save as Detection'}
          </button>
          <button
            onClick={() => {
              setQuery('');
              onResultsChange(null);
              setError(null);
            }}
            className="btn"
          >
            Clear
          </button>
        </div>
      </div>

      {error && (
        <div className="mx-4 mt-4 p-3 rounded bg-gruvbox-light-red/20 dark:bg-gruvbox-dark-red/20 text-gruvbox-light-red dark:text-gruvbox-dark-red border border-gruvbox-light-red dark:border-gruvbox-dark-red">
          {error}
        </div>
      )}

      {saveMode && (
        <div className="mx-4 mt-4 p-4 card space-y-3">
          <h3 className="font-bold">Save Detection</h3>
          <input
            type="text"
            placeholder="Title"
            value={saveForm.title}
            onChange={(e) => setSaveForm({ ...saveForm, title: e.target.value })}
            className="input w-full"
          />
          <textarea
            placeholder="Description"
            value={saveForm.description}
            onChange={(e) => setSaveForm({ ...saveForm, description: e.target.value })}
            className="input w-full h-20"
          />
          <input
            type="text"
            placeholder="Author"
            value={saveForm.author}
            onChange={(e) => setSaveForm({ ...saveForm, author: e.target.value })}
            className="input w-full"
          />
          <input
            type="text"
            placeholder="Schedule (cron format)"
            value={saveForm.schedule}
            onChange={(e) => setSaveForm({ ...saveForm, schedule: e.target.value })}
            className="input w-full"
          />
          <select
            value={saveForm.status}
            onChange={(e) => setSaveForm({ ...saveForm, status: e.target.value })}
            className="input w-full"
          >
            <option value="enabled">Enabled</option>
            <option value="disabled">Disabled</option>
            <option value="testing">Testing</option>
          </select>
          <button onClick={saveDetection} className="btn-success">
            Save Detection
          </button>
        </div>
      )}

      <div className="flex-1 m-4 border border-gruvbox-light-bg2 dark:border-gruvbox-dark-bg2 rounded overflow-hidden">
        <Editor
          height="100%"
          defaultLanguage="plaintext"
          value={query}
          onChange={(value) => setQuery(value || '')}
          theme={theme === 'dark' ? 'vs-dark' : 'vs-light'}
          options={{
            minimap: { enabled: false },
            fontSize: 14,
            lineNumbers: 'on',
            scrollBeyondLastLine: false,
            automaticLayout: true,
            tabSize: 2,
          }}
        />
      </div>
    </div>
  );
}
