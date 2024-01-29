import re


pattern = re.compile(r'(\+|-)?\d+\.\d+')


prueba_strings = ['-20.43', '0.3216', '329.', '217.92', '+2019', '+.762', '-.4555']


for prueba in prueba_strings:
    if pattern.fullmatch(prueba):
        print(f"'{prueba}' Coincide correctamente con la expresión")
    else:
        print(f"'{prueba}' No coincide la expresión")
