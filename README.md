**README**

# MOSS-OWLC (Compilador de Linguagem Web de Ontologia de Mossoró)

O MOSS-OWLC é um compilador para OWL (Ontology Web Language) desenvolvido como um projeto para a disciplina de compiladores na UFERSA (Universidade Federal do Semi-Árido), termo 2023.2, localizada em Mossoró/RN, Brasil.

## Visão Geral

O MOSS-OWLC tem como objetivo fornecer uma ferramenta para compilar OWL, uma linguagem usada para representar conhecimento sobre um domínio e descrever as relações entre entidades dentro desse domínio. Este compilador analisa o código OWL e gera uma saída correspondente legível por máquina.

## Funcionalidades

- Análise léxica usando o OLA (Owl Lexical Analyzer) para tokenização.
- Análise sintática para verificar a estrutura gramatical do código OWL.
- Compilação de código OWL em formato legível por máquina.
- Geração de tabela de símbolos para rastrear os tipos de token e suas ocorrências.

## OLA (Analisador Léxico de OWL)

OLA serve como o analisador léxico para o MOSS-OWLC. Ele tokeniza o código OWL, identificando lexemas e gerando uma tabela de símbolos contendo os tipos de token e suas frequências.

## Como Começar

Para executar o MOSS-OWLC e o OLA, siga estes passos:

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
   ```

6. Execute o analisador sintático:
   ```bash
   python3 sintatico.py
   ```

## Uso

Ao executar o analisador sintático, o programa verificará a estrutura gramatical do código OWL, exibindo mensagens de erro se encontrar uma estrutura inválida.

## Contribuidores

Este projeto foi desenvolvido pelos estudantes da disciplina de compiladores na UFERSA, termo 2023.2, sob a orientação do [Nome do Professor].

## Feedback

Para quaisquer perguntas, feedback ou problemas relacionados ao MOSS-OWLC, entre em contato com [Seu Nome] em [seu endereço de e-mail].

---
Substitua espaços reservados como [Nome do Professor], [Seu Nome] e [seu endereço de e-mail] pelas informações apropriadas.
