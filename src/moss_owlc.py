"""
    Script para definição de um compilador de owl manchester syntax utilizando a biblioteca ply-lex.

    By: Arthur Lennon && João Goulart
    At: UFERSA - Campus Mossoró - 22/04/2023
    Version: 0.1.0
"""

from utils.functions import *


# Loop principal do programa
while True:
    user_choice = display_menu()
    if user_choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        handle_user_choice(user_choice)
    else:
        print("Escolha inválida!")
