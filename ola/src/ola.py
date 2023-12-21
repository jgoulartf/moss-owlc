"""
    ┏┓┓ ┏┓      ┏┓┓ ┏┓   ┓           ┓  ┏┓    ┓       
    ┃┃┃ ┣┫  ━━  ┃┃┃┃┃┃   ┃ ┏┓┓┏ ┓┏┏┏┓┃  ┣┫┏┓┏┓┃┓┏┓┏┓┏┓
    ┗┛┗┛┛┗      ┗┛┗┻┛┗┛  ┗┛┗ ┛┗ ┗┫┗┗┻┗  ┛┗┛┗┗┻┗┗┫┗┗ ┛ 
                                 ┛              ┛     
                                 
    Script para definição de um analisador léxico utilizando a biblioteca ply.
    Ply é um port do yacc-lex para python
    
    
    By: Arthur Lennon && João Goulart
    At: UFERSA - Campus Mossoró - 07/12/2023
"""

import lex
import pandas as pd

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
    'IDENT_KEYWORD',
    'CARDINALITY',
    'IDENT_LPAREN',
]

literals = [
    ''
]

def t_KEYWORD(t):
    r'Class: | EquivalentTo: | Individuals: | SubClassOf: | DisjointClasses: | \
    SOME | some | ALL | all | VALUE | value | MIN | min | MAX | max | EXACTLY \
    | exactly | THAT | that | NOT | not | AND | and | OR | or | Only | only'
    return t

def t_CLASS(t):
    r'([A-Z][a-zA-Z]*)\s | (([A-Z][a-zA-Z]*))\)'
    return t

def t_INDIVIDUAL(t):
    r'([A-Z][a-zA-Z]*|([A-Z][a-zA-Z]*([A-Z][a-zA-Z]*|_[A-Z][a-zA-Z]*)*))[0-9]+'
    return t

def t_PROPERTY(t):
    r'has[A-Z][a-zA-Z]*|is.*Of| [a-z]+[A-Z]+[a-z]+ | \(([a-z]+)\s'
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
    r'\[ | \] | \( | \) | { | } | < | > | = | == | \,'
    return t

def t_NAMESPACE(t):
    r'([a-z]+):'
    return t

def t_SPACE(t):
    r'\s'
    return t

# Ignorar caracteres em branco
t_ignore = '\t\n'

# Tratamento de erros>=
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

owl_source_4 = """
Pizza THAT
    hasCaloricContent some integer[>="400"]
"""

owl_source_5 = """
Pizza THAT
    hasTopping SOME MozzarellaTopping AND
    hasTopping SOME TomatoTopping AND
    hasTopping ONLY 
        (MozzarellaTopping OR
            TomatoTopping OR
            PepperonniTopping)
"""

# Lendo arquivo de teste fornecido pelo professor
with open('Pizza_Ontology_in_OWL_Manchester_Syntax.txt') as f:
    source = f.read()

source = str(source)

source_code_list = [source]
lexical_analysis = []

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Instaciando o lexer e aplicando nos codigos fontes definidos acima
lexer = lex.lex(debug=1)

print("\n\n..........................")
print("...OWL LEXYCAL ANALYZER...")
print("..........................")

# Dicionario para contar cada tipo de lexema.
counters = {
    "KEYWORD": 0,
    "CLASS": 0,
    "INDIVIDUAL": 0,
    "PROPERTY": 0,
    "CARDINALITY": 0,
    "TYPE": 0,
    "NUMERAL": 0,
    "STRING": 0,
    "SPECIAL_SYMBOL": 0,
    "NAMESPACE": 0,
    "SPACE": 0
    }

# Aplicando o lexer em cada codigo fonte e retornando uma lista com os lexemas de cada
for index, src in enumerate(source_code_list):
    print(f"\n\nLENDO CODIGO FONTE {index + 1} E GERANDO LEXEMAS")
    print("...................................................")
    lexer.input(src)
    while True:
        tok = lexer.token()
        
        if not tok:
            break
        
        #counters[f"{tok.type}"] += 1
        #print(f"{tok.type}")
        token = tok.type
        #print("tok", tok.type)
        counters[token] += 1
        
        
        if tok.type != "SPACE":
            print(f"Lexem: {tok.type}, Value: {tok.value}")
        
        lexical_analysis.append(tok)
    print("...................................................")


# TODO: Construir dataframe pandas para representar a tabela de símbolos, quantificando cada tipo de lexema.



symbols_table = pd.DataFrame(list(counters.items()), columns=['Token Type', 'Count'])
print(symbols_table)

