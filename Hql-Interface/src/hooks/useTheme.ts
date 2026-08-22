import { useEffect } from 'react'
import { useAppDispatch, useAppState } from '../state/store'

export function useTheme(): { theme: 'dark' | 'light'; toggle: () => void } {
  const { theme } = useAppState()
  const dispatch = useAppDispatch()

  useEffect(() => {
    document.documentElement.classList.toggle('dark', theme === 'dark')
  }, [theme])

  return {
    theme,
    toggle: () => dispatch({ type: 'setTheme', theme: theme === 'dark' ? 'light' : 'dark' }),
  }
}
