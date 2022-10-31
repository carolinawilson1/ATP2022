
import csv

import matplotlib.pyplot as plt

def readDataset(fnome):
    f = open(fnome, encoding='utf-8')
    f.readline()
    csv_reader = csv.reader(f, delimiter=';')
    obras = []
    for row in csv_reader:
        obras.append(tuple(row))
    return obras 

def tamanhoObras(obras):
    return len(obras)

def imprime(obras):
    print(f"{'Nome' : 20} | {'Descricao' : 25} | {'Ano' : 8} | {'Compositor' : 15} |")
    for nome,desc,ano,_,comp,*_ in obras:
        print(f"{nome[:20] : 20} | {desc[:25] : 25} | {ano : 8} | {comp[:15] : 15} |")


#----------------
#ListaTitAno
#----------------
def ordTit(t):
    return t[0]

def titAno(obras):
    res = []
    for nome, _, ano, *_ in obras:
        res.append((nome,ano))
    res.sort(key=ordTit)
    return res

def titPorAno(obras):
    res = {}
    for nome, _, ano, *_ in obras:
        if ano in res.keys():
            res[ano].append(nome)
        else:
            res[ano] = [nome]
    return res

def nomeano(obras):
    lista = []
    for nome, _, ano, *_ in obras:
        lista.append((nome,ano))
    lista.sort(key = ordTit)
    return (lista)

def compOrd(obras):
    nomes = []
    for _,_,_,_, compositor, *_ in obras:
        if compositor not in nomes:
            nomes.append(compositor)
    nomes.sort()
    print(nomes)

def distPeriodos(obras):
    dicio = {}
    for _, _, _, periodo, *_ in obras:
        if periodo in dicio.keys():
            dicio[periodo] += 1
        else:
            dicio[periodo] = 1
    return dicio

def distAno(obras):
    dicio = {}
    for _, _, ano, *_ in obras:
        if ano in dicio.keys():
            dicio[ano] += 1
        else:
            dicio[ano] = 1 
        
        print("Há {} compositores do ano {}".format (dicio[ano],ano))

def distComp(obras):
    dicio = {}
    for _,_,_,_, compositor, *_ in obras:
        if compositor in dicio.keys():
            dicio[compositor] += 1
        else:
            dicio[compositor] = 1
        
        print("Há {} obras feitas por {}".format (dicio[compositor],compositor))  

def grafico(obras):
    n = int(input("Indique o gráfico que pretende: \n (1) Periodo \n (2) Ano \n (3) compositor"))

    dicio = {}
    if n == 1:
        for _,_,_, periodo, *_ in obras:
            if periodo in dicio.keys():
                dicio[periodo] += 1
            else:
                dicio[periodo] = 1
    
    if n == 2:
        for _,_, ano, *_ in obras:
            if ano in dicio.keys():
                dicio[ano] += 1
            else:
                dicio[ano] = 1
    
    if n == 3:
         for _,_, ano, *_ in obras:
            if ano in dicio.keys():
                dicio[ano] += 1
            else:
                dicio[ano] = 1
    
    plt.bar(dicio.keys(), dicio.values())
    plt.show()

def desenhargrafico (dicio):
    x = []
    y = []
    for key in dicio:
        x.append(key)
        y.append(dicio[key])
    return plt(x,y)

def obracomp(obras):
    dicio = {}
    for nome,_,_,_, compositor, *_ in obras:
        if compositor not in dicio:
            lista = [nome]
            dicio[compositor] = lista
        else:
            lista.append(nome)
            dicio[compositor] = lista
    
    return dicio

def tabela(obras):
    print (f"{'compositor:':31} | {'nome da obra:':100}")

    dicio = {}
    lista = []

    for nome,_,_,_, compositor, *_ in obras:
        if compositor not in dicio:
            lista = [nome]
            dicio[compositor] = lista
        else:
            lista.append(nome)
            dicio[compositor] = lista
    
    n = 0
    t = len(dicio)
    p = list(dicio.keys())
    d = list(dicio.values())
    while t > 0:
        print (f"{str(p[n]):30} | {str(d[n]):100}")
        n += 1
        t = t - 1

