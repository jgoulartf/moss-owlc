import ply.lex as lex
import re

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
    'LCOLCH',
    'RCOLCH',
    'LKEY',
    'RKEY',
    'TWOPOINTS',
    'SPECIAL_SYMBOL',
    'NAMESPACE',
    'TYPE',
    'NUMERAL',
    'INDIVIDUAL',
    'INSTANCE'
]

t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LCOLCH  = r'\['
t_RCOLCH  = r'\]'
t_LKEY = r'\{'
t_RKEY = r'\}'

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
    r'has[A-Z][a-zA-Z]*|is.*Of|[a-z]+[A-Z]+[a-z]+(?![a-zA-Z]) \s | ssn'
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
    r'{ | } | < | > | = | == | \,'
    return t

def t_NAMESPACE(t):
    r'([a-z]+)'
    #print("t:", t)
    #re.search(r'([a-z]+):',t)
    #print("re.match: ", )
    #t.value = re.match(r'([a-z]+):', t.value).group(1)
    #t.value = t.value[:-1]  # Removing the colon from the matched text
    return t

def t_TWOPOINTS(t):
    r':'
    return t

# Ignorar tabulação e novalinha
t_ignore = ' \t\n'

# Tratamento de erros
def t_error(t):
    print(f"Caractere não reconhecido: {t.value[0]}")
    #t.lexer.skip(1)

# Função principal que lida com a entrada do usuário e analisa o código OWL
def parse_owl_input(input_text):
    # Build the lexer
    lexer = lex.lex()

    # Applying lexer on the OWL code input and returning a list with the lexemes
    lexer.input(input_text)

    print("\n\n..........................")
    print("...OWL LEXYCAL ANALYZER...")
    print("..........................")

    # Dictionary for the symbol table
    symbols_table = {token_type: 0 for token_type in tokens}

    # Applying the lexer on the OWL code and returning a list with the lexemes
    print(f"\n\nREADING SOURCE CODE...")
    print(f"\n\nGENERATING LEXEMS\n")
    print("...................................................")

    while True:
        try:
            tok = lexer.token()
            #if tok.type == "NAMESPACE":
            #    print("TOK: ", tok)
            #    print("LEXMATCH: ", lexer.lexmatch)
            #
            #    #tok.value = lexer.lexmatch.group(0)

        except:
            break


        if not tok:
            break

        token = tok.type
        symbols_table[token] += 1

        if tok.type != "SPACE":
            print(f"Lexem: {tok.type}, Value: {tok.value}")

    print("\n\n\n.........................")
    print("......Symbols table......")
    print(".........................")

    for token_type, count in symbols_table.items():
        print(f'{token_type:15} {count}')

# Função para exibir o menu e obter a escolha do usuário
def display_menu():
    print("\nEscolha o que deseja analisar:")
    print("1. Classe primitiva")
    print("2. Classe definida")
    print("3. Classe com axioma de fechamento (closure axiom)")
    print("4. Classe com descrições aninhadas")
    print("5. Classe enumerada")
    print("6. Classe coberta")
    print("7. Ontologia das pizzas")
    print("8. Ontologia do Manoel - Soberania de dados")
    return input("Escolha a entrada do analisador sintático: ")

# Loop principal do programa
#while True:
#    user_choice = display_menu()
#    if user_choice in ['1', '2', '3', '4', '5', '6', '7', '8']:
#        handle_user_choice(user_choice)
#    else:
#        print("Escolha inválida!")

