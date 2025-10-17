import { useState, useEffect, forwardRef, useImperativeHandle } from 'react';
import { api } from '../services/api';
import type { Detection } from '../types';

interface DetectionsSidebarProps {
  onLoadDetection?: (query: string) => void;
}

export interface DetectionsSidebarHandle {
  reloadDetections: () => Promise<void>;
}

export const DetectionsSidebar = forwardRef<DetectionsSidebarHandle, DetectionsSidebarProps>(({ onLoadDetection }, ref) => {
  const [detections, setDetections] = useState<Detection[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [searchTerm, setSearchTerm] = useState('');
  const [filterStatus, setFilterStatus] = useState<string>('all');
  const [selectedDetection, setSelectedDetection] = useState<Detection | null>(null);
  const [loadingDetection, setLoadingDetection] = useState(false);

  useEffect(() => {
    loadDetections();

    // Set up periodic reload every 60 seconds
    const intervalId = setInterval(() => {
      loadDetections();
    }, 60000);

    // Cleanup interval on unmount
    return () => clearInterval(intervalId);
  }, []);

  const loadDetections = async () => {
    try {
      const data = await api.getDetections();
      setDetections(data);
      setError(null);
    } catch (err) {
      setError('Failed to load detections');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  // Expose reload method to parent
  useImperativeHandle(ref, () => ({
    reloadDetections: loadDetections,
  }));

  const filterDetections = () => {
    return detections.filter((det) => {
      const matchesSearch =
        det.title?.toLowerCase().includes(searchTerm.toLowerCase()) ||
        det.description?.toLowerCase().includes(searchTerm.toLowerCase());
      const matchesStatus =
        filterStatus === 'all' || det.status === filterStatus;
      return matchesSearch && matchesStatus;
    });
  };

  const handleDetectionClick = (detection: Detection) => {
    setSelectedDetection(detection);
  };

  const handleDetectionDoubleClick = async (detectionId: string) => {
    if (!onLoadDetection) return;

    setLoadingDetection(true);
    try {
      const response = await fetch(`/api/detections/${detectionId}`);
      if (!response.ok) {
        throw new Error('Failed to load detection');
      }

      const detectionData = await response.json();
      if (detectionData.hql) {
        onLoadDetection(detectionData.hql);
      }
    } catch (err) {
      console.error('Failed to load detection:', err);
      setError(err instanceof Error ? err.message : 'Failed to load detection');
    } finally {
      setLoadingDetection(false);
    }
  };

  return (
    <div className="sidebar w-80 flex flex-col h-full">
      <div className="p-4 border-b border-gruvbox-light-bg2 dark:border-gruvbox-dark-bg2">
        <div className="flex items-center justify-between mb-3">
          <h3 className="font-bold">Detections</h3>
          <button
            onClick={loadDetections}
            className="text-xs btn px-2 py-1"
            title="Refresh"
          >
            ↻
          </button>
        </div>
        <input
          type="text"
          placeholder="Search detections..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          className="input w-full text-sm mb-2"
        />
        <select
          value={filterStatus}
          onChange={(e) => setFilterStatus(e.target.value)}
          className="input w-full text-sm"
        >
          <option value="all">All Statuses</option>
          <option value="enabled">Enabled</option>
          <option value="disabled">Disabled</option>
          <option value="testing">Testing</option>
        </select>
      </div>

      <div className="flex-1 overflow-y-auto">
        {loading && (
          <div className="text-sm text-gruvbox-light-gray dark:text-gruvbox-dark-gray p-4">
            Loading detections...
          </div>
        )}

        {error && (
          <div className="text-sm text-gruvbox-light-red dark:text-gruvbox-dark-red p-4">
            {error}
            <button
              onClick={loadDetections}
              className="block mt-2 text-xs underline"
            >
              Retry
            </button>
          </div>
        )}

        {!loading && !error && filterDetections().length === 0 && (
          <div className="text-sm text-gruvbox-light-gray dark:text-gruvbox-dark-gray p-4">
            No detections found
          </div>
        )}

        {!loading && !error && (
          <div className="divide-y divide-gruvbox-light-bg2 dark:divide-gruvbox-dark-bg2">
            {filterDetections().map((detection) => (
              <div
                key={detection.id}
                className={`p-3 cursor-pointer hover:bg-gruvbox-light-bg2 dark:hover:bg-gruvbox-dark-bg2 ${
                  selectedDetection?.id === detection.id
                    ? 'bg-gruvbox-light-bg2 dark:bg-gruvbox-dark-bg2'
                    : ''
                }`}
                onClick={() => handleDetectionClick(detection)}
                onDoubleClick={() => handleDetectionDoubleClick(detection.id)}
                title="Double-click to load query"
              >
                <div className="font-medium text-sm mb-1">{detection.title || 'Untitled'}</div>
                {detection.description && (
                  <div className="text-xs text-gruvbox-light-gray dark:text-gruvbox-dark-gray mb-2 line-clamp-2">
                    {detection.description}
                  </div>
                )}
                <div className="flex items-center gap-2 text-xs">
                  <span
                    className={`px-2 py-0.5 rounded ${
                      detection.status === 'enabled'
                        ? 'bg-gruvbox-light-green dark:bg-gruvbox-dark-green text-gruvbox-light-bg dark:text-gruvbox-dark-bg'
                        : detection.status === 'disabled'
                        ? 'bg-gruvbox-light-red dark:bg-gruvbox-dark-red text-gruvbox-light-bg dark:text-gruvbox-dark-bg'
                        : 'bg-gruvbox-light-yellow dark:bg-gruvbox-dark-yellow text-gruvbox-light-bg dark:text-gruvbox-dark-bg'
                    }`}
                  >
                    {detection.status}
                  </span>
                  {detection.schedule && (
                    <span className="text-gruvbox-light-gray dark:text-gruvbox-dark-gray">
                      {detection.schedule}
                    </span>
                  )}
                </div>
                {detection.author && (
                  <div className="text-xs text-gruvbox-light-gray dark:text-gruvbox-dark-gray mt-1">
                    by {detection.author}
                  </div>
                )}
              </div>
            ))}
          </div>
        )}
      </div>

      <div className="p-2 border-t border-gruvbox-light-bg2 dark:border-gruvbox-dark-bg2 text-xs text-gruvbox-light-gray dark:text-gruvbox-dark-gray">
        {loadingDetection ? (
          <span className="text-gruvbox-light-blue dark:text-gruvbox-dark-blue">Loading detection...</span>
        ) : (
          <span>{filterDetections().length} of {detections.length} detections</span>
        )}
      </div>
    </div>
  );
});
