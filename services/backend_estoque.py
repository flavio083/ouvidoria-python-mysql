from database.operacoesbd import (
    listarBancoDados,
    insertNoBancoDados,
    atualizarBancoDados,
    excluirBancoDados,
)
 
 
def listarProdutos(conexao):
    consulta = 'SELECT * FROM Produtos'
    produtos = listarBancoDados(conexao, consulta)
 
    if len(produtos) > 0:
        print("\n-- Lista de Produtos --")
        print(f"{'ID':<5} {'Nome':<25} {'Categoria':<20} {'Qtd':<8} {'Preço (R$)':<12} {'Fornecedor'}")
        print("-" * 80)
        for item in produtos:
            print(f"{item[0]:<5} {item[1]:<25} {item[2]:<20} {item[3]:<8} {float(item[4]):<12.2f} {item[5]}")
    else:
        print("Nenhum produto encontrado no estoque.")
 
 
def novoProduto(conexao):
    nome = input("Nome do produto: ").strip()
    if len(nome) == 0:
        print("O nome deve ter ao menos 1 caractere!")
        return
 
    categoria = input("Categoria: ").strip()
    if len(categoria) == 0:
        print("A categoria deve ter ao menos 1 caractere!")
        return
 
    try:
        quantidade = int(input("Quantidade em estoque: "))
        preco = float(input("Preço unitário (R$): "))
    except ValueError:
        print("Quantidade e preço devem ser números válidos.")
        return
 
    fornecedor = input("Fornecedor: ").strip()
 
    consulta = 'INSERT INTO Produtos (nome, categoria, quantidade, preco, fornecedor) VALUES (%s, %s, %s, %s, %s)'
    dados = [nome, categoria, quantidade, preco, fornecedor]
 
    codigo = insertNoBancoDados(conexao, consulta, dados)
    print(f"Produto adicionado com sucesso! O código é {codigo}")
 
 
def pesquisarProduto(conexao):
    try:
        codigoProduto = int(input("Digite o código do produto a atualizar: "))
    except ValueError:
        print("O código deve ser um número inteiro.")
        return
    consulta = 'SELECT * FROM Produtos WHERE id = %s'
    dados = [codigoProduto]
 
    produtos = listarBancoDados(conexao, consulta, dados)
 
    if len(produtos) > 0:
        p = produtos[0]
        print(f"\n-- Produto Encontrado --")
        print(f"ID:         {p[0]}")
        print(f"Nome:       {p[1]}")
        print(f"Categoria:  {p[2]}")
        print(f"Quantidade: {p[3]}")
        print(f"Preço:      R$ {float(p[4]):.2f}")
        print(f"Fornecedor: {p[5]}")
    else:
        print("O código informado não é válido.")
 
 
def atualizarQuantidade(conexao):
    try:
        codigoProduto = int(input("Digite o código do produto a atualizar: "))
    except ValueError:
        print("O código deve ser um número inteiro.")
        return
 
    try:
        novaQuantidade = int(input("Digite a nova quantidade: "))
    except ValueError:
        print("A quantidade deve ser um número inteiro.")
        return
 
    consulta = 'UPDATE Produtos SET quantidade = %s WHERE id = %s'
    dados = [novaQuantidade, codigoProduto]
 
    linhasAfetadas = atualizarBancoDados(conexao, consulta, dados)
 
    if linhasAfetadas == 0:
        print("Não possui nenhum produto para o código informado.")
    else:
        print("Quantidade atualizada com sucesso!")
 
 
def atualizarPreco(conexao):
    try:
        codigoProduto = int(input("Digite o código do produto a atualizar: "))
    except ValueError:
        print("O código deve ser um número inteiro.")
        return
 
    try:
        novoPreco = float(input("Digite o novo preço (R$): "))
    except ValueError:
        print("O preço deve ser um número válido.")
        return
 
    consulta = 'UPDATE Produtos SET preco = %s WHERE id = %s'
    dados = [novoPreco, codigoProduto]
 
    linhasAfetadas = atualizarBancoDados(conexao, consulta, dados)
 
    if linhasAfetadas == 0:
        print("Não possui nenhum produto para o código informado.")
    else:
        print("Preço atualizado com sucesso!")
 
 
def removerProduto(conexao):
    try:
        codigoProduto = int(input("Digite o código do produto a ser removido: "))
    except ValueError:
        print("O código deve ser um número inteiro.")
        return
    consulta = 'DELETE FROM Produtos WHERE id = %s'
    dados = [codigoProduto]
 
    linhasAfetadas = excluirBancoDados(conexao, consulta, dados)
 
    if linhasAfetadas == 0:
        print("O código informado não é válido.")
    else:
        print("Produto removido com sucesso!")
 
 
def alertaEstoqueBaixo(conexao):
    try:
        limite = int(input("Digite o limite mínimo de quantidade (padrão 5): ") or "5")
    except ValueError:
        limite = 5
 
    consulta = 'SELECT * FROM Produtos WHERE quantidade <= %s ORDER BY quantidade ASC'
    dados = [limite]
 
    produtos = listarBancoDados(conexao, consulta, dados)
 
    if len(produtos) > 0:
        print(f"\n⚠️  -- Produtos com estoque baixo (≤ {limite} unidades) --")
        print(f"{'ID':<5} {'Nome':<25} {'Qtd':<8} {'Categoria'}")
        print("-" * 50)
        for item in produtos:
            print(f"{item[0]:<5} {item[1]:<25} {item[3]:<8} {item[2]}")
    else:
        print(f"Nenhum produto com estoque abaixo de {limite} unidades.")
 
 
def resumoEstoque(conexao):
    consulta_total = 'SELECT COUNT(*), SUM(quantidade), SUM(quantidade * preco) FROM Produtos'
    resultado = listarBancoDados(conexao, consulta_total)
 
    total_produtos = resultado[0][0] or 0
    total_itens = resultado[0][1] or 0
    valor_total = resultado[0][2] or 0.0
 
    print("\n-- Resumo do Estoque --")
    print(f"Tipos de produto cadastrados: {total_produtos}")
    print(f"Total de itens em estoque:    {total_itens}")
    print(f"Valor total do estoque:       R$ {float(valor_total):.2f}")