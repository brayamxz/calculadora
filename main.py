def add(x, y):
 return x + y  

def sub(x,  y):
  return x - y

def mult(x, y):
  return x * y 

def div(x, y):
 return x / y

#calculadora 
print("selecione uma operação.")
print("1. adição.")
print("2. Subtração.")
print("3. Multiplicação.")
print("4. Divisão.")

while True: 
  escolha = input("Escolha um numero (1/2/3/4): ")
  
  if escolha in  ('1' , '2', '3', '4' ):
    num1 = float(input("Digite um numero: "))
    num2 = float(input("digite outro numero: "))
                 

    if escolha == '1':
      print(num1, "+", num2, "=", add(num1, num2))

    elif escolha == '2' :
      print(num1, "-", num2, "=", sub(num1, num2))

    elif escolha == '3':
      print(num1, "*", num2, "=", mult(num1, num2))

    elif escolha == '4':
      print(num1, "/", num2, "=", div(num1, num2))

    else:
      print("Numero invalido. ")
 