import { autocompletion } from '@codemirror/autocomplete'
import { linter, lintGutter } from '@codemirror/lint'
import type { Extension } from '@codemirror/state'
import { hqlCompletionSource } from './complete.ts'
import { hqlHighlighter } from './highlight.ts'
import { hqlLintSource } from './lint.ts'

/**
 * Grammar-driven editor features. This module (and everything it imports)
 * must only ever be loaded via dynamic import('../hql') — see Editor.tsx —
 * so Vite splits the ~1 MB generated parser into a lazy chunk and the app
 * shell paints without it. The editor starts plain and upgrades in place.
 */
export function hqlExtensions(): Extension {
  return [
    hqlHighlighter,
    linter(hqlLintSource, { delay: 500 }),
    lintGutter(),
    autocompletion({ override: [hqlCompletionSource] }),
  ]
}
