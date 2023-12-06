"""
    OLA - OWL Lexycal Analyzer
"""

import ply.lex as lex

# Lista de tokens
tokens = [
    'SOME',
    'ALL',
    'VALUE',
    'MIN',
    'MAX',
    'EXACTLY',
    'THAT',
    'NOT',
    'AND',
    'OR',
    'IDENT_CLASS',
    'IDENT_PROPERTY',
    'CARDINALITY'
]

# Expressões regulares para os tokens
t_SOME = r'SOME'
t_ALL = r'ALL'
t_VALUE = r'VALUE'
t_MIN = r'MIN'
t_MAX = r'MAX'
t_EXACTLY = r'EXACTLY'
t_THAT = r'THAT'
t_NOT = r'NOT'
t_AND = r'AND'
t_OR = r'OR'

def t_IDENT_KEYWORD(t):
    r'SOME | ALL | VALUE | MIN | MAX | EXACTLY | THAT | NOT | AND| OR'
    t.value = t.value
    return t

def t_IDENT_CLASS(t):
    r'[A-Z][a-zA-Z]*|([A-Z][a-zA-Z]*([A-Z][a-zA-Z]*|_[A-Z][a-zA-Z]*)*)'
    t.value = t.value
    return t

def t_IDENT_PROPERTY(t):
    r'has[A-Z][a-zA-Z]*|is.*Of'
    t.value = t.value
    return t

def t_CARDINALITY(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar caracteres em branco
t_ignore = ' \t\n'

# Tratamento de erros
def t_error(t):
    print(f"Caractere não reconhecido: {t.value[0]}")
    t.lexer.skip(1)

# Criar o lexer
lexer = lex.lex()

# Exemplo de uso
owl_source = "Pizza THAT hasTopping SOME MozzarellaTopping AND hasTopping SOME TomatoTopping AND hasTopping ONLY (MozzarellaTopping OR TomatoTopping OR PepperonniTopping)"
lexer.input(owl_source)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)




