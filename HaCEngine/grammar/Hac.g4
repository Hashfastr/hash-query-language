grammar Hac;

import HacTokens;

dacBlock:
    COMMENTSTART (Tags+=tagSection)+ COMMENTEND NEWLINE* (Hql=hqlText)?;

tagSection:
      List=listStart
    | Text=textStart
    | Empty=emptyLine
    ;
    
emptyLine:
      preline endline;
    
listStart:
    preline Name=listTag endline (Items+=listLine)*;
    
listLine:
    preline Item=listItem;
    
listItem:
    DASH SPACE+ Data=data endline;

textStart:
    preline Name=textTag (Root=singleTextLine | endline) (Lines+=textLine)*;
    
textTag:
    ATSIGN Name=TEXTTAG;

listTag:
    ATSIGN Name=LISTTAG;

singleTextLine:
    SPACE+ Line=allData endline;

textLine:
      preline Line=data endline
    | emptyLine;
    
preline:
    SPACE ASTERISK SPACE*;

endline:
    SPACE* NEWLINE;

data:
    ~(ATSIGN | NEWLINE | SPACE) (CHAR | DASH | SPACE | ASTERISK | ATSIGN | TEXTTAG | LISTTAG)+;

allData:
    (CHAR | DASH | SPACE | ASTERISK | ATSIGN | TEXTTAG | LISTTAG)+;
    
hqlText:
    (Lines+=hqlLine)+;

hqlLine:
    Data=allData NEWLINE;
