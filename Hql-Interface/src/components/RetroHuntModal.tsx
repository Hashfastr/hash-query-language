import { useState } from 'react';
import { api, ApiError } from '../services/api';

interface RetroHuntModalProps {
  query: string;
  isOpen: boolean;
  onClose: () => void;
}

export function RetroHuntModal({ query, isOpen, onClose }: RetroHuntModalProps) {
  const [isExecuting, setIsExecuting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Default: 1 hour ago to now
  const getDefaultStart = () => {
    const date = new Date();
    date.setHours(date.getHours() - 1);
    return formatDateTimeLocal(date);
  };

  const getDefaultEnd = () => {
    return formatDateTimeLocal(new Date());
  };

  const [startDate, setStartDate] = useState(getDefaultStart());
  const [endDate, setEndDate] = useState(getDefaultEnd());

  // Format date for datetime-local input (YYYY-MM-DDTHH:mm)
  function formatDateTimeLocal(date: Date): string {
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    const hours = String(date.getHours()).padStart(2, '0');
    const minutes = String(date.getMinutes()).padStart(2, '0');
    return `${year}-${month}-${day}T${hours}:${minutes}`;
  }

  const handleExecute = async () => {
    if (!query.trim()) {
      setError('Please enter a query');
      return;
    }

    setIsExecuting(true);
    setError(null);

    try {
      const start = new Date(startDate);
      const end = new Date(endDate);

      if (start >= end) {
        setError('Start date must be before end date');
        setIsExecuting(false);
        return;
      }

      const response = await api.retroHunt(query, start, end);

      setError(null);
      alert(`Retro hunt initiated successfully! ${response.ids?.length || 0} runs created.`);
      onClose();
    } catch (err) {
      if (err instanceof ApiError) {
        setError(`API Error: ${err.message}`);
      } else if (err instanceof Error) {
        setError(err.message);
      } else {
        setError('Failed to execute retro hunt');
      }
    } finally {
      setIsExecuting(false);
    }
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div className="bg-gruvbox-light-bg dark:bg-gruvbox-dark-bg border-2 border-gruvbox-light-bg2 dark:border-gruvbox-dark-bg2 rounded-lg p-6 w-full max-w-md">
        <h2 className="text-xl font-bold mb-4">Retro Hunt</h2>

        {error && (
          <div className="mb-4 p-3 rounded bg-gruvbox-light-red/20 dark:bg-gruvbox-dark-red/20 text-gruvbox-light-red dark:text-gruvbox-dark-red border border-gruvbox-light-red dark:border-gruvbox-dark-red">
            {error}
          </div>
        )}

        <div className="space-y-4">
          <div>
            <label className="block text-sm font-medium mb-2">
              Start Date & Time
            </label>
            <input
              type="datetime-local"
              value={startDate}
              onChange={(e) => setStartDate(e.target.value)}
              className="w-full px-3 py-2 border border-gruvbox-light-bg2 dark:border-gruvbox-dark-bg2 rounded bg-gruvbox-light-bg1 dark:bg-gruvbox-dark-bg1 focus:outline-none focus:ring-2 focus:ring-gruvbox-light-blue dark:focus:ring-gruvbox-dark-blue"
            />
          </div>

          <div>
            <label className="block text-sm font-medium mb-2">
              End Date & Time
            </label>
            <input
              type="datetime-local"
              value={endDate}
              onChange={(e) => setEndDate(e.target.value)}
              className="w-full px-3 py-2 border border-gruvbox-light-bg2 dark:border-gruvbox-dark-bg2 rounded bg-gruvbox-light-bg1 dark:bg-gruvbox-dark-bg1 focus:outline-none focus:ring-2 focus:ring-gruvbox-light-blue dark:focus:ring-gruvbox-dark-blue"
            />
          </div>
        </div>

        <div className="flex gap-2 mt-6">
          <button
            onClick={handleExecute}
            disabled={isExecuting}
            className="flex-1 bg-gruvbox-light-purple hover:opacity-90 dark:bg-gruvbox-dark-purple text-gruvbox-light-bg dark:text-gruvbox-dark-bg font-medium py-2 px-4 rounded transition-opacity disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {isExecuting ? 'Executing...' : 'Execute Retro Hunt'}
          </button>
          <button
            onClick={onClose}
            disabled={isExecuting}
            className="btn"
          >
            Cancel
          </button>
        </div>
      </div>
    </div>
  );
}
