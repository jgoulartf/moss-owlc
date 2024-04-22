from src.ola import lex_owl_input as lexer_parser
from src.osa import parse_owl_input as sint_parser
import os

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()


def display_menu():

    print("\nEscolha o que deseja analisar:")
    print("1. Classe primitiva")
    print("2. Classe definida")
    print("3. Classe com axioma de fechamento (closure axiom)")
    print("4. Classe com descrições aninhadas")
    print("5. Classe enumerada")
    print("6. Classe coberta")
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
    print("7. Classe primitiva com erro semântico")
    print("8. Classe com axioma de fechamento com erro semântico")
    return input("Escolha a entrada do analisador sintático: ")


def parse_input_and_lexical_analysis():
    input_text = input("Insira o código OWL: ")
    lexer_parser(input_text)


def handle_user_choice(choice):
    if choice == '1':
        print("Analisando classe primitiva...")
        lexer_parser(read_file("../assets/classe_primitiva.txt"))
        sint_parser(read_file('../assets/classe_primitiva.txt'))

    elif choice == '2':
        print("Analisando classe definida...")
        lexer_parser(read_file("../assets/classe_definida.txt"))
        sint_parser(read_file('../assets/classe_definida.txt'))

    elif choice == '3':
        print("Analisando classe com axioma de fechamento...")
        lexer_parser(read_file("../assets/classe_fechamento.txt"))
        sint_parser(read_file('../assets/classe_fechamento.txt'))

    elif choice == '4':
        print("Analisando classe com descrições aninhadas...")
        lexer_parser(read_file("../assets/classe_aninhada.txt"))
        sint_parser(read_file('../assets/classe_aninhada.txt'))

    elif choice == '5':
        print("Analisando classe enumerada...")
        lexer_parser(read_file("../assets/classe_enumerada.txt"))
        sint_parser(read_file('../assets/classe_enumerada.txt'))

    elif choice == '6':
        print("Analisando classe coberta...")
        lexer_parser(read_file("../assets/classe_coberta.txt"))
        sint_parser(read_file('../assets/classe_coberta.txt'))

    elif choice == '7':
        print("Analisando classe primitiva com erro semântico...")
        lexer_parser(read_file("../assets/classe_primitiva_erro_semantico.txt"))
        sint_parser(read_file('../assets/classe_primitiva_erro_semantico.txt'))

    elif choice == '8':
        print("Classe com axioma de fechamento com erro semântico...")
        lexer_parser(read_file("../assets/classe_fechamento_erro_semantico.txt"))
        sint_parser(read_file('../assets/classe_fechamento_erro_semantico.txt'))

    elif choice == '9':
        print("Classe definida com erro semântico...")
        lexer_parser(read_file("../assets/classe_definida_erro_semantico.txt"))
        sint_parser(read_file('../assets/classe_definida_erro_semantico.txt'))

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
