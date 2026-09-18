def Circulo():
    raio = int (input ("qual o Raio do circulo? "))
    raio = raio * raio
    print (f"A área do circulo é: {raio * 3.14}")
def Triângulo():
    base = int (input ("qual a base do Triângulo? "))
    altura = int (input ("qual a altura do Trângulo? "))
    calculo = base * altura
    print (f"A área do Triângulo é: {calculo / 2}")
def Quadrado():
    lado = int (input ("qual o valor de um dos lados do Quadrado? "))
    print (f"A área do Quadrado é: {lado * lado}")
def Retângulo():
    base = int (input ("qual a base do Retângulo? "))
    altura = int (input ("qual a altura do Retângulo? "))
    print (f"A área do Retângulo é: {base * altura}")
def Paralelogramo():
    base = int (input ("qual a base do Paralelogramo? "))
    altura = int (input ("qual a altura do Paralelogramo? "))
    print (f"A área do Paralelogramo é: {base * altura}")
def Losango():
    diagonalmaior = int (input ("qual a diagonal maior do losango? "))
    diagonalmenor = int (input ("qual a diagonal menor do losango? "))
    calculo = diagonalmaior * diagonalmenor
    print (f"A área do Losango é: {calculo / 2}")
def Trapézio():
    basemaior = int (input ("qual a base maior do Trapézio? "))
    basemenor = int (input ("qual a base menor do Trapézio? "))
    altura = int (input ("qual a altura do Trapézio? "))
    calculo1 = basemaior + basemenor
    calculo2 = calculo1 * altura
    print (f"A área do Losango é: {calculo2 / 2}")

while True: 
    print ("CALCULADORA")
    print ("1 - Circulo")
    print ("2 - Triângulo")
    print ("3 - Quadrado")
    print ("4 - Retângulo")
    print ("5 - Paralelogramo")
    print ("6 - Losango")
    print ("7 - Trapézio")
    print ("0 - Sair")

    opcao = input ("Escolha uma opção: ")

    if opcao == "1":
        Circulo()
    elif opcao == "2":
        Triângulo()
    elif opcao == "3":
        Quadrado()
    elif opcao == "4":
        Retângulo()
    elif opcao == "5":
        Paralelogramo()
    elif opcao == "6":
        Losango()
    elif opcao == "7":
        Trapézio()
    elif opcao == "0":
        print ("Saindo do sistema...")
        break
