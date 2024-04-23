from src.ola import lex_owl_input as lexer_parser
from src.osa import parse_owl_input as sint_parser
import os

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()


def display_menu():
    print("""
    \t\t\t\t███╗   ███╗ ██████╗ ███████╗███████╗       ██████╗ ██╗    ██╗██╗      ██████╗
    \t\t\t\t████╗ ████║██╔═══██╗██╔════╝██╔════╝      ██╔═══██╗██║    ██║██║     ██╔════╝
    \t\t\t\t██╔████╔██║██║   ██║███████╗███████╗█████╗██║   ██║██║ █╗ ██║██║     ██║     
    \t\t\t\t██║╚██╔╝██║██║   ██║╚════██║╚════██║╚════╝██║   ██║██║███╗██║██║     ██║     
    \t\t\t\t██║ ╚═╝ ██║╚██████╔╝███████║███████║      ╚██████╔╝╚███╔███╔╝███████╗╚██████╗
    \t\t\t\t╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚══════╝       ╚═════╝  ╚══╝╚══╝ ╚══════╝ ╚═════╝                                                                                                                                                                                                                                    
    """)

    print("- - - - - - - - - - - - - - - - - - - -")
    print("- - - - - OPÇÕES DE ENTRADA - - - - - -")
    print("- - - - - - - - - - - - - - - - - - - -\n")
    print("\t1. Classe primitiva")
    print("\t2. Classe definida")
    print("\t3. Classe com axioma de fechamento (closure axiom)")
    print("\t4. Classe com descrições aninhadas")
    print("\t5. Classe enumerada")
    print("\t6. Classe coberta")
    #print("- - - - - - - - - - - - - - - - - - - -")
    print("\n- - - TESTES COM ERROS SEMÂNTICOS - - -")
    #print("- - - - - - - - - - - - - - - - - - - -")
    print("\t7. Classe primitiva com erro semântico de precedência de operadores")
    print("\t8. Classe com axioma de fechamento com erro semântico de precedência de operadores")
    print("\t9. Classe primitiva com erro semântico de coerção de tipo\n")

    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

    print("\n- - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("\tEscolha a entrada do analisador sintático")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - -")
    input_user = input("->")
    return input_user


def parse_input_and_lexical_analysis():
    input_text = input("Insira o código OWL: ")
    lexer_parser(input_text)


def handle_user_choice(choice):

    if choice == '1':
        print("Analisando classe primitiva...")
        lexer_parser(read_file("./assets/classe_primitiva.txt"))
        sint_parser(read_file('./assets/classe_primitiva.txt'))

    elif choice == '2':
        print("Analisando classe definida...")
        lexer_parser(read_file("./assets/classe_definida.txt"))
        sint_parser(read_file('./assets/classe_definida.txt'))

    elif choice == '3':
        print("Analisando classe com axioma de fechamento...")
        lexer_parser(read_file("./assets/classe_fechamento.txt"))
        sint_parser(read_file('./assets/classe_fechamento.txt'))

    elif choice == '4':
        print("Analisando classe com descrições aninhadas...")
        lexer_parser(read_file("./assets/classe_aninhada.txt"))
        sint_parser(read_file('./assets/classe_aninhada.txt'))

    elif choice == '5':
        print("Analisando classe enumerada...")
        lexer_parser(read_file("./assets/classe_enumerada.txt"))
        sint_parser(read_file('./assets/classe_enumerada.txt'))

    elif choice == '6':
        print("Analisando classe coberta...")
        lexer_parser(read_file("./assets/classe_coberta.txt"))
        sint_parser(read_file('./assets/classe_coberta.txt'))

    elif choice == '7':
        print("Analisando classe primitiva com erro semântico...")
        lexer_parser(read_file("./assets/classe_primitiva_erro_semantico.txt"))
        sint_parser(read_file('./assets/classe_primitiva_erro_semantico.txt'))

    elif choice == '8':
        print("Classe com axioma de fechamento com erro semântico...")
        lexer_parser(read_file("./assets/classe_fechamento_erro_semantico.txt"))
        sint_parser(read_file('./assets/classe_fechamento_erro_semantico.txt'))

    elif choice == '9':
        print("Classe definida com erro semântico...")
        lexer_parser(read_file("./assets/classe_definida_erro_semantico.txt"))
        sint_parser(read_file('./assets/classe_definida_erro_semantico.txt'))

    #elif choice == '9':
    #    print("Analisando a ontologia das pizzas...")
    #    lexer_parser(read_file("../assets/ontologia_pizzas.txt"))
    #    sint_parser(read_file('../assets/ontologia_pizzas.txt'))

    #elif choice == '':
    #    print("Analisando a ontologia do Manoel - Soberania de dados...")
    #    lexer_parser(read_file("../assets/ontologia_manoel.txt"))
    #    sint_parser(read_file('../assets/ontologia_manoel.txt'))

    else:
        print("Escolha inválida!")
