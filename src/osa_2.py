"""
    ┏┓┓ ┏┓      ┏┓┓ ┏┓   ┓           ┓  ┏┓    ┓
    ┃┃┃ ┣┫  ━━  ┃┃┃┃┃┃   ┃ ┏┓┓┏ ┓┏┏┏┓┃  ┣┫┏┓┏┓┃┓┏┓┏┓┏┓
    ┗┛┗┛┛┗      ┗┛┗┻┛┗┛  ┗┛┗ ┛┗ ┗┫┗┗┻┗  ┛┗┛┗┗┻┗┗┫┗┗ ┛
                                 ┛              ┛

    Script para definição de um analisador sintát de owl manchester syntax utilizando a biblioteca ply-lex.


    By: Arthur Lennon && João Goulart
    At: UFERSA - Campus Mossoró - 07/12/2023
    Version: 0.1.0
"""

import ply.yacc

# Importando os tokens do analisador léxico e função de análise léxica
from ola_2 import tokens
from ola_2 import parse_owl_input as lexer_parser

def p_error(p):
    if p:
        print("\nERROR:")
        print(f"  - Token type: {p.type}\n  - Token value: {p.value}\n  - Line number: {p.lineno}\n  - Token position: {p.lexpos}\n  - Text near token: {p.lexer.lexdata[max(p.lexpos-10, 0):p.lexpos+10]}")
    else:
        print("Syntax error: Unexpected end of file")


# Gramática do analisador sintático
def p_start(p):
    '''

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


    '''

# Função para representar o token vazio
def p_empty(p):
    'empty :'
    pass


# Função principal que lida com a entrada do usuário e analisa o código OWL
def parse_owl_input(input_text):
    # Build the parser
    parser = ply.yacc.yacc()

    result = parser.parse(input_text)

    if result is None:
        print("Análise sintática concluída")


# Função para ler o arquivo de texto e retornar seu conteúdo
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()


# Função principal que lida com a entrada do usuário e chama o analisador léxico
def parse_input_and_lexical_analysis():
    input_text = input("Insira o código OWL: ")
    lexer_parser(input_text)  # Chamando o analisador léxico


# Função para lidar com a escolha do usuário e chamar a função de análise correspondente
def handle_user_choice(choice):
    if choice == '1':
        print("Analisando classe primitiva...")
        lexer_parser(read_file("../assets/classe_primitiva.txt"))
        parse_owl_input(read_file('../assets/classe_primitiva.txt'))

    elif choice == '2':
        print("Analisando classe definida...")
        lexer_parser(read_file("../assets/classe_definida.txt"))
        parse_owl_input(read_file('../assets/classe_definida.txt'))

    elif choice == '3':
        print("Analisando classe com axioma de fechamento...")
        lexer_parser(read_file("../assets/classe_fechamento.txt"))
        parse_owl_input(read_file('../assets/classe_fechamento.txt'))

    elif choice == '4':
        print("Analisando classe com descrições aninhadas...")
        lexer_parser(read_file("../assets/classe_aninhada.txt"))
        parse_owl_input(read_file('../assets/classe_aninhada.txt'))

    elif choice == '5':
        print("Analisando classe enumerada...")
        lexer_parser(read_file("../assets/classe_enumerada.txt"))
        parse_owl_input(read_file('../assets/classe_enumerada.txt'))

    elif choice == '6':
        print("Analisando classe coberta...")
        lexer_parser(read_file("../assets/classe_coberta.txt"))
        parse_owl_input(read_file('../assets/classe_coberta.txt'))

    elif choice == '7':
        print("Analisando a ontologia das pizzas...")
        lexer_parser(read_file("../assets/ontologia_pizzas.txt"))
        parse_owl_input(read_file('../assets/ontologia_pizzas.txt'))

    elif choice == '8':
        print("Analisando a ontologia do Manoel - Soberania de dados...")
        lexer_parser(read_file("../assets/ontologia_manoel.txt"))
        parse_owl_input(read_file('../assets/ontologia_manoel.txt'))

    else:
        print("Escolha inválida!")

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
while True:
    user_choice = display_menu()
    if user_choice in ['1', '2', '3', '4', '5', '6', '7', '8']:
        handle_user_choice(user_choice)
    else:
        print("Escolha inválida!")
