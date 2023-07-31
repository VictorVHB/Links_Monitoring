import subprocess, os, socket

Minas_Center = "172.25.0.101"

Command_Minas_Center='sshpass -pHelp2018@ ssh helpdesk@{} -p 9922 <<EOF \n\
        system-view \n\
        bgp 262316 \n\
        display this | inc 177.124.48 \n\
        display this | inc 177.124.50 \n\
        display this | inc 177.124.51 \n\
        display this | inc 167.250.154 \n\
        display this | inc 167.250.155 \n\
        display this | inc 177.74.66 \n\
        display this | inc 177.74.67 \n\
        display this | inc 177.74.69 \n\
        display this | inc 2804:7C0:1000:: \n\
        q \n\
        q \n\
        q \n\
        EOF'.format(Minas_Center)

Envia_Comando = subprocess.run(Command_Minas_Center, shell=True, capture_output=True)

Retorno = Envia_Comando.stdout
Retorno_Trabalhado = Retorno.decode('utf-8')
Retorno_Dividido = Retorno_Trabalhado.split("\r\n")

print("Minas Center\n\n")

for linha in Retorno_Dividido:
    if linha.find("network 177.124.48.0 255.255.255.0") > 0:
            print(linha)
    elif linha.find("network 177.124.50.0 255.255.255.0") > 0:
            print(linha)    
    elif linha.find("network 177.124.51.0 255.255.255.0") > 0:
            print(linha)
    elif linha.find("network 167.250.154.0 255.255.255.0") > 0:
            print(linha)        
    elif linha.find("network 167.250.155.0 255.255.255.0") > 0:
            print(linha)            
    elif linha.find("network 177.74.66.0 255.255.255.0") > 0:
            print(linha) 
    elif linha.find("network 177.74.67.0 255.255.255.0") > 0:
            print(linha) 
    elif linha.find("network 177.74.69.0 255.255.255.0") > 0:
            print(linha) 
    elif linha.find("network 2804:7C0:1000:: 36") > 0:
            print(linha) 
            
#São Ludgero

Sao_Ludgero = "172.18.0.142"

Command_Sao_Ludgero='sshpass -pHelp2018@ ssh helpdesk@{} -p 9922 <<EOF \n\
        system-view \n\
        bgp 262316 \n\
        display this | inc 177.74.75.0 \n\
        display this | inc 131.221.200.0 \n\
        display this | inc 131.221.203.0 \n\
        display this | inc 2804:7C0:2000:: 36 \n\
        q \n\
        q \n\
        q \n\
        EOF'.format(Sao_Ludgero)

Envia_Comando_Sao_Ludgero = subprocess.run(Command_Sao_Ludgero, shell=True, capture_output=True)

Retorno_Sao_Ludgero = Envia_Comando_Sao_Ludgero.stdout
Retorno__Sao_Ludgero_Trabalhado = Retorno_Sao_Ludgero.decode('utf-8')
Retorno_Sao_Ludgero_Dividido = Retorno__Sao_Ludgero_Trabalhado.split("\r\n")

print("São Ludgero\n\n")

for linha in Retorno_Sao_Ludgero_Dividido:
    if linha.find("network 177.74.75.0 255.255.255.0") > 0:
            print(linha)
    elif linha.find("network 131.221.200.0 255.255.255.0") > 0:
            print(linha)    
    elif linha.find("network 131.221.203.0 255.255.255.0") > 0:
            print(linha)
    elif linha.find("network 2804:7C0:2000:: 36") > 0:
            print(linha)

#Urussanga

Urussanga = "172.20.4.143"

Command_Urussanga='sshpass -pHelp2018@ ssh helpdesk@{} -p 9922 <<EOF \n\
        system-view \n\
        bgp 262316 \n\
        display this | inc 177.74.78.0 \n\
        display this | inc 177.74.76.0 \n\
        display this | inc 138.117.195.0 \n\
        display this | inc 177.74.77.0 \n\
        display this | inc 2804:7C0:3000:: 36 \n\
        q \n\
        q \n\
        q \n\
        EOF'.format(Urussanga)

Envia_Comando_Urussanga = subprocess.run(Command_Urussanga, shell=True, capture_output=True)

Retorno_Urussanga = Envia_Comando_Urussanga.stdout
Retorno__Urussanga_Trabalhado = Retorno_Urussanga.decode('utf-8')
Retorno_Urussanga_Dividido = Retorno__Urussanga_Trabalhado.split("\r\n")

print("Urussanga\n\n")

for linha in Retorno_Urussanga_Dividido:
    if linha.find("network 177.74.78.0 255.255.255.0") > 0:
            print(linha)
    elif linha.find("network 177.74.76.0 255.255.255.0") > 0:
            print(linha)
    elif linha.find("network 138.117.195.0 255.255.255.0") > 0:
            print(linha)
    elif linha.find("network 177.74.77.0 255.255.255.0") > 0:
            print(linha)
    elif linha.find("network 2804:7C0:3000:: 36") > 0:
            print(linha)
            
#Santo Antonio de Padua

Santo_Antonio_De_Padua = "172.28.0.109"

Command_Santo_Antonio_De_Padua='sshpass -pHelp2018@ ssh helpdesk@{} -p 9922 <<EOF \n\
        system-view \n\
        bgp 262316 \n\
        display this | inc 177.74.68.0 \n\
        display this | inc 138.117.194.0 \n\
        display this | inc 131.221.202.0 \n\
        display this | inc 2804:7C0:9000:: 36 \n\
        q \n\
        q \n\
        q \n\
        EOF'.format(Santo_Antonio_De_Padua)

Envia_Comando_Santo_Antonio_De_Padua = subprocess.run(Command_Santo_Antonio_De_Padua, shell=True, capture_output=True)

Retorno_Santo_Antonio_De_Padua = Envia_Comando_Santo_Antonio_De_Padua.stdout
Retorno__Santo_Antonio_De_Padua_Trabalhado = Retorno_Santo_Antonio_De_Padua.decode('utf-8')
Retorno_Santo_Antonio_De_Padua_Dividido = Retorno__Santo_Antonio_De_Padua_Trabalhado.split("\r\n")

print("Santo_Antonio_De_Padua\n\n")

for linha in Retorno_Santo_Antonio_De_Padua_Dividido:
    if linha.find("network 177.74.68.0 255.255.255.0") > 0:
            print(linha)
    elif linha.find("network 138.117.194.0 255.255.255.0") > 0:
            print(linha)
    elif linha.find("network 131.221.202.0 255.255.255.0") > 0:
            print(linha)
    elif linha.find("network 2804:7C0:9000:: 36") > 0:
            print(linha)
            
#Orleans

Orleans = "172.23.5.134"

Command_Orleans='sshpass -pHelp2018@ ssh helpdesk@{} -p 9922 <<EOF \n\
        system-view \n\
        bgp 262316 \n\
        display this | inc 177.74.65.0 \n\
        display this | inc 177.74.79.0 \n\
        display this | inc 2804:7C0:4000:: 36 \n\
        q \n\
        q \n\
        q \n\
        EOF'.format(Orleans)

Envia_Comando_Orleans = subprocess.run(Command_Orleans, shell=True, capture_output=True)

Retorno_Orleans = Envia_Comando_Orleans.stdout
Retorno__Orleans_Trabalhado = Retorno_Orleans.decode('utf-8')
Retorno_Orleans_Dividido = Retorno__Orleans_Trabalhado.split("\r\n")

print("Orleans\n\n")

for linha in Retorno_Orleans_Dividido:
    if linha.find("network 177.74.65.0 255.255.255.0") > 0:
            print(linha)
    elif linha.find("network 177.74.79.0 255.255.255.0") > 0:
            print(linha)
    elif linha.find("network 2804:7C0:4000:: 36") > 0:
            print(linha)

#Boa_Vista

Boa_Vista = "172.29.0.100"

Command_Boa_Vista='sshpass -pHelp2018@ ssh helpdesk@{} -p 9922 <<EOF \n\
        system-view \n\
        bgp 262316 \n\
        display this | inc 177.74.70.0 \n\
        display this | inc 177.74.72.0 \n\
        display this | inc 2804:7C0:B000:: 36 \n\
        q \n\
        q \n\
        q \n\
        EOF'.format(Boa_Vista)

Envia_Comando_Boa_Vista = subprocess.run(Command_Boa_Vista, shell=True, capture_output=True)

Retorno_Boa_Vista = Envia_Comando_Boa_Vista.stdout
Retorno__Boa_Vista_Trabalhado = Retorno_Boa_Vista.decode('utf-8')
Retorno_Boa_Vista_Dividido = Retorno__Boa_Vista_Trabalhado.split("\r\n")

print("Boa_Vista\n\n")

for linha in Retorno_Boa_Vista_Dividido:
    if linha.find("network 177.74.70.0 255.255.255.0") > 0:
            print(linha)
    elif linha.find("network 177.74.72.0 255.255.255.0") > 0:
            print(linha)
    elif linha.find("network 2804:7C0:B000:: 36") > 0:
            print(linha)
            
#Jardim_Amelia

Jardim_Amelia = "172.29.4.100"

Command_Jardim_Amelia='sshpass -pHelp2018@ ssh helpdesk@{} -p 9922 <<EOF \n\
        system-view \n\
        bgp 262316 \n\
        display this | inc 177.74.71.0 \n\
        display this | inc 167.250.152.0 \n\
        display this | inc 2804:7C0:C000:: 36 \n\
        q \n\
        q \n\
        q \n\
        EOF'.format(Jardim_Amelia)

Envia_Comando_Jardim_Amelia = subprocess.run(Command_Jardim_Amelia, shell=True, capture_output=True)

Retorno_Jardim_Amelia = Envia_Comando_Jardim_Amelia.stdout
Retorno__Jardim_Amelia_Trabalhado = Retorno_Jardim_Amelia.decode('utf-8')
Retorno_Jardim_Amelia_Dividido = Retorno__Jardim_Amelia_Trabalhado.split("\r\n")

print("Jardim_Amelia\n\n")

for linha in Retorno_Jardim_Amelia_Dividido:
    if linha.find("network 177.74.71.0 255.255.255.0") > 0:
            print(linha)
    elif linha.find("network 167.250.152.0 255.255.255.0") > 0:
            print(linha)
    elif linha.find("network 2804:7C0:C000:: 36") > 0:
            print(linha)