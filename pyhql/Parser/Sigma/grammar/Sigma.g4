grammar Sigma;

import SigmaTokens;

condition:
      Statement=orStatement;

orStatement:
      Left=andStatement (OR Right+=andStatement)*;
    
andStatement:
      Left=statement (AND Right+=statement)*;

statement:
      ofStatement
    | notStatement
    | bracketStatement
    | selectionIdentifier
    ;
    
notStatement:
    NOT (Bracket=bracketStatement | Selection=selectionIdentifier);

bracketStatement:
    LP Statement=condition RP;
    
ofStatement:
    Specifier=ofSpecifier OF Target=ofTarget;
    
ofSpecifier:
      Int=INT
    | All=ALL
    ;

ofTarget:
      Them=THEM
    | Pattern=patternIdentifier
    ;

selectionIdentifier:
      Basic=basicIdentifier;
      
patternIdentifier: Wildcard=wildcardIdentifier;
    
basicIdentifier:
    Identifier=IDENTIFIER;
    
wildcardIdentifier:
    Identifier=WILDCARD;
    
regexIdentifier:
    Identifier=REGEXIDENTIFIER;
