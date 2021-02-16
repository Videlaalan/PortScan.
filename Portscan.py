import socket

ip = input ("Escrbir la direccio IP: ")

puerto = input("Escribir el puerto para Escanear: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

resultado = s.connect_ex((ip,int (puerto)))

if resultado == 0:
	print ("El puerto " + puerto + "esta abierto :=) ")
else:
	print("El puerto "+ puerto + " esta cerrado :=( ")