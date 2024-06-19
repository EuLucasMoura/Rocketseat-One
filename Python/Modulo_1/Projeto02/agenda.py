def adicionar_contato(contatos, nome_contato, telefone, email):
    contato = {
    "nome": nome_contato,
    "telefone": telefone, 
    "email": email,
    "favorito": False
    }
    contatos.append(contato)
    print(f"O contato {nome_contato} foi adicionado com sucesso!")
    return

def ver_contatos(contatos):
    print("Lista de contatos")
    for indice, contato in enumerate(contatos, start=1):
        favorito = "✓" if contato["favorito"] else " "
        nome_contato = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]
        print(f"{indice}. [{favorito}] [{nome_contato}] [{email}] [{telefone}]")
    return

def atualizar_contato(contatos, indice_contato, novo_nome,):
    indice_contato_ajustado = ajuste_indice(indice_contato) -1
    def atualizar_nome(contato):

    return

def ajuste_indice(indice_contato):
    try:
        return int(indice_contato)
    except ValueError:
        return -1
    
contatos = []

while True:
    print("-=" * 3 + " Agenda " + "=-" * 3)
    print("\n1. Adicionar contato")
    print("2. Ver contatos")
    print("3. Editar Contatos")
    print("4. Marcar contato favorito")
    print("5. Lista de favoritos")
    print("6. Apagar contato")
    print("7. Sair")

    opcao = input("\n Digite uma opção: ")

    if opcao == "1":
        nome_contato = input("Qual o nome do contato? ")
        email = input("Qual o email do contato? ")
        telefone = input("Qual o telefone do contato? ")
        adicionar_contato(contatos,nome_contato, telefone, email)
    
    elif opcao == "2":
        ver_contatos(contatos)
    
    elif opcao == "3":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja atualizar: ")
        campo = input("Digite o campo que deseja alterar: ")
        novo_nome = input("Digite o novo nome do contato: ")
        atualizar_contato(contatos, indice_contato, novo_nome)

    elif opcao == "7":
        break
print("Programa finalizado.")