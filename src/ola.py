"""
    ┏┓┓ ┏┓      ┏┓┓ ┏┓   ┓           ┓  ┏┓    ┓
    ┃┃┃ ┣┫  ━━  ┃┃┃┃┃┃   ┃ ┏┓┓┏ ┓┏┏┏┓┃  ┣┫┏┓┏┓┃┓┏┓┏┓┏┓
    ┗┛┗┛┛┗      ┗┛┗┻┛┗┛  ┗┛┗ ┛┗ ┗┫┗┗┻┗  ┛┗┛┗┗┻┗┗┫┗┗ ┛
                                 ┛              ┛

    Script para definição de um analisador léxico de owl manchester syntax utilizando a biblioteca ply-lex.


    By: Arthur Lennon && João Goulart
    At: UFERSA - Campus Mossoró - 07/12/2023
    Version: 0.1.0
"""

import ply.lex as lex

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
    'CLASS',
    'PROPERTY',
    'KEYWORD',
    'KEYWORD_CLASS',
    'KEYWORD_EQUIVALENTTO',
    'KEYWORD_INDIVIDUALS',
    'KEYWORD_SUBCLASSOF',
    'KEYWORD_DISJOINT',
    'CARDINALITY',
    'IDENT_LPAREN',
    'LPAREN',
    'RPAREN',
    'TWOPOINTS',
    'SPECIAL_SYMBOL',
    'NAMESPACE',
    'TYPE',
    'NUMERAL',
    'INDIVIDUAL'
]

t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_TWOPOINTS  = r':'

def t_KEYWORD(t):
    r' SOME | some | ALL | all | VALUE | value | MIN | min | MAX | max | EXACTLY \
    | exactly | THAT | that | NOT | not | AND | and | OR | or | Only | only'
    return t

def t_KEYWORD_CLASS(t):
    r'Class'
    return t

def t_KEYWORD_EQUIVALENTTO(t):
    r'EquivalentTo'
    return t

def t_KEYWORD_INDIVIDUALS(t):
    r'Individuals'
    return t

def t_KEYWORD_SUBCLASSOF(t):
    r'SubClassOf'
    return t

def t_KEYWORD_DISJOINT(t):
    r'DisjointClasses'
    return t

def t_CLASS(t):
    r'[A-Z][a-zA-Z]*(?![a-zA-Z0-9_])'
    return t


def t_INDIVIDUAL(t):
    r'[A-Z][a-zA-Z]*(?:_[A-Z][a-zA-Z]*)*[0-9]+'
    return t


def t_PROPERTY(t):
    r'has[A-Z][a-zA-Z]*|is.*Of|[a-z]+[A-Z]+[a-z]+(?![a-zA-Z]) \s'
    return t


def t_CARDINALITY(t):
    r'\s+[0-9]\s+'
    t.value = int(t.value)
    return t


def t_TYPE(t):
    r'(integer | INTEGER | boolean | BOOLEAN | decimal | DECIMAL | string | String | REAL | real)'
    return t


def t_NUMERAL(t):
    r'([0-9]+)'
    return t


def t_STRING(t):
    r'"([A-z]+)"'
    return t


def t_SPECIAL_SYMBOL(t):
    r'\[ | \] | { | } | < | > | = | == | \,'
    return t


def t_NAMESPACE(t):
    r'([a-z]+)'
    return t

#def t_SPACE(t):
#    r''
#    return t

# Ignorar tabulação e novalinha
t_ignore = ' \t\n'

# Tratamento de erros
def t_error(t):
    print(f"Caractere não reconhecido: {t.value[0]}")
    t.lexer.skip(1)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Lendo arquivo de teste
with open('../assets/Pizza_Ontology_in_OWL_Manchester_Syntax.txt') as f:
    owl_source = f.read()

owl_source = str(owl_source)
owl_source_2 = """
Class: Pizza

SubClassOf:
    hasBase some PizzaBase,
    hasCaloricContent some xsd:integer

DisjointClasses:
    Pizza, PizzaBase, PizzaTopping

Individuals:
    CustomPizza1,
    CustomPizza2
"""

owl_input_2 = """Class: Pizza"""


lexems = []

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Instaciando o lexer e aplicando no codigos fonte OWL MS
lexer = lex.lex()

print("\n\n..........................")
print("...OWL LEXYCAL ANALYZER...")
print("..........................")

# Dicionário para a tabela de símbolos
symbols_table = {
    "KEYWORD": 0,
    "KEYWORD_CLASS": 0,
    "KEYWORD_EQUIVALENTTO": 0,
    "KEYWORD_INDIVIDUALS": 0,
    "KEYWORD_SUBCLASSOF": 0,
    "KEYWORD_DISJOINT": 0,
    "CLASS": 0,
    "INDIVIDUAL": 0,
    "PROPERTY": 0,
    "CARDINALITY": 0,
    "TYPE": 0,
    "NUMERAL": 0,
    "STRING": 0,
    "SPECIAL_SYMBOL": 0,
    "NAMESPACE": 0,
    "SPACE": 0,
    "TWOPOINTS": 0,
    "LPAREN": 0,
    "RPAREN": 0,
}

# Aplicando o lexer no codigo fonte e retornando uma lista com os lexemas
print(f"\n\nLENDO CÓDIGO FONTE...")
print(f"\n\nGERANDO LEXEMAS\n")
print("...................................................")

lexer.input(owl_source_2)

while True:
    tok = lexer.token()

    if not tok:
        break

    token = tok.type
    symbols_table[token] += 1
    lexems.append(tok)

    if tok.type != "SPACE":
        print(f"Lexem: {tok.type}, Value: {tok.value}")


print("\n\n\n.........................")
print("......Symbols table......")
print(".........................")

for token_type, count in symbols_table.items():
    print(f'{token_type:15} {count}')
