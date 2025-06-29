grammar Hac;

import HacTokens;

dacBlock:
    COMMENTSTART (Tags+=tagSection)+ COMMENTEND;

tagSection:
      List=listStart
    | Text=textStart
    | Empty=emptyLine
    ;
    
emptyLine:
      PRELINE NEWLINE
    | SPACE+ ASTERISK NEWLINE;
    
listStart:
    PRELINE ATSIGN Name=LISTTAG SPACE* NEWLINE (Items+=listLine)*;
    
listLine:
    PRELINE Item=listItem;
    
listItem:
    DASH SPACE+ Data=data NEWLINE;

textStart:
    PRELINE ATSIGN Name=TEXTTAG
    (Root=singleTextLine)? NEWLINE (Lines+=textLine)*;

singleTextLine:
    SPACE+ Line=data;

textLine:
      PRELINE Data=data NEWLINE
    | emptyLine;

data:
    ~(ATSIGN) (CHAR | DASH | SPACE | ASTERISK | ATSIGN | TEXTTAG | LISTTAG)+;
