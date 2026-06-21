def calcular(operacao, num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return "Digite Apenas Numeros"

    resultado = None

    if operacao == "soma":
        resultado = num1 + num2
    elif operacao == "subtracao":
        resultado = num1 - num2
    elif operacao == "multiplicacao":
        resultado = num1 * num2
    elif operacao == "divisao":
        if num2 == 0:
            return "Operacao invalida (divisao por zero)"
        resultado = num1 / num2
    else:
        return "Operacao invalida"

    if resultado < 0 or resultado > 10:
        return "Operacao invalida"
    return f"Resultado: {resultado}"


def main():
    print("Escolha a operacao:")
    print("1. Soma")
    print("2. Subtracao")
    print("3. Multiplicacao")
    print("4. Divisao")
    print("5- Historico de Calculos")
    escolha = input("Digite o numero da operacao: ").strip()

    operacoes = {
        "1": "soma",
        "2": "subtracao",
        "3": "multiplicacao",
        "4": "divisao",
        "5": "historico"
   
    }

historico = []

def salvar_historico(calculo):
    historico.append(calculo)

def mostrar_historico():
    for item in historico:
        print(item)




    operacao = operacoes.get(escolha)
    if not operacao:
        print("Operacao invalida")
        return

    num1 = input("Digite o primeiro numero: ").strip()
    num2 = input("Digite o segundo numero: ").strip()

    resultado = calcular(operacao, num1, num2)
    print(resultado)

 
if __name__ == "__main__":
    main()