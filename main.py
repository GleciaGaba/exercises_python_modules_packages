"""
Les packages en Python sont des collections de modules organisées en répertoires hiérarchiques.
Un module est un fichier contenant des définitions et des instructions Python.
Les packages permettent de structurer les programmes Python de manière à faciliter la gestion,
la réutilisation et l'organisation du code. Voici quelques points clés concernant les packages en Python :
"""

#  Modules


# Définition : Un module est un simple fichier Python (.py) qui peut contenir des fonctions, des classes et des
# variables.

# Utilisation : On peut importer des modules pour utiliser les fonctionnalités qu'ils offrent.

#  import module_name

# Packages

"""Définition : Un package est un répertoire qui contient un fichier spécial __init__.py et d'autres modules et 
sous-packages. 

Structure : Le fichier __init__.py peut être vide ou contenir du code d'initialisation pour le package.


my_package/
    __init__.py
    module1.py
    module2.py
    sub_package/
        __init__.py
        module3.py
"""

#  Importation des Modules et Packages

# Module

# import my_package.module1

# Package

# from my_package import module1
# from my_package.sub_package import module3
