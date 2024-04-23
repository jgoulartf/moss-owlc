"""
    Script para definição de um analisador sintático de owl manchester syntax utilizando a biblioteca ply-lex.


    By: Arthur Lennon && João Goulart
    At: UFERSA - Campus Mossoró - 07/03/2023
    Version: 0.1.0
"""
import ply.yacc
from ola import tokens
from ply.yacc import Grammar, GrammarError

# Global
error_count = 0
parser = None
prod_counter = 0


# Gramática do analisador sintático
def p_start(p):
    """

    S : primitive_class
      | defined_class
      | closure_class
      | nested_class
      | covered_class
      | enumerated_class
      | other_class
      | empty

    primitive_class : KEYWORD_CLASS TWOPOINTS CLASS sub_class_of disjoint_classes individuals primitive_class
                    | empty

    other_class     : KEYWORD_CLASS TWOPOINTS CLASS sub_class_of individuals other_class
                    | empty

    defined_class : KEYWORD_CLASS TWOPOINTS CLASS equivalent_to individuals defined_class
                  | empty

    nested_class  : KEYWORD_CLASS TWOPOINTS CLASS equivalent_to
                  | empty

    covered_class : KEYWORD_CLASS TWOPOINTS CLASS equivalent_to individuals
                  | KEYWORD_CLASS TWOPOINTS CLASS equivalent_to

    enumerated_class : KEYWORD_CLASS TWOPOINTS CLASS equivalent_to individuals
                     | KEYWORD_CLASS TWOPOINTS CLASS equivalent_to

    closure_class : KEYWORD_CLASS TWOPOINTS CLASS sub_class_of
                  | empty

    sub_class_of : KEYWORD_SUBCLASSOF TWOPOINTS sub_class_expression sub_class_of_optional
                 | KEYWORD_SUBCLASSOF TWOPOINTS CLASS KEYWORD sub_class_of
                 | KEYWORD_SUBCLASSOF TWOPOINTS CLASS SPECIAL_SYMBOL sub_class_of
                 | KEYWORD_SUBCLASSOF TWOPOINTS NAMESPACE KEYWORD LPAREN property_expression sub_class_of
                 | KEYWORD_SUBCLASSOF CLASS SPECIAL_SYMBOL sub_class_of
                 | PROPERTY KEYWORD CLASS SPECIAL_SYMBOL sub_class_of
                 | PROPERTY KEYWORD LPAREN CLASS RPAREN sub_class_of
                 | PROPERTY KEYWORD LPAREN equivalent_to_covered_expression RPAREN sub_class_of
                 | empty

    sub_class_expression : PROPERTY KEYWORD CLASS sub_class_expression
                         | SPECIAL_SYMBOL PROPERTY KEYWORD NAMESPACE TWOPOINTS TYPE sub_class_expression
                         | empty


    sub_class_of_optional : sub_class_expression sub_class_of
                          | disjoint_classes
                          | empty

    equivalent_to : KEYWORD_EQUIVALENTTO TWOPOINTS equivalent_to_expression
                  | empty



    equivalent_to_expression : CLASS KEYWORD LPAREN PROPERTY KEYWORD NAMESPACE TWOPOINTS TYPE LCOLCH SPECIAL_SYMBOL SPECIAL_SYMBOL NUMERAL RCOLCH RPAREN
                             | CLASS KEYWORD LPAREN PROPERTY KEYWORD CLASS RPAREN equivalent_to_expression
                             | CLASS KEYWORD LPAREN PROPERTY KEYWORD LPAREN property_expression equivalent_to_expression
                             | KEYWORD LPAREN PROPERTY KEYWORD LPAREN property_expression equivalent_to_expression
                             | KEYWORD LPAREN PROPERTY KEYWORD NAMESPACE TWOPOINTS TYPE RPAREN equivalent_to_expression
                             | SPECIAL_SYMBOL CLASS equivalent_to_expression
                             | SPECIAL_SYMBOL CLASS SPECIAL_SYMBOL equivalent_to_expression
                             | equivalent_to_enumerated_expression
                             | equivalent_to_nested_expression
                             | equivalent_to_covered_expression
                             | empty

    equivalent_to_enumerated_expression  : LKEY INSTANCE SPECIAL_SYMBOL
                                        | INSTANCE SPECIAL_SYMBOL
                                        | INSTANCE RKEY
                                        | empty

    equivalent_to_nested_expression : CLASS KEYWORD equivalent_to_nested_expression
                                    | KEYWORD LPAREN PROPERTY KEYWORD equivalent_to_nested_expression
                                    | LPAREN PROPERTY KEYWORD CLASS RPAREN equivalent_to_nested_expression
                                    |

    individuals : KEYWORD_INDIVIDUALS TWOPOINTS INDIVIDUAL individuals
                | SPECIAL_SYMBOL INDIVIDUAL individuals
                | empty

    property_expression  : PROPERTY KEYWORD CLASS SPECIAL_SYMBOL property_expression
                         | PROPERTY KEYWORD NUMERAL NAMESPACE TWOPOINTS TYPE property_expression
                         | PROPERTY KEYWORD LPAREN property_expression
                         | PROPERTY KEYWORD property_expression_closure
                         | PROPERTY KEYWORD CLASS RPAREN property_expression
                         | PROPERTY KEYWORD NAMESPACE TWOPOINTS TYPE SPECIAL_SYMBOL SPECIAL_SYMBOL NUMERAL SPECIAL_SYMBOL
                         | PROPERTY KEYWORD NAMESPACE TWOPOINTS TYPE SPECIAL_SYMBOL NUMERAL SPECIAL_SYMBOL
                         | PROPERTY KEYWORD NAMESPACE TWOPOINTS TYPE RPAREN
                         | RPAREN property_expression
                         | empty

    equivalent_to_covered_expression : CLASS KEYWORD equivalent_to_covered_expression
                                     | CLASS equivalent_to_covered_expression
                                     | KEYWORD CLASS
                                     | empty

    disjoint_classes : KEYWORD_DISJOINT TWOPOINTS CLASS disjoint_classes
                     | SPECIAL_SYMBOL CLASS disjoint_classes
                     | empty

    property_expression_closure : LPAREN CLASS property_expression_closure
                                | KEYWORD CLASS property_expression_closure
                                | KEYWORD CLASS RPAREN property_expression
                                | empty

    nested_descriptions_class : KEYWORD_CLASS TWOPOINTS CLASS equivalent_to individuals
                              | KEYWORD_CLASS TWOPOINTS CLASS equivalent_to


    """
    global prod_counter
    prod_counter += 1
    #print(p.slice)
    #print(p.parser.statestack)
    #print(p.parser.symstack)


def p_error(p):
    global error_count
    error_count = error_count + 1

    if p:
        print("\nERROR:")
        print(
            f"  - Token type: {p.type}\n  - Token value: {p.value}\n  - Line number: {p.lineno}\n  - Token position: {p.lexpos}\n  - Text near token: {p.lexer.lexdata[max(p.lexpos - 10, 0):p.lexpos + 10]}")
        print(f"Unexpected {p.type} at line {p.lineno} position {p.lexpos}")
    else:
        print("Syntax error: Unexpected end of file")


def p_empty(p):
    """empty :"""
    pass


def parse_owl_input(input_text):
    global parser

    parser = ply.yacc.yacc()

    result = parser.parse(input_text, tracking=True)

    if result is None and error_count == 0:
        print("\n\n- - - - - - - - - - - - - - -")
        print("Análise concluída SEM ERROS")
        print("- - - - - - - - - - - - - - -")
    elif error_count > 0:
        print("\n\n- - - - - - - - - - - - - - -")
        print("Análise concluída COM ERROS")
        print("- - - - - - - - - - - - - - -")
