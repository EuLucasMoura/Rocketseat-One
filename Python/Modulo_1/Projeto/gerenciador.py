def adicionar_tarefas(tarefas, nome_tarefa):   
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"A tarefa {nome_tarefa} foi adicionada com sucesso!")
    return

def ver_tarefas(tarefas):
    print("Lista de tarefas")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["completada"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice}. [{status}] [{nome_tarefa}]")
    return

def atualizar_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
    indice_tarefa_ajustado = ajuste_indice(indice_tarefa)
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["tarefa"] = novo_nome_tarefa
        print(f"Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}.")
    else:
        print("Índice de tarefa inválido.")
    return

def completar_tarefas(tarefas, indice_tarefa):
    indice_tarefa_ajustado = ajuste_indice(indice_tarefa)
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["completada"] = True
        print(f"Tarefa {indice_tarefa} marcada como completada.")
    else:
        print("Índice de tarefa inválido.")
    return

def deletar_tarefas_completadas(tarefas):
    for tarefa in tarefas:
        if tarefa["completada"]:
            tarefas.remove(tarefa)
    print("Tarefas completadas foram deletadas.")
    return

def ajuste_indice(indice_tarefa):
    try:
        return int(indice_tarefa) - 1
    except ValueError:
        return -1

tarefas = []

while True:
    print("-=" * 3 +" Menu do gerenciador de Lista de tarefas " + "=-" * 3)
    print("\n1. Adicionar tarefas")
    print("2. Ver tarefas")
    print("3. Atualizar tarefas")
    print("4. Completar tarefas")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    escolha = input("\nDigite uma opção: ")
    if escolha == "1":
        nome_tarefa = input("Qual o nome da sua tarefa? ")
        adicionar_tarefas(tarefas, nome_tarefa)
    
    elif escolha == "2":
        ver_tarefas(tarefas)

    elif escolha == "3":
        ver_tarefas(tarefas)
        indice_tarefa = input("Digite o número da tarefa que deseja atualizar: ")
        novo_nome_tarefa = input("Digite o novo nome da tarefa: ")
        atualizar_tarefa(tarefas, indice_tarefa, novo_nome_tarefa)

    elif escolha == "4":
        ver_tarefas(tarefas)
        indice_tarefa = input("Digite o número da tarefa que deseja completar: ")
        completar_tarefas(tarefas, indice_tarefa)

    elif escolha == "5":
        deletar_tarefas_completadas(tarefas)
        ver_tarefas(tarefas)

    elif escolha == "6":
        break

print("Programa Finalizado.")
