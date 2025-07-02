#DICCIONARIO
# auto={
#     "marca":"ford",
#     "modelo":"mustang",
#     "año":2022
# }
# auto.pop("marcas")
# auto["año"]=2023
# print(auto["modelo"])
# print(auto)
#EJERCICIO DE PRACTICA
# LISTA=[]
# V1=float(input("Ingrese su nota : "))
# V2=float(input("Ingrese su nota : "))
# V3=float(input("Ingrese su nota : "))
# LISTA.append(V1)
# LISTA.append(V2)
# LISTA.append(V3)
# LISTA.append("promedio es ")
# VF=(V1+V2+V3)/3
# LISTA.append(VF)
# print(LISTA)
#EJERCICIO 2
# productos={
#     "Papa":200,
#     "cebolla":400,
#     "arracacha":700
# }
# print(f"lista  de productos disponibles : {productos}")
# POR=int(input("cuanto es el porcentaje de cambio : "))
# productos["Papa"]+= productos["Papa"] * (POR/100)
# productos["cebolla"]+= productos["cebolla"] * (POR/100)
# productos["arracacha"]+= productos["arracacha"] * (POR/100)
# print(f"con el aumento de porcentaje quedan al costo de : {productos}")
#EJERCICIO 3
# c=float(input("Dar la temperatura : "))
# c1=float(input("Dar la temperatura : "))
# c2=float(input("Dar la temperatura : "))
# c3=float(input("Dar la temperatura : "))
# c4=float(input("Dar la temperatura : "))
# celsios=(c,c1,c2,c3,c4)
# f=c*9/5+32
# f1=c1*9/5+32
# f2=c2*9/5+32
# f3=c3*9/5+32
# f4=c4*9/5+32
# farent=(f,f1,f2,f3,f4)
# print(f"en grados celsios la temperatura esta en {celsios}")
# print(f"la temperatura en fahrenhelt esta en {farent}")
#EJERCICIO 4
# edad=[int(input("escriba su edad: ")),int(input("escriba su edad: ")),int(input("escriba su edad: ")),int(input("escriba su edad: ")),int(input("escriba su edad: "))]
# prom= sum(edad) / len(edad)
# print(f"la edad mas alta es {max(edad)} y la edad mas baja es {min(edad)} y el promedio de todo es : {prom}")
#EJERCICIO 5 
# fru={
#     "kiwi":2000,
#     "manzana":3000,
#     "naranja":2500,
# }
# pedi=[int(input("dar cuantos kilos quieres de kiwi : ")),int(input(f"dar cuantos kilos quieres de : ")),int(input("dar cuantos kilos quieres de naranja : "))]
# h=[(fru["kiwi"]*(pedi[0]))+(fru["manzana"]*(pedi[1]))+(fru["naranja"]*(pedi[2]))]
# print(f"su total a pagar por todos los productos es de {h} . Gracias por su compra.")
#EJERCICIO 6
# tup=(2+3+4+67+21)
# print(tup)
#EJERCICIO 7 
# p={input("ingresse su primer producto: ")}
# p1={"a":int(input(f"ingrese cuanto quiere de {p}: "))*int(input(f"ingrese el valor de {p} "))}
# p2={input("ingresse su segundo producto: ")}
# p3={"e":int(input(f"ingrese cuanto quiere de {p2} : "))*int(input(f"ingrese el valor de {p2}"))}
# p4={input("ingresse su tercer producto: ")}
# p5={"i":int(input(f"ingrese cuanto quiere de {p4} : "))*int(input(f"ingrese el valor de {p4} "))}
# x=[p1["a"]+p3["e"]+p5["i"]]
# print(f"el valor total de todo esto ronda en : {x}")
#EJERCICIO 8
# li=["papa",600,"cebolla",500,"naranja",1000]
# print(f"los  productos se encuentra a : {li}")
# us=float(input("Nuevo valor de los productos en porcentaje % : "))
# li[1]=(us)*li[1]/100
# li[3]=(us)*li[3]/100
# li[5]=(us)*li[5]/100
# print(f"con la modificacion el valor esta en  : {li}")
#EJERCICIO 9
# u=[float(input("ingrese su primer nota : ")),
# float(input("ingrese su segunda nota : ")),
# float(input("ingrese su tercera nota : ")),
# float(input("ingrese su cuarta  nota : "))]
# t=tuple(u)
# M=max(u)
# m=min(u)
# print(f"{t} el valor mas alto de las nota es {M} mientras que el mas bajo es {m}")
#EJERCICIO 10
# dis={
#     "Km":1000,
#     "cm":100,
#     "mm":1000,
# }
# c=float(input("ingrese una medida en metros para pasar a Km , cm , mm : "))
# me=["en kilometros",c/dis["Km"],"centimetros ", dis["cm"]*c ,"milimetros :", dis["mm"]*c]
# print(f"la conversion da como resultado {me}")
#EJERCICIO 11
# p=[float(input("ingrese un precio : ")),float(input("ingrese un segundo precio : ")),float(input("ingrese un tercer  precio : "))]
# iv=19/100
# a=p[0]*iv
# a1=p[1]*iv
# a2=p[2]*iv
# p[0]=p[0]+a
# p[1]=p[1]+a1
# p[2]=p[2]+a2
# print(f"con el aumento de 19% sus precios estan en :{p}")
#EJERCICIO 12
# q=float(input("digite un numero : "))
# q1=float(input("digite un segundo numero : "))
# li=[]
# li.append(q+q1)
# li.append(q-q1)
# li.append(q*q1)
# li.append(q/q1)
# di={li.insert(0,"suma :"),li.insert(2,"resta :"),li.insert(4,"multiplicacion :"),li.insert(6,"division :")}
# tu=tuple(li)
# print(tu)
#EJERCICIO 13
# dic={"juan":5.0,"sofia":4.5,"manuel":3.9,"monica":4.3,"laura":4.0}
# print(dic)
# prom=[(dic["juan"]+dic["sofia"]+dic["manuel"]+dic["monica"]+dic["laura"])/5]
# print(f"el promedio de notas de los estudiantes es de : {prom}")
#EJERCICIO 14
# dis={"a":int(input("ingrese un primer salario : ")),"e":int(input("ingrese un primer salario : ")),"i":int(input("ingrese un primer salario : ")),"o":int(input("ingrese un primer salario : ")),"u":int(input("ingrese un primer salario : "))}
# por=10/100
# sal=[dis["a"]*por+dis["a"],dis["e"]*por+dis["e"],dis["i"]*por+dis["i"],dis["o"]*por+dis["o"],dis["u"]*por+dis["u"]]
# print(f"con un aumento del 10% los salarios quedaron con un total de : {sal}")
#EJERCICIO 15
# im={
#     "arroz":2500,
#     "pan":500,
#     "papel higienico":5000,
#     "jabon":2500,
#     "manzanas":800
# }
# print(im)
# user=float(input("digite el valor de los impuestos % : "))
# x=user/100
# imp=[im["arroz"]*user+im["arroz"],"arroz",im["jabon"]*user+im["jabon"],"jabon ",im["manzanas"]*user+im["manzanas"],"manzanas",im["pan"]*user+im["pan"],"pan",im["papel higienico"]*user+im["papel higienico"],"papel higienico"]
# print(f"el precio de cada uno de los productos despues de impuestos es de:{imp} ")
# EJERCICIO 16
# US=[int(input("ingrese edad : ")),int(input("ingrese edad : ")),int(input("ingrese edad : ")),int(input("ingrese edad : "))]
# if US[0] >= 18:
#     print(f"es mayor {US[0]}")
# else:
#     print(f"es menor de edad {US[0]}")
# if US[1] >=18 :
#     print(f"es mayor {US[1]}")
# else:
#     print(f"es menor de edad {US[1]}")
# if US[2] >=18 :
#     print(f"es mayor {US[2]}")
# else:
#     print(f"es menor de edad {US[2]}")
# if US[3] >=18 :
#     print(f"es mayor {US[3]}")
# else:
#     print(f"es menor de edad {US[3]}")
#EJERCICIO 17
# # t=("dolar=0.85 euros","dolar=145.64 yenes")
# A=float(input("Ingrese cuantos dolares va a convertir : "))
# a=A-0.15
# b=A*145.64
# r=[]
# r.append(a)
# r.append(b)
# tu=tuple(r)
# print(f"AL final de la conversion dio {tu}")
#EJERCICIO 18
# P={"a":input("ingrese el primer producto : "),"aa":int(input("cantidad del producto : ")),"b":input("ingrese el primer producto : "),"ab":int(input("cantidad del producto : ")),"c":input("ingrese el primer producto : "),"ac":int(input("cantidad del producto : "))}
# tot=P["aa"]+P["ab"]+P["ac"]
# print(f"el total vendido de los productos da {tot}")
#EJERCICIO 19
