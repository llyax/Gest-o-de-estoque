def cadastrar_produto(nome, quantidade, preco, categoria, estoque):
    if nome in estoque:
        estoque[nome][0] += quantidade
        estoque[nome][1] = preco
        print(f"Produto '{nome}' atualizado! Nova quantidade: {int(estoque[nome][0])}. Novo preço: R${estoque[nome][1]:.2f}")
    else:
        estoque[nome] = [quantidade, preco, categoria]
        print(f"Produto '{nome}' adicionado. Quantidade: {int(quantidade)}, Preço: R${preco:.2f}")

def consultar_estoque(estoque):
    if not estoque:
        print("Estoque vazio.")
    else:
        print(f"{'PRODUTO':<15} {'CATEGORIA':<15} {'QUANTIDADE':>8} {'PREÇO':>12}")
        for nome, dados in estoque.items():
            quantidade, preco, categoria = dados[0], dados[1], dados[2]
            print(f"{nome:<15} | {categoria:<15} | {int(quantidade):>4} | R${preco:>8.2f}")
        

def estoque_baixo(estoque, limite):
    poucos_produtos = []
    for nome, dados in estoque.items():
        quantidade = dados[0]
        if quantidade <= limite:
            poucos_produtos.append((nome, quantidade))
    if not poucos_produtos:
        print("Nenhum produto com estoque baixo.")
    else:
        print(f"Produtos com estoque baixo (limite: {int(limite)} unidades):")
        for nome, quantidade in poucos_produtos:
            print(f"Produto: {nome} Quantidade: {int(quantidade)}")
      

def preco_total(estoque):
    total = 0
    for dados in estoque.values():
        total += dados[0] * dados[1]
    return total
