sex = 0
op = 0
n1 = 0
n2 = 0
answer = 0 

sex = int(input(" Gostaria de ultilizar a calculadora? se sim digite 1, se não, digite 0 = "))
while(sex!=0):
    op = int(input("Certo! escolha a operação desejada digitando: (1)multiplicação (2)divisão (3)adição (4)subtração = "))
    print("\n")

    if (op==1):
     print("Multiplicação")
     n1 = float(input("digite o primeiro valor = "))
     n2 = float(input("digite o segundo valor = "))
     answer = n1*n2
     print (n1, "X", n2, "=", answer)
     
    elif (op==2):
     print("Divisão")
     n1 = float(input("digite o primeiro valor = "))
     n2 = float(input("digite o segundo valor = "))
     answer = n1/n2
     print (n1, "/", n2, "=", answer)

    elif (op==3):
     print("Adição")
     n1 = float(input("digite o primeiro valor = "))
     n2 = float(input("digite o segundo valor = "))
     answer = n1+n2
     print (n1, "+", n2, "=", answer)

    elif (op==4):
     print("Subtração")
     n1 = float(input("digite o primeiro valor = "))
     n2 = float(input("digite o segundo valor = "))
     answer = n1-n2
     print (n1, "-", n2, "=", answer)

    sex = int(input(" Gostaria de ultilizar a calculadora novamente? se sim digite 1, se não, digite 0 = "))
     
print("Beleza! calculadora encerrada.")
