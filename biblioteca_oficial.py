########################################################################################################################
import csv
import time


###FUNÇÃO CRIA UM LINHA, QUE PODE SER USADA PARA ORGANIZAÇÃO
def separador(tamanho=70):
    return '\033[31m~\033[m'*tamanho


###FUNÇÃO CRIA UMA PALAVRA CENTRALIZADA ENTRE DUAS LINHAS,USANDO A FUNÇÃO SEPARADOR
def separador_duplo(palavra):
    print(separador())
    print(palavra.center(70))
    print(separador())


###FUNÇÃO VERIFICA POSSÍVEIS ERROS NA ENTRADA DO USUÁRIO.
def leitor_de_inteiros(numero):
    

    while True:
        try:
            x = int(input(numero))
        except (ValueError,TypeError):

            separador_duplo('\033[31mERRO: A OPÇÃO DIGITADA É INVALIDA....\033[m')
            continue

        except (KeyboardInterrupt):

            separador_duplo('\033[31mERRO: USUARIO FINALIZOU SEM DIGITAR.....\033[m')
            return 0
        else:
            return x

###FUNÇÃO CRIA UM MENU A PARTIR DE UMA LISTA
def menu(lista):

    separador_duplo('MENU DE OPÇÕES:')
    cont = 1
    for opc in lista:
        print(f'\033[33m{cont}\033[m -\033[34m{opc}\033[m')
        cont += 1
    print(separador(70))
    entrada = leitor_de_inteiros('\033[33mDIGITE UMA OPÇÃO: \033[m')

    return entrada


###FUNÇÃO CADASTRA UM USUARIO.
def cadastrar_usuario(nome, cpf, email):
    
    with open('csv/login.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['nome','cpf','email']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'nome': nome, 'cpf': cpf, 'email': email})

    print(separador(70)) 

    print(f'\033[33mUSUARIO\033[m \033[34m {nome} \033[m, \033[33mCOM CPF\033[m \033[34m {cpf} \033[m, \033[33mCADASTRADO SUCESSO!\033[m')

    print(separador(70))

    return True


###FUNÇAO CADASTRA LIVRO
def cadastrar_livro(titulo, autor, ano, quantidade):
    
    with open('csv/livros.csv', 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Titulo', 'Autor', 'Ano', 'QuantidadeTotal', 'QuantidadeDisponivel']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({
            'Titulo': titulo, 
            'Autor': autor, 
            'Ano': ano, 
            'QuantidadeTotal': quantidade, 
            'QuantidadeDisponivel': quantidade})
         
    print(separador(70))

    print(f'\033[33mO LIVRO DE TITULO\033[m \033[34m {titulo}\033[m \033[33m, DO AUTOR\033[m \033[34m {autor} \033[m \033[33m, FOI CADASTRADO COM SUCESSO!\033[m')

    print(separador(70))

    return True 


###VERIFICA SE O LIVRO FOI CADASTRADO
def verifica_livros_repetidos(titulo):
    with open('csv/livros.csv', 'r', newline='', encoding='utf-8') as csvfile:
        csv_file = csv.DictReader(csvfile)
        for row in csv_file:
            if titulo in row['Titulo']:
                print('Livro ja cadastrtado!') 
                return True
            

###VERIFICA SE O CPF É VALIDO, RETIRA OS caracteres DEIXANDO APENAS NÚMEROS.
def trata_cpf():
    while True:
        cpf = input("\033[33mDIGITE SEU CPF: \033[m")

        ###DEIXA APENAS OS NÚMEROS.
        aux_cpf = ''
        for char in cpf:
            if char.isdigit():
                aux_cpf += char

        ###USA A FUNÇÃO LEN PARA VERIFICAR SE EXISTEM 11 DÍGITOS.
        if len(aux_cpf) == 11:
            return aux_cpf
        else:
            separador_duplo("\033[31mCPF INVÁLIDO,POR FAVOR DIGITE NOVAMENTE:\033[m ")


###VERIFICA SE O ANO DE PUBLICAÇÃO ESTA CORRETO.
def trata_ano():
    while True:
        ano = input("\033[33mDIGITE O ANO DE PUBLICAÇÃO:  ")

        ###DEIXA APENAS OS NÚMEROS.
        aux_ano = ''
        for char in ano:
            if char.isdigit():
                aux_ano += char

        ###USA A FUNÇÃO LEN PARA VERIFICAR SE EXISTEM 4 DÍGITOS.
        if len(aux_ano) == 4:
            int_ano = int(ano)
            
            if(int_ano>2023):
                separador_duplo(f'\033[31mERRO:ESSA DATA {aux_ano} É INVALIDA.\033[m')
            else:
                return aux_ano

        else:
            separador_duplo("\033[31mANO INVÁLIDO,POR FAVOR DIGITE NOVAMENTE:\033[m ")


###VERICA SE O E-MAIL É VALIDO ATRAVEZ DO @, NÃO FAZ VALIDAÇÃO REAL.
def verifica_email():

    while True:
        e =input('\033[33mINFORME O E-MAIL:\033[m').upper()

        if '@' in e:
            return e
        else:
            separador_duplo("\033[31mE-MAIL INVÁLIDO,POR FAVOR DIGITE NOVAMENTE:\033[m ")

###CRIA TABELA DE USUARIOS
def cria_tabela_usuarios(matriz):
    ###COLUNAS NOME CPF E-MAIL
    print("| {:<15} | {:<15} | {:<25} |".format("Nome", "CPF", "Email"))
    print(separador(70))

    ###PERCORRE A MATRIZ ACRECENTANDO AS LINAHS USANDO FORMAT
    for l in matriz:
        nome, cpf, email = l
        print("| {:<15} | {:<15} | {:<25} |".format(nome, cpf, email))


###CRIA UMA TABELA DE EMPRESTIMOS
def cria_tabela_emprestimos(matriz):
    ###COLUNAS NOME CPF E-MAIL
    print("| {:<15} | {:<15} | {:<25} |".format("CPF", "NOME", "TITULO"))
    print(separador(70))

    ###PERCORRE A MATRIZ ACRECENTANDO AS LINAHS USANDO FORMAT
    for l in matriz:
        cpf, nome, titulo = l
        print("| {:<15} | {:<15} | {:<25} |".format( cpf,nome,titulo))

        
###CRIA TABELA COM LIVROS CADASTRADOS      
def cria_tabela_livros(MatrizUm,MatrizDois):
    print("| {:<30} | {:<30} |".format("TITULO","AUTOR"))
    print(separador(70))

    for l in range(len(MatrizUm)):
        print("| {:30} | {:<30} |".format(MatrizUm[l], MatrizDois[l]))
        
     
def cria_tabela_livros_excluir(MatrizUm):
    print("| {:<30} |".format("TITULO"))
    print(separador(70))

    for l in MatrizUm:
        print("| {:30} |".format(l))


###FUNÇAO COMPLEMENTAR A cria_tabela_usuarios, REALIZA A LEITURA DOS ARQUIVOS .CSV
def leitor_csv(arquivocsv):
    with open(arquivocsv, 'r', newline='') as arquivo:
        leitor_csv = csv.reader(arquivo)
        dados = list(leitor_csv)
    return dados


###VERIFICA SE USUÁRIO JÁ FOI CADASTRADO,REMOVENDO USUARIOS REPETIDOS.
def verifica_usuarios_repetidos(cpf, email):

    with open('csv/login.csv', 'r', newline='', encoding='utf-8') as csvfile:
        csv_file = csv.DictReader(csvfile)
        for linha in csv_file:
            if cpf == linha['cpf'] or email ==  linha['email']:
                print('Usuario ja cadastratado!') 
                return True
        return False
    

###VERIFCA SE O CAMPO ESTA EM BRANCO
def entrada_em_branco(nome):

    while not nome.strip():
        separador_duplo("\033[31mENTREDA INVALIDA\033[m")
        nome = input("\033[33m[-]DIGITE NOVAMENTE:\033[m ").upper()

    return nome


###VERIFICA ENTRADA EM BRANCO NO LOGIN
def entrada_em_branco_LOGIN(nome,senha):

    while not nome.strip():
        separador_duplo("\033[31mENTREDA INVALIDA\033[m")
        nome = input("\033[33m[-]DIGITE O USUARIO NOVAMENTE:\033[m ")
        senha = input("\033[33m[-]DIGITE SUA SENHA NOVAMENTE:\033[m ")

    return nome,senha


###VERIFICA USUARIO E SENHA ROOT
def login_inicial(user, senha, matriz_root):

    for entrada_user in matriz_root:
        if entrada_user[0] == user and entrada_user[1] == senha:
            return True
    return False


###FUNÇÃO QUE EMPRESTA LIVRO
def emprestar_livro(cpf,nome_usuario_e, titulo_livro_e):
    nome = nome_usuario_e.upper()
    titulo = titulo_livro_e.upper()

    aux_usuarios = []
    aux_cpf = []
    aux_lista = []

    ###ADICIONA OS ELEMENTOS QUE ESTAO NO ARQUIVO CSV EM LISTAS AUXILIARES
    with open('csv/login.csv', encoding='utf-8') as usuarios:
        csv_file_usuarios = csv.DictReader(usuarios)
        for usuario in csv_file_usuarios:
            aux_usuarios.append(usuario['nome'])
            aux_cpf.append(usuario['cpf'])
            aux_lista.append(usuario)

    ###VERIFICA SE O CPF QUE O USER DIGITOU EXISTE NA LISTA QUE FOI GERADA A PARTIR DO CSV 
    if cpf not in aux_cpf:
        print(f"\033[31mCPF \033[m'\033[34m{cpf}\033[m'\033[31m NÃO ENCONTRADO.\033[m")
        return True

    
    aux_livros = []
    aux_livros_quantidade = []
    linhas = [] 

    ###PERCORRE O ARQUIVO CSV ONDE OS LIVROS CADASTRADOS ESTAO ARMAZENADOS E ADICIONA EM UMA LISTA
    with open('csv/livros.csv', newline='', encoding='utf-8') as livros:
        csv_file = csv.DictReader(livros)
        for livro in csv_file:
            aux_livros.append(livro['Titulo'])
            aux_livros_quantidade.append(livro['QuantidadeDisponivel'])
            linhas.append(livro)
            
    ### VERIFICA SE O LIVRO EXISTE NA LISTA QUE VEIO DO ARQUIVO CSV
    if titulo not in aux_livros:
        print(f"\033[31mLIVRO \033[m'\033[34m{titulo}\033[m'\033[31m NÃO ENCONTRADO.\033[m")
        return True

    ###ACESSA A QUANTIDADE DE EXEMPLARES DISPONIVEIS
    indice = aux_livros.index(titulo)
    quantidade_disponivel = int(aux_livros_quantidade[indice])
    if quantidade_disponivel < 1:
        print(f"\033[31mNÃO HÁ MAIS EXEMPLARES DO LIVRO \033[m'\033[34m{titulo}\033[m'\033[31m DISPONÍVEIS.\033[m")
        return True

    ###ADICIONA AS INFORMAÇÕES DO EMPRESTIMO
    with open('csv/emprestimos.csv', 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['cpf','usuario', 'titulo']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({
            'cpf': cpf,
            'usuario': nome,
            'titulo': titulo})

    ###DIMINUI A QUANTIDADE DE LIVROS DISPONIVEIS PARA EMPRESTIMO
    quantidade_disponivel -= 1
    aux_livros_quantidade[indice] = str(quantidade_disponivel)

    with open('csv/livros.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Titulo','Autor','Ano','QuantidadeTotal','QuantidadeDisponivel']
        escritor_csv = csv.DictWriter(csvfile, fieldnames=fieldnames)
        escritor_csv.writeheader()
        for linha in linhas:
            escritor_csv.writerow({'Titulo': linha['Titulo'], 'Autor': linha['Autor'], 'Ano': linha['Ano'], 'QuantidadeTotal': linha['QuantidadeTotal'], 'QuantidadeDisponivel': aux_livros_quantidade[aux_livros.index(linha['Titulo'])]})
    
    print(separador(70))
    print(separador(70))
    print(f'\033[33mO LIVRO DE TITULO\033[m \033[34m {titulo}\033[m \033[33m, FOI EMPRESTADO AO USUARIO \033[m \033[34m {nome} \033[m')


###FUNÇÃO QUE EXCLUI UM LIVRO,VERIFICANDO SE ESTA EMPRESTADO OU NÃO.
aux_Lista_De_Livros_Emprestados = []

def excluir_livro(titulo):
    titulo = titulo.upper()
    
    Acessar_Listas()
    
    livros_emprestados = open('csv/emprestimos.csv')
    csv_file = csv.DictReader(livros_emprestados)
    for livro in csv_file:
        Lista_De_Livros_Emprestados.append(livro)
    
    if titulo in Lista_De_Livros_Emprestados:
            print(separador(70))
            print(f'\033[31mO LIVRO\033[m \033[34m{titulo}\033[m \033[31m,ESTÁ EMPRESTADO, IMPOSSIBILITANDO SUA EXCLUSÃO.\033[m')
            print(separador(70))
            return 
    elif titulo not in Lista_De_Livros_Cadastrados:
        
        separador_duplo('\033[31mLIVRO NÃO CADASTRADO, IMPOSSIBILITANDO A EXCLUSÃO\033[m')
        
    else:
        linhas = []
        with open('csv/livros.csv', 'r', newline='') as csvfile:
            leitor_csv = csv.reader(csvfile)
            for indice, linha in enumerate(leitor_csv): 
                if linha[0] != titulo:
                    linhas.append(linha)
            
        with open('csv/livros.csv', 'w', newline='') as csvfile:
            escritor_csv = csv.writer(csvfile)
            escritor_csv.writerows(linhas)
            
        print(separador(70))
        print(f'\033[31mO LIVRO DE TITULO \033[33m{titulo}\033[m,\033[31m FOI EXCLUÍDO COM SUCESSO.\033[m')
        print(separador(70))

        Zerar_Listas()
        return 

###FUNÇÃO EXCLUIR USUARIO
def excluir_usuario(Usuario_Excluir):
    Acessar_Listas()
    
    if Usuario_Excluir in Lista_De_Livros_Emprestados:
        print(separador(70))
        print(f'\033[31mO USUARIO\033[m \033[34m{Usuario_Excluir},\033[m \033[31mESTÁ DEVENDO UM LIVRO,IMPOSSIBILITANDO SUA EXCLUSÃO.\033[m')
        print(separador(70))

    else:
        usuarios = []
        with open('csv/login.csv', 'r', newline='', encoding='utf-8') as csvfile:
            leitor_csv = csv.reader(csvfile)
            for indice, linha in enumerate(leitor_csv):
                if linha[1] != Usuario_Excluir:
                    usuarios.append(linha)
                    
        with open('csv/login.csv', 'w', newline='', encoding='utf-8') as csvfile:
            escritor_csv = csv.writer(csvfile)
            escritor_csv.writerows(usuarios)

        print(separador(70))
        print(f'\033[31mO USUARIO \033[34m{Usuario_Excluir}\033[m,\033[31m FOI EXCLUÍDO COM SUCESSO.\033[m')
        print(separador(70))
        
        Zerar_Listas()
        return usuarios

###FUNÇÃO REMOVE EMPRESTIMO
def remover_emprestimo(cpf,nome_livro, titulo_livro):
    nome = nome_livro.upper()
    titulo = titulo_livro.upper()

    emprestimos = []

    with open('csv/emprestimos.csv', 'r', newline='', encoding='utf-8') as csvfile:
        leitor_csv = csv.DictReader(csvfile)
        for linha in leitor_csv:
            if cpf not in ['cpf'] and nome not in linha['usuario'] and titulo not in linha['titulo']:
                emprestimos.append(linha)

    with open('csv/emprestimos.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['cpf','usuario', 'titulo']
        escritor_csv = csv.DictWriter(csvfile, fieldnames=fieldnames)
        escritor_csv.writeheader()
        escritor_csv.writerows(emprestimos)

    livros_cadastrados = []

    with open('csv/livros.csv', 'r', newline='', encoding='utf-8') as livros:
        csv_file = csv.DictReader(livros)
        for livro in csv_file:
            livros_cadastrados.append(livro)

    for livro in livros_cadastrados:
        if livro['Titulo'].upper() == titulo:
            quantidade_disponivel = int(livro['QuantidadeDisponivel'])
            quantidade_disponivel += 1
            livro['QuantidadeDisponivel'] = str(quantidade_disponivel)

    with open('csv/livros.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Titulo', 'Autor', 'Ano', 'QuantidadeTotal', 'QuantidadeDisponivel']
        escritor_csv = csv.DictWriter(csvfile, fieldnames=fieldnames)
        escritor_csv.writeheader()
        escritor_csv.writerows(livros_cadastrados)
        
    print(f'\033[33mO LIVRO DE TITULO\033[m \033[34m {titulo}\033[m \033[33m, FOI DEVOLVIDO PELO USUARIO \033[m \033[34m {nome} \033[m')
    


###FUNÇÃO PARA ACESSAR INFORMAÇÕES ARMAZENADAS NO CSV
Lista_De_Usuarios_Cadastrados = []
Lista_De_Livros_Cadastrados = []
Lista_De_Livros_Emprestados = []
Lista_De_Usuarios_Com_Emprestimo = []
aux_Lista_De_Livros_Cadastrados = []
aux_Lista_De_Livros_Emprestados = []

def Acessar_Listas(): #dar um jeito aqui
                
    livros_cadastrados = open('csv/livros.csv')
    csv_file = csv.DictReader(livros_cadastrados)
    for livro in csv_file:
        Lista_De_Livros_Cadastrados.append(livro['Titulo'])
                    
    usuarios_cadastrados = open('csv/login.csv')
    csv_file = csv.DictReader(usuarios_cadastrados)
    for usuario in csv_file:
        Lista_De_Usuarios_Cadastrados.append(usuario['nome'])
        
    livros_emprestados = open('csv/emprestimos.csv')
    csv_file = csv.DictReader(livros_emprestados)
    for livro in csv_file:
        Lista_De_Livros_Emprestados.append(livro['titulo'])
        
    Usuarios_Com_Emprestimos = open('csv/emprestimos.csv')
    csv_file = csv.DictReader(Usuarios_Com_Emprestimos)
    for livro in csv_file:
        Lista_De_Usuarios_Com_Emprestimo.append(livro['usuario'])
    
    return Lista_De_Livros_Cadastrados, Lista_De_Usuarios_Cadastrados, Lista_De_Livros_Emprestados, Usuarios_Com_Emprestimos

### FUNÇÃO PARA ZERAR LISTAS
def Zerar_Listas():
    Lista_De_Usuarios_Cadastrados = []
    Lista_De_Livros_Cadastrados = []
    Lista_De_Livros_Emprestados = []
    Lista_De_Usuarios_Com_Emprestimo = []
    aux_Lista_De_Livros_Emprestados = []
    aux_Lista_De_Livros_Cadastrados = []
    
    return Lista_De_Livros_Cadastrados, Lista_De_Usuarios_Cadastrados, Lista_De_Livros_Emprestados, aux_Lista_De_Livros_Cadastrados, aux_Lista_De_Livros_Emprestados, Lista_De_Usuarios_Com_Emprestimo



########################################################################################################################


########################################################################################################################
#Programação 1.
#Projeto final de periodo .
#Crud sem banco de dados, (criar, ler, atualizar, excluir).
#Deve simular pequenas necessidades de um sistema de biblioteca.
#BIBLIOTECA 


user_root = [['Barros','@123'],['Sarinho','@123']]

separador_duplo(' BIBLIOTECA')
separador_duplo('LOGIN DO USUARIO:')

while True: #dar um jeito aqui

    nomeL = input('\033[36m[-]USER ROOT:\033[m')
    senha = input('\033[36m[-]SENHA ROOT:\033[m')
    print(separador(70))
    nomeL,senha = entrada_em_branco_LOGIN(nomeL,senha)


    start = login_inicial(nomeL,senha,user_root)


    if (start):

        while True:

            separador_duplo(f'\033[36mUSUÁRI(O/A): \033[31m{nomeL}\033[m')

            resposta = menu(['CADASTRAR USUARIO','CADASTRAR LIVRO','EXCLUIR USUARIO','EXCLUIR LIVRO','EMPRESTIMO','DEVOLUÇÃO','SAIR'])

            if (resposta == 1):
                separador_duplo('VAMOS COMEÇAR O CADASTRO:')

                nome = input("\033[33mDIGITE O NOME POR FAVOR: \033[m").upper()
                e = entrada_em_branco(nome)
                nome = e

                cpf = trata_cpf()

                email = verifica_email()

                if verifica_usuarios_repetidos(cpf,email):
                    continue 
                
                cadastrar_usuario(nome, cpf, email)

            elif (resposta == 2 ):
                separador_duplo('CADASTRAR LIVROS:')

                titulo = input('\033[33mDIGITE O TITULO: \033[m').upper()
                e = entrada_em_branco(titulo)
                titulo = e

                autor = input(('\033[33mDIGITE O NOME DO AUTOR: \033[m')).upper()
                e2 = entrada_em_branco(autor)
                autor = e2

                ano_de_publicacao = trata_ano()
                
                quantidade = int(input('\033[33mDIGITE A QUANTIDADE: \033[m'))
                
                if verifica_livros_repetidos(titulo):
                    continue

                cadastrar_livro(titulo,autor,ano_de_publicacao,quantidade)


            elif(resposta == 3):
                Acessar_Listas()
                
                separador_duplo('EXCLUIR USUARIO:')
                print(separador(70))
                
                aux = len(Lista_De_Usuarios_Cadastrados)
                
                if(aux>=1):
                    
                    usuarios_cadastrados = open('csv/login.csv', encoding='utf-8')
                    csv_file = csv.DictReader(usuarios_cadastrados)

                    for usuario in csv_file:
                        Lista_De_Usuarios_Cadastrados.append(usuario['cpf'])

                    tabela_csv = leitor_csv('csv/login.csv')    

                    cria_tabela_usuarios(tabela_csv)
                    

                    print(separador(70))
                    delete_user = trata_cpf()
                    
                    excluir_usuario(delete_user)
                    
                    aux_Lista_De_Usuarios_Cadastrados = []
                    Usuarios_Lista = open('csv/login.csv', encoding='utf-8')
                    csv_file = csv.DictReader(Usuarios_Lista)
                    for livro in csv_file:
                        aux_Lista_De_Usuarios_Cadastrados.append(livro)
                    
                    
                    
                else:
                    print(separador(70))
                    print('\033[m31LISTA DE USUARIO ESTÁ VAZIO, IMPOSSIBILITANDO EXCLUIR USUARIO.\033[m')
                
                aux_Lista_De_Usuarios_Cadastrados = []
                Lista_De_Usuarios_Cadastrados = []


            elif(resposta == 4):
                separador_duplo('EXCLUIR LIVRO:')
                Lista_De_Livros_Cadastrados = []

                print(separador(70))
                                
                Acessar_Listas()
                
                aux = len(Lista_De_Livros_Cadastrados)

                if(aux >= 1):
                    print('\033[33mACERVO DE LIVROS:\033[m')
                    print(separador(70))
                    cria_tabela_livros_excluir(Lista_De_Livros_Cadastrados)
                    
                    print(separador(70))
                    titulo_livro = input('\033[33mDIGITE O TITULO A SER EXCLUIDO: \033[m')

                    e = entrada_em_branco(titulo_livro).upper()
                    titulo_livro = e

                    
                    x = excluir_livro(titulo_livro)
                    
                    aux_Lista_De_Livros_Cadastrados = []
                    items_lista = open('csv/livros.csv')
                    csv_file = csv.DictReader(items_lista)
                    for livro in csv_file:
                        aux_Lista_De_Livros_Cadastrados.append(livro['Titulo'])
                    
                    print('\033[33mACERVO DE LIVROS ATUALIZADO:\033[m', aux_Lista_De_Livros_Cadastrados)
                    
                else:
                    print(separador(70))
                    print('\033[m31ACERVO DE LIVROS ESTÁ VAZIO, IMPOSSIBILITANDO EXCLUIR LIVROS.\033[m')

                Lista_De_Livros_Cadastrados = []
            
            elif(resposta == 5):
                separador_duplo('EMPRESTAR LIVRO:')
                
                Lista_De_Livros_Cadastrados = []
                Lista_De_Autores = []
                livros_cadastrados = open('csv/livros.csv', encoding='utf-8')
                csv_file = csv.DictReader(livros_cadastrados)
                for livro in csv_file:
                    Lista_De_Livros_Cadastrados.append(livro['Titulo'])
                    Lista_De_Autores.append(livro['Autor'])
                    
                
                Lista_De_Cpf_Cadastrados = []                
                Lista_De_Usuarios_Cadastrados = []
                usuarios_cadastrados = open('csv/login.csv', encoding='utf-8')
                csv_file = csv.DictReader(usuarios_cadastrados)
                for usuario in csv_file:
                    Lista_De_Usuarios_Cadastrados.append(usuario['nome'])
                    Lista_De_Cpf_Cadastrados.append(usuario['cpf'])
                    

                separador(70)
                
                cont = len(Lista_De_Livros_Cadastrados)
                cont2 = len(Lista_De_Usuarios_Cadastrados)

                if(cont>=1):
                    print('\033[33mLISTA DE USUARIOS:\033[m')
                    print(separador(70))

                    tabela_csv = leitor_csv('csv/login.csv')    

                    cria_tabela_usuarios(tabela_csv)

                    print(separador(70))
                    print('\033[33mACERVO DE LIVROS:\033[m')
                    print(separador(70))
                    cria_tabela_livros(Lista_De_Livros_Cadastrados, Lista_De_Autores)

                    if(cont2>=1):
                        cpf = trata_cpf()
                        
                        nome_user = input('\033[33mDIGITE O NOME DO USUARIO: \033[m').upper()
                        e1 = entrada_em_branco(nome_user)
                        nome_user = e1

                        titulo_livro = input('\033[33mDIGITE O TITULO DO LIVRO: \033[m').upper()
                        e2 = entrada_em_branco(titulo_livro)
                        titulo_livro = e2
                        
                        
                        emprestar_livro(cpf,nome_user,titulo_livro)
                        Zerar_Listas()

                    else:
                        print('\033[31mNENHUM USUARIO CADASTRADO NO MOMENTO PARA RETIRAR LIVROS.\033[m')
                        
                    Lista_De_Usuarios_Cadastrados = []
                    Lista_De_Livros_Cadastrados = []
                    Lista_De_Autores = []

                else:
                    print('\033[31mNENHUM LIVRO CADASTRADO NO MOMENTO PARA SER EMPRESTADO.\033[m')


            elif(resposta ==  6):
                separador_duplo('DEVOLUÇÃO:')
                
                Lista_De_Usuarios_Com_Emprestimo = []
                Usuarios_Lista = open('csv/emprestimos.csv', encoding='utf-8')
                csv_file = csv.DictReader(Usuarios_Lista)
                for livro in csv_file:
                    Lista_De_Usuarios_Com_Emprestimo.append(livro)

                cont = len(Lista_De_Usuarios_Com_Emprestimo)
                
                if cont>=1:
                    print('\033[33mDADOS DE USUARIOS COM EMPRESTIMO: \033[m')
                    print(separador(70))

                    tabela_csv = leitor_csv('csv/emprestimos.csv')    

                    cria_tabela_emprestimos(tabela_csv)
                    
                    print(separador(70))
                    
                    cpf_d = trata_cpf()

                    nome_d = input('\033[33mDIGITE O NOME DO USUARIO:\033[m')
                    d = entrada_em_branco(nome_d)
                    nome_d = d

                    titulo_d = input('\033[33mDIGITE O TITULO:\033[m')
                    d2 = entrada_em_branco(titulo_d)
                    titulo_livro = d2
                    
                    remover_emprestimo(cpf_d,nome_d,titulo_d)
                    
                    Lista_De_Usuarios_Com_Emprestimo = []
                else:
                    print('\033[31mNENHUM LIVRO EMPRESTADO NO MOMENTO.\033[m')
                    
                print(separador(70))
                Zerar_Listas()
                
            elif(resposta == 7):
                
                separador_duplo('PROGRAMA FINALIZADO')
                print('\033[31m[-]PROGRAMA FINALIZADO....\033[m')
                print(separador(70))
                time.sleep(3)
                break

            else:
                separador_duplo('\033[33mA OPÇÃO DIGITADA NÃO ESTÁ NO MENU DE OPÇÕES.\033[m ')

    else:
        print(separador(70))
        print("\033[31m[-]ERRO USURIO INCORRETO, TENTE NOVAMENTE MAIS TARDE...\033[m")
        time.sleep(8)
        print(separador(70))
