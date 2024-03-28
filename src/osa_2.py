# Yacc example

import ply.yacc

# Importando os tokens do analisador léxico e função de análise léxica
from ola_2 import tokens
from ola_2 import parse_owl_input as lexer_parser

# Função para manipular erros de sintaxe
def p_error(p):
    if p is not None:
        print("\nErro de sintaxe na entrada!\n")
        print("ERRO: ", p)

def p_start(p):
    '''S : primitive_class
            | defined_class
            | closure_class
            | nested_class
            | empty
    '''
    print("Classe primitiva:", p)


# Função para representar uma classe primitiva
def p_primitive_class(p):
    '''primitive_class : KEYWORD_CLASS TWOPOINTS CLASS sub_class_of disjoint_classes individuals primitive_class
                       | empty
    '''
    print("Classe primitiva:", p)

# Função para representar uma classe definida
def p_defined_class(p):
   '''defined_class : KEYWORD_CLASS TWOPOINTS CLASS equivalent_to individuals defined_class
                    | empty
   '''
   print("Classe definida:", p)

# Função para representar uma expressão de subclasse para axioma de fechamento
def p_closure_class(p):
    '''
        closure_class : KEYWORD_CLASS TWOPOINTS CLASS sub_class_of
                      | empty
    '''
    print("Classe para axioma de fechamento:", p)

def p_nested_class(p):
    '''
        nested_class  : KEYWORD_CLASS TWOPOINTS CLASS equivalent_to
                      | empty
    '''
    print("Classe para axioma de fechamento:", p)


# Função para representar uma expressão de subclasse para axioma de fechamento
#def p_closure_subclass_of(p):
#    '''
#        closure_subclass_of :
#    '''
#    print("Subclasse de para axioma de fechamento:", p)


#| SPECIAL_SYMBOL CLASS KEYWORD LPAREN PROPERTY KEYWORD CLASS RPAREN
#| SPECIAL_SYMBOL CLASS KEYWORD LPAREN PROPERTY KEYWORD NAMESPACE TWOPOINTS TYPE LCOLCH SPECIAL_SYMBOL SPECIAL_SYMBOL NUMERAL RCOLCH RPAREN
def p_property_expression(p):
    '''
        property_expression  : PROPERTY KEYWORD CLASS SPECIAL_SYMBOL property_expression
                             | PROPERTY KEYWORD property_expression_closure
                             | PROPERTY KEYWORD NAMESPACE TWOPOINTS TYPE SPECIAL_SYMBOL SPECIAL_SYMBOL NUMERAL SPECIAL_SYMBOL
                             | PROPERTY KEYWORD NAMESPACE TWOPOINTS TYPE SPECIAL_SYMBOL NUMERAL SPECIAL_SYMBOL

                             | empty
    '''
    print("Subclasse de para expressão de propriedade", p)

def p_property_expression_closure(p):
    '''
        property_expression_closure : LPAREN CLASS property_expression_closure
                                    | KEYWORD CLASS property_expression_closure
                                    | KEYWORD CLASS RPAREN property_expression
                                    | empty
    '''





# Função para representar uma classe com axioma de fechamento
#def p_closure_axiom_class(p):
#    '''closure_axiom_class : KEYWORD_CLASS TWOPOINTS CLASS sub_class_of_closure individuals
#                           | KEYWORD_CLASS TWOPOINTS CLASS sub_class_of_closure
#    '''
#    print("Classe com axioma de fechamento:", p)

# Função para representar uma classe com descrições aninhadas
def p_nested_descriptions_class(p):
    '''nested_descriptions_class : KEYWORD_CLASS TWOPOINTS CLASS equivalent_to individuals
                                 | KEYWORD_CLASS TWOPOINTS CLASS equivalent_to
    '''
    print("Classe com descrições aninhadas:", p)

# Função para representar uma classe enumerada
def p_enumerated_class(p):
   '''enumerated_class : KEYWORD_CLASS TWOPOINTS CLASS equivalent_to individuals
                       | KEYWORD_CLASS TWOPOINTS CLASS equivalent_to
   '''
   print("Classe enumerada:", p)

# Função para representar uma classe coberta
def p_covered_class(p):
   '''covered_class : KEYWORD_CLASS TWOPOINTS CLASS equivalent_to individuals
                    | KEYWORD_CLASS TWOPOINTS CLASS equivalent_to
   '''
   print("Classe coberta:", p)

# Função para representar a relação de subclasse
def p_sub_class_of(p):
    '''sub_class_of : KEYWORD_SUBCLASSOF TWOPOINTS sub_class_expression sub_class_of_optional
                    | KEYWORD_SUBCLASSOF TWOPOINTS CLASS SPECIAL_SYMBOL sub_class_of
                    | property_expression SPECIAL_SYMBOL sub_class_of
                    | KEYWORD_SUBCLASSOF CLASS SPECIAL_SYMBOL
                    | empty
    '''
    print("P sub_class_of", p)

def p_sub_class_of_optional(p):
    '''sub_class_of_optional  : sub_class_expression sub_class_of
                              | disjoint_classes
                              | empty
    '''
    print("P p_sub_class_of_optional", p)


# Função para representar a expressão da subclasse
def p_sub_class_expression(p):
    '''
        sub_class_expression : PROPERTY KEYWORD CLASS sub_class_expression
                             | SPECIAL_SYMBOL PROPERTY KEYWORD NAMESPACE TWOPOINTS TYPE sub_class_expression
                             | empty
    '''
    print("P p_sub_class_expression", p)


# Função para representar classes disjuntas
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

# Função para representar uma expressão equivalente
def p_equivalent_to(p):
    '''
        equivalent_to : KEYWORD_EQUIVALENTTO TWOPOINTS equivalent_to_expression
                      | empty
    '''
    print("Equivalente a:", p)

# Função para representar uma expressão equivalente
def p_equivalent_to_expression(p):
   '''
       equivalent_to_expression : CLASS KEYWORD LPAREN PROPERTY KEYWORD NAMESPACE TWOPOINTS TYPE LCOLCH SPECIAL_SYMBOL SPECIAL_SYMBOL NUMERAL RCOLCH RPAREN
                                | CLASS KEYWORD LPAREN PROPERTY KEYWORD CLASS RPAREN
                                | equivalent_to_enumerated_expression

                                | equivalent_to_nested_expression
                                | empty
   '''
   print("Expressão equivalente:", p)

def p_equivalent_to_enumerated_expression(p):
   '''
       equivalent_to_enumerated_expression  : LKEY INSTANCE SPECIAL_SYMBOL
                                            | INSTANCE SPECIAL_SYMBOL
                                            | INSTANCE RKEY
                                            | empty
   '''
   print("Expressão equivalente:", p)

def p_equivalent_to_covered_expression(p):
    '''
        equivalent_to_nested_expression : CLASS KEYWORD equivalent_to_nested_expression
                                        | KEYWORD LPAREN PROPERTY KEYWORD equivalent_to_nested_expression
                                        | LPAREN PROPERTY KEYWORD CLASS RPAREN equivalent_to_nested_expression
                                        |
    '''
    print("Expressão equivalente:", p)


# Função para representar uma expressão de subclasse opcional
# def p_sub_class_of_optional(p):
#    '''sub_class_of_optional  : sub_class_expression sub_class_of
#                              | disjoint_classes
#                              | empty
#    '''
#    print("Subclasse de (opcional):", p)

def p_class_or(p):
    '''
        class_or    : CLASS KEYWORD class_or
                    | CLASS class_or
                    | KEYWORD CLASS
                    | empty
    '''
    print("Subclasse de para expressão de propriedade", p)



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
