import { useEffect, useRef, useState } from 'react'

// Shared pointer-drag resize logic for the right panel (width) and the
// editor/results splitter (height). Sizes are stored under their own
// localStorage keys, NOT in the versioned persist.ts blob: a persistence
// schema bump shouldn't reset someone's panel layout.

interface Options {
  storageKey: string
  defaultSize: number
  min: number
  /** Called at drag time so the bound tracks the current window size */
  max: () => number
  axis: 'x' | 'y'
  /** +1: grows as the pointer moves right/down; -1: grows left/up */
  direction: 1 | -1
}

function load(key: string, fallback: number, min: number): number {
  const v = Number(localStorage.getItem(key))
  return Number.isFinite(v) && v >= min ? v : fallback
}

export function useDragResize({ storageKey, defaultSize, min, max, axis, direction }: Options) {
  const [size, setSize] = useState(() => load(storageKey, defaultSize, min))
  const sizeRef = useRef(size)
  sizeRef.current = size

  // Re-read when the caller switches keys (e.g. inspector vs detections mode)
  useEffect(() => {
    setSize(load(storageKey, defaultSize, min))
  }, [storageKey, defaultSize, min])

  const startDrag = (e: React.PointerEvent<HTMLElement>) => {
    e.preventDefault()
    const handle = e.currentTarget
    const startPos = axis === 'x' ? e.clientX : e.clientY
    const startSize = sizeRef.current
    handle.setPointerCapture(e.pointerId)

    const clamp = (v: number) => Math.min(Math.max(v, min), max())
    const move = (ev: PointerEvent) => {
      const pos = axis === 'x' ? ev.clientX : ev.clientY
      setSize(clamp(startSize + direction * (pos - startPos)))
    }
    const up = () => {
      handle.removeEventListener('pointermove', move)
      localStorage.setItem(storageKey, String(sizeRef.current))
    }
    handle.addEventListener('pointermove', move)
    handle.addEventListener('pointerup', up, { once: true })
  }

  return { size, startDrag }
}
