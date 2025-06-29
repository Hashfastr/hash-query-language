lexer grammar HacTokens;

ASTERISK: '*';
SPACE: (' ' | '\t');
NEWLINE: ('\n' | '\r');
COMMENTSTART: '/' ASTERISK+ NEWLINE;
COMMENTEND: SPACE+ ASTERISK+ '/';
PRELINE: SPACE ASTERISK SPACE+;
ATSIGN: '@';
DASH: '-';

TEXTTAG: (
      'title'
    | 'author'
    | 'id'
    | 'status'
    | 'level'
    | 'description'
    | 'triage'
    | 'authornotes'
);

LISTTAG: (
      'tags'
    | 'falsepositives'
    | 'references'
    | 'changelog'
);

CHAR: ~('\n' | '\r');
