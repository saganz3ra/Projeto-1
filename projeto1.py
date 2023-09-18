# Dicionário de produtos
produtos = {
    1: {"nome": "Smartphone", "preco": 1979.50, "descricao": "Samsung Galaxy S21 FE 5G, 128GB, Tela 6.4 Polegadas, Câmeras 12MB, Preto"},
    2: {"nome": "Tablet", "preco": 2650.50, "descricao": "Samsung Galaxy S6 128GB, Wifi, 4G, Tela de 10.4, Android 12, Cinza"},
    3: {"nome": "Notebook", "preco": 5499.00, "descricao": "Asus TUF Intel Core i7-12700H, 8GB RAM, GeForce RTX 3050, SSD 512GB, 15.6 Full HD 144Hz, KeepOS, Cinza"},
    4: {"nome": "Pc Gamer", "preco": 12000.50, "descricao": "Verdant Gamer AMD Ryzen 7 5800x, 32GB RAM, SSD Nvme 2.0 650GB, SSD 2TB, RTX 4070 Ti"},
    5: {"nome": "Console", "preco": 4200.00, "descricao": "Sony Playstation 5, SSD 825GB, Controle sem fio DualSense, Com Mídia Física, Branco"}
}

carrinho = []

# Função para exibir a descrição do produto
def exibirDescricao(idProduto):
    if idProduto in produtos:
        print(produtos[idProduto]['descricao'])
    else:
        print("Produto não encontrado.")
    input("Pressione Enter para continuar...") # Pausar a exibição no console, para melhor visualização

# Função para exibir os produtos 
def exibirProdutos():
    print("Produtos disponíveis:")
    for id, produto in produtos.items(): # É usado para obter lista de tuplas, onde cada tupla contém chave-valor do dicionário. 
        print(f"{id}: {produto['nome']} - R${produto['preco']:.2f}")
    input("Pressione Enter para continuar...")

# Função para adicionar produtos ao carrinho
def adicionarCarrinho(idProduto, quantidade):
    if idProduto in produtos:
        produto = produtos[idProduto]
        produto_no_carrinho = {
            "nome": produto["nome"],
            "preco": produto["preco"],
            "quantidade": quantidade
        }
        carrinho.append(produto_no_carrinho) # Usado para modificar a lista original, adicionando um único elemento como seu último item.
        print(f"{quantidade}x {produto['nome']} adicionado(s) ao carrinho.")
    else:
        print("Produto não encontrado.")

# Função para calcular o total da compra
def calcularTotal():
    total = sum(produto['preco'] for produto in carrinho)
    return total

# Função para exibir o carrinho de compras
def exibirCarrinho():
    if not carrinho:
        print("Seu carrinho está vazio.")
    else:
        print("Seu carrinho de compras:")
        for produto in carrinho:
            print(f"{produto['nome']} - R${produto['preco']:.2f}")
        print(f"Total: R${calcularTotal():.2f}")
    input("Pressione Enter para continuar...")

# Função para realizar o pagamento
def realizarPagamento():
    total = calcularTotal()
    if total > 0:
        print(f"Total a pagar: R${total:.2f}")
        while True:
            valor_pago = float(input("Digite o valor pago: R$")) # FLOAT usado para trabalhar com números decimais
            if valor_pago >= total:
                troco = valor_pago - total
                print(f"Pagamento realizado com sucesso! Troco: R${troco:.2f}")
                carrinho.clear()
                break # Interromper o loop imediatamente 
            else:
                print("Valor insuficiente. Por favor, insira um valor igual ou maior ao total.")

# Função para continuar comprando
def continuarComprando():
    resposta = input("Deseja continuar comprando? (S/N): ").strip().lower() # STRIP remove espaços em branco da palavra escrita. LOWER converte toda a string em letras minúsculas
    if resposta == 's':
        main()  # Chama a função principal novamente
    elif resposta == 'n': # Elif avalia  múltiplas condições em sequência só executa se for verdadeira, se n else
        print("Obrigado por comprar conosco. Volte sempre!")
    else:
        print("Resposta inválida. Por favor, digite 'S' para Sim ou 'N' para Não.")
        continuarComprando()  # Chama a função recursivamente em caso de resposta inválida 

# Função principal
def main():
    while True:
        print("\nBem-vindo à Loja Bodéga Produtos Eletrônicos")
        print("---------------------------------------------")
        print("Opções:")
        print("1 - Listar produtos")
        print("2 - Adicionar ao carrinho")
        print("3 - Exibir carrinho")
        print("4 - Realizar pagamento")
        print("5 - Exibir descrição de produto")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")
        print("---------------------------------------------")

        if opcao == "1":
            exibirProdutos()
        elif opcao == "2":
            idProduto = int(input("Digite o ID do produto que deseja adicionar ao carrinho: "))
            quantidade = int(input(f"Quantidade de '{produtos[idProduto]['nome']}': "))
            adicionarCarrinho(idProduto, quantidade)
            continuarComprando()  
        elif opcao == "3":
            exibirCarrinho()
            continuarComprando()
        elif opcao == "4":
            realizarPagamento()
            continuarComprando()
        elif opcao == "5":
            idProduto = int(input("Digite o ID do produto para ver a descrição: "))
            exibirDescricao(idProduto)
            continuarComprando()
        elif opcao == "6":
            print("Obrigado por comprar conosco. Volte sempre!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__": # Garente que o código 'main' só e executado quando o arquivo Python for executado diretamente. Reutilizável executável como um programa independente.
    main()