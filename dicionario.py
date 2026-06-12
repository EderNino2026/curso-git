//cambio en la rama
fh = open('mbox-short.txt')
counts = dict()
bigcount = None
bigemail = None
for lista in fh :
    # lista = lista.strip()
    datos = lista.split()
    # print (datos)
    if len(datos)< 3 or datos[0] !='From':
        continue
    email = datos[1]
    counts[email] = counts.get(email,0) + 1
for email,count in counts.items():
    if bigcount is None or count > bigcount:
        bigemail = email
        bigcount = count
print(bigemail,bigcount)
