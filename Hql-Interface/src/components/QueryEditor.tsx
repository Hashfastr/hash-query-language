import { useState } from 'react';
import Editor from '@monaco-editor/react';
import { api, ApiError } from '../services/api';
import type { QueryResult } from '../types';
import { RetroHuntModal } from './RetroHuntModal';

interface QueryEditorProps {
  query?: string;
  onQueryChange?: (query: string) => void;
  onResultsChange: (results: QueryResult | null) => void;
  onDetectionSaved?: () => void;
  theme: 'light' | 'dark';
}

export function QueryEditor({ query: externalQuery, onQueryChange, onResultsChange, onDetectionSaved, theme }: QueryEditorProps) {
  const [internalQuery, setInternalQuery] = useState('');
  const [isExecuting, setIsExecuting] = useState(false);
  const [isInitializingHac, setIsInitializingHac] = useState(false);
  const [isConvertingSigma, setIsConvertingSigma] = useState(false);
  const [showRetroModal, setShowRetroModal] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Use external query if provided, otherwise use internal state
  const query = externalQuery !== undefined ? externalQuery : internalQuery;

  const handleQueryChange = (newQuery: string) => {
    if (onQueryChange) {
      onQueryChange(newQuery);
    } else {
      setInternalQuery(newQuery);
    }
  };

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
        // Flatten nested objects one level deep
        const flattenedData = resultData.map(row => flattenRow(row));

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

    try {
      // Send raw query body to backend
      const response = await fetch('/api/detections', {
        method: 'POST',
        headers: {
          'Content-Type': 'text/plain',
        },
        body: query,
      });

      if (!response.ok) {
        const error = await response.text();
        throw new Error(error || response.statusText);
      }

      setError(null);
      alert('Detection saved successfully');

      // Trigger reload of detections list after 1 second
      if (onDetectionSaved) {
        setTimeout(() => {
          onDetectionSaved();
        }, 1000);
      }
    } catch (err) {
      if (err instanceof Error) {
        setError(`Failed to save: ${err.message}`);
      }
    }
  };

  const initHac = async () => {
    if (!query.trim()) {
      setError('Please enter a query');
      return;
    }

    setIsInitializingHac(true);
    setError(null);

    try {
      const response = await api.initHac(query);

      // Replace the query with the HAC-initialized version
      handleQueryChange(response.hql);

    } catch (err) {
      if (err instanceof ApiError) {
        setError(`API Error: ${err.message}`);
      } else if (err instanceof Error) {
        setError(err.message);
      } else {
        setError('Failed to initialize HAC');
      }
    } finally {
      setIsInitializingHac(false);
    }
  };

  const convertSigma = async () => {
    if (!query.trim()) {
      setError('Please enter a query');
      return;
    }

    setIsConvertingSigma(true);
    setError(null);

    try {
      const response = await api.convertSigma(query);

      // Replace the query with the converted version
      handleQueryChange(response.hql);

    } catch (err) {
      if (err instanceof ApiError) {
        setError(`API Error: ${err.message}`);
      } else if (err instanceof Error) {
        setError(err.message);
      } else {
        setError('Failed to convert Sigma');
      }
    } finally {
      setIsConvertingSigma(false);
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
            onClick={saveDetection}
            className="btn-primary"
          >
            Save as Detection
          </button>
          <button
            onClick={initHac}
            disabled={isInitializingHac}
            className="btn-primary"
          >
            {isInitializingHac ? 'Initializing HAC...' : 'Init HAC'}
          </button>
          <button
            onClick={convertSigma}
            disabled={isConvertingSigma}
            className="bg-gruvbox-light-orange hover:opacity-90 text-gruvbox-light-bg dark:bg-gruvbox-dark-orange dark:text-gruvbox-dark-bg font-medium py-2 px-4 rounded transition-opacity disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {isConvertingSigma ? 'Converting...' : 'Convert Sigma'}
          </button>
          <button
            onClick={() => setShowRetroModal(true)}
            className="bg-gruvbox-light-purple hover:opacity-90 text-gruvbox-light-bg dark:bg-gruvbox-dark-purple dark:text-gruvbox-dark-bg font-medium py-2 px-4 rounded transition-opacity"
          >
            Retro Hunt
          </button>
          <button
            onClick={() => {
              handleQueryChange('');
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

      <div className="flex-1 m-4 border border-gruvbox-light-bg2 dark:border-gruvbox-dark-bg2 rounded overflow-hidden">
        <Editor
          height="100%"
          defaultLanguage="plaintext"
          value={query}
          onChange={(value) => handleQueryChange(value || '')}
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

      <RetroHuntModal
        query={query}
        isOpen={showRetroModal}
        onClose={() => setShowRetroModal(false)}
      />
    </div>
  );
}
