import type { Diagnostic } from '@codemirror/lint'
import type { EditorView } from '@codemirror/view'
import { parseWithErrors } from './parse.ts'

export function hqlLintSource(view: EditorView): Diagnostic[] {
  const doc = view.state.doc
  const text = doc.toString()
  if (!text.trim()) return []

  return parseWithErrors(text).errors.map((err) => {
    const line = doc.line(Math.max(1, Math.min(err.line, doc.lines)))
    const from = Math.min(line.from + err.column, line.to)
    const to = Math.max(from, Math.min(from + Math.max(err.length, 1), doc.length))
    return { from, to, severity: 'error' as const, message: err.message }
  })
}
