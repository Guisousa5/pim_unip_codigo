import json
import os

# Nome do arquivo JSON para salvar os dados
ARQUIVO_JSON = "dados_usuarios.json"

def carregar_dados():
    """Carrega os dados do arquivo JSON, retorna lista vazia se arquivo não existir."""
    if not os.path.exists(ARQUIVO_JSON):
        return []
    with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_dados(dados):
    """Salva a lista de dados no arquivo JSON."""
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def adicionar_usuario(nome, idade, email,endereco):
    """Adiciona um novo usuário ao arquivo JSON."""
    dados = carregar_dados()
    
    # Verificar se usuário já existe pelo email
    if any(u["email"] == email for u in dados):
        print(f"Usuário com email {email} já cadastrado.")
        return False
    
    usuario = {
        "nome": nome,
        "idade": idade,
        "email": email,
        "acessos": 0,
        "tempo_uso_minutos": 0,
        "endereco": endereco
    }
    dados.append(usuario)
    salvar_dados(dados)
    print(f"Usuário {nome} adicionado com sucesso.")
    return True

def registrar_acesso(email, minutos):
    """Registra um acesso aumentando contagem e tempo de uso do usuário."""
    dados = carregar_dados()
    for u in dados:
        if u["email"] == email:
            u["acessos"] += 1
            u["tempo_uso_minutos"] += minutos
            salvar_dados(dados)
            print(f"Acesso registrado para {email}: +1 acesso, +{minutos} minutos")
            return True
    print(f"Usuário com email {email} não encontrado.")
    return False

def listar_usuarios():
    """Lista todos os usuários cadastrados."""
    dados = carregar_dados()
    if not dados:
        print("Nenhum usuário cadastrado.")
        return
    print("Usuários cadastrados:")
    for u in dados:
        print(f"Nome: {u['nome']}, Idade: {u['idade']}, Email: {u['email']}, "
              f"Acessos: {u['acessos']}, Tempo de uso: {u['tempo_uso_minutos']} minutos"
              f"Endereço: {u['endereco']}")

def buscar_usuario(email):
    """Busca um usuário pelo email e retorna seus dados."""
    dados = carregar_dados()
    for u in dados:
        if u["email"] == email:
            return u
    return None

def menu():
    """Menu simples para interagir com o programa."""
    while True:
        print("\n--- Plataforma de Usuários ---")
        print("1 - Adicionar usuário")
        print("2 - Registrar acesso")
        print("3 - Listar usuários")
        print("4 - Buscar usuário por email")
        print("0 - Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            email = input("Email: ")
            endereco = input("Endereco:")
            adicionar_usuario(nome, idade, email,endereco)
        elif escolha == "2":
            email = input("Email do usuário: ")
            minutos = int(input("Tempo de uso em minutos: "))
            registrar_acesso(email, minutos)
        elif escolha == "3":
            listar_usuarios()
        elif escolha == "4":
            email = input("Email para busca: ")
            usuario = buscar_usuario(email)
            if usuario:
                print(f"Usuário encontrado: {usuario}")
            else:
                print("Usuário não encontrado.")
        elif escolha == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
