import re

pattern = re.compile(r'[ab]*abb')

prueba_strings = ['abb', 'aabb', 'babb', 'aaabb', 'ababb', 'baabb', 'bbabb', 'abc', 'aabbc', 'bba']

for prueba in prueba_strings:
    if pattern.fullmatch(prueba):
        print(f"'{prueba}' coincide con la expresión regular")
    else:
        print(f"'{prueba}' no coincide con la expresión regular")
