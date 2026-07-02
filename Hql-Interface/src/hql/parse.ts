import {
  BaseErrorListener,
  CharStream,
  CommonTokenStream,
  Token,
  type ATNSimulator,
  type RecognitionException,
  type Recognizer,
} from 'antlr4ng'
import { HqlLexer } from './generated/HqlLexer.ts'
import { HqlParser } from './generated/HqlParser.ts'

export interface SyntaxError {
  line: number // 1-based
  column: number // 0-based char position in line
  length: number // offending token length, 0 if unknown
  message: string
}

class CollectingErrorListener extends BaseErrorListener {
  errors: SyntaxError[] = []

  override syntaxError<S extends Token, T extends ATNSimulator>(
    _recognizer: Recognizer<T>,
    offendingSymbol: S | null,
    line: number,
    charPositionInLine: number,
    msg: string,
    _e: RecognitionException | null,
  ): void {
    let length = 0
    if (offendingSymbol && offendingSymbol.text) {
      length = offendingSymbol.text.length
    }
    this.errors.push({ line, column: charPositionInLine, length, message: msg })
  }
}

export function createLexer(input: string): HqlLexer {
  const lexer = new HqlLexer(CharStream.fromString(input))
  lexer.removeErrorListeners()
  return lexer
}

/** All tokens including hidden channel (comments, whitespace). */
export function lexAll(input: string): Token[] {
  const lexer = createLexer(input)
  return lexer.getAllTokens()
}

export interface ParseResult {
  parser: HqlParser
  tokens: CommonTokenStream
  errors: SyntaxError[]
}

export function parseWithErrors(input: string): ParseResult {
  const lexer = createLexer(input)
  const errorListener = new CollectingErrorListener()
  lexer.addErrorListener(errorListener)

  const tokens = new CommonTokenStream(lexer)
  const parser = new HqlParser(tokens)
  parser.removeErrorListeners()
  parser.addErrorListener(errorListener)
  parser.top()

  return { parser, tokens, errors: errorListener.errors }
}

// Parsing runs on the main thread: interactive queries are small (<5 KB) and
// lint/completion are debounced. If profiling ever shows hitches, this module
// is the single seam to move behind a web worker.
