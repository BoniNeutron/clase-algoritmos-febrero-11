#comandos del lenguaje:
    # print() -> Escribir(), Mostrar(), imprimirPantalla()
    # type() -> permite conocer el tipo de dato
    # input() -> ingresar()

#entradas
print("por favor ingresar un numero")
num1=int(input())
print("por favor ingresar el segundo numero")
num2=int(input())
ope=str(input("que operacion desea realizar:\n1.suma\n2.resta\n3.multiplicacion\n4.Division\n"))
#procesos

if ope=="suma" or ope=="1" or ope=="Suma" or ope=="SUMA":
	suma= num1 +num2
	print("el resultado de la suma es ")
	print(suma)
elif ope=="resta":
	rest=num1 - num2
	print("el resultado de la resta es ", rest)
elif ope=="multiplicacion":
	mult= num1* num2
	print("el resultado de la multiplicacion "+str(mult))
elif ope=="division":
	divi=num1//num2
	print(f"el resultado de la division es {divi} y el residuo de la division es {num1%num2}")
else:
	print("error: la opcion elegida es invalida")