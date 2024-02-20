#inicio da funcao
def somar(valor_inicial, taxa_juros, periodo):
    valor_final = valor_inicial * (1 + taxa_juros )** periodo

    valor_total= 'valor finaldo investimento: R$ {:.2f}' .format(valor_final)
    return valor_total



print(somar(5000,0.08,5))

print(somar(1000,0.06,3))

print(somar(20000,0.04,10))