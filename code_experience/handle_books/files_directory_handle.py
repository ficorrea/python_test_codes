import os
import shutil as sh

std = '/mnt/Dados/livros/'
init = 'lelivros_1'
dest = 'all_books'

# Busca nome dos livros
path = '{}{}'.format(std, init)
all_books = [i for i in os.listdir(path)]

# Separa o nome do autor
files = [i.replace('--', '-') for i in all_books]
temp_dirs = [i.split('-')[-1].split('.epub')[0].strip() for i in files]
dirs = list(set(temp_dirs))

# Loop para mover arquivos
for d in dirs:
    src = [i for i in all_books if d in i]  
    for s in src:
        font = '{}{}/{}'.format(std, init, s)
        destiny = '{}{}/{}'.format(std, dest, d)
        try:
            sh.move(font, destiny)
            print('Livros dx {} transferidos com sucesso'.format(d))
        except Exception as error:
            with open('error_transfer.txt', 'w+') as file:
                file.write('Ocorreu o erro {} autor(a) {}\n'.format(error, d))

# paths = ['/mnt/Dados/livros_download/all_books/{}'.format(i) for i in dirs]

# for p in paths:
#     try:
#         os.mkdir(p, 0o755)
#         print('Diretorio {} criado com sucesso.'.format(p))
#     except Exception as error:
#         print(error)

# os.mkdir()

# with open('lelivros_1.txt', 'w+') as file:
#     for f in dirs:
#         file.write('{}\n'.format(f))