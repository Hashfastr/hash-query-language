import { useState, useRef } from 'react';
import { useTheme } from './hooks/useTheme';
import { ThemeToggle } from './components/ThemeToggle';
import { TabManager } from './components/TabManager';
import { DetectionsSidebar, type DetectionsSidebarHandle } from './components/DetectionsSidebar';

function App() {
  const { theme } = useTheme();
  const [showDetections, setShowDetections] = useState(true);
  const tabManagerRef = useRef<{ loadDetectionIntoActiveTab: (query: string) => void }>(null);
  const detectionsSidebarRef = useRef<DetectionsSidebarHandle>(null);

  return (
    <div className="h-screen flex flex-col">
      {/* Header */}
      <header className="flex items-center justify-between px-6 py-3 border-b border-gruvbox-light-bg2 dark:border-gruvbox-dark-bg2 bg-gruvbox-light-bg1 dark:bg-gruvbox-dark-bg1">
        <div className="flex items-center gap-4">
          <h1 className="text-xl font-bold">HQL Interface</h1>
          <div className="flex gap-2">
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
        {/* Center - Tabs with Editor and Results */}
        <div className="flex-1 overflow-hidden">
          <TabManager
            ref={tabManagerRef}
            theme={theme}
            onDetectionSaved={() => detectionsSidebarRef.current?.reloadDetections()}
          />
        </div>

        {/* Right Sidebar - Detections */}
        {showDetections && (
          <DetectionsSidebar
            ref={detectionsSidebarRef}
            onLoadDetection={(query) => {
              tabManagerRef.current?.loadDetectionIntoActiveTab(query);
            }}
          />
        )}
      </div>
    </div>
  );
}

export default App;
