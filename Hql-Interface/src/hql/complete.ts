import type { Completion, CompletionContext, CompletionResult } from '@codemirror/autocomplete'
import { Token } from 'antlr4ng'
import { CodeCompletionCore } from 'antlr4-c3'
import { createLexer, parseWithErrors } from './parse.ts'

// Tokens that make no sense as keyword completions: punctuation, identifiers,
// and literal classes. Derived from the vocabulary once.
const ignored: Set<number> = (() => {
  const set = new Set<number>([Token.EOF])
  const vocab = createLexer('').vocabulary
  for (let t = 1; t <= vocab.maxTokenType; t++) {
    const literal = vocab.getLiteralName(t)?.replace(/^'|'$/g, '')
    if (!literal || !/^[a-zA-Z]/.test(literal)) set.add(t)
  }
  return set
})()

/** Index of the token at the caret: the token containing it, else the next one. */
function caretTokenIndex(tokens: Token[], caret: number): number {
  let eofIndex = 0
  for (const t of tokens) {
    if (t.type === Token.EOF) {
      eofIndex = t.tokenIndex
      break
    }
    if (t.channel !== Token.DEFAULT_CHANNEL) continue
    if (caret >= t.start && caret <= t.stop + 1) return t.tokenIndex
    if (t.start > caret) return t.tokenIndex
  }
  return eofIndex
}

// Keyword completion via antlr4-c3: parse to the caret, ask the ATN what
// tokens may follow. Column/table-name completion is the intended next step —
// set core.preferredRules to the grammar's name-reference rules and feed
// candidates.rules from schemas of prior runs; nothing else needs to change.
export function hqlCompletionSource(context: CompletionContext): CompletionResult | null {
  const word = context.matchBefore(/[\w-]+/)
  if (!word && !context.explicit) return null

  const text = context.state.doc.toString()
  const { parser, tokens } = parseWithErrors(text)
  const vocab = parser.vocabulary

  const core = new CodeCompletionCore(parser)
  core.ignoredTokens = ignored
  const caret = caretTokenIndex(tokens.getTokens(), word ? word.from : context.pos)
  const candidates = core.collectCandidates(caret)

  const options: Completion[] = []
  const seen = new Set<string>()
  for (const [type] of candidates.tokens) {
    const label = vocab.getLiteralName(type)?.replace(/^'|'$/g, '')
    if (!label || !/^[a-zA-Z]/.test(label) || seen.has(label)) continue
    seen.add(label)
    options.push({ label, type: 'keyword' })
  }
  if (options.length === 0) return null

  return {
    from: word ? word.from : context.pos,
    options,
    // validFor lets CM filter the ~280-keyword list client-side as the user
    // types instead of re-running this (parse + c3) source per keystroke.
    validFor: /^[\w-]*$/,
  }
}
