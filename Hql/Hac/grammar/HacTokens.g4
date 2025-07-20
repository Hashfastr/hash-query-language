lexer grammar HacTokens;

ASTERISK: '*';
SPACE: (' ' | '\t');
NEWLINE: ('\n' | '\r');
COMMENTSTART: '/' ASTERISK+ NEWLINE;
COMMENTEND: SPACE+ ASTERISK+ '/';
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
    | 'schedule'
);

LISTTAG: (
      'tags'
    | 'falsepositives'
    | 'references'
    | 'changelog'
    | 'actions'
);

CHAR: ~('\n' | '\r');
