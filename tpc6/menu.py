import obras
myObras = obras.readDataset("obras.csv")
def menu():
    opcao = int(input("Introduza o numero da opcao "))
    if opcao == 1:
        print(obras.tamanhoObras(myObras))
    elif opcao == 2:
        obras.tabela(myObras)
    elif opcao == 3:
        print(obras.titPorAno(myObras))
    elif opcao == 4:
        print(obras.titAno(myObras))
    elif opcao == 5:
        print(obras.compOrd(myObras))
    elif opcao == 6:
        print(obras.distPeriodos(myObras))
    elif opcao == 7:
        print(obras.distAno(myObras))
    elif opcao == 8:
        print(obras.distComp(myObras))
    elif opcao == 9:
        obras.desenhargrafico(obras.distAno(myObras))
    elif opcao == 10:
        print(obras.obracomp(myObras))
    
        