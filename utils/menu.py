from controller.controller_candidato import cadastrar_candidato, apagar_candidato


def menu():
    print("\n=== URNA ELETRÔNICA ===")
    print("1. Cadastro")
    print("2. Votar")
    print("3. Finalizar votação")
    print("4. Sair\n")

    escolha = input("Escolha uma opção: ")

    match escolha:
        case "1":
            menu_candidato()
        case "2":
            print("listar_candidatos()")
        case "3":
           print("apagar_candidato()")
        case "4":
            print("Saindo do programa...")
            return True
        case _:
            print("Opção inválida. Tente novamente.")


def menu_cadastro():
    print("\n--- Menu Cadastro ---")  
    print("1. Cadastro candidato")
    print("2. Cadastro eleitor")
    print("3. Cadastro partido")
    print("4. Sair\n")

    escolha = input("Escolha uma opção: ")

    match escolha:
        case "1":
            menu_candidato()

def menu_candidato():
    print("\n--- Menu Candidato ---")
    print("1. Cadastrar candidato")
    print("2. Listar candidatos")
    print("3. Apagar candidato")
    print("4. Sair\n")

    escolha = input("Escolha uma opção: ")

    match escolha:
        case "1":
            cadastrar_candidato()
        case "2":
            print("Listando")
            #listar_candidatos()
        case "3":
            apagar_candidato()
