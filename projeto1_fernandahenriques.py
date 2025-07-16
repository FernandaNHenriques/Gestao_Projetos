#Desenvolver uma aplicação em Python para gerir projetos de desenvolvimento
#de software. A aplicação deverá permitir ao utilizador adicionar, visualizar,
#remover e listar projetos, bem como calcular a receita total esperada.

import os

def limpar_tela():
    """
    Clears the terminal screen based on the operating system.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
print("Bem-vindo ao Gerenciador de Projetos de Desenvolvimento de Software!")

def main():
    projetos = {}
    nomes_projetos = set()

    while True:
        menu_principal()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_projeto(projetos, nomes_projetos)
        elif opcao == "2":
            ver_detalhes_projeto(projetos)
        elif opcao == "3":
            listar_projetos(projetos)
        elif opcao == "4":
            remover_projeto(projetos, nomes_projetos)
        elif opcao == "5":
            calcular_receita_total(projetos)
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_principal():

    print("""
==== MENU PRINCIPAL ====
1 - Adicionar Projeto
2 - Ver Detalhes do Projeto
3 - Listar Projetos
4 - Remover Projeto
5 - Calcular Receita Total
0 - Sair
""")


def adicionar_projeto(projetos, nomes_projetos):
    nome = input("Digite o nome do projeto: ").strip()

    if nome in nomes_projetos:
        print("Já existe um projeto com esse nome. Escolha outro.")
        return
    try:
        inscricoes = int(input("Número de inscrições: "))
        duracao = int(input("Duração do curso (em horas): "))
        valor = float(input("Valor por inscrição (€): "))
    except ValueError:
        print("Entrada inválida. Use apenas números válidos.")
        return

    projeto = {
        'inscricoes': inscricoes,
        'duracao': duracao,
        'valor': valor
    }
    projetos[nome] = projeto
    nomes_projetos.add(nome)

    print("Projeto adicionado com sucesso!")


def ver_detalhes_projeto(projetos):
    nome = input("Digite o nome do projeto que deseja consultar: ").strip()

    if nome in projetos:
        projeto = projetos[nome]
        print("\nDetalhes do Projeto:")
        print(f"Nome: {nome}")
        print(f"Inscrições: {projeto['inscricoes']}")
        print(f"Duração: {projeto['duracao']} horas")
        print(f"Valor por inscrição: €{projeto['valor']:.2f}")
    else:
        print("Projeto não encontrado.")


def listar_projetos(projetos):
    if not projetos:
        print("Nenhum projeto cadastrado.")
        return

    print("\nProjetos Registrados:")
    for nome in projetos:
        print(f"- {nome}")

def remover_projeto(projetos, nomes_projetos):
    nome = input("Digite o nome do projeto que deseja remover: ").strip()

    if nome in projetos:
        del projetos[nome]            
        nomes_projetos.discard(nome)
        print("Projeto removido com sucesso!")
    else:
        print("Projeto não encontrado.")


def calcular_receita_total(projetos):
    if not projetos:
        print("Nenhum projeto cadastrado.")
        return

    receita_total = 0

    for dados in projetos.values():
        receita = dados['valor'] * dados['inscricoes']
        receita_total += receita

    print(f"\nReceita total estimada: €{receita_total:.2f}")

if __name__ == "__main__":
    main()

    
