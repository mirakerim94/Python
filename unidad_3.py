#ejercicios sesion3:
#1) escribir una expresion para saber si un numero es mas grande que otro. Guardarla en una variable de tipo bool e imprimirla por pantalla para ver su valor:
numero1 = 10
numero2 = 544
es_mas_grande = numero1 > numero2
print(es_mas_grande)

#ej2/ Repetir el punto anterior pero con la expresión que determina que una letra NO es vocal.
letra = "n"
es_vocal = letra in "a,i,o,e,u"
print(es_vocal)

#ej3 / Repetir pero para la expresión que permite saber si un número es par y menor a 10.
numero = 8
es_par = numero % 2 == 0
es_menor_a_10 = numero < 10
print(es_par and es_menor_a_10)

"""Crear una función que dado un número, devuelva su valor absoluto. El valor absoluto de un número es
el mismo número sin considerar el signo.
Por ejemplo, el absoluto de 2 es 2 (|2| = 2) y el absoluto de -4 es 4 (|-4|=4)."""
def valor_absoluto(num):
  if num < 0:
    return num * -1
  else:
    return num

print(valor_absoluto(-7))

"""ej 5/ Crear el programa al que sea imposible ganarle en el juego de “Piedra, papel o tijera”. Cada elemento va
a ser representado con una letra: R para piedra, P para papel y T para tijera.
a. Hacer una función que le haga al usuario ingresar alguna de esas letras, e imprima por pantalla
la jugada para ganarle. Por ejemplo:
> ¡Juguemos! Ingresá piedra ( R), papel (P) o tijera (T)
> P
> Tijera. ¡Te gané!
ATENCIÓN: Observar cómo se usa una frase inicial para darle a entender al usuario lo que tiene
que hacer (en este caso ingresar alguna de las tres letras)
Mostrar por pantalla el mensaje “NO vale” cuando el usuario ingresa una letra no válida
(distinta de R, P o T)."""
def piedra_papel():
  usuario = input("¡Juguemos! Ingresá piedra (R), papel (P) o tijera (T)")
  upper_case = usuario.upper()
  if upper_case not in ["R","P","T"]:
    print("NO vale!")
  elif upper_case == "P":
    print("Tijera. ¡Te gané!")
  elif upper_case == "T":
    print("R(Piedra). ¡Te gané!")
  else:
    print("Papel. ¡Te gané!")
    
piedra_papel()

"""ej 6 / Escribir código que dado dos enteros, determine si la suma de ambos da menos que 100. Si la suma de
ambos es menor a 100, calcular cuánto falta para llegar a 100 y mostrar por pantalla un mensaje con
ese valor. Si la suma es mayor a 100, mostrar un mensaje diciendo “Llega a 100”.
Extra: ¿Cómo harían para que el programa quede generalizado para cualquier límite, a elección del
usuario, y no solo para 100?."""

def total():
  num1 = int(input("ingrese primer numero: "))
  num2 = int(input("ingrese el segundo numero: "))
  suma = num1 + num2
  if suma < 100:
    menos_de_100 = 100 - suma
    print("Falta ", menos_de_100, "para llegar a 100")
  elif suma > 100 :
    print("Llega a 100")
  else:
    print("La suma es igual a 100")

total()
# Input de dos enteros
num1 = int(input("Ingrese el primer entero: "))
num2 = int(input("Ingrese el segundo entero: "))

# Input del límite
limite = int(input("Ingrese el límite deseado: "))

# Suma de los dos enteros
suma = num1 + num2

# Comprobar si la suma es menor que el límite
if suma < limite:
    diferencia = limite - suma
    print("La suma es menor que", limite, ". Faltan", diferencia, "para llegar al límite.")
elif suma > limite:
    print("Llega a", limite, ".")
else:
    print("La suma es igual a", limite, ".")

"""ej 7 / Se tienen letras para representar las estaciones del año:
● V para verano
● O para otoño
● I para invierno
● P para primavera
Crear una función que dada una letra, imprima por pantalla la estación del año que representa (es
decir, si se ingresa V se mostrará por pantalla el mensaje “Verano”). En caso de no representar a
ninguna estación mostrar un mensaje que diga “error”. Probar la función creada llamándola con A, P, O,
B, V e I."""

def estaciones():
    estacion = input("Ingrese una letra: V, O, I, P")

    if estacion == "V" or "v":
        print("Verano")
    elif estacion == "O" or "o":
        print("Otoño")
    elif estacion == "I" or "i":
        print("Invierno")
    elif estacion == "P" or "p":
        print("Primavera")
    else:
        print("Error")

estaciones()

"""ej 8 / Se quiere hacer un programa para enseñar a unos niños a contar. Crear una función que reciba un
número entero e imprima por pantalla los números del 1 hasta ese número con la estructura de control
iterativa for."""

def conta(num):
  for i in range(1, num + 1):
    print(i)

conta(14)

"""ej9 / Se quiere mejorar el programa para enseñar matemáticas pensado en el ejercicio anterior. Ahora se
necesita una funcionalidad que permita a los niños aprender las tablas. Crear una función que reciba un
número entero e imprima por pantalla la tabla de ese número del 1 al 10."""

def tabla(num):
    if num < 1 or num > 10:
        print("El número debe estar entre 1 y 10!")
        return

    print(f"Tabla de multiplicar del {num}:")

    for i in range(1, 11):
        resultado = i * num
        print(f"El resultado de multiplicación es: {resultado}")

tabla(100)

"""ej10/ 0. Crear una función que simule un cumpleaños: que dado un entero imprima “Que los cumplas feliz” esa
cantidad de veces."""

def cumple(num):
  for i in range (num):
    print("Que los cumplas feliz!")

cumple(7)

"""ej11 / En un almacén están buscando la forma de hacer los cobros más automáticamente. Para esto, se nos
pide crear una función que reciba un número entero que representa lo que hay que cobrar, le pida al
usuario ingresar un monto, y se vaya mostrando por pantalla cuánto falta para completar el pago.
Repetir este proceso hasta que la deuda sea 0 o menor. Por ejemplo, si se recibe el monto 30:
> El importe a pagar es de 30 pesos. Por favor, ingrese un monto.
> 10
> El importe a pagar es de 20 pesos. Por favor, ingrese un monto.
> 15
> El importe a pagar es de 5 pesos. Por favor, ingrese un monto.
> 5"""

def pago_automatico():
  #deuda inicial:
  deuda = int(input("Ingrese el monto total a pagar: "))
  while deuda > 0:
    monto = int(input(f"Falta pagar {deuda} pesos. Ingrese el monto a pagar: "))
    deuda -= monto
    if deuda == 0:
      print("Pagado!")


pago_automatico()

"""ej12/ Escribir código que recorra los números del 1 al 20 y determine para cada uno si es par o impar,
imprimiendo un mensaje por pantalla en cada caso. Es decir, el output esperado sería:
> El número 1 es impar.
> El número 2 es par.
…
> El número 20 es par"""
def par_impar(num):
  for n in range(1, num + 1):
    if n % 2 == 0:
      print(f"{n} es par")
    else:
      print(f"{n} es impar")

par_impar(10)

"""ej13 / . Se tiene una máquina de sacar juguetes que funciona cuando se ingresa una determinada cantidad de
fichas, y se quiere hacer una función que imite ese comportamiento.
a. Hacer una función que reciba un número que represente el precio de la máquina, e imprima
por pantalla “Ingresá x fichas para comenzar” hasta que se hayan ingresado esa cantidad de
letras F (que representan una ficha), y luego “¡A jugar!” cuando se hayan ingresado todas las
fichas necesarias. Por ejemplo, si la función recibe 3, debería tener el siguiente
comportamiento:
> Ingresá 3 fichas para comenzar
> F
> Ingresá 3 fichas para comenzar
> F
> Ingresá 3 fichas para comenzar
> B
> Ingresá 3 fichas para comenzar
> F
> ¡A jugar!
ATENCIÓN: notar cómo cuando se ingresa una letra distinta de F, esta se ignora a la hora de contar la
cantidad de fichas que fueron ingresadas.
b. Ahora se quiere que se vaya mostrando por pantalla, cuántas fichas FALTAN ingresar para
empezar a jugar Es decir:
> Ingresá 3 fichas (F) para comenzar
> F
> Ingresá 2 fichas (F) para comenzar
> F
> Ingresá 1 fichas (F) para comenzar
> B
> Ingresá 1 fichas (F) para comenzar
> F
> ¡A jugar!
c. Agregar a la función el mensaje de error “Por favor solamente ingrese fichas reales (F)” cuando
se recibe una letra distinta de F."""

def game(n):
  count = 0
  user = ""
  while count < n:
    print(count)
    if count != 0:
      print(count) 
      faltantes = n - count
      user = input(f"Te faltan {faltantes} fichas: ")
    else:
      user = input(f"Ingresa {n} fichas: ")

    if user == "F":
      count += 1

    else:
      print("Error")

  print("A jugar!")

game(3)

"""ej14/ Crear una función que reciba un número entero e imprima los números primos entre 0 y el número
ingresado.
AYUDA: un número es primo cuando solamente es divisible por sí mismo y por 1, es decir que para ver
si es primo hay que ver que el módulo (%) de ese número con los anteriores hasta el 1 (sin incluirlo) sea
distinto de 0, o sea que no sea divisible."""

def es_primo(numero):
   if numero < 2:
       return False
   for i in range(2, numero):
       if numero % i == 0:
           return False
   return True

def numeros_primos_hasta_n(n):
   for i in range(2, n + 1):
       if es_primo(i):
           print(i)

 # Solicitar al usuario un número entero
numero = int(input("Ingrese un número entero: "))
print("Números primos hasta", numero, ":")
numeros_primos_hasta_n(numero)