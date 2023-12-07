"""
    OLA - OWL Lexycal Analyzer

    Script para definição de um analisador léxico utilizando a biblioteca ply.
    Ply é um port do yacc-lex para python
    
    TODO: Saber se é possivel fazer o analisador sintático usando o ply

    At: UFERSA - Campus Mossoró - 07/12/2023
"""

import lex

# Determinando propriedades do analisador, tokens e expressoes regulares necessárias para o parser

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
    'IDENT_KEYWORD'
    'CARDINALITY'
]

def t_IDENT_KEYWORD(t):
    r'SOME | some | ALL | all | VALUE | value | MIN | min | MAX | max | EXACTLY | exactly | THAT | that | NOT | not | AND | and | OR | or'
    
    return t

def t_IDENT_CLASS(t):
    r'[A-Z][a-zA-Z]*|([A-Z][a-zA-Z]*([A-Z][a-zA-Z]*|_[A-Z][a-zA-Z]*)*)'
    
    return t

def t_IDENT_PROPERTY(t):
    r'has[A-Z][a-zA-Z]*|is.*Of'
    t.value = t.value
    return t

def t_IDENT_CARDINALITY(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar caracteres em branco
t_ignore = ' \t\n'

# Tratamento de erros
def t_error(t):
    print(f"Caractere não reconhecido: {t.value[0]}")
    t.lexer.skip(1)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Exemplos de codigo fonte owl em manchester syntax
owl_source_1 = """
Pizza THAT 
    hasTopping SOME MozzarellaTopping AND 
    hasTopping SOME TomatoTopping AND 
    hasTopping ONLY (MozzarellaTopping OR TomatoTopping OR PepperonniTopping)
"""

owl_source_2 = """
Pizza THAT
    hasTopping min 3
"""

owl_source_3 = """
PizzaTopping AND
    CheeseTopping THAT
        hasSpiciness SOME Mild and
        hasCountryOfOrigin VALUE Italy
"""

# Listando codigos fontes em OWL
source_code_list = [owl_source_1, owl_source_2, owl_source_3]
lexical_analysis = []

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Instaciando o lexer e aplicando nos codigos fontes definidos acima
lexer = lex.lex()

print("\n\n..........................")
print("...OWL LEXYCAL ANALYZER...")
print("..........................")

# Aplicando o lexer em cada codigo fonte e retornando uma lista com os lexemas de cada
for index, src in enumerate(source_code_list):
    print(f"\n\nLENDO CODIGO FONTE {index + 1} E GERANDO LEXEMAS")
    print("...................................................")
    lexer.input(src)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
        lexical_analysis.append(tok)
    print("...................................................")

print()

