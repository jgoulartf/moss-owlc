import ply.lex as lex
import re

from colorama import Fore, Style

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
    'INSTANCE',
    'NEWLINE'
]

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCOLCH = r'\['
t_RCOLCH = r'\]'
t_LKEY = r'\{'
t_RKEY = r'\}'


def t_KEYWORD(t):
    r""" SOME | some | ALL | all | VALUE | value | MIN | min | MAX | max | EXACTLY \
    | exactly | THAT | that | NOT | not | AND | and | OR | or | Only | only"""
    return t


def t_KEYWORD_CLASS(t):
    r"""Class"""
    return t


def t_KEYWORD_EQUIVALENTTO(t):
    r"""EquivalentTo"""
    return t


def t_KEYWORD_INDIVIDUALS(t):
    r"""Individuals"""
    return t


def t_KEYWORD_SUBCLASSOF(t):
    r"""SubClassOf"""
    return t


def t_KEYWORD_DISJOINT(t):
    r"""DisjointClasses"""
    return t


def t_CLASS(t):
    r"""[A-Z][a-zA-Z]*(?![a-zA-Z0-9_])"""
    return t


def t_INDIVIDUAL(t):
    r"""[A-Z][a-zA-Z]*(?:_[A-Z][a-zA-Z]*)*[0-9]+"""
    return t


def t_PROPERTY(t):
    r"""has[A-Z][a-zA-Z]*|is.*Of|[a-z]+[A-Z]+[a-z]+(?![a-zA-Z]) \s | ssn"""
    return t


def t_CARDINALITY(t):
    r"""\s+[0-9]\s+"""
    t.value = int(t.value)
    return t


def t_TYPE(t):
    r"""(integer | INTEGER | boolean | BOOLEAN | decimal | DECIMAL | string | String | REAL | real)"""
    return t


def t_NUMERAL(t):
    r"""([0-9]+)"""
    return t


def t_STRING(t):
    r""""([A-z]+)\""""
    return t


def t_SPECIAL_SYMBOL(t):
    r"""{ | } | < | > | = | == | \,"""
    return t


def t_NAMESPACE(t):
    r"""([a-z]+)"""
    #print("t:", t)
    #re.search(r'([a-z]+):',t)
    #print("re.match: ", )
    #t.value = re.match(r'([a-z]+):', t.value).group(1)
    #t.value = t.value[:-1]  # Removing the colon from the matched text
    return t


def t_TWOPOINTS(t):
    r""":"""
    return t


def t_NEWLINE(t):
    r"""\n"""
    #print("NEWLINE PRINT: ", t.value, t.lexer.lineno)

    #t.lexer.lineno += len(t.value)



t_ignore = ' \t'


def t_error(t):
    print(f"Caractere não reconhecido: {t.value[0]}")
    #t.lexer.skip(1)


def lex_owl_input(input_text):
    # Build the lexer
    lexer = lex.lex()

    # Applying lexer on the OWL code input and returning a list with the lexemes
    lexer.input(input_text)

    print("\n- - - - - - - - - - - - - - - - - - -")
    print("- - - - OWL LEXYCAL ANALYZER - - - -")
    print("- - - - - - - - - - - - - - - - - - -")

    # Dictionary for the symbol table
    symbols_table = {token_type: 0 for token_type in tokens}

    # Applying the lexer on the OWL code and returning a list with the lexemes
    print("\n- - - - - - - - - - - - - - - - - - -")
    print(f"- - - - - GERANDO LEXEMAS - - - - - -")
    print(f"- - - - - - - - - - - - - - - - - - -")

    while True:
        try:
            tok = lexer.token()

        except:
            break

        if not tok:
            break

        token = tok.type
        symbols_table[token] += 1

        if tok.type != "SPACE":
            print(Fore.GREEN + f"\tLexem: {tok.type}, Value: {tok.value}")

    print(Style.RESET_ALL + "\n- - - - - - - - - - - - - - - - - - -")
    print("- - - - - - Symbols table - - - - - -")
    print("- - - - - - - - - - - - - - - - - - -")

    for token_type, count in symbols_table.items():
        print(Fore.GREEN + f'\t{token_type:15}\t{count}')

    print(Style.RESET_ALL)
