Sistema de Gestão de Projetos de Extensão (Python - Terminal)

Este é um projeto simples em Python desenvolvido como parte da disciplina de **Programação em Python**, com o objetivo de gerir cursos de extensão universitários na área de desenvolvimento de software. A aplicação funciona via terminal e permite controlar os projetos disponíveis, visualizar detalhes, calcular receitas e muito mais.

---

Funcionalidades

- Adicionar novo projeto
- Ver detalhes de um projeto específico
- Listar todos os projetos registrados
- Remover um projeto existente
- Calcular a receita total esperada dos projetos
- Sair do sistema com segurança

---

Estrutura de Dados Utilizada

- **Dicionário (`dict`)**: Armazena os projetos, com o nome como chave e os detalhes como valor.
- **Conjunto (`set`)**: Garante nomes únicos para os projetos, otimizando a verificação de duplicatas.

### Exemplo de estrutura:
```python
projetos = {
    "Curso Python Básico": {
        "inscricoes": 30,
        "duracao": 20,
        "valor": 50.0
    }
}

nomes_projetos = {"Curso Python Básico"}
