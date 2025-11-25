# Leitura dos dados de entrada
peso = float(input("Qual o peso? "))
preco_por_tonelada = float(input("Qual o preço por tonelada? "))

# definição da função estava incorreta
def cliente_tipo(): 
    tipo_cliente = int(input("Qual tipo de cliente? [1]Novo Cliente [2]Cliente fidelizado [3]Cliente Premium: "))  
    if tipo_cliente == 1:   
        print("Novo Cliente")
        return "Novo Cliente"   
    elif tipo_cliente == 2:   
        print("Cliente fidelizado")
        return "Cliente fidelizado"   
    elif tipo_cliente == 3:   
        print("Cliente Premium")
        return "Cliente Premium"   
    else:  
        print("Opção inválida, considerado como Novo Cliente")   
        return "Novo Cliente"   

# função de desconto estava incorreta
def desconto(tipo_cliente):   
    if tipo_cliente == "Novo Cliente":   
        return 0.0   
    elif tipo_cliente == "Cliente fidelizado":   
        return 0.05   
    elif tipo_cliente == "Cliente Premium":   
        return 0.10   

# Calcula o valor total sem desconto
valor_total = peso * preco_por_tonelada

# TODO Aplique o desconto conforme o tipo de cliente
tipo_cliente = cliente_tipo()
desconto_aplicado = desconto(tipo_cliente)  

valor_final = valor_total * (1 - desconto_aplicado)   

# Exibe o resultado formatado com duas casas decimais

print(f"Valor final: {valor_final:.2f}")   
