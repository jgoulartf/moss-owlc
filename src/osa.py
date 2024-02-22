"""
    ┏┓┓ ┏┓      ┏┓┓ ┏┓   ┓           ┓  ┏┓    ┓       
    ┃┃┃ ┣┫  ━━  ┃┃┃┃┃┃   ┃ ┏┓┓┏ ┓┏┏┏┓┃  ┣┫┏┓┏┓┃┓┏┓┏┓┏┓ 
    ┗┛┗┛┛┗      ┗┛┗┻┛┗┛  ┗┛┗ ┛┗ ┗┫┗┗┻┗  ┛┗┛┗┗┻┗┗┫┗┗ ┛ 
                                 ┛              ┛     
                                 
    Script para definição de um analisador sintático de owl manchester syntax utilizando a biblioteca ply-yacc.
    
    
    By: Arthur Lennon && João Goulart
    At: UFERSA - Campus Mossoró - 07/12/2023
    Version: 0.1.0
"""

import ply.yacc as yacc
from ola import tokens

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
#parser = yacc.yacc()

#while True:
#   try:
#       s = raw_input('calc > ')
#   except EOFError:
#       break
#   if not s: continue
#   result = parser.parse(s)
#   print(result)



#
## Determinando propriedades do analisador, tokens e expressoes regulares necessárias para o parser
#tokens = [
#    'SOME',
#    'ALL',
#    'VALUE',
#    'MIN',
#    'MAX',
#    'EXACTLY',
#    'THAT',
#    'NOT',
#    'AND',
#    'OR',
#    'IDENT_CLASS',
#    'IDENT_PROPERTY',
#    'IDENT_KEYWORD',
#    'CARDINALITY',
#    'IDENT_LPAREN',
#    'LPAREN',
#    'RPAREN',
#    'TWOPOINTS',
#]
#
#t_LPAREN  = r'\('
#t_RPAREN  = r'\)'
#t_TWOPOINTS  = r':'
#
#def t_KEYWORD(t):
#    r'Class | EquivalentTo | Individuals | SubClassOf | DisjointClasses | \
#    SOME | some | ALL | all | VALUE | value | MIN | min | MAX | max | EXACTLY \
#    | exactly | THAT | that | NOT | not | AND | and | OR | or | Only | only'
#    return t
#
#
#def t_CLASS(t):
#    r'[A-Z][a-zA-Z]*(?![a-zA-Z0-9_])'
#    return t
#
#
#def t_INDIVIDUAL(t):
#    r'[A-Z][a-zA-Z]*(?:_[A-Z][a-zA-Z]*)*[0-9]+'
#    return t
#
#
#def t_PROPERTY(t):
#    r'has[A-Z][a-zA-Z]*|is.*Of|[a-z]+[A-Z]+[a-z]+(?![a-zA-Z]) | ([a-z]+)\s'
#    return t
#
#
#def t_CARDINALITY(t):
#    r'\s+[0-9]\s+'
#    t.value = int(t.value)
#    return t
#
#
#def t_TYPE(t):
#    r'(integer | INTEGER | boolean | BOOLEAN | decimal | DECIMAL | string | String | REAL | real)'
#    return t
#
#
#def t_NUMERAL(t):
#    r'([0-9]+)'
#    return t
#    
#    
#def t_STRING(t):
#    r'"([A-z]+)"'
#    return t
#
#
#def t_SPECIAL_SYMBOL(t):
#    r'\[ | \] | { | } | < | > | = | == | \,'
#    return t
#
#
#def t_NAMESPACE(t):
#    r'([a-z]+)'
#    return t
#
#
#def t_SPACE(t):
#    r'\s'
#    return t
#
#
## Ignorar tabulação e novalinha
#t_ignore = '\t\n'
#
## Tratamento de erros
#def t_error(t):
#    print(f"Caractere não reconhecido: {t.value[0]}")
#    t.lexer.skip(1)
#
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#
## Lendo arquivo de teste 
#with open('Pizza_Ontology_in_OWL_Manchester_Syntax.txt') as f:
#    owl_source = f.read()
#
#owl_source = str(owl_source)
#lexems = []
#
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#
## Instaciando o lexer e aplicando no codigos fonte OWL MS
#lexer = lex.lex()
#
#print("\n\n..........................")
#print("...OWL LEXYCAL ANALYZER...")
#print("..........................")
#
## Dicionário para a tabela de símbolos
#symbols_table = {
#    "KEYWORD": 0,
#    "CLASS": 0,
#    "INDIVIDUAL": 0,
#    "PROPERTY": 0,
#    "CARDINALITY": 0,
#    "TYPE": 0,
#    "NUMERAL": 0,
#    "STRING": 0,
#    "SPECIAL_SYMBOL": 0,
#    "NAMESPACE": 0,
#    "SPACE": 0,
#    "TWOPOINTS": 0,
#    "LPAREN": 0,
#    "RPAREN": 0,
#}
#
## Aplicando o lexer no codigo fonte e retornando uma lista com os lexemas
#print(f"\n\nLENDO CÓDIGO FONTE...")
#print(f"\n\nGERANDO LEXEMAS\n")
#print("...................................................")
#
#lexer.input(owl_source)
#
#while True:
#    tok = lexer.token()
#    
#    if not tok:
#        break
#    
#    token = tok.type
#    symbols_table[token] += 1
#    lexems.append(tok)
#    
#    if tok.type != "SPACE":
#        print(f"Lexem: {tok.type}, Value: {tok.value}")
#    
#    
#print("\n\n\n.........................")
#print("......Symbols table......")
#print(".........................")
#
#for token_type, count in symbols_table.items():
#    print(f'{token_type:15} {count}')
#