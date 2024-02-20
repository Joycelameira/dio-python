nome = "Joyce"
idade = 37
profissão = "programadora"
linguagem = "Python"

print("nome: %s idade: %d" % (nome, idade) )
print("nome: {} idade: {}".format(nome, idade))
print("nome: {1} idade: {0}".format(idade, nome))
print("nome: {nome} idade: {idade}".format(nome=nome, idade=idade))