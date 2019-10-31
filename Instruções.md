# TrabComp
2º Trabalho de Computação I 2019.2 - Programa de gerenciamento de associados a uma clínica médica

##### Cabeçario #######



############# Funções menuA ##################

def menuA():

	print(‘MENU INICIAL’’\n’)
	print(‘_______________________________’’\n’)
	print(‘Escolha a opção desejada: ‘’\n’)
	print(‘1 – Ver lista de Cadastros’)
	print(‘2 – Incluir novo Cadastro’)
	print(‘3 – Editar Cadastro (senha)’)
	print(‘4 – Verificar Situação de Associado’)
	print(‘5 – Controle Financeiro (senha)’’\n’)
	print(‘0 – Sair’’\n’)
	print(‘_______________________________’’\n’)





############ Funções menuB (funções dos filtros)###################

def menuB():

	print(‘Escolha a opção desejada:’’\n’)
	print(‘1 – Filtrar por Nº’)
	print(‘2 – Filtrar por Nome’)
	print(‘3 – Filtrar por Data de Cadastro’)
	print(‘4 – Filtrar por Vencimento’)
	print(‘5 – Filtrar por Tipo’)
	print(‘6 – Filtrar por Nº de Matrícula’)
	print(‘7 – Filtrar por Situação’)
	print(‘8 – Ordenar alfabeticamente’’\n’)
	print(‘0 – Menu Inicial’)















############# PROGRAMA PRINCIPAL ###################



def main():

	opcaoA = -1
	
	while ( opcaoA != 0):
		
		menuA()
		opcaoA = int(input())

		if (opcaoA == 1):
			print(‘Lista de Cadastros:’’\n’)
			opcaoB = -1 
			while ( opcaoB != 0):
				
				menuB()
				opcaoB = int(input())

				if (opcaoB == 1):

					print(‘Filtro por Nº:’’\n’)

				elif (opcaoB == 2):

					print(‘Filtro por Nome:’’\n’)

				elif (opcaoB == 3):

					print(‘Filtro por Data de Cadastro:’’\n’)

				elif (opcaoB == 4):

					print(‘Filtro por Vencimento:’’\n’)

				elif (opcaoB == 5):

					print(‘Filtro por Tipo:’’\n’)

				elif (opcaoB == 6):

					print(‘Filtro por Nº de Matrícula:’’\n’)

				elif (opcaoB == 7):

					print(‘Filtro por Situação:’’\n’)

				elif (opcaoB == 8): 

					print(‘Lista de Cadastros:’’\n’)
 		
    elif (opcaoA == 2):

			print(‘NOVO CADASTRO:’’\n’)

		elif (opcaoA == 3):

			print(‘EDITAR CADASTRO:’’\n’)

		elif (opcaoA == 4):

			print(‘VERIFICAR SITUAÇÃO DE ASSOCIADO:’’\n’)

		elif (opcaoA == 5):

			print(‘Controle Financeiro:’’\n’)

			opcaoB = -1 
			while ( opcaoB != 0):
				
				menuB()
				opcaoB = int(input())

				if (opcaoB == 1):
					print(‘Controle Financeiro:’’\n’)
					print(‘Filtro por Nº:’’\n’)

				elif (opcaoB == 2):
					print(‘Controle Financeiro:’’\n’)
					print(‘Filtro por Nome:’’\n’)

				elif (opcaoB == 3):
					print(‘Controle Financeiro:’’\n’)
					print(‘Filtro por Data de Cadastro:’’\n’)

				elif (opcaoB == 4):
					print(‘Controle Financeiro:’’\n’)
					print(‘Filtro por Vencimento:’’\n’)

				elif (opcaoB == 5):
					print(‘Controle Financeiro:’’\n’)
					print(‘Filtro por Tipo:’’\n’)

				elif (opcaoB == 6):
					print(‘Controle Financeiro:’’\n’)
					print(‘Filtro por Nº de Matrícula:’’\n’)

				elif (opcaoB == 7):
					print(‘Controle Financeiro:’’\n’)
					print(‘Filtro por Situação:’’\n’)

				elif (opcaoB == 8): 
					print(‘Controle Financeiro:’’\n’)
					print(‘Lista de Cadastros:’’\n’)
          
         
main()




