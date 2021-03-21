def params(nome, idade, telefone):
    params = {"nome": nome,
              "idade": idade,
              "telefone": telefone}
    return params

def param(nome, idade, telefone):
    params = [nome, idade, telefone]
    return params

nome = 'Felipe'
idade = 34
telefone = '8435'

user_params = params(nome, idade, telefone)
user_param = param(nome, idade, telefone)

def function(nome, idade, telefone):
    user = 'Nome: {} com {} e telefone {}'.format(nome, idade, telefone)
    print(user)

# Para dict **parametros
function(**user_params)

# Para list *parametro
function(*user_param)


