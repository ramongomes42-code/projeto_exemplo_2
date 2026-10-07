# Sistema de Biblioteca

Sistema de biblioteca desenvolvido em Python para gerenciar livros, usuários, empréstimos e devoluções por meio de um menu interativo no terminal.

## Funcionalidades

### Livros

- Cadastrar livros com título, autor, ano e quantidade.
- Listar livros cadastrados.
- Buscar por título exato, código ou trecho do título.
- Alterar autor, ano e quantidade.
- Remover livros.
- Filtrar livros disponíveis para empréstimo.
- Ordenar livros por título.

### Usuários

- Cadastrar usuários com nome e matrícula.
- Listar usuários cadastrados.
- Buscar usuários por matrícula.

### Empréstimos

- Registrar empréstimos de livros para usuários.
- Registrar devoluções.
- Controlar automaticamente a quantidade disponível.
- Impedir empréstimos quando não há cópias disponíveis ou quando o usuário já possui o livro.

## Requisitos

- Python 3.x

## Como executar

Salve o código em um arquivo Python, como `biblioteca.py`, e execute:

```bash
python biblioteca.py
```

O sistema exibirá um menu com todas as operações disponíveis. Para encerrar, escolha a opção `0 - Sair`.

## Estrutura principal

- `Usuario`: representa um usuário da biblioteca.
- `Livro`: representa um livro e controla seus empréstimos.
- `lista_usuarios`: armazena os usuários cadastrados.
- `lista_livros`: armazena os livros cadastrados.
- `proximo_codigo`: gera códigos únicos para os livros.

## Observação

Os dados são armazenados apenas em memória e são perdidos quando o programa é encerrado.
