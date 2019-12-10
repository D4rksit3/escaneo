#!/usr/bin/python
#-*- coding:utf8-*-

import socket
import os,sys,time
import requests
import platform
import urllib


version = sys.version[0]
def ip_publica():
	if version == '2':
	  import urllib2 as urllib
	else:
	  import urllib.request as urllib

	url1 = None
	servidor1 = 'http://www.soporteweb.com'

	consulta1 = urllib.build_opener()
	consulta1.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0')] 

	try:
	  url1 = consulta1.open(servidor1, timeout=17)
	  respuesta1 = url1.read()
	  if version == '3':
	    try:
	      respuesta1 = respuesta1.decode('UTF-8')
	    except UnicodeDecodeError:
	      respuesta1 = respuesta1.decode('ISO-8859-1')

	  url1.close()
	  print('\033[93m Tu IP publica es: \033[32m'+respuesta1)
  
	except:
	  print('Falló la consulta ip a '+servidor1)


def direccion():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("iplocation.com", 80))
	print("\033[93m Tu IP privada es: \033[32m"+s.getsockname()[0])
	s.close()

def banner():
	time.sleep(0.5)
	direccion()
	time.sleep(0.5)
	ip_publica()
	time.sleep(0.3)
	print ("\n\033[97m [1]- Obtener direccion IP de una website")
	time.sleep(0.2)
	print (" [2]- Escaneo de red + puertos (rápido)")
	time.sleep(0.2)
	print (" [3]- Escaneo de puertos TCP ")
	time.sleep(0.2)
	print (" [4]- Escanear todos los puertos ")
	time.sleep(0.2)
	print (" [5]- Escaneo TCP SYN (opción por defecto)")
	time.sleep(0.2)
	print (" [6]- Escaneo de sistema operativo")
	time.sleep(0.2)
	print (" [7]- Escaneo de servicios agresivo")
	time.sleep(0.2)
	print (" [8]- Escaneo de servicios de banner ligero")
	time.sleep(0.2)
	print (" [9]- Escaneo de toda la red")
	time.sleep(0.2)
	print (" [10]- Escaneo de red completa sigiloso con detección de SO ")
	time.sleep(0.2)
	print (" \033[31m[11]- Carpeta SCRIPT!")
	time.sleep(0.2)
	print (" \033[93m[12]- Evitar el descubrimiento de hosts ")


	time.sleep(0.5)
	entrada = raw_input("\n\033[32m DarkGhost-$ \033[97m")

	if entrada == '1':
		obtener_info_equipo_remoto()
		ent = raw_input ("\033[31m Menu Principal [S/s]: ")
		if ent == 'si' or ent == 's':
			os.system("clear")
			banner()
		elif ent == 'S' or ent == 'SI':
			os.system("clear")
			banner()
	elif entrada == '2':
		host = raw_input("\033[93m Introduce la direccion a escanear: \033[97m")
		rango = raw_input("\033[93m Introduce el rango(24): \033[97m")
		os.system(" nmap -F %s/%s"%(host,rango))
		print ("\n\033[31m [!] Tu escaneo se ha completado correctamente\033[97m\n")
		banner()

	elif entrada == '3':
		host = raw_input("\033[93m Introduce la direccion a escanear: \033[97m")
		rango = raw_input("\033[93m Introduce el rango(24): \033[97m")
		os.system(" nmap -V %s/%s"%(host,rango))
		print ("\n\033[31m [!] Tu escaneo se ha completado correctamente\033[97m\n")
		banner()

	elif entrada == '4':
		host = raw_input("\033[93m Introduce la direccion a escanear: \033[97m")
		
		os.system(" nmap -p- %s"%(host))
		print ("\n\033[31m [!] Tu escaneo se ha completado correctamente\033[97m\n")
		banner()		
	elif entrada == '5':
		host = raw_input("\033[93m Introduce la direccion a escanear: \033[97m")
		
		os.system(" nmap -sS %s"%(host))
		print ("\n\033[31m [!] Tu escaneo se ha completado correctamente\033[97m\n")
		banner()
	elif entrada == '6':
		host = raw_input("\033[93m Introduce la direccion a escanear: \033[97m")
		
		os.system(" nmap -A %s"%(host))
		print ("\n\033[31m [!] Tu escaneo se ha completado correctamente\033[97m\n")
		banner()
	elif entrada == '7':
		host = raw_input("\033[93m Introduce la direccion a escanear: \033[97m")
		
		os.system(" nmap -sV --version-intensity 5 %s"%(host))
		print ("\n\033[31m [!] Tu escaneo se ha completado correctamente\033[97m\n")
		banner()
	elif entrada == '8':
		host = raw_input("\033[93m Introduce la direccion a escanear: \033[97m")
		
		os.system(" nmap -sV --version-intensity 0 %s"%(host))
		print ("\n\033[31m [!] Tu escaneo se ha completado correctamente\033[97m\n")
		banner()
	elif entrada == '9':
		host = raw_input("\033[93m Introduce la direccion a escanear: \033[97m")
		rango = raw_input("\033[93m Introduce el rango(24): \033[97m")
		os.system(" nmap -sP %s/%s"%(host,rango))
		print ("\n\033[31m [!] Tu escaneo se ha completado correctamente\033[97m\n")
		banner()
	elif entrada == '10':
		host = raw_input("\033[93m Introduce la direccion a escanear: \033[97m")
		rango = raw_input("\033[93m Introduce el rango(24): \033[97m")
		os.system(" nmap -sS -O %s/%s"%(host,rango))
		print ("\n\033[31m [!] Tu escaneo se ha completado correctamente\033[97m\n")
		banner()
	elif entrada == '11':
		print ("[1]- Script disponibles")
		print ("[2]- Actualizar la base de datos de scripts ")


		ent = raw_input ("\n\033[32m DarkGhost-$ \033[97m")
		if ent == '1':
			os.system("locate nse | grep script")
			banner()
		elif ent == '2':
			os.system ("nmap --script-updatedb")
			banner()
	elif entrada == '12':
		ent = raw_input ("Ingrese url desconocida")

		os.system("nmap -PN -p 80 %s"%(ent))
		banner()

	else:
		print ("\n\033[31m [!] Has ingresado una entrada incorrecta")
		
		print (" \n\033[31m[!] Menu principal\n")
		time.sleep(0.5)
		os.system("clear")
		banner()
def formato_direccion_ip():
	web =  raw_input("Ingresa el url: ")	

	equipo_remoto_a = socket.gethostbyname(web)

	for dir_ip in [equipo_remoto_a]:

		print ("Direccion Ip: %s ")%(dir_ip)

def obtener_info_equipo_remoto():
		 url = raw_input ("\n\033[93m Ingrese la url: \033[97m")
		 equipo_remoto = (url)
		 try:
					 print ("\n\033[93m El equipo remoto es: \033[97m%s ") %equipo_remoto
					 print ("\033[93m La direccion IP es: \033[97m%s ") %socket.gethostbyname(equipo_remoto)
		 except socket.error, err_msg:
					 print ("%s: %s" )%(equipo_remoto, err_msg)


nombre_equipo = socket.gethostname()



os.system("clear")
print ("""""""\033[93m                           Recolectar informacion""")
time.sleep(1)
print ("\n\033[31m Hola \033[97m%s\033[31m recolectamos tu siguiente informacion")%nombre_equipo
time.sleep(0.5)
print (" Tranquilo esto es seguro, ya que es de codigo abierto.")

time.sleep(0.5)
banner()
