import { useState } from 'react'

function JsonNode({ name, value, depth }: { name?: string; value: unknown; depth: number }) {
  const [open, setOpen] = useState(depth < 3)

  const label = name !== undefined && (
    <span className="text-gruvbox-light-blue dark:text-gruvbox-dark-blue">"{name}": </span>
  )

  if (value === null || value === undefined) {
    return (
      <div>
        {label}
        <span className="text-gruvbox-light-gray dark:text-gruvbox-dark-gray italic">null</span>
      </div>
    )
  }

  if (typeof value === 'string') {
    return (
      <div className="break-all">
        {label}
        <span className="text-gruvbox-light-green dark:text-gruvbox-dark-green">
          "{value}"
        </span>
      </div>
    )
  }

  if (typeof value === 'number' || typeof value === 'boolean') {
    return (
      <div>
        {label}
        <span className="text-gruvbox-light-purple dark:text-gruvbox-dark-purple">
          {String(value)}
        </span>
      </div>
    )
  }

  const isArray = Array.isArray(value)
  const entries = isArray
    ? (value as unknown[]).map((v, i) => [String(i), v] as const)
    : Object.entries(value as Record<string, unknown>)
  const brackets = isArray ? '[]' : '{}'

  if (entries.length === 0) {
    return (
      <div>
        {label}
        {brackets}
      </div>
    )
  }

  return (
    <div>
      <button
        className="select-none text-gruvbox-light-fg3 dark:text-gruvbox-dark-fg3 hover:text-gruvbox-light-orange dark:hover:text-gruvbox-dark-orange"
        onClick={() => setOpen(!open)}
      >
        {open ? '▾' : '▸'} {label}
        {!open && (
          <span className="text-gruvbox-light-gray dark:text-gruvbox-dark-gray">
            {brackets[0]}
            {entries.length}
            {brackets[1]}
          </span>
        )}
      </button>
      {open && (
        <div className="ml-4 border-l border-gruvbox-light-bg2 dark:border-gruvbox-dark-bg2 pl-2">
          {entries.map(([k, v]) => (
            <JsonNode key={k} name={isArray ? undefined : k} value={v} depth={depth + 1} />
          ))}
        </div>
      )}
    </div>
  )
}

export function RowInspector({ row, onClose }: { row: unknown; onClose: () => void }) {
  return (
    <div className="flex h-full flex-col">
      <div className="flex items-center justify-between border-b border-gruvbox-light-bg2 dark:border-gruvbox-dark-bg2 px-2 py-1">
        <span className="text-sm font-semibold">Row</span>
        <div className="flex gap-1">
          <button
            className="btn"
            title="Copy row as JSON"
            onClick={() => void navigator.clipboard.writeText(JSON.stringify(row, null, 2))}
          >
            Copy
          </button>
          <button className="btn" title="Close (Esc)" onClick={onClose}>
            ×
          </button>
        </div>
      </div>
      <div className="min-h-0 flex-1 overflow-auto p-2 font-mono text-xs">
        <JsonNode value={row} depth={0} />
      </div>
    </div>
  )
}
