n1 = input('Digite algo: ')
print(f'É númerico? {n1.isnumeric()}')
print('É alfanúmerico?', n1.isalnum())
print('Só tem espaços?', n1.isspace())
print('Só tem letras maíusculas?', n1.isupper())
print('Só tem letras minúsculas?', n1.islower())
print('Tem decimais?', n1.isdecimal())
print('Está capitalizada?', n1.istitle())
