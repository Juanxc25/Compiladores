import re


pattern = re.compile(r'^1(11)*(00)*$')


prueba_strings = ['100', '10000', '1000000', '11100', '1110000', '111110000', '1010', '1111', '000', '1110']


for prueba in prueba_strings:
    if pattern.fullmatch(prueba):
        print(f"'{prueba}' Coindice correctamente con la expresión regular")
    else:
        print(f"'{prueba}' No coincide con la expresión regular ")
