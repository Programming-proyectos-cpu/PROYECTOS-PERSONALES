import math
import random
import os

def suma(a, b):
    print("valor es",a + b)
    
    
def resta(a, b):
    print("valor es",a - b)
    
def multiplicacion(a, b):
    print("valor es",a * b)
    
def division(a, b):
    print("valor es", a / b)
    
   
def potencia(a, b):
    print("Valor es", a ** b)
    
def raiz(a):
    print("raiz es",math.sqrt(a))
    
def pi():
    print("El valor de pi es",math.pi)
    
def numero_random():
    num_random=random.randint(1,99999)
    print(num_random)
    
def nivel_facil():
    num_random1=random.randint(1,5)
    num_jugador1=input("Adivine un número del 1 al 5: ")
    
    if num_random1==num_jugador1:
        print("Correcto por ahora: ")
    else:
        print("Incorrecto jaja")
def nivel_medio():
    num_random2=random.randint(1,20)
    num_jugador2=input("Adivine un número del 1 al 20: ")
    
    if num_random2==num_jugador2:
        print("Correcto por ahora: ")
    else:
        print("Incorrecto jaja")

def nivel_dificil():
    num_random3=random.randint(1,50)
    num_jugador3=input("Adivine un número del 1 al 50: ")
    
    if num_random3==num_jugador3:
        print("Correcto por ahora: ")
    else:
        print("Incorrecto jaja")
    
    
    
while True:
    print("(7,8...)RESULTADOS ⬆️⬆️⬆️⬆️⬆️")
    print("============================")
    print(" ==^===^== ")
    print("|===®---®===")
    print("|====^=^====|")
    print("=====###====")
    print("   =======      ")
    print("101001010010101")
    
    print("===========================")
    print("   ππππππ")
    print(" π")
    print("π")
    print("π                         X")
    print("π")
    print(" π")
    print("   ππππππ")
    print("============================")
    
    print("============================")
    print("∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆")
    print("=BIENVENIDO USUARIO=")
    print(" =[1]suma           =")
    print("  =[2]resta          =")
    print("   =[3]multiplicacion =")
    print("    =[4]division       =")
    print("     =[5]potencia       =")
    print("      =[6]raiz           =")
    print("       =[7]pi             =")
    print("        =[8]numero random  =")
    print("         =[9]mini juego     =")
    print("          =[10]clear chat    =")
    print(".          =[11]salir.        =")
    print("            ππππππππππππππππππππ")
    print("_________________________________________")
    print("indentation america latina creado in IAN|")
    print("-----------------------------------------")
    operacion=input("Ingrese operacion (1,10): ")

    match operacion:
        case '7':
            os.system('clear')
            pi()
            continue
        case '8':
            os.system('clear')
            numero_random()
            continue
        case '9':
             os.system('clear')
             
             print("  ⬜⬜⬜⬜⬜⬜    ")
             print("⬜⬜⬜🔲🔲⬜⬜⬜⬜")
             print("⬜⬜⬜🔲🔲⬜⬜⬜⬜")
             print("⬜⬛⬛⬜⬜⬛⬛⬜")
             print("⬜⬛⬛⬛⬛⬛⬛⬜")
             print("⬜⬛⬛⬜⬜⬛⬛⬜")
             print("⬜⬜⬜⬜⬜⬜⬜⬜")
             print("⬛⬛⬛⬛⬛⬛⬛⬛")
             print("⬛⬛⬛⬛⬛⬛⬛⬛")
             print("  ⬛⬛⬛⬛⬛⬛")
             print("⬛⬛⬛⬛⬛⬛⬛⬛")
             print("==========================")  
             print("πDIFICULTAD MINI JUEGO%π")
             print("|-----------------------|")
             print("-[1]facil               ")
             print("-[2]medio        ")
             print("-[3]dificil")
             print("-[4]salir")
             print("________________________")
           
             dificultad=int(input("Ingrese dificultad: "))
             
             match dificultad:
                 case '1':
                     nivel_facil()
                     continue
                 case '2':
                     nivel_medio
                     continue
                 case '3':
                     nivel_dificil()
                     continue
                 case '4':
                     print("Ok chau brother")
                     continue
             
                 case '10':
                     print("chat limpio")
                     os.system('clear')
              
                 case '11':
                     print("Chau brother")
                     break

    num1=float(input("Ingrese su primer numero: ")) # <- 4 espacios
    
             
         
    if operacion == '6':
        raiz(num1)
        continue # <- 8 espacios
    os.system('clear')
    num2=float(input("Ingrese su segundo numero: ")) # <- 4 espacios
    
    
    
    match operacion:
          case '1':
              suma(num1, num2)
          case '2':
              resta(num1, num2)
          case '3':
              multiplicacion(num1, num2)
          case '4':
              if num2==0:
                  print("Nono bb asi no es ,es imposible dividir por 0")
              else:
                  division(num1, num2)
          case '5':
              potencia(num1, num2)
