## Trabalho feito por: Vinícius Fernandes, Pedro Enrico, Pedro Moura e Larissa Beatriz

contatos = [
    {"nome": "Pedro", "telefone": "99999-9999", "email": "pedro@ex.com"}
]

def cadastro():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    contatos.append({"nome": nome, "telefone": telefone, "email": email})
    print("Contato cadastrado!")

def lista():
    if not contatos:
        print("Nenhum contato cadastrado!")
        return
    for i, c in enumerate(contatos):
        print(f"{i} - {c['nome']} | {c['telefone']} | {c['email']}")

def atualizar():
    lista()
    try:
        idx = int(input("Índice do contato para atualizar: "))
    except ValueError:
        print("Índice inválido!")
        return
    if idx < 0 or idx >= len(contatos):
        print("Índice inválido!")
        return
    
    contato = contatos[idx]
    novo_nome = input(f"Nome [{contato['nome']}]: ")
    novo_telefone = input(f"Telefone [{contato['telefone']}]: ")
    novo_email = input(f"E-mail [{contato['email']}]: ")

    if novo_nome: contato['nome'] = novo_nome
    if novo_telefone: contato['telefone'] = novo_telefone
    if novo_email: contato['email'] = novo_email

    print("Contato atualizado!")

def excluir():
    lista()
    try:
        idx = int(input("Índice do contato para excluir: "))
    except ValueError:
        print("Índice inválido!")
        return
    if 0 <= idx < len(contatos):
        removed = contatos.pop(idx)
        print(f"Removido: {removed['nome']}")
    else:
        print("Índice inválido!")

while True:
    print("\n1 - Cadastrar\n2 - Listar\n3 - Atualizar\n4 - Excluir\n5 - Sair")
    opc = input("Escolha: ").strip()
    if opc == "1": cadastro()
    elif opc == "2": lista()
    elif opc == "3": atualizar()
    elif opc == "4": excluir()
    elif opc == "5":
        print("Saindo..."); break
    else:
        print("Opção inválida.")

