import os
from random import sample, randint

std = '/mnt/Dados/livros/'
drct = 'all_books'

# Nome dos autores
path = '{}{}'.format(std, drct)
all_dirs = [i for i in os.listdir(path)]

# Sortea autor
autor = all_dirs[randint(0, len(all_dirs) - 1)]

# Busca livros do autor
path = '{}{}/{}'.format(std, drct, autor)
author_books = [i for i in os.listdir(path)]

escolhido = sample(author_books, 1)

print('Livro sorteado: {}'.format(escolhido[0]))
