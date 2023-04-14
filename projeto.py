

def calcular_total_pedido(qtds, precos): # Função para calcular o valor total do pedido
    total = 0
    for qtd, preco in zip(qtds, precos):
        total += qtd * preco
    return total

# Mensagem de boas-vindas
print("Olá, seja bem-vindo à Vinheria Agnello!")

# Cadastro do cliente
nome = input("Por favor, informe o seu nome completo: ")
idade = int(input("Informe a sua idade: "))
endereco_cliente = input("Informe o seu endereço: ")
endereco_entrega = input("Informe o endereço de entrega: ")

# Verificação de idade do comprador
if idade < 18:
    print("Desculpe, mas a venda de bebidas alcoólicas é permitida somente para maiores de 18 anos.")
else:
    # Catálogo de vinhos e preços
    vinhos = ["Vinho Tinto", "Vinho Branco", "Vinho Rosé", "Espumante", "Vinho do Porto"]
    precos = [30, 25, 35, 50, 60]

    # Quantidade de cada vinho a ser comprada
    qtds = []
    for vinho in vinhos:
        qtd = int(input(f"Informe a quantidade de {vinho}s que deseja comprar: "))
        qtds.append(qtd)

    # Cálculo do valor total do pedido
    total_pedido = calcular_total_pedido(qtds, precos)

    # Verificação do valor mínimo de compra
    if total_pedido < 100:
        print("Desculpe, o valor mínimo para compra é de R$ 100,00.")
    else:
        # Verificação do valor do frete
        if total_pedido > 200:
            frete = 0
            mensagem_frete = "Frete grátis!"
        else:
            frete = 10
            mensagem_frete = f"Frete: R$ {frete:.2f}"

        # Mostrar o resumo do pedido
        print(f"\nResumo do pedido:\n{mensagem_frete}")
        for vinho, qtd, preco in zip(vinhos, qtds, precos):
            if qtd > 0:
                print(f"{vinho} x {qtd} = R$ {qtd * preco:.2f}")
        print(f"Valor total do pedido: R$ {total_pedido + frete:.2f}")
        print(f"Endereço de entrega: {endereco_entrega}")
        print("Obrigado pela sua compra!")
