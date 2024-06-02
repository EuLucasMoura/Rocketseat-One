def saudacao(nome):
    print("Olá", nome)

print("Chamando a função saudação:")
saudacao("Alice")
saudacao("Bob")


def quadrado(numero):
    resultado = numero ** 2
    return resultado

print("\n Chamando funcao quadrado:")
resultado_quadrado = quadrado(10)
print("\n Resultado funcao quadrado: ", resultado_quadrado)
