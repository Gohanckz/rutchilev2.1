#!/usr/bin/python
#_*_ coding: utf8 _*_

#--------------------------------------------------------------------
# ----            GENERADOR DICCIONARIOS CON RUTs CHILENOS      ----|
# ----            Gohanckz                                      ----|
# ----            Contact : gohanckz@gmail.cl                   ----|
# ----            Version : 2.1                                 ----|
#--------------------------------------------------------------------


try:
    import argparse
    from prettytable import PrettyTable
except ImportError as error:
    print("Falta instalar algunas librerías")
    print(error)

x = PrettyTable()
x.field_names = ["Argumento","Descripción","Ejemplo"]
x.add_row(["-f","Generar diccionario de RUTs con puntos, guión y dígito verificador Ej: 12.345.678-9","python rutchile.py -f"])
x.add_row(["-d","Generar diccionario de RUTs solo con dígito verificador Ej: 12345678-9","python rutchile.py -d"])
x.add_row(["-l","Generar diccionario de RUTs sin puntos ni guión con dígito verificador Ej: 123456789","python rutchile.py -l"])
x.add_row(["-m","Generar diccionario de RUTs sin dígito verificador Ej: 12345678","python rutchile.py -m"])


parser = argparse.ArgumentParser(description="RUT CHILE V2.1 by @Gohanckz")
parser.add_argument('-f','--full', action='store_true', help="Generar RUTs con puntos, guión y dígito verificador Ej: 12.345.678-9")
parser.add_argument('-d','--digit', action='store_true', help="Generar RUTs solo con dígito verificador Ej: 12345678-9")
parser.add_argument('-l','--list', action='store_true', help="Generar RUTs sin puntos ni guión con dígito verificador Ej: 123456789")
parser.add_argument('-m','--miss', action='store_true', help="Generar solo RUTs sin dígito verificador Ej: 12345678")
parser.add_argument('-i','--info',action='store_true', help=print(x))
parser = parser.parse_args()


def main():
    if parser.full:
        rut_ini = str(input("[+] Indique el RUT inicial de 8 dígitos ↴ \n"))
        while len(rut_ini) != 8:
            print("[!] El largo del RUT inicial debe ser de 8 dígitos.")
            print("[!] Ejemplo: 12345678")
            rut_ini = input("[+] Indique el RUT inicial de 8 dígitos ↴ \n")

        rut_fin = str(input("[+] Indique el RUT final de 8 dígitos ↴ \n"))
        while len(rut_fin) != 8:
            print("[!] El largo del RUT final debe ser de 8 dígitos.")
            print("[!] Ejemplo: 12345678")
            rut_fin = input("[+] Indique el RUT final de 8 dígitos ↴ \n")

        f = open('diccionario.txt','w')
        for i in range(int(rut_ini),int(rut_fin)+1):
            rut = str(i)
            dig_1 = int(rut[0])*3
            dig_2 = int(rut[1])*2
            dig_3 = int(rut[2])*7
            dig_4 = int(rut[3])*6
            dig_5 = int(rut[4])*5
            dig_6 = int(rut[5])*4
            dig_7 = int(rut[6])*3
            dig_8 = int(rut[7])*2
            suma = dig_1+dig_2+dig_3+dig_4+dig_5+dig_6+dig_7+dig_8
            digito = str((suma%11)-11)
            if digito == "-11":
                digito = "-0"
            elif digito == "-10":
                digito = "-k"
            print(rut[0]+rut[1]+"."+rut[2]+rut[3]+rut[4]+"."+rut[5]+rut[6]+rut[7]+digito)
            f.write(rut[0]+rut[1]+"."+rut[2]+rut[3]+rut[4]+"."+rut[5]+rut[6]+rut[7]+digito+"\n")
        f.close()
            

    elif parser.digit:
        rut_ini = str(input("[+] Indique el RUT inicial de 8 dígitos ↴ \n"))
        while len(rut_ini) != 8:
            print("[!] El largo del RUT inicial debe ser de 8 dígitos.")
            print("[!] Ejemplo: 12345678")
            rut_ini = input("[+] Indique el RUT inicial de 8 dígitos ↴ \n")

        rut_fin = str(input("[+] Indique el RUT final de 8 dígitos ↴ \n"))
        while len(rut_fin) != 8:
            print("[!] El largo del RUT final debe ser de 8 dígitos.")
            print("[!] Ejemplo: 12345678")
            rut_fin = input("[+] Indique el RUT final de 8 dígitos ↴ \n")

        f = open('diccionario.txt','w')
        for i in range(int(rut_ini),int(rut_fin)+1):
            rut = str(i)
            dig_1 = int(rut[0])*3
            dig_2 = int(rut[1])*2
            dig_3 = int(rut[2])*7
            dig_4 = int(rut[3])*6
            dig_5 = int(rut[4])*5
            dig_6 = int(rut[5])*4
            dig_7 = int(rut[6])*3
            dig_8 = int(rut[7])*2
            suma = dig_1+dig_2+dig_3+dig_4+dig_5+dig_6+dig_7+dig_8
            digito = str((suma%11)-11)
            if digito == "-11":
                digito = "-0"
            elif digito == "-10":
                digito = "-k"
            print(rut+digito)
            f.write(rut+digito+"\n")
        f.close()

    elif parser.list:
        rut_ini = str(input("[+] Indique el RUT inicial de 8 dígitos ↴ \n"))
        while len(rut_ini) != 8:
            print("[!] El largo del RUT inicial debe ser de 8 dígitos.")
            print("[!] Ejemplo: 12345678")
            rut_ini = input("[+] Indique el RUT inicial de 8 dígitos ↴ \n")

        rut_fin = str(input("[+] Indique el RUT final de 8 dígitos ↴ \n"))
        while len(rut_fin) != 8:
            print("[!] El largo del RUT final debe ser de 8 dígitos.")
            print("[!] Ejemplo: 12345678")
            rut_fin = input("[+] Indique el RUT final de 8 dígitos ↴ \n")

        f = open('diccionario.txt','w')
        for i in range(int(rut_ini),int(rut_fin)+1):
            rut = str(i)
            dig_1 = int(rut[0])*3
            dig_2 = int(rut[1])*2
            dig_3 = int(rut[2])*7
            dig_4 = int(rut[3])*6
            dig_5 = int(rut[4])*5
            dig_6 = int(rut[5])*4
            dig_7 = int(rut[6])*3
            dig_8 = int(rut[7])*2
            suma = dig_1+dig_2+dig_3+dig_4+dig_5+dig_6+dig_7+dig_8
            digito = str(abs((suma%11)-11))
            if digito == "-11":
                digito = "0"
            elif digito == "-10":
                digito = "k"
            print(rut+digito)
            f.write(rut+digito+"\n")
        f.close()

    elif parser.miss:
        rut_ini = str(input("[+] Indique el RUT inicial de 8 dígitos ↴ \n"))
        while len(rut_ini) != 8:
            print("[!] El largo del RUT inicial debe ser de 8 dígitos.")
            print("[!] Ejemplo: 12345678")
            rut_ini = input("[+] Indique el RUT inicial de 8 dígitos ↴ \n")

        rut_fin = str(input("[+] Indique el RUT final de 8 dígitos ↴ \n"))
        while len(rut_fin) != 8:
            print("[!] El largo del RUT final debe ser de 8 dígitos.")
            print("[!] Ejemplo: 12345678")
            rut_fin = input("[+] Indique el RUT final de 8 dígitos ↴ \n")

        f = open('diccionario.txt','w')
        for i in range(int(rut_ini),int(rut_fin)+1):
            rut = str(i)
            dig_1 = int(rut[0])*3
            dig_2 = int(rut[1])*2
            dig_3 = int(rut[2])*7
            dig_4 = int(rut[3])*6
            dig_5 = int(rut[4])*5
            dig_6 = int(rut[5])*4
            dig_7 = int(rut[6])*3
            dig_8 = int(rut[7])*2
            print(rut)
            f.write(rut+"\n")
        f.close()

if __name__ == '__main__':
    main()
    