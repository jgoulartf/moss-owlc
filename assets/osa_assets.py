"""
    ┏┓┓ ┏┓      ┏┓┓ ┏┓   ┓           ┓  ┏┓    ┓       
    ┃┃┃ ┣┫  ━━  ┃┃┃┃┃┃   ┃ ┏┓┓┏ ┓┏┏┏┓┃  ┣┫┏┓┏┓┃┓┏┓┏┓┏┓
    ┗┛┗┛┛┗      ┗┛┗┻┛┗┛  ┗┛┗ ┛┗ ┗┫┗┗┻┗  ┛┗┛┗┗┻┗┗┫┗┗ ┛ 
                                 ┛              ┛     
                                 
    Exemplos de código fonte utilizados durante o desenvolvimento da primeira versão.
    
    
    By: Arthur Lennon && João Goulart
    At: UFERSA - Campus Mossoró - 21/12/2023
    Version: 0.1.0
"""

# Classe primitiva: é uma classe cujos indivíduos podem herdar suas propriedades, mas
# indivíduos avulsos que tenham tais propriedades não podem ser classificados como membros
# dessas classes. No exemplo a seguir, é possível notar que a declaração deste tipo de classe
# inclui as definições de propriedades abaixo do axioma “SubClassOf”, ou seja, todos os
# indivíduos da classe primitiva Pizza serão também membros de tudo o que tem alguma base
# (PizzaBase) e tudo o que tem conteúdo calórico de algum valor inteiro. Todas as classes podem
# conter as seções “DisjointClasses” e “Individuals” em suas descrições.

owl_source_1 = """
Class: Pizza

SubClassOf:
    hasBase some PizzaBase,
    hasCaloricContent some xsd:integer

DisjointClasses:
    Pizza, PizzaBase, PizzaTopping

Individuals:
    CustomPizza1,
    CustomPizza2
"""

owl_source_2 = """
Pizza THAT
    hasTopping min 3
"""

owl_source_3 = """
PizzaTopping AND
    CheeseTopping THAT
        hasSpiciness SOME Mild and
        hasCountryOfOrigin VALUE Italy
"""

owl_source_4 = """
Pizza THAT
    hasCaloricContent some integer[>="400"]
"""

owl_source_5 = """
Pizza THAT
    hasTopping SOME MozzarellaTopping AND
    hasTopping SOME TomatoTopping AND
    hasTopping ONLY 
        (MozzarellaTopping OR
            TomatoTopping OR
            PepperonniTopping)
"""