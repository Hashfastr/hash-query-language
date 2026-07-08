import type { Row } from '../types'

export interface Column {
  /** Top-level field name in the row */
  key: string
  /** Dot-separated display name, e.g. winlog.computer_name */
  header: string
  /** Path below the top-level key to the flattened leaf; empty = no flattening */
  path: string[]
}

const SAMPLE_ROWS = 50

function isPlainObject(v: unknown): v is Record<string, unknown> {
  return typeof v === 'object' && v !== null && !Array.isArray(v)
}

/**
 * If every sampled non-null value of a column is an object with the same
 * single key (repeatedly, down a chain), the column collapses to that
 * dot-separated path and cells render the leaf value.
 *
 * Detection is data-driven rather than schema-driven because the backend
 * schema types nested fields as just `dynamic` — it can't tell us the shape.
 * Sampling instead of scanning all rows is a deliberate trade: a column that
 * changes shape after row 50 mis-flattens, but the original row is always
 * available in the inspector and via copy, so the failure mode is cosmetic.
 */
function singlePath(rows: Row[], key: string): string[] {
  const path: string[] = []
  let values = rows
    .slice(0, SAMPLE_ROWS)
    .map((r) => r[key])
    .filter((v) => v !== null && v !== undefined)

  for (;;) {
    if (values.length === 0) return path
    let step: string | null = null
    for (const v of values) {
      if (!isPlainObject(v)) return path
      const keys = Object.keys(v)
      if (keys.length !== 1) return path
      if (step === null) step = keys[0]
      else if (step !== keys[0]) return path
    }
    if (step === null) return path
    path.push(step)
    values = values.map((v) => (v as Record<string, unknown>)[step as string])
      .filter((v) => v !== null && v !== undefined)
  }
}

export function deriveColumns(rows: Row[], schema: Record<string, string> | undefined): Column[] {
  // Schema gives authoritative order; union with observed keys as a safety net
  const keys: string[] = []
  const seen = new Set<string>()
  for (const k of Object.keys(schema ?? {})) {
    keys.push(k)
    seen.add(k)
  }
  for (const row of rows.slice(0, SAMPLE_ROWS)) {
    for (const k of Object.keys(row)) {
      if (!seen.has(k)) {
        keys.push(k)
        seen.add(k)
      }
    }
  }

  return keys.map((key) => {
    const path = singlePath(rows, key)
    return {
      key,
      header: path.length > 0 ? [key, ...path].join('.') : key,
      path,
    }
  })
}

/** Resolve a cell through a flattened path; stops at null/undefined. */
export function cellValue(row: Row, col: Column): unknown {
  let v: unknown = row[col.key]
  for (const step of col.path) {
    if (!isPlainObject(v)) return v
    v = v[step]
  }
  return v
}
