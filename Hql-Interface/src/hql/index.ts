import { autocompletion } from '@codemirror/autocomplete'
import { linter, lintGutter } from '@codemirror/lint'
import type { Extension } from '@codemirror/state'
import { hqlCompletionSource } from './complete.ts'
import { hqlHighlighter } from './highlight.ts'
import { hqlLintSource } from './lint.ts'

/** Grammar-driven editor features; loaded lazily since the parser is ~1 MB. */
export function hqlExtensions(): Extension {
  return [
    hqlHighlighter,
    linter(hqlLintSource, { delay: 500 }),
    lintGutter(),
    autocompletion({ override: [hqlCompletionSource] }),
  ]
}
