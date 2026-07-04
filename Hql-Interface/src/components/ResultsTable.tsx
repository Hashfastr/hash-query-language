import { useMemo, useState } from 'react'
import { cellValue, deriveColumns, type Column } from '../lib/columns'
import { useAppDispatch } from '../state/store'
import type { Row } from '../types'
import { ContextMenu, type MenuItem } from './ContextMenu'

// Hand-rolled <table> instead of a table library: the features needed here
// (sticky header, custom cells, context menu, expansion that renders OUTSIDE
// the table into the right panel) are trivial without one, and tanstack's
// in-table expansion model actively fights the replace-the-sidebar design.
// Render cap + "Load more" instead of virtualization for the same
// minimal-complexity reason; bump PAGE before reaching for react-window.
const PAGE = 500
const TRUNCATE = 120

function formatCell(v: unknown): { text: string; kind: 'null' | 'json' | 'plain' } {
  if (v === null || v === undefined) return { text: 'null', kind: 'null' }
  if (typeof v === 'object') {
    let s = JSON.stringify(v)
    if (s.length > TRUNCATE) s = s.slice(0, TRUNCATE) + '…'
    return { text: s, kind: 'json' }
  }
  return { text: String(v), kind: 'plain' }
}

function copyText(v: unknown) {
  const text =
    v !== null && typeof v === 'object' ? JSON.stringify(v, null, 2) : String(v ?? 'null')
  void navigator.clipboard.writeText(text)
}

export function ResultsTable({
  tabId,
  table,
  rows,
  schema,
}: {
  tabId: string
  table: string
  rows: Row[]
  schema?: Record<string, string>
}) {
  const dispatch = useAppDispatch()
  const [limit, setLimit] = useState(PAGE)
  const [menu, setMenu] = useState<{ x: number; y: number; items: MenuItem[] } | null>(null)

  const columns = useMemo(() => deriveColumns(rows, schema), [rows, schema])

  const openMenu = (e: React.MouseEvent, row: Row, col: Column) => {
    e.preventDefault()
    setMenu({
      x: e.clientX,
      y: e.clientY,
      items: [
        { label: 'Copy value', action: () => copyText(cellValue(row, col)) },
        { label: 'Copy row as JSON', action: () => copyText(row) },
      ],
    })
  }

  return (
    <div className="h-full overflow-auto">
      <table className="w-full border-collapse text-sm">
        <thead className="sticky top-0 z-10 bg-gruvbox-light-bg1 dark:bg-gruvbox-dark-bg1">
          <tr>
            <th className="w-8 border-b border-gruvbox-light-bg3 dark:border-gruvbox-dark-bg3" />
            {columns.map((col) => (
              <th
                key={col.header}
                className="border-b border-gruvbox-light-bg3 dark:border-gruvbox-dark-bg3 px-2 py-1 text-left font-semibold whitespace-nowrap"
              >
                {col.header}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {rows.slice(0, limit).map((row, i) => (
            <tr
              key={i}
              className="hover:bg-gruvbox-light-bg1 dark:hover:bg-gruvbox-dark-bg1 align-top"
            >
              <td className="px-1 text-center">
                <button
                  className="text-gruvbox-light-gray dark:text-gruvbox-dark-gray hover:text-gruvbox-light-orange dark:hover:text-gruvbox-dark-orange"
                  title="Inspect row"
                  onClick={() => dispatch({ type: 'expandRow', tabId, table, rowIndex: i })}
                >
                  ›
                </button>
              </td>
              {columns.map((col) => {
                const v = cellValue(row, col)
                const { text, kind } = formatCell(v)
                return (
                  <td
                    key={col.header}
                    className={`border-b border-gruvbox-light-bg1 dark:border-gruvbox-dark-bg1 px-2 py-1 whitespace-nowrap max-w-md overflow-hidden text-ellipsis ${
                      kind === 'null'
                        ? 'text-gruvbox-light-gray dark:text-gruvbox-dark-gray italic'
                        : kind === 'json'
                          ? 'font-mono text-xs text-gruvbox-light-fg3 dark:text-gruvbox-dark-fg3'
                          : ''
                    }`}
                    onContextMenu={(e) => openMenu(e, row, col)}
                  >
                    {text}
                  </td>
                )
              })}
            </tr>
          ))}
        </tbody>
      </table>
      {rows.length > limit && (
        <div className="p-2 text-center text-sm">
          Showing {limit} of {rows.length} rows{' '}
          <button className="btn ml-2" onClick={() => setLimit(limit + PAGE)}>
            Load more
          </button>
        </div>
      )}
      {menu && <ContextMenu x={menu.x} y={menu.y} items={menu.items} onClose={() => setMenu(null)} />}
    </div>
  )
}
