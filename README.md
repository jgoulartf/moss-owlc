**README**

# MOSS-OWLC (Compilador de Linguagem Web de Ontologia de Mossoró)

O MOSS-OWLC é um compilador para OWL (Ontology Web Language) desenvolvido como um projeto para a disciplina de compiladores na UFERSA (Universidade Federal do Semi-Árido), termo 2023.2, localizada em Mossoró/RN, Brasil.

> Estado atual: O MOSS-OWLC está em fase de desenvolvimento e atualmente está sendo construido o analisador sintático do compilador completo, portanto, executar o OLA isoladamente não faz mais sentido.

## Visão Geral

O MOSS-OWLC tem como objetivo fornecer uma ferramenta para compilar OWL, uma linguagem usada para representar conhecimento sobre um domínio e descrever as relações entre entidades dentro desse domínio. 
<u>Este compilador analisa o código OWL e gera uma saída correspondente legível por máquina.</u>

## Funcionalidades

- Análise léxica usando o OLA (Owl Lexical Analyzer) para tokenização.
- Análise sintática para verificar a estrutura gramatical do código OWL.
<u>- Compilação de código OWL em formato legível por máquina.</u>
- Geração de tabela de símbolos para rastrear os tipos de token e suas ocorrências.

## OLA (Analisador Léxico de OWL)

OLA serve como o analisador léxico para o MOSS-OWLC. Ele tokeniza o código OWL, identificando lexemas e gerando uma tabela de símbolos contendo os tipos de token e suas frequências.

## OSA (Analisador Léxico de OWL)

OLA serve como o analisador sintático para o MOSS-OWLC. Ele analisa a sintaxe d código OWL a partir de uma grmática livre de contexto que analisa os lexemas gerados pelo OLA e cria uma arvore de produções gramaticáis.

## Como Começar

Para executar o MOSS-OWLC e o OSA, siga estes passos:

1. Certifique-se de que o Python está instalado em sua máquina.

2. Navegue até o diretório `moss-owlc/ola/src/`.

3. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python3 -m venv venv
   ```

4. Ative o ambiente virtual:
   - No Linux/macOS:
     ```bash
     source venv/bin/activate
     ```
   - No Windows (PowerShell):
     ```bash
     .\venv\Scripts\Activate.ps1
     ```
   - No Windows (cmd):
     ```bash
     .\venv\Scripts\activate.bat
     ```

5. Instale a biblioteca necessária `PLY`:
   ```bash
   pip install ply
   pip install colorama
   ```

6. Execute o analisador sintático:
   ```bash
   python3 moss_owlc.py
   ```

## Uso

Ao executar o analisador sintático, o programa verificará a estrutura gramatical do código OWL, exibindo mensagens de erro se encontrar uma estrutura inválida.

## Contribuidores

Este projeto foi desenvolvido pelos estudantes João Goulart e Arthur Lennon da disciplina de compiladores na UFERSA, termo 2023.2, sob a orientação do Professor Patrício Alencar.
