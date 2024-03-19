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
owl_source_1 = """
Pizza THAT 
    hasTopping SOME MozzarellaTopping AND 
    hasTopping SOME TomatoTopping AND 
    hasTopping ONLY (MozzarellaTopping OR TomatoTopping OR PepperonniTopping)
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