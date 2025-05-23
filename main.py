import json
import os
import hashlib
from datetime import datetime
import statistics

class PlataformaEducacaoDigital:
    def __init__(self):
        self.arquivo_usuarios = "usuarios.json"
        self.arquivo_cursos = "cursos.json"
        self.arquivo_acessos = "acessos.json"
        self.usuarios = self.carregar_dados(self.arquivo_usuarios)
        self.cursos = self.carregar_dados(self.arquivo_cursos)
        self.acessos = self.carregar_dados(self.arquivo_acessos)
        self.inicializar_cursos()

    def carregar_dados(self, arquivo):
        """Carrega dados do arquivo JSON ou retorna lista vazia se não existir"""
        if os.path.exists(arquivo):
            try:
                with open(arquivo, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []

    def salvar_dados(self, dados, arquivo):
        """Salva dados no arquivo JSON"""
        try:
            with open(arquivo, 'w', encoding='utf-8') as f:
                json.dump(dados, f, ensure_ascii=False, indent=2)
            return True
        except:
            return False

    def criptografar_senha(self, senha):
        """Criptografa a senha usando SHA-256"""
        return hashlib.sha256(senha.encode()).hexdigest()

    def inicializar_cursos(self):
        """Inicializa cursos básicos se não existirem"""
        if not self.cursos:
            cursos_basicos = [
                {
                    "id": 1,
                    "nome": "Pensamento Lógico Computacional",
                    "descricao": "Introdução aos conceitos básicos de lógica de programação",
                    "duracao_minutos": 60,
                    "topicos": [
                        "Algoritmos básicos",
                        "Estruturas de decisão",
                        "Estruturas de repetição",
                        "Variáveis e tipos de dados"
                    ]
                },
                {
                    "id": 2,
                    "nome": "Programação Python Básica",
                    "descricao": "Fundamentos da linguagem Python",
                    "duracao_minutos": 90,
                    "topicos": [
                        "Sintaxe básica do Python",
                        "Funções",
                        "Listas e dicionários",
                        "Tratamento de erros"
                    ]
                },
                {
                    "id": 3,
                    "nome": "Segurança Digital",
                    "descricao": "Boas práticas de segurança na internet",
                    "duracao_minutos": 45,
                    "topicos": [
                        "Senhas seguras",
                        "Proteção contra phishing",
                        "Backup de dados",
                        "Navegação segura"
                    ]
                }
            ]
            self.cursos = cursos_basicos
            self.salvar_dados(self.cursos, self.arquivo_cursos)

    def cadastrar_usuario(self):
        """Cadastra um novo usuário"""
        print("\n=== CADASTRO DE USUÁRIO ===")
        nome = input("Nome completo: ").strip()
        if not nome:
            print("Nome não pode estar vazio!")
            return False

        email = input("Email: ").strip()
        if not email:
            print("Email não pode estar vazio!")
            return False

        # Verifica se email já existe
        for usuario in self.usuarios:
            if usuario['email'] == email:
                print("Email já cadastrado!")
                return False

        idade = input("Idade: ").strip()
        try:
            idade = int(idade)
            if idade < 0 or idade > 120:
                print("Idade inválida!")
                return False
        except:
            print("Idade deve ser um número!")
            return False

        senha = input("Senha (mínimo 6 caracteres): ").strip()
        if len(senha) < 6:
            print("Senha deve ter pelo menos 6 caracteres!")
            return False

        # Cria novo usuário
        novo_usuario = {
            "id": len(self.usuarios) + 1,
            "nome": nome,
            "email": email,
            "idade": idade,
            "senha": self.criptografar_senha(senha),
            "data_cadastro": datetime.now().isoformat(),
            "cursos_concluidos": [],
            "tempo_total_estudo": 0
        }

        self.usuarios.append(novo_usuario)
        
        if self.salvar_dados(self.usuarios, self.arquivo_usuarios):
            print(f"Usuário {nome} cadastrado com sucesso!")
            return True
        else:
            print("Erro ao salvar usuário!")
            return False

    def fazer_login(self):
        """Realiza login do usuário"""
        print("\n=== LOGIN ===")
        email = input("Email: ").strip()
        senha = input("Senha: ").strip()
        
        senha_hash = self.criptografar_senha(senha)
        
        for usuario in self.usuarios:
            if usuario['email'] == email and usuario['senha'] == senha_hash:
                print(f"Login realizado com sucesso! Bem-vindo(a), {usuario['nome']}!")
                self.registrar_acesso(usuario['id'])
                return usuario
        
        print("Email ou senha incorretos!")
        return None

    def registrar_acesso(self, usuario_id):
        """Registra um acesso do usuário"""
        acesso = {
            "usuario_id": usuario_id,
            "data_hora": datetime.now().isoformat(),
            "duracao_sessao": 0
        }
        self.acessos.append(acesso)
        self.salvar_dados(self.acessos, self.arquivo_acessos)

    def listar_cursos(self):
        """Lista todos os cursos disponíveis"""
        print("\n=== CURSOS DISPONÍVEIS ===")
        for i, curso in enumerate(self.cursos, 1):
            print(f"{i}. {curso['nome']}")
            print(f"   Descrição: {curso['descricao']}")
            print(f"   Duração: {curso['duracao_minutos']} minutos")
            print(f"   Tópicos: {', '.join(curso['topicos'])}")
            print("-" * 50)

    def iniciar_curso(self, usuario):
        """Simula o início de um curso"""
        self.listar_cursos()
        try:
            escolha = int(input("\nEscolha um curso (número): ")) - 1
            if 0 <= escolha < len(self.cursos):
                curso = self.cursos[escolha]
                print(f"\nIniciando curso: {curso['nome']}")
                print("Simulando conclusão do curso...")
                
                # Simula tempo de estudo
                usuario['cursos_concluidos'].append(curso['id'])
                usuario['tempo_total_estudo'] += curso['duracao_minutos']
                
                # Atualiza dados do usuário
                for i, u in enumerate(self.usuarios):
                    if u['id'] == usuario['id']:
                        self.usuarios[i] = usuario
                        break
                
                self.salvar_dados(self.usuarios, self.arquivo_usuarios)
                print(f"Curso '{curso['nome']}' concluído com sucesso!")
                return True
            else:
                print("Curso inválido!")
                return False
        except:
            print("Opção inválida!")
            return False

    def gerar_estatisticas(self):
        """Gera estatísticas básicas da plataforma"""
        print("\n=== ESTATÍSTICAS DA PLATAFORMA ===")
        
        if not self.usuarios:
            print("Nenhum usuário cadastrado ainda.")
            return
        
        # Estatísticas de usuários
        total_usuarios = len(self.usuarios)
        idades = [u['idade'] for u in self.usuarios]
        tempos_estudo = [u['tempo_total_estudo'] for u in self.usuarios]
        total_acessos = len(self.acessos)
        
        print(f"Total de usuários: {total_usuarios}")
        print(f"Total de acessos: {total_acessos}")
        
        if idades:
            print(f"\nEstatísticas de Idade:")
            print(f"  Média: {statistics.mean(idades):.1f} anos")
            print(f"  Mediana: {statistics.median(idades):.1f} anos")
            try:
                print(f"  Moda: {statistics.mode(idades)} anos")
            except:
                print("  Moda: Não há moda única")
        
        if tempos_estudo and any(t > 0 for t in tempos_estudo):
            tempos_validos = [t for t in tempos_estudo if t > 0]
            print(f"\nEstatísticas de Tempo de Estudo (minutos):")
            print(f"  Média: {statistics.mean(tempos_validos):.1f} min")
            print(f"  Mediana: {statistics.median(tempos_validos):.1f} min")
            try:
                print(f"  Moda: {statistics.mode(tempos_validos)} min")
            except:
                print("  Moda: Não há moda única")
        
        # Curso mais popular
        if self.usuarios:
            todos_cursos_feitos = []
            for usuario in self.usuarios:
                todos_cursos_feitos.extend(usuario['cursos_concluidos'])
            
            if todos_cursos_feitos:
                curso_mais_popular = max(set(todos_cursos_feitos), key=todos_cursos_feitos.count)
                nome_curso = next(c['nome'] for c in self.cursos if c['id'] == curso_mais_popular)
                print(f"\nCurso mais popular: {nome_curso}")

    def menu_principal(self):
        """Menu principal da aplicação"""
        while True:
            print("\n" + "="*50)
            print("PLATAFORMA DE EDUCAÇÃO DIGITAL SEGURA")
            print("="*50)
            print("1. Cadastrar usuário")
            print("2. Fazer login")
            print("3. Ver estatísticas")
            print("4. Listar cursos")
            print("5. Sobre segurança digital")
            print("0. Sair")
            
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao == "1":
                self.cadastrar_usuario()
            
            elif opcao == "2":
                usuario = self.fazer_login()
                if usuario:
                    self.menu_usuario(usuario)
            
            elif opcao == "3":
                self.gerar_estatisticas()
            
            elif opcao == "4":
                self.listar_cursos()
            
            elif opcao == "5":
                self.mostrar_dicas_seguranca()
            
            elif opcao == "0":
                print("Obrigado por usar nossa plataforma!")
                break
            
            else:
                print("Opção inválida!")

    def menu_usuario(self, usuario):
        """Menu do usuário logado"""
        while True:
            print(f"\n=== BEM-VINDO(A), {usuario['nome'].upper()}! ===")
            print("1. Iniciar curso")
            print("2. Meus cursos concluídos")
            print("3. Meu progresso")
            print("0. Logout")
            
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao == "1":
                self.iniciar_curso(usuario)
            
            elif opcao == "2":
                self.mostrar_cursos_concluidos(usuario)
            
            elif opcao == "3":
                self.mostrar_progresso(usuario)
            
            elif opcao == "0":
                print("Logout realizado com sucesso!")
                break
            
            else:
                print("Opção inválida!")

    def mostrar_cursos_concluidos(self, usuario):
        """Mostra os cursos concluídos pelo usuário"""
        print(f"\n=== CURSOS CONCLUÍDOS POR {usuario['nome']} ===")
        if not usuario['cursos_concluidos']:
            print("Nenhum curso concluído ainda.")
            return
        
        for curso_id in usuario['cursos_concluidos']:
            curso = next((c for c in self.cursos if c['id'] == curso_id), None)
            if curso:
                print(f"✓ {curso['nome']} - {curso['duracao_minutos']} min")

    def mostrar_progresso(self, usuario):
        """Mostra o progresso do usuário"""
        print(f"\n=== PROGRESSO DE {usuario['nome']} ===")
        total_cursos = len(self.cursos)
        cursos_concluidos = len(usuario['cursos_concluidos'])
        percentual = (cursos_concluidos / total_cursos) * 100 if total_cursos > 0 else 0
        
        print(f"Cursos concluídos: {cursos_concluidos}/{total_cursos}")
        print(f"Progresso: {percentual:.1f}%")
        print(f"Tempo total de estudo: {usuario['tempo_total_estudo']} minutos")

    def mostrar_dicas_seguranca(self):
        """Mostra dicas de segurança digital"""
        print("\n=== DICAS DE SEGURANÇA DIGITAL ===")
        dicas = [
            "1. Use senhas fortes com pelo menos 8 caracteres, incluindo números e símbolos",
            "2. Não clique em links suspeitos ou anexos de emails desconhecidos",
            "3. Mantenha seus softwares sempre atualizados",
            "4. Faça backup regular dos seus dados importantes",
            "5. Use autenticação de dois fatores quando disponível",
            "6. Não compartilhe informações pessoais em redes sociais públicas",
            "7. Verifique sempre o endereço dos sites antes de inserir dados pessoais",
            "8. Use antivírus confiável e mantenha-o atualizado"
        ]
        
        for dica in dicas:
            print(dica)
        
        print("\nLembre-se: A segurança digital é responsabilidade de todos!")

def main():
    """Função principal"""
    print("Inicializando Plataforma de Educação Digital Segura...")
    plataforma = PlataformaEducacaoDigital()
    plataforma.menu_principal()

if __name__ == "__main__":
    main()
