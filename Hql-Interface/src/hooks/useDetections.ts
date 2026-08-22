import { useCallback } from 'react'
import * as api from '../services/api'
import { useAppDispatch } from '../state/store'

export function useDetections() {
  const dispatch = useAppDispatch()

  const reload = useCallback(async () => {
    dispatch({ type: 'detectionsLoading' })
    try {
      const items = await api.getDetections()
      dispatch({ type: 'detectionsLoaded', items })
    } catch (e) {
      dispatch({ type: 'detectionsError', error: e instanceof Error ? e.message : String(e) })
    }
  }, [dispatch])

  return { reload }
}
