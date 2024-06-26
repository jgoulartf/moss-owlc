"""
    Script para definição de um compilador de owl manchester syntax utilizando a biblioteca ply-lex.

    By: Arthur Lennon && João Goulart
    At: UFERSA - Campus Mossoró - 22/04/2023
    Version: 0.1.0
"""
import sys
import os
print(os.getcwd())
from colorama import just_fix_windows_console, init, Fore
from utils.functions import *


just_fix_windows_console()
init()


executando = True
nova_analise = False

# Loop principal do programa
while executando:
    user_choice = display_menu()
    if user_choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
        handle_user_choice(user_choice)
        nova_analise = True
    else:
        print("\n->Opção inválida<-\n")

    while nova_analise:
        input_nova_analise = input(Fore.WHITE + "\nDeseja analisar outro caso?\n[1] Sim \n[2] Não\n->")
        if input_nova_analise in ['1', '2']:
            if input_nova_analise == '1':
                executando = True
                nova_analise = False
            elif input_nova_analise == '2':
                executando = False
                nova_analise = False
                print("\nExecução do MOSS-OWLC finalizada...")
        else:
            print("\n->Opção inválida<-")
