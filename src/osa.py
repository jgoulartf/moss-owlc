"""
    ┏┓┏┓┏┓      ┏┓┓ ┏┓   ┏┓        •   ┓  ┏┓    ┓
    ┃┃┗┓┣┫  ━━  ┃┃┃┃┃┃   ┗┓┓┏┏┓╋┏┓╋┓┏┏┓┃  ┣┫┏┓┏┓┃┓┏┓┏┓┏┓
    ┗┛┗┛┛┗      ┗┛┗┻┛┗┛  ┗┛┗┫┛┗┗┗┻┗┗┗┗┻┗  ┛┗┛┗┗┻┗┗┫┗┗ ┛
                            ┛                     ┛
    Script para definição de um analisador sintático de owl manchester syntax utilizando a biblioteca ply-yacc.


    By: Arthur Lennon && João Goulart
    At: UFERSA - Campus Mossoró - 07/12/2023
    Version: 0.1.0
"""

import ply.yacc
from ola import tokens
from ola import lexems

def p_error(p):
    print("\nSyntax error in input!\n")
    print(p)
    #if p:
    #    print(f"\nUnexpected \"{p.value}\" at position {p.lexpos} line {p.lineno}\n")
    #else:
    #    print("\nUnexpected end of input\n")


def p_primitive_class(p):
    '''primitive_class : KEYWORD_CLASS TWOPOINTS CLASS sub_class_of disjoint_classes individuals
                       | empty
    '''
    print("P primitive class", p)

#def p_primitive_class(p):
#    '''primitive_class : KEYWORD TWOPOINTS CLASS
#                       | empty
#    '''

# Volta pra cá e bate no keyword...
def p_sub_class_of(p):
    '''sub_class_of : KEYWORD_SUBCLASSOF TWOPOINTS sub_class_expression sub_class_of_optional
                    | empty
    '''
    print("P sub_class_of", p)

def p_sub_class_of_optional(p):
    '''sub_class_of_optional  : sub_class_expression sub_class_of
                              | disjoint_classes
                              | empty
    '''
    print("P p_sub_class_of_optional", p)


# PROPERTY KEYWORD NAMESPACE TWOPOINTS TYPE SPECIAL_SYMBOL SPECIAL_SYMBOL SPECIAL_SYMBOL NUMERAL SPECIAL_SYMBOL
# 
def p_sub_class_expression(p):
    '''
        sub_class_expression : PROPERTY KEYWORD CLASS sub_class_expression
                             | SPECIAL_SYMBOL PROPERTY KEYWORD NAMESPACE TWOPOINTS TYPE sub_class_expression
                             | empty
    '''
    print("P p_sub_class_expression", p)

# def p_closure_class(p):
#     '''
#         closure_class   : CLASS closure_subclass_of
#                         | empty
#     '''

# def p_closure_subclass_of(p):
#     '''
#         closure_subclass_of : CLASS SPECIAL_SYMBOL closure_subclass_of
#                             | PROPERTY KEYWORD NAMESPACE TWOPOINTS TYPE sub_class_expression
#                             | empty
#     '''


def p_disjoint_classes(p):
    '''
        disjoint_classes : KEYWORD_DISJOINT TWOPOINTS CLASS disjoint_classes
                         | SPECIAL_SYMBOL CLASS disjoint_classes
                         | empty
    '''
    print("P p_sub_class_expression", p)


def p_individuals(p):
    '''
        individuals : KEYWORD_INDIVIDUALS TWOPOINTS INDIVIDUAL individuals
                    | SPECIAL_SYMBOL INDIVIDUAL
                    | empty
    '''
    print("P p_individuals", p)


def p_empty(p):
    'empty :'
    pass


owl_input = """
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


# Build the parser
parser = ply.yacc.yacc()

#while True:
#    try:
#       s = owl_input('calc > ')
#    except EOFError:
#       break
#    if not s: continue
    # Analisar a entrada

result = parser.parse(owl_input)

if(result is None):
    print("syntactic analysis completed")
