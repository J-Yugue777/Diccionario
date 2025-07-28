#EJERCICIO 1
# ed=int(input("ingrese su edad :"))
# if ed >= 18 and ed <=65:
#     print("usted es mayor de edad")
# elif ed >= 65:
#     print("usted es adulto mayor")
# else:
#     print("usted es menor de edad")
#EJERCICIO 2
# al=float(input("ingrese su edad : "))
# if al >= 1.5 and al < 1.8:
#     print("usted esta en la altura media ")
# elif al >=1.8:
#     print("usted es alto")
# else:
#     print("su altura es demasiado baja ")
#EJERCICIO 3
# MUL=int(input("ingrese un numero "))
# if MUL % 2== 0:
#     print("su numero es multiplo de 2")
# elif MUL % 3==0:
#     print("su numero es multiplo de 3")
# else: 
#     print("no es multiplo ni de dos o tres ")
#EJERCICIO 4
# m=float(input("ingrese un numero en decimales : "))
# a=str(m)
# if a == 1:
#     print("posee un decimal")
# else:
#     print("posee mas de dos decimales")
#EJERCICIO 5
# t=("COLOMBIA","PERU","ARGENTINA","MEXICO")
# i=input("ingrese un pais : ")
# if i == t[0]:
#     print("lo agregado si esta en la lista ")
# elif i == t[1]:
#     print("SI ESTA EN LA LISTA")
# elif i == t[2]:
#     print("SI ESTA EN LA LISTA")
# elif i == t[3]:
#     print("SI ESTA EN LA LISTA")
# else:
#     print("no esta en la lista ")
#EJERCICIO 6 
# DIC={
#     "A":"B",
#     "O":"AB",
#     "B":"O",
#     "AB":"A"
# }
# print(f" segun la lista  {DIC}   escriba su tipo de sangre :")
# san=input("escriba su tipo de sangre : ")
# if san == DIC["A"]:
#     print("es compatible con A")
# elif san == DIC["O"]:
#     print("compatible con O")
# elif san == DIC["B"]:
#     print("su compatibilidad es  con B")
# elif san==DIC["AB"]:
#     print("es compatible con AB")
#EJRCICIO 7
# t=float(input("ingrese la temperatura : "))
# if  t >=10 and t < 25:
#     print("la temperatura esta en templado ")
# elif t >=25:
#     print("QUE CALOR ")
# else:
#     print("mucho frio ")
#EJERCICIO 8
# o=int(input("ingrese primer numero : "))
# w=input("que operacion va a realizar :opcion = suma,resta,multiplicacion ,division : ")
# u=int(input("ingrese segundo numero : "))
# suma=o+u
# resta=o-u
# multiplicacion=o*u
# division=o/u
# if w=="suma":
#     print(f"la suma da {suma}")
# elif w=="resta":
#     print(f"la resta da {resta}")
# elif w=="multiplicacion":
#     print(f"la multiplicacion{multiplicacion}")
# elif w=="division":
#     print(f"la division da {division}")
#EJERCICIO 9
# dic={
#     1:"enero",2:"febrero",3:"marzo",4:"abril",5:"mayo",6:"junio",7:"julio",8:"agosto",9:"septiembre",10:"octubre",11:"noviembre",12:"diciembre"
# }
# me=int(input("ingrese un numero del 1 al 12 : "))
# if me == 1:
#     print(f"su mes es {dic[1]}")
# elif me == 2:
#     print(f"su mes es {dic[2]}")
# elif me == 3:
#     print(f"su mes es {dic[3]}")
# elif me == 4:
#     print(f"su mes es {dic[4]}")
# elif me == 5:
#     print(f"su mes es {dic[5]}")
# elif me == 6:
#     print(f"su mes es {dic[6]}")
# elif me == 7:
#     print(f"su mes es {dic[7]}")
# elif me == 8:
#     print(f"su mes es {dic[8]}")
# elif me == 9:
#     print(f"su mes es {dic[9]}")
# elif me == 10:
#     print(f"su mes es {dic[10]}")
# elif me == 11:
#     print(f"su mes es {dic[11]}")
# elif me == 12:
#     print(f"su mes es {dic[12]}")
# else:
#     print("error")
#EJERCICIO 10
# nu=int(input("ingrese un numero"))
#EJERCICIO 11 
#EJERCICIO 12
# li=["manzana","pera","piña"]
# print(li)
# f=input("ingrese una de las frutas para saber su precio : ")
# if f == li[0]:
#     print(f"la fruta {f} tiene un costo de 1000")
# elif f== li[1]:
#     print(f"la fruta{f} vale 1700 ")
# elif f== li[2]:
#     print(f"la fruta {f} esta en un valor de 5000")
# else:
#     print("ERROR NO DISPONIBLE")
#EJERCICIO 13
# ca=int(input("ingrese su calificacion : "))
# if ca >= 3 and ca <= 4:
#     print("usted aprobo ")
# elif ca >= 5:
#     print("excelente calificacion")
# else:
#     print("usted a reprobado")
#EJERCICIO 14
# w=int(input("ingrese un numero : "))
# if w %  4 == 0:
#     print("si es divisible en tre 4 ")
# else :
#     print("NO es divisible entre 4")
# if w % 6==0:
#     print("es divisible por 6 ")
# else :
#     print("no es divisible por 6")
#EJERCICIO 15
# dix={
#     "user":"JUAN",
#     "PASS":1234
# }
# a=input("ingrese su nombre de usuario : ")
# b=int(input("ingrese su contraseña : "))
# if a== dix["user"] and b== dix["PASS"]:
#     print(f"BIENVENIDO {a}")

# else:
#     print("ERROR DIGITOS INVALIDOS.")
#EJERCICIO 16
# j=int(input("ingrese su edad : "))
# if j >=13 and j <=17:
#     print("usted es un joven adolencente ")
# elif j >= 18 and j <= 64:
#     print("usted es mayot de edad ,un adulto")
# elif j>=65:
#     print("usted es ya un adulto mayor ")
# else:
#     print("eres aun un niño")
#EJERCICIO 17
# c=("cairo","palmira","roma","vennesi","california","pekin")
# city=input("ingrese una ciudad : ")
# if city == c[0]:
#     print("ciudad capital ")
# elif city == c[1]:
#     print("ciudad capital")
# elif city == c[2]:
#     print("ciudad capital")
# elif city == c[3]:
#     print("ciudad capital")
# elif city == c[4]:
#     print("ciudad capital")
# elif city == c[5]:
#     print("ciudad capital")

# else :
#     print("ciudad secundaria")
#EJERCICIO 18
# p=int(input("ingrese el valor de su compra : "))
# r=p-(p*0.1) 
# if p >= 100000 and p <=  200000:
#     print(f"su valor de compra es de {r}")
# elif p > 200000:
#     f=p-(p*0.15)
#     print(f"su valor apagar esta en {f}")
# else :
#     print(f"valor es {p}")
#EJERCICIO 19 
# a=input("ingrese su nombre : ")
# e=int(input("ingrse sus horas de trabajo : "))
# q=10000*e
# if e>= 40:
#     print(f"{a} su salario es de : {(q*0.2)+q}")
# else:
#     print(f"{a} su salario es de {q}")
#PRUEBA
# d={
#     "a":int(input("dar")),
#     "e":int(input("dar"))

# }
# f=d["a"]+ d["e"]
# li=[]
# li.append(f)
# t=tuple(li)
# print(t)

#29/07/2025
#EJERCIO 1
# a=int(input("ingrese un numero : "))
# if a > 0:
#     print("es un positivo ")
# elif a <=-1:
#     print("es un negativo ")
# else:
#     print("es un cero")
#EJERCICIO 2
# a=float(input("ingrese primer valor : "))
# b=float(input("ingrese segundo valor "))
# if a>b:
#     print(f"es {a} mayor a {b}")
# else:
#     print(f"es {b} mayor que {a}")
# a=int(input("ingrese un valor : "))
# if a % 2 == 0:
#     print("es par ")
# else : 
#     print("es un impar")
#EJERCICIO 4
# e=int(input("ingrese un valor : "))
# if e >=10 and e <=20 :
#     print("esta en el rango de 10-20")
# else:
#     print("no esta el rango de edad")
#EJERCICIO 5
# i=int(input("ingrese un numero : "))
# i1=int(input("ingrese un numero : "))
# i2=int(input("ingrese un numero : "))
# if i>i1 and i1>i2:
#     print(f"el mayor es {i}")
# elif i1>i and i1>i2:
#     print(f"{i1} es mayor")
# else:
#     print(f"es mayor {i2}")
#EJERCICIO  6
# produc=int(input("ingrese el valor del producto : "))
# if produc >= 100:
#     print(f"{produc-produc*0.1} es su valor total")
# else:
#     print(f"su valor sigue siendo de {produc}")
#EJERCICIO 7
# eda=int(input("ingrese su edad : "))
# if eda>=18:
#     print("usted es mayor de edad, usted puede votar ")
# else:
#     print("usted es menor no puede votar ")
#EJERCICIO 8
# catal=input("¿usted posee membresia VIP? (si o no) : ")
# valo=int(input("ingrese sel costode su compra "))
# if catal == "si":
#     print(f"su total a pagar es de {valo-valo*0.2}")
# else :
#     print(f"su valor de {valo}")
#EJERCICIO 9
# num=int(input("ingrese un numero : "))
# if num % 5==0 and num % 3 == 0:
#     print("este numero es multiplo de 5 y 3")
# else:
#     print("no es multiplo de 5 y 3 ")
#EJERCICIO 10 
# a=int(input("ingrese un numero : "))
# e=int(input("ingrese un numero divisor : "))
# i=int(input("ingrse segundo numero divisor : "))
# if a % e ==0 and a % i == 0 :
#     print(f"es divisible por {e} da {a/e} y {i} da {a/i}")
# else:
#     print("no es divisible por los dos ")
#EJERCICIO 11
# lis=[int(input("ingrse numero : ")),int(input("ingrse numero : ")),int(input("ingrse numero : ")),int(input("ingrse numero : ")),int(input("ingrse numero : "))]
# if lis[2] >= 10:
#     print(" mayor a 10 ")
# else:
#     print("menor a 10 ")
#EJERCICIO 12
# li=[int(input("ingrese un numero :")),int(input("ingrese un numero :")),int(input("ingrese un numero :")),int(input("ingrese un numero :")),int(input("ingrese un numero :"))]
# if li[0] == 7 or li[1]==7 or li[2]==7 or li[3]==7 or li[4]==7:
#     print("si esta ")
# else:
#     print("no esta ")
# print(li)
#EJERCICIO 13
# li=[int(input("ingrese un numero a la lista ")),int(input("ingrese un numero a la lista ")),int(input("ingrese un numero a la lista ")),int(input("ingrese un numero a la lista "))]
# if li[0]+li[1]>=10:
#     print("es mayor a 10 ")
# else :
#     print("es menor a 10 ")
#EJERCICIO 14
# lis=["ana","luis","pedro","marta"]
# if lis[0]=="marta" or lis[1]=="marta" or lis[2]=="marta" or lis[3]=="marta":
#     print("si esta en la lista ")
# else:
#     print("no esta en la lista ")
# print(lis)
#EJERCICIO 15
l=[input("ingrse un color"),input("ingrse un color"),input("ingrse un color")]
if l[1]=="azul":
    nclor=input("ingrese nuevo color : ")
    print(l.insert)
else:
    print(l)