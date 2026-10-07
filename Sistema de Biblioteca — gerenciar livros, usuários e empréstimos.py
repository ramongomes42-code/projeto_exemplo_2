class Usuario:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} (Matrícula: {self.matricula})"

lista_usuarios = []

proximo_codigo = 1  # variável global para gerar códigos únicos

class Livro:
    def __init__(self, titulo, autor, ano, quantidade):
        global proximo_codigo
        self.codigo = proximo_codigo
        proximo_codigo += 1
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.quantidade = quantidade
        self.usuarios_com_livro = []  # lista de objetos Usuario com uma cópia emprestada

    def __str__(self):
        return f"[{self.codigo}] {self.titulo} | Autor: {self.autor} | Ano: {self.ano} | Qtd: {self.quantidade} | Emprestados: {len(self.usuarios_com_livro)}"

lista_livros = []

# ---------- CRUD de Livro ----------

def cadastrar_livro():
    while True:
        titulo = input("Título: ").strip()
        if titulo != "":
            break
        print("Erro: título não pode ser vazio.")

    while True:
        autor = input("Autor: ").strip()
        if autor != "":
            break
        print("Erro: autor não pode ser vazio.")

    while True:
        try:
            ano = int(input("Ano: "))
            break
        except ValueError:
            print("Erro: ano deve ser um número inteiro.")

    while True:
        try:
            quantidade = int(input("Quantidade: "))
            if quantidade < 0:
                print("Erro: quantidade não pode ser negativa.")
                continue
            break
        except ValueError:
            print("Erro: quantidade deve ser um número inteiro.")

    novo_livro = Livro(titulo, autor, ano, quantidade)
    lista_livros.append(novo_livro)
    print("Livro cadastrado com sucesso!")

def listar_livros():
    if len(lista_livros) == 0:
        print("Nenhum livro cadastrado.")
        return

    print("\n--- Livros cadastrados ---")
    for i, livro in enumerate(lista_livros, start=1):
        print(f"{i}. {livro}")

def buscar_livro_por_titulo(titulo_busca):
    for livro in lista_livros:
        if livro.titulo.lower() == titulo_busca.lower():
            return livro
    return None

def buscar_livro():
    titulo_busca = input("Digite o título do livro que deseja buscar: ").strip()
    livro = buscar_livro_por_titulo(titulo_busca)

    if livro is None:
        print("Livro não encontrado.")
    else:
        print(f"Encontrado: {livro}")

def buscar_livro_por_codigo(codigo_busca):
    for livro in lista_livros:
        if livro.codigo == codigo_busca:
            return livro
    return None

def buscar_livro_por_codigo_menu():
    try:
        codigo_busca = int(input("Digite o código do livro que deseja buscar: ").strip())
    except ValueError:
        print("Código inválido. Deve ser um número.")
        return

    livro = buscar_livro_por_codigo(codigo_busca)
    if livro is None:
        print("Livro não encontrado.")
    else:
        print(f"Encontrado: {livro}")

def buscar_livro_por_trecho_titulo():
    trecho_busca = input("Digite um trecho do título do livro que deseja buscar: ").strip().lower()
    encontrados = [livro for livro in lista_livros if trecho_busca in livro.titulo.lower()]

    if len(encontrados) == 0:
        print("Nenhum livro encontrado com esse trecho no título.")
        return

    print(f"\n--- Resultados para '{trecho_busca}' ---")
    for livro in encontrados:
        print(livro)

def alterar_livro():
    titulo_busca = input("Digite o título do livro que deseja alterar: ").strip()
    livro = buscar_livro_por_titulo(titulo_busca)

    if livro is None:
        print("Livro não encontrado.")
        return

    print(f"Livro encontrado: {livro}")
    print("Deixe em branco para manter o valor atual.")

    novo_autor = input(f"Novo autor ({livro.autor}): ").strip()
    if novo_autor != "":
        livro.autor = novo_autor

    novo_ano = input(f"Novo ano ({livro.ano}): ").strip()
    if novo_ano != "":
        try:
            livro.ano = int(novo_ano)
        except ValueError:
            print("Ano inválido, mantendo o valor anterior.")

    nova_quantidade = input(f"Nova quantidade ({livro.quantidade}): ").strip()
    if nova_quantidade != "":
        try:
            valor = int(nova_quantidade)
            if valor < 0:
                print("Quantidade não pode ser negativa, mantendo o valor anterior.")
            else:
                livro.quantidade = valor
        except ValueError:
            print("Quantidade inválida, mantendo o valor anterior.")

    print("Livro atualizado com sucesso!")

def remover_livro():
    titulo_busca = input("Digite o título do livro que deseja remover: ").strip()
    livro = buscar_livro_por_titulo(titulo_busca)

    if livro is None:
        print("Livro não encontrado.")
        return

    print(f"Livro encontrado: {livro}")
    confirmacao = input("Tem certeza que deseja remover este livro? (s/n): ").strip().lower()

    if confirmacao == "s":
        lista_livros.remove(livro)
        print("Livro removido com sucesso!")
    else:
        print("Remoção cancelada.")
def filtrar_livros_disponiveis():
    disponiveis = [livro for livro in lista_livros if livro.quantidade > 0]

    if len(disponiveis) == 0:
        print("Nenhum livro disponível para empréstimo.")
        return

    print("\n--- Livros disponíveis para empréstimo ---")
    for livro in disponiveis:
        print(livro)

def ordenar_livros_por_titulo():
    if len(lista_livros) == 0:
        print("Nenhum livro cadastrado.")
        return
    ordenados = sorted(lista_livros, key=lambda livro: livro.titulo.lower())
    print("\n--- Livros ordenados por título ---") 
    for livro in ordenados:
        print(livro)

# ---------- CRUD de Usuário ----------

def cadastrar_usuario():
    while True:
        nome = input("Nome do usuário: ").strip()
        if nome != "":
            break
        print("Erro: nome não pode ser vazio.")

    while True:
        matricula = input("Matrícula: ").strip()
        if matricula != "":
            break
        print("Erro: matrícula não pode ser vazia.")

    novo_usuario = Usuario(nome, matricula)
    lista_usuarios.append(novo_usuario)
    print("Usuário cadastrado com sucesso!")

def listar_usuarios():
    if len(lista_usuarios) == 0:
        print("Nenhum usuário cadastrado.")
        return

    print("\n--- Usuários cadastrados ---")
    for i, usuario in enumerate(lista_usuarios, start=1):
        print(f"{i}. {usuario}")

def buscar_usuario_por_matricula(matricula_busca):
    for usuario in lista_usuarios:
        if usuario.matricula == matricula_busca:
            return usuario
    return None

# ---------- Empréstimo / Devolução ----------

def emprestar_livro():
    titulo_busca = input("Digite o título do livro que deseja emprestar: ").strip()
    livro = buscar_livro_por_titulo(titulo_busca)

    if livro is None:
        print("Livro não encontrado.")
        return

    if livro.quantidade <= 0:
        print("Não há cópias disponíveis para empréstimo.")
        return

    matricula_usuario = input("Digite a matrícula do usuário: ").strip()
    usuario = buscar_usuario_por_matricula(matricula_usuario)

    if usuario is None:
        print("Usuário não encontrado.")
        return

    if usuario in livro.usuarios_com_livro:
        print("Este usuário já possui uma cópia deste livro emprestada.")
        return

    livro.quantidade -= 1
    livro.usuarios_com_livro.append(usuario)
    print(f"Livro '{livro.titulo}' emprestado para {usuario.nome} com sucesso!")

def devolver_livro():
    titulo_busca = input("Digite o título do livro que deseja devolver: ").strip()
    livro = buscar_livro_por_titulo(titulo_busca)

    if livro is None:
        print("Livro não encontrado.")
        return

    matricula_usuario = input("Digite a matrícula do usuário: ").strip()
    usuario = buscar_usuario_por_matricula(matricula_usuario)

    if usuario is None:
        print("Usuário não encontrado.")
        return

    if usuario not in livro.usuarios_com_livro:
        print("Este usuário não possui uma cópia deste livro emprestada.")
        return

    livro.quantidade += 1
    livro.usuarios_com_livro.remove(usuario)
    print(f"Livro '{livro.titulo}' devolvido por {usuario.nome} com sucesso!")

# ---------- Menu ----------

def exibir_menu():
    print("\n=== Sistema de Biblioteca ===")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Buscar livro por título (exato)")
    print("4 - Alterar livro")
    print("5 - Remover livro")
    print("6 - Cadastrar usuário")
    print("7 - Listar usuários")
    print("8 - Emprestar livro")
    print("9 - Devolver livro")
    print("10 - Buscar livro por código")
    print("11 - Buscar livro por trecho do título")
    print("12 - Filtrar livros disponíveis para empréstimo")
    print("13 - Ordenar livros por título")
    print("0 - Sair")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_livro()
        elif opcao == "2":
            listar_livros()
        elif opcao == "3":
            buscar_livro()
        elif opcao == "4":
            alterar_livro()
        elif opcao == "5":
            remover_livro()
        elif opcao == "6":
            cadastrar_usuario()
        elif opcao == "7":
            listar_usuarios()
        elif opcao == "8":
            emprestar_livro()
        elif opcao == "9":
            devolver_livro()
        elif opcao == "10":
            buscar_livro_por_codigo_menu()
        elif opcao == "11":
            buscar_livro_por_trecho_titulo()
        elif opcao == "12":
            filtrar_livros_disponiveis()
        elif opcao == "13":
            ordenar_livros_por_titulo()
        elif opcao == "0":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()