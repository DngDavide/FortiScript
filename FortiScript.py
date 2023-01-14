from cgi import print_directory

DizionarioSubnet = {
    "0":"0.0.0.0",
    "8":"255.0.0.0",
    "9":"255.128.0.0",
    "10":"255.192.0.0",
    "11":"255.224.0.0",
    "12":"255.240.0.0",
    "13":"255.248.0.0",
    "14":"255.252.0.0",
    "15":"255.254.0.0",
    "16":"255.255.0.0",
    "17":"255.255.128.0",
    "18":"255.255.192.0",
    "19":"255.255.224.0",
    "20":"255.255.240.0",
    "21":"255.255.248.0",
    "22":"255.255.252.0",
    "23":"255.255.254.0",
    "24":"255.255.255.0",
    "25":"255.255.255.128",
    "26":"255.255.255.192",
    "27":"255.255.255.224",
    "28":"255.255.255.240",
    "29":"255.255.255.248",
    "30":"255.255.255.252",
    "31":"255.255.255.254",
    "32":"255.255.255.255",
    }

print("\n")
filename = input(" INSERIRE NOME FILE IN INGRESSO: ")
groupname = input(" INSERIRE NOME GRUPPO: ")
print("\n")



file = open(filename)
conta = 0
vec_indirizzi = []
vec_smask = []

for i in file:
    conta += 1   
    until_slash = 0
    for char in i:
        if char != "/":
            until_slash += 1
        else :
            break
        
    vec_indirizzi.append(i[:until_slash].strip("\n"))
    vec_smask.append(i[until_slash+1:].strip("\n"))
    
print(vec_smask)

file.close()
# dato il file.xxx   in ingresso,  conta il numero di righe all'interno
# e carica il vettore vec_indirizzi con le righe del file 
        
vec_ipv4 = []
for i in range(0, len(vec_indirizzi)):
    vec_ipv4.append('"ipv4-'+str(vec_indirizzi[i])+'"')

print(vec_ipv4)
# il vettore vec_ipv4 è caricato con gli indirizzi ip di vec_indirizzi
# con il prefisso 'ipv4-'

        
with open("risultato.txt","w") as file:
    file.write("config firewall address")
    
    for i in range(0,conta):
        file.write("\nedit ipv4-")
        file.write(vec_indirizzi[i])
        file.write("\nset subnet ")
        file.write(vec_indirizzi[i])
        file.write(" ")
        file.write(DizionarioSubnet[str(vec_smask[i])])
        file.write("\nnext")

    file.write("\nend")
    
    for i in range(0,2):
        file.write("\n")
    file.write("-----------------------------------------------")    
    for i in range(0,2):
        file.write("\n")
        
    
    file.write("config firewall addrgrp")
    file.write("\nedit ")
    file.write(groupname)
    file.write("\nset member ")
    for i in vec_ipv4:
        file.write(i)
        file.write(" ")
    file.write("\nend")
    