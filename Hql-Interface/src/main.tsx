import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App'
import { StoreProvider } from './state/store'
import { loadPersisted } from './lib/persist'
import './styles/index.css'

// Apply theme class before first paint to avoid a light-mode flash
const persisted = loadPersisted()
document.documentElement.classList.toggle('dark', (persisted?.theme ?? 'dark') === 'dark')

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <StoreProvider>
      <App />
    </StoreProvider>
  </StrictMode>,
)
