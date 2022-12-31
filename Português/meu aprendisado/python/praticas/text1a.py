n = input('digite um algo')
print(type(n))
print('O digito é um numero',n.isnumeric())
print('O digito é alphanumerico', n.isalnum())
print('O digito é decimal', n.isdecimal())
#3.c.5 unir e quebrar linhas
print('O digito é \n alphabetico', n.isalpha(), end='>>> ')
print('O digito \n é um espaco', n.isspace(), end=' ')
print('O digito é un ', n.islower())