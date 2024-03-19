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

#start = 'primitive_class'

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

#def p_primitive_class(p):
#    '''primitive_class : KEYWORD TWOPOINTS CLASS sub_class_of disjoint_classes individuals
#                       | empty
#    '''

def p_primitive_class(p):
    '''primitive_class : KEYWORD TWOPOINTS CLASS primitive_class
                       | empty
    '''
#
#
#
#def p_sub_class_of(p):
#    '''sub_class_of : KEYWORD TWOPOINTS sub_class_expression sub_class_of
#                    | SPECIAL_SYMBOL sub_class_expression sub_class_of
#                    | empty
#    '''
#
#def p_sub_class_expression(p):
#    '''
#        sub_class_expression : PROPERTY KEYWORD CLASS
#                             | PROPERTY KEYWORD NAMESPACE TWOPOINTS TYPE SPECIAL_SYMBOL SPECIAL_SYMBOL SPECIAL_SYMBOL NUMERAL SPECIAL_SYMBOL
#                             | empty
#    '''
#
#def p_disjoint_classes(p):
#    '''
#        disjoint_classes : KEYWORD TWOPOINTS CLASS disjoint_classes
#                         | SPECIAL_SYMBOL CLASS
#                         | empty
#    '''
#
#def p_individuals(p):
#    '''
#        individuals : KEYWORD TWOPOINTS INDIVIDUAL individuals
#                    | SPECIAL_SYMBOL INDIVIDUAL
#                    | empty
#    '''

def p_empty(p):
    'empty :'
    pass

owl_input = """
Class: Pizza
"""

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
print(result)
