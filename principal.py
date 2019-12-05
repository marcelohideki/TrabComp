############# Funcoes auxiliares do programa ############

def abrirArquivo():

    arquivo = open('cadastros.txt','a')
    arquivo.close()

    return arquivo

def cadastros(numero, nome, data, vencimento, tipo, matricula, situacao):

    cadastro = {"Numero":numero, "Nome":nome, "Data":data, "Vencimento":vencimento, "Tipo":tipo, "Matricula":matricula, "Situacao":situacao}

    return cadastro

def separar(data):
    separa = data.split('/')
    return separa

#def numero():

#def matricula():

#def situacao():

def splitNum(numero):

    with open('cadastros.txt') as file:

        for cliente in file:
            separa = cliente.split(';')
            numero = separa[0]    

def splitNome():
    arquivo = open('cadastro.txt', 'r')
    linha = arquivo.readlines
    for cliente in linha:
        separa = cliente.split(';')
        nome = separa[1]

def splitData():
    arquivo = open('cadastro.txt', 'r')
    linha = arquivo.readlines
    for cliente in linha:
        separa = cliente.split(';')
        data = separa[2]

def splitVenc():
    arquivo = open('cadastro.txt', 'r')
    linha = arquivo.readlines
    for cliente in linha:
        separa = cliente.split(';')
        vencimento = separa[3]

def splitTipo():
    arquivo = open('cadastro.txt', 'r')
    linha = arquivo.readlines
    for cliente in linha:
        separa = cliente.split(';')
        tipo = separa[4]

def splitMat():
    arquivo = open('cadastro.txt', 'r')
    linha = arquivo.readlines
    for cliente in linha:
        separa = cliente.split(';')
        matricula = separa[5]

def splitSit():

    arquivo = open('cadastro.txt', 'r')
    linha = arquivo.readlines
    for cliente in linha:
        separa = cliente.split(';')
        situacao = separa[6]

############# Funcao menuA ##################

def menuA():

    print('\n''MENU INICIAL''\n')
    print('_______________________________''\n')
    print('Escolha a opção desejada: ''\n')
    print('1 – Ver lista de Cadastros')
    print('2 – Incluir novo Cadastro')
    print('3 – Editar Cadastro')
    print('4 – Verificar Situação de Associado')
    print('5 – Controle Financeiro''\n')
    print('0 – Sair''\n')
    print('_______________________________''\n')

############ Funcao menuB (funcoes dos filtros) ###################

def menuB():

    print('Escolha a opção desejada:''\n')
    print('1 – Filtrar por Numero')
    print('2 – Filtrar por Nome')
    print('3 – Filtrar por Data de Cadastro')
    print('4 – Filtrar por Vencimento')
    print('5 – Filtrar por Tipo')
    print('6 – Filtrar por Nº de Matrícula')
    print('7 – Filtrar por Situação')
    print('8 – Ordenar alfabeticamente''\n')
    print('0 – Menu Inicial')

############# PROGRAMA PRINCIPAL ###################

def main():
#Abre o menu A
    opcaoA = -1

    while (opcaoA != 0):
	
        menuA()
        opcaoA = int(input())

        if (opcaoA == 1):
            
            print('\n''Lista de Cadastros''\n')
            opcaoB = -1 
            
            while (opcaoB != 0):
			
                menuB()
                opcaoB = int(input())
                
                if (opcaoB == 1):
                    print('Filtro por Numero:''\n')
                    num = int(input('Entre com o numero do cliente: '))
                    if num == splitNum(num):
                        print (splitNum(num))

                elif (opcaoB == 2):

                    print('Filtro por Nome:''\n')

                elif (opcaoB == 3):

                    print('Filtro por Data de Cadastro:''\n')

                elif (opcaoB == 4):

                    print('Filtro por Vencimento:''\n')

                elif (opcaoB == 5):

                    print('Filtro por Tipo:''\n')
                    
                elif (opcaoB == 6):

                    print('Filtro por Nº de Matrícula:''\n')

                elif (opcaoB == 7):

                    print('Filtro por Situação:''\n')

                elif (opcaoB == 8): 

                    print('Lista de Cadastros:''\n')
	
        elif (opcaoA == 2):

            print('\n''NOVO CADASTRO:''\n')
            
            num = input('Numero do cliente: ')            
            nome = input('Nome do cliente: ')
            
            dataCad = input('Data do cadastro: ')
            
            dataHoje = input('data de Hoje: ')
            corteHoje = separar(dataHoje)
            diaHoje = int(corteHoje[0])
            mesHoje = int(corteHoje[1])
            anoHoje = int(corteHoje[2])
            
                                   
            escVenc = False
            while escVenc != True:
                venc = input('Dia do vencimento da conta: [5, 15 ou 25] ')
                if venc == '05' or venc == '5':
                    venc = '5'
                    escVenc = True
                elif venc == '15':
                    venc = '15'
                    escVenc = True
                elif venc == '25':
                    venc = '25'
                    escVenc = True
                else: 
                    escVenc = False
                    print('Opcao invalida''\n')        
            intVenc = int(venc)

            escTipo = False
            while escTipo != True:
                tipo = input('Titular ou Dependente: [t ou d]')
                if tipo == 't' or tipo == 'T':
                    tipo = 'Titular'
                    escTipo = True
                elif tipo == 'd' or tipo == 'D':
                    tipo = 'Dependente'
                    escTipo = True
                else:
                    escTipo = False
                    print('Opcao invalida''\n')

            mat = input('Entre com a matricula: ')
            
            if diaHoje > intVenc:
                sit = 'Inadimplente'
            else:
                sit = 'Ok'

            cliente = cadastros(num, nome, dataCad, venc, tipo, mat, sit)
            cadNum = str(cliente['Numero'])
            cadNome = str(cliente['Nome'])
            cadDat = str(cliente['Data'])
            cadVen = str(cliente['Vencimento'])
            cadTip = str(cliente['Tipo'])
            cadMat = str(cliente['Matricula'])
            cadSit = str(cliente['Situacao'])

            arquivo = open('cadastros.txt', 'a')
            arquivo.write(cadNum)
            arquivo.write(';')
            arquivo.write(cadNome)
            arquivo.write(';')
            arquivo.write(cadDat)
            arquivo.write(';')
            arquivo.write(cadVen)
            arquivo.write(';')
            arquivo.write(cadTip)
            arquivo.write(';')
            arquivo.write(cadMat)
            arquivo.write(';')
            arquivo.write(cadSit)
            arquivo.write('\n')
            arquivo.close

        elif (opcaoA == 3):

            print('\n''EDITAR CADASTRO:''\n')

        elif (opcaoA == 4):

            print('\n''VERIFICAR SITUAÇÃO DE ASSOCIADO:''\n')

        elif (opcaoA == 5):

            print('\n''Controle Financeiro''\n')
            opcaoB = -1 
            
            while (opcaoB != 0):
                
                menuB()
                opcaoB = int(input())

                if (opcaoB == 1):
                    print('Controle Financeiro''\n')
                    print('Filtro por Nº:''\n')
                
                elif (opcaoB == 2):
                    print('Controle Financeiro''\n')
                    print('Filtro por Nome:''\n')
                
                elif (opcaoB == 3):
                    print('Controle Financeiro''\n')
                    print('Filtro por Data de Cadastro:''\n')
                
                elif (opcaoB == 4):
                    print('Controle Financeiro''\n')
                    print('Filtro por Vencimento:''\n')
                
                elif (opcaoB == 5):
                    print('Controle Financeiro''\n')
                    print('Filtro por Tipo:''\n')
                
                elif (opcaoB == 6):
                    print('Controle Financeiro''\n')
                    print('Filtro por Nº de Matrícula:''\n')
                
                elif (opcaoB == 7):
                    print('Controle Financeiro''\n')
                    print('Filtro por Situação:''\n')
                
                elif (opcaoB == 8): 
                    print('Controle Financeiro''\n')
                    print('Lista de Cadastros:''\n')

main()
