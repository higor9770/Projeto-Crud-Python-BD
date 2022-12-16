from conexaoBD import ConexaoDB
from mysql.connector import Error


class senac: #criação de classe 

    def __init__(self):
        pass 
    
    def read(self):
        print("Escolha uma das opções para visualizar\n")
        print("\n 1 - Funcionários\n 2 - Aluno\n 3 - Curso\n 4 - Disciplina")
        escolha2 = int(input("\nEscolha: ")) # escolha2 para dar acesso as condiçoes 
        
        if escolha2 == 1:
            # entra em funcionarios para decidir qual seguir 
            # seja professor ou Tec administrativo 
            print("\nAqui você pode visualizar as informações básicas dos funcionários")
            print("\ndigite o CPF do funcionários para visualizar as informações cadastradas do mesmo")
            self.CPF = input("\ndigite o CPF: ")
            try:
                c = ConexaoDB() # faz a conexão com o banco 
                sql = f"select * from funcionarios where CPF='{self.CPF}'" # define o que será feito na tabela funcionário
                c.executarDQL(sql)
                print("essas são as informações dos funcionários")
                c.desconectar()
            except Error as ex:
                print('Erro de conexão:', ex)

            print("\nVamos visualizar as informações especificas dos funcionários!")
            print("\nDefina qual tipo de funcionário: ")
            print("\n1 - Profesor\n2 - Técnico Administrativo")
            escolha3 = int(input("\nEscolha: ")) # escolha3 para dar acesso as condições dentro de outro if
            if escolha3 == 1:
                print("\ndigite qual a titulação que deseja visualizar")
                self.titulacao = input("\ntitulação: ")
                try:
                    c = ConexaoDB() # faz a conexão com o banco 
                    sql = f"select * from professor where titulacao='{self.titulacao}'" # define o que será feito na tabela funcionário
                    c.executarDQL(sql)
                    c.desconectar()
                except Error as ex:
                    print('Erro de conexão:', ex)

                print("\ndeseja visualizar mais alguma informação ?")
                escolha4 = int(input("\n 1 - visualizar\n 2 - voltar ao Menu\n 3 - Finalizar o programa\n Escolha: "))
                if escolha4 == 1:
                    self.read() # voltar para a função read
                elif escolha4 == 2:
                    self.menu()
                else:
                    self.finalizar() # ir para a função de finalizar
            elif escolha3 == 2:
                print("\ndigite qual o setor que deseja visualizar")
                self.setor = input("setor: ")
                try:
                    c = ConexaoDB() # faz a conexão com o banco 
                    sql = f"select * from tec_administrativo where setor='{self.setor}'" # define o que será feito na tabela funcionário
                    c.executarDQL(sql)
                    c.desconectar()
                except Error as ex:
                    print('Erro de conexão:', ex)

                print("\ndeseja visualizar mais alguma informação ?")
                escolha4 = int(input("\n 1 - visualizar\n 2 - voltar ao Menu\n 3 - Finalizar o programa\n Escolha: "))
                if escolha4 == 1:
                    self.read() # voltar para a função read
                elif escolha4 == 2:
                    self.menu()
                else:
                    self.finalizar() # ir para a função de finalizar                
            else:
                print("\n\nnerro!") # caso for um número diferente de 1 ou 2 printa o erro e 
                self.read()          # e vai para o inicio da função read´         
        
        elif escolha2 == 2:
            print("\nAqui você vai visualizar todos os dados cadastrados do aluno a partir do CPF")
            self.CPF = input("\nDigite o CPF do aluno: ")
            try:
                c = ConexaoDB() # faz a conexão com o banco 
                sql = f"select * from aluno where CPF='{self.CPF}'" # define o que será feito na tabela funcionário
                c.executarDQL(sql)
                c.desconectar()
            except Error as ex:
                print('Erro de conexão:', ex)

            print("\ndeseja visualizar mais alguma informação ?")
            escolha4 = int(input("\n 1 - visualizar\n 2 - voltar ao Menu\n 3 - Finalizar o programa\n Escolha: "))
            if escolha4 == 1:
                self.read() # voltar para a função read
            elif escolha4 == 2:
                self.menu()
            else:
                self.finalizar() # ir para a função de finalizar 
            # aluno
        elif escolha2 == 3:
            print("\nAqui você vai visualizar todos os dados cadastrados a partir do nome do curso")
            self.nomeCurso = input("\nDigite o nome do curso: ")
            try:
                c = ConexaoDB() # faz a conexão com o banco 
                sql = f"select * from curso where nomeCurso='{self.nomeCurso}'" # define o que será feito na tabela funcionário
                c.executarDQL(sql)
                print("essas são as informações dos cursos")
                c.desconectar()
            except Error as ex:
                print('Erro de conexão:', ex)

            print("\ndeseja visualizar mais alguma informação ?")
            escolha4 = int(input("\n 1 - visualizar\n 2 - voltar ao Menu\n 3 - Finalizar o programa\n Escolha: "))
            if escolha4 == 1:
                self.read() # voltar para a função read
            elif escolha4 == 2:
                self.menu()
            else:
                self.finalizar() # ir para a função de finalizar 

            # Curso 
        elif escolha2 == 4:
            print("\nAqui você vai visualizar todos os dados cadastrados a partir do nome da disciplina")
            self.nomeDisciplina = input("\nDigite o nome da disciplina: ")
            try:
                c = ConexaoDB() # faz a conexão com o banco 
                sql = f"select * from disciplina where nomeDisciplina='{self.nomeDisciplina}'" # define o que será feito na tabela funcionário
                c.executarDQL(sql) # comando que jogo os dados para o banco de dados
                print("\nEsses são os dados da disciplina!")
                c.desconectar()
            except Error as ex:
                print('Erro de conexão:', ex)

            print("\ndeseja visualizar mais alguma informação ?")
            escolha4 = int(input("\n 1 - visualizar\n 2 - voltar ao Menu\n 3 - Finalizar o programa\n Escolha: "))
            if escolha4 == 1:
                self.read() # voltar para a função read
            elif escolha4 == 2:
                self.menu()
            else:
                self.finalizar() # ir para a função de finalizar 

            # Disciplina
        elif escolha2 != 1 or escolha2 != 2 or escolha2 != 3 or escolha2 != 4: # define que se tiver um numero diferente desses
            print("\nNúmero errado! Digite um número dentro da escolha.\n")  # ele vai ser reenviado para o inicio da função read
            self.read() 

        else: 
            print("\nerro!")

    def registrar(self):
        print("\nEscolha uma das opções para registrar")
        print("\n 1 - Funcionários\n 2 - Aluno\n 3 - Curso\n 4 - Disciplina")
        escolha2 = int(input("\nEscolha: ")) # escolha2 para dar acesso as condiçoes 
        
        if escolha2 == 1:
            # entra em funcionarios para decidir qual seguir 
            # seja professor ou Tec administrativo 
            print("\nVocê iniciou um novo cadastro do funcionário! Por favor, insira as informações corretamente.")
            print("\nColoque aqui as informações básicas de cada funcionário")
            self.nome = input("Nome: ")
            self.CPF = int(input("CPF:  ")) 
            self.telefone = input("Telefone: ")
            self.salario = int(input("Salário: "))
            self.endereco = input("Endereço: ")
            try:
                c = ConexaoDB() # faz a conexão com o banco 
                sql = f"insert into funcionarios (nome, CPF, telefone, salario, endereco) " # define o que será feito na tabela funcionário
                sql += f"values ('{self.nome}','{self.CPF}','{self.telefone}','{self.salario}','{self.endereco}')" # nomeia os campos da tabela os quais os valores serão inseridos
                c.executarDML(sql) # comando que jogo os dados para o banco de dados
            except Error as ex:
                print('Erro de conexão:', ex)


            print("\nAgora especifique qual a ocupação desse novo funcionário: ")
            print("\n1 - Profesor\n 2 - Técnico Administrativo")
            escolha3 = int(input("\nEscolha: ")) # escolha para dar acesso as condições dentro de outro if
            if escolha3 == 1:
                # cadastrando especificações do professor
                print("\nPor favor, insira as informações corretamente.\n")
                self.titulacao = input("\nTitulação: ")
                self.area_formacao = input("\nÁrea de Formação:  ")
                try:
                    c = ConexaoDB() # faz a conexão com o banco 
                    sql = f"insert into professor (titulacao, area_formacao) " # define o que será feito na tabela funcionário
                    sql += f"values ('{self.titulacao}','{self.area_formacao}')" # nomeia os campos da tabela os quais os valores serão inseridos
                    c.executarDML(sql) # comando que jogo os dados para o banco de dados
                    print("Dados cadastrados com sucesso!")
                    c.desconectar()
                except Error as ex:
                    print('Erro de conexão:', ex)

                print("\ndeseja adicionar mais algum funcionário ?")
                escolha4 = int(input("\n 1 - Registrar\n 2 - voltar ao Menu\n 3 - Finalizar o programa\nEscolha: "))
                if escolha4 == 1:
                    self.registrar() # voltar para a função registrar
                elif escolha4 == 2:
                    self.menu()
                else:
                    self.finalizar() # ir para a função de finalizar

            elif escolha3 == 2:
                # cadastrando especificações do tecnico admnistrativo
                print("\nPor favor, insira as informações corretamente.")
                self.setor = input("\nSetor: ")
                try:
                    c = ConexaoDB() # faz a conexão com o banco 
                    sql = f"insert into tec_administrativo (setor) " # define o que será feito na tabela funcionário
                    sql += f"values ('{self.setor}')" # nomeia os campos da tabela os quais os valores serão inseridos
                    c.executarDML(sql) # comando que jogo os dados para o banco de dados
                    print("\nDados cadastrados com sucesso!")
                    c.desconectar()
                except SystemError as ex:
                    print('Erro de conexão:', ex)

                print("\ndeseja adicionar mais algum funcionário ?")
                escolha4 = int(input("\n 1 - Registrar\n 2 - voltar ao Menu\n 3 - Finalizar o programa\nEscolha: "))
                if escolha4 == 1:
                    self.registrar() # voltar para a função registrar
                elif escolha4 == 2:
                    self.menu()
                else:
                    self.finalizar() # ir para a função de finalizar 
            else:
                print("\nNúmero errado! Defina a opção que queira visualizar novamente!.") # caso for um número diferente de 1 ou 2 printa o erro e 
                self.registrar()     # e vai para o inicio da função registrar

        elif escolha2 == 2:
            # cadastrar aluno
            print("\n Você iniciou um novo cadastro de aluno! Por favor, insira as informações corretamente.")
            self.nome = input("Nome do aluno: ")
            self.matricula = int(input("matricula:  "))
            self.CPF = int(input("CPF do aluno: "))
            try:
                c = ConexaoDB() # faz a conexão com o banco 
                sql = f"insert into aluno (nome, matricula, CPF) " # define o que será feito na tabela funcionário 
                sql += f"values ('{self.nome}','{self.matricula}','{self.CPF}')" # nomeia os campos da tabela os quais os valores serão inseridos
                c.executarDML(sql) # comando que jogo os dados para o banco de dados
                print("\nDados cadastrados com sucesso!")
                c.desconectar()
            except SystemError as ex:
                print('Erro de conexão:', ex)
                    
            print("\ndeseja adicionar mais algum aluno ?")
            escolha4 = int(input("\n 1 - Registrar\n 2 - voltar ao Menu\n 3 - Finalizar o programa\nEscolha: "))
            if escolha4 == 1:
                self.registrar() # voltar para a função registrar
            elif escolha4 == 2:
                self.menu()
            else:
                self.finalizar() # ir para a função de finalizar

        elif escolha2 == 3:
            # cadastrar curso
            print("\nVocê iniciou um novo cadastro de Curso! Por favor, insira as informações corretamente.")
            self.nomeCurso = input("Nome do curso: ")
            self.duracao = int(input("Duração em horas:  "))
            try: 
                c = ConexaoDB() # faz a conexão com o banco 
                sql = f"insert into curso (nomeCurso, duracao)" # define o que será feito na tabela funcionário
                sql += f"values ('{self.nomeCurso}','{self.duracao}')" # nomeia os campos da tabela os quais os valores serão inseridos
                c.executarDML(sql) # comando que jogo os dados para o banco de dados
                print("\nDados cadastrados com sucesso!")
                c.desconectar()
            except SystemError as ex:
                print('Erro de conexão:', ex)
                    
            print("\nDeseja adicionar mais algum curso ?")
            escolha4 = int(input("\n 1 - Registrar\n 2 - voltar ao Menu\n 3 - Finalizar o programa\nEscolha: "))
            if escolha4 == 1:
                self.registrar() # voltar para a função registrar
            elif escolha4 == 2:
                self.menu()
            else:
                self.finalizar() # ir para a função de finalizar

        elif escolha2 == 4:
            # cadastrar Disciplina
            print("\nVocê iniciou um novo cadastro de Disciplina! Por favor, insira as informações corretamente.")
            self.nomeDisciplina = input("Nome da Disciplina: ")
            self.carga_horaria = int(input("Duração em horas:  ")) 
            try:
                c = ConexaoDB() # faz a conexão com o banco 
                sql = f"insert into disciplina (nomeDisciplina, carga_horaria)" # define o que será feito na tabela funcionário 
                sql += f"values ('{self.nomeDisciplina}','{self.carga_horaria}')" # nomeia os campos da tabela os quais os valores serão inseridos
                c.executarDML(sql) # comando que jogo os dados para o banco de dados
                print("\nDados cadastrados com sucesso!")
                c.desconectar()
            except SystemError as ex:
                print('Erro de conexão:', ex)
                        
            print("\nDeseja adicionar mais alguma disciplina ?")
            escolha4 = int(input("\n 1 - Registrar\n 2 - voltar ao Menu\n 3 - Finalizar o programa\nEscolha: "))
            if escolha4 == 1:
                self.registrar() # voltar para a função registrar
            elif escolha4 == 2:
                self.menu()
            else:
                self.finalizar() # ir para a função de finalizar

        elif escolha2 != 1 or escolha2 != 2 or escolha2 != 3 or escolha2 != 4: # define que se tiver um numero diferente desses
            print("\nNúmero errado! Digite um número dentro da escolha.\n")    # ele vai ser reenviado para o inicio da função registrar
            self.registrar() 

        else: 
            print("erro!")

    def deletar(self):
        print("\nEscolha uma das opções para deletar")
        print("\n 1 - Funcionários\n 2 - Aluno\n 3 - Curso\n 4 - Disciplina")
        escolha2 = int(input("\nEscolha: "))
        
        if escolha2 == 1:
            print("\nAqui você vai deletar as informações dos funcionários")
            print("\ninsira o CPF do funcionário para confimação que deseja deletar os dados do funcionário")
            self.CPF = input("\nCPF: ")
            try:
                c = ConexaoDB() # faz a conexão com o banco 
                sql = f"delete from funcionarios where CPF='{self.CPF}'" # define o que será feito na tabela funcionário
                c.executarDML(sql) # comando que jogo os dados para o banco de dados
                print("\ndados deletados com sucesso!")
                c.desconectar()
            except SystemError as ex:
                print('Erro de conexão:', ex)

            # entra em funcionarios para decidir qual seguir 
            # seja professor ou Tec administrativo 
            print("\n Agora vamos deletar as espeficações desse funcionário: ")
            print("\n 1 - Profesor\n 2 - Técnico Administrativo")
            escolha3 = int(input("Escolha: ")) # escolha3 para dar acesso as condições dentro de outro if
            if escolha3 == 1:
                try:
                    print("\ninsira o Id do funcionário certo para confimação que deseja deletar as especificações do professor")
                    self.id_professor = int(input("\ndigite o id do professor: "))
                    c = ConexaoDB() # faz a conexão com o banco 
                    sql = f"delete from professor where id_professor='{self.id_professor}'" # define o que será feito na tabela funcionário
                    c.executarDML(sql) # comando que jogo os dados para o banco de dados
                    print("\ndados deletados com sucesso!")
                    c.desconectar()
                    print("\ndeseja excluir mais algum dado ?")
                    escolha4 = int(input("\n 1- Deletar\n 2- Menu\n 3- finalizar o programa"))
                    if escolha4 == 1:
                        self.deletar() # voltar para a função registrar
                    elif escolha4 == 2:
                        self.menu()
                    else:
                        self.finalizar() # ir para a função de finalizar
                except SystemError as ex:
                    print('Erro de conexão:', ex)
            elif escolha3 == 2:
                try:
                    print("\ninsira o Id do funcionário certo para confimação que deseja deletar as especificações do técnico administrativo")
                    self.id_tec_adminstrativo = int(input("\ndigite o id do técnico administrativo: "))
                    c = ConexaoDB() # faz a conexão com o banco 
                    sql = f"delete from tec_administrativo where id_tec_administrativo ='{self.id_tec_adminstrativo}'" # define o que será feito na tabela funcionário
                    c.executarDML(sql) # comando que jogo os dados para o banco de dados
                    print("\ndados deletados com sucesso!")
                    c.desconectar()
                    print("\ndeseja excluir mais algum dado ?")
                    escolha4 = int(input("\n 1- Deletar\n 2- Menu\n 3- finalizar o programa"))
                    if escolha4 == 1:
                        self.deletar() # voltar para a função registrar
                    elif escolha4 == 2:
                        self.menu()
                    else:
                        self.finalizar() # ir para a função de finalizar
                except SystemError as ex:
                    print('Erro de conexão:', ex)
            else:
                print("\n\n\nerro!") # casso for um número diferente de 1 ou 2 printa o erro e 
                self.deletar()          # e vai para o inicio da função read 
            # funcionário    
        elif escolha2 == 2:
            # Aluno
            print("\nAqui você vai deletar os dados de alunos")
            print("\nPor qual dado deseja deletar: \n1- Matricula\n 2- CPF")
            escolha3 = int(input("\nopção: "))
            
            if escolha3 == 1:
                print("\ninsira a matricula para confimação que deseja deletar os dados do aluno")
                self.matricula = input("\nMatricula: ")
                try:
                    c = ConexaoDB()
                    sql = f"delete from aluno where matricula='{self.matricula}'"
                    c.executarDML(sql)
                    print('\nDados excluidos com sucesso!')
                    c.desconectar()
                except SystemError as ex:
                    print('Erro de conexão:', ex)
                    
                print("deseja excluir mais alguma informação ?")
                escolha4 = int(input("\n 1- Deletar\n 2- Menu\n 3- finalizar o programa"))
                if escolha4 == 1:
                    self.deletar() # voltar para a função registrar
                elif escolha4 == 2:
                    self.menu()
                else:
                    self.finalizar() # ir para a função de finalizar

            elif escolha3 == 2:
                print("\ninsira o nome certo para confimação que deseja deletar seus dados")
                self.CPF = input("\nCPF: ")
                try:
                    c = ConexaoDB()
                    sql = f"delete from aluno where CPF='{self.CPF}'"
                    c.executarDML(sql)
                    print('\nDados excluidos com sucesso!')
                    c.desconectar()
                except SystemError as ex:
                    print('Erro de conexão:', ex)
                    
                print("\nDeseja excluir mais alguma informação ?")
                escolha4 = int(input("\n 1- Deletar\n 2- Menu\n 3- finalizar o programa"))
                if escolha4 == 1:
                    self.deletar() # voltar para a função registrar
                elif escolha4 == 2:
                    self.menu()
                else:
                    self.finalizar() # ir para a função de finalizar

            elif escolha3 != 1 or escolha3 != 2:
                print("\nNúmero errado! Digite um número dentro da escolha.\n")
                self.deletar()

            else: 
                print("erro!")
            # aluno
        elif escolha2 == 3:
            #deletar curso
            print("\nAqui você vai deletar os dados de curso")
            print("\ninsira o nome certo para confimação que deseja deletar seus dados")
            self.nomeCurso = input("\nNome do curso: ")
            try:
                c = ConexaoDB()
                sql = f"delete from curso where nomeCurso='{self.nomeCurso}'"
                c.executarDML(sql)
                print('\nDados excluidos com sucesso!')
                c.desconectar()
            except SystemError as ex:
                print('Erro de conexão:', ex)   

            print("\ndeseja excluir mais alguma informação ?")
            escolha4 = int(input("\n 1- Deletar\n 2- Menu\n 3- finalizar o programa"))
            if escolha4 == 1:
                self.deletar() # voltar para a função registrar
            elif escolha4 == 2:
                self.menu()
            else:
                self.finalizar() # ir para a função de finalizar
            # Curso 
        elif escolha2 == 4:
            #deletar disciplina
            print("\nAqui você vai deletar os dados de Disciplina")
            print("\ninsira o nome certo para confimação que deseja deletar seus dados")
            self.nomeDisciplina = input("\nNome da Disciplina: ")
            try:
                c = ConexaoDB()
                sql = f"delete from disciplina where nomeDisciplina='{self.nomeDisciplina}'"
                c.executarDML(sql)
                print('\nDados excluidos com sucesso!')
                c.desconectar()
            except SystemError as ex:
                print('Erro de conexão:', ex)   
            
            print("\ndeseja excluir mais algum dado ?")
            escolha4 = int(input("\n 1- Deletar\n 2- Menu\n 3- finalizar o programa"))
            if escolha4 == 1:
                self.deletar() # voltar para a função registrar
            elif escolha4 == 2:
                self.menu()
            else:
                self.finalizar() # ir para a função de finalizar
            # Disciplina
        elif escolha2 != 1 or escolha2 != 2 or escolha2 != 3 or escolha2 != 4: # define que se tiver um numero diferente desses
            print("\nNúmero errado! Digite um número dentro da escolha.\n")    # ele vai ser reenviado para o inicio da função deletar
            self.deletar()                                                        
        else: 
            print("erro!")

    def alterar(self):
        print("\nEscolha uma das opções para alterar")
        print("\n 1 - Funcionários\n 2 - Aluno\n 3 - Curso\n 4 - Disciplina")
        escolha2 = int(input("Escolha: ")) # escolha2 para dar acesso as condiçoes 
        
        if escolha2 == 1:
            # entra em funcionarios para decidir qual seguir
            print("\nAqui vamos alterar um dado do Funcionário:")
            print("\nO que você deseja alterar?\n 1 - Nome\n 2 - telefone\n 3 - salário\n 4 - endereço") 
            escolha3 = int(input("\nEscolha: "))
            if escolha3 == 1:
                # mudar o nome
                self.nome = input("\ndigite um novo nome: ")
                self.CPF = int(input("\nconfime seu CPF: "))
                try:
                    c = ConexaoDB() # faz a conexão com o banco 
                    sql = f"update funcionarios " 
                    sql += f"set nome ='{self.nome}' where CPF='{self.CPF}'"
                    c.executarDML(sql)
                    print("\ndados alterados com sucesso!")
                    c.desconectar()
                except SystemError as ex:
                    print('Erro de conexão:', ex)
            elif escolha3 == 2:
                # mudar o telefone
                self.telefone = input("\ndigite um novo telefone: ")
                self.CPF = int(input("\nconfime seu CPF: "))
                try:
                    c = ConexaoDB() # faz a conexão com o banco 
                    sql = f"update funcionarios " 
                    sql += f"set telefone ='{self.nome}' where CPF='{self.CPF}'"
                    c.executarDML(sql)
                    print("\ndados alterados com sucesso!")
                    c.desconectar()
                except SystemError as ex:
                    print('Erro de conexão:', ex)
            elif escolha3 == 3:
                # mudar o salário
                self.salario = input("\ndigite um novo salario: ")
                self.CPF = int(input("\nconfime seu CPF: "))
                try:
                    c = ConexaoDB() # faz a conexão com o banco 
                    sql = f"update funcionarios " 
                    sql += f"set salario ='{self.nome}' where CPF='{self.CPF}'"
                    c.executarDML(sql)
                    print("\ndados alterados com sucesso!")
                    c.desconectar()
                except SystemError as ex:
                    print('Erro de conexão:', ex)
            elif escolha3 == 4:
                # mudar o endereço
                self.endereco = input("\ndigite um novo endereço: ")
                self.CPF = int(input("\nconfime seu CPF: "))
                try:
                    c = ConexaoDB() # faz a conexão com o banco 
                    sql = f"update funcionarios " 
                    sql += f"set endereco ='{self.nome}' where CPF='{self.CPF}'"
                    c.executarDML(sql)
                    print("\ndados alterados com sucesso!")
                    c.desconectar()
                except SystemError as ex:
                    print('Erro de conexão:', ex)

            # seja professor ou Tec administrativo 
            print("\nAinda deseja alterar mais alguma informação?  ")
            print("\n 1 - Professor\n 2 - Técnico Administrativo\n 3 - voltar para o MENU\n 4 - finalizar o programa ")
            escolha4 = int(input("\nEscolha: ")) # escolha3 para dar acesso as condições dentro de outro if
            if escolha4 == 1:
                # alterar professor
                print("\nvamos alterar o dado do professor")
                escolha5 = int(input("\nQual dado do professor você quer alterar?\n 1 - Titulação\n 2 - Área de formação\n Escolha: "))
                if escolha5 == 1:
                    # alterar a titulação 
                    self.titulacao = input("\ndigite sua nova titulação: ")
                    self.id_professor = int(input("\nconfime seu ID: "))
                    try:
                        c = ConexaoDB() # faz a conexão com o banco 
                        sql = f"update professor " 
                        sql += f"set titulação ='{self.titulacao}' where id_professor='{self.id_professor}'"
                        c.executarDML(sql)
                        print("\ndados alterados com sucesso!")
                        c.desconectar()
                    except SystemError as ex:
                        print('Erro de conexão:', ex)

                    print("deseja alterar mais algum dado ?")
                    escolha4 = int(input("\n1 - Alterar\n 2 - voltar ao Menu\n 3 - Finalizar o programa"))
                    if escolha4 == 1:
                        self.alterar() # voltar para a função alterar
                    elif escolha4 == 2:
                        self.menu()
                    else:
                        self.finalizar() # ir para a função de finalizar

                elif escolha5 == 2:
                    # alterar a área de formação
                    self.area_formacao = input("\ndigite sua nova área de formação: ")
                    self.id_professor = int(input("\nconfime seu ID: "))
                    try:
                        c = ConexaoDB() # faz a conexão com o banco 
                        sql = f"update professor " 
                        sql += f"set area_formacao ='{self.area_formacao}' where id_professor='{self.id_professor}'"
                        c.executarDML(sql)
                        print("\ndados alterados com sucesso!")
                        c.desconectar()
                    except SystemError as ex:
                        print('Erro de conexão:', ex)

                    print("\ndeseja alterar mais algum dado ?")
                    escolha4 = int(input("\n1- Alterar\n 2 - voltar ao Menu\n 3 - Finalizar o programa"))
                    if escolha4 == 1:
                        self.alterar() # voltar para a função alterar
                    elif escolha4 == 2:
                        self.menu() # voltar para o menu
                    else:
                        self.finalizar() # ir para a função de finalizar      
                elif escolha5 != 1 or escolha5 != 2:
                    print("\nA escolha foi diferente das opções dadas e devido isso te redirecionamos para o MENU.")
                    self.menu() 
                else:
                    print(">>> ERRO <<<")

            elif escolha4 == 2:
                # alterar Técnico Administrativo
                print("\nvamos alterar o setor do técnico administrativo!")
                self.setor = input("\ndigite o novo setor: ")
                self.id_tec_adminstrativo = int(input("\nconfime seu ID: "))
                try:
                    c = ConexaoDB() # faz a conexão com o banco 
                    sql = f"update tec_administrativo " 
                    sql += f"set setor ='{self.setor}' where id_tecnico_administrativo='{self.id_tec_adminstrativo}'"
                    c.executarDML(sql)
                    print("\ndados alterados com sucesso!")
                    c.desconectar()
                except SystemError as ex:
                        print('Erro de conexão:', ex)

                print("\ndeseja alterar mais algum dado ?")
                escolha4 = int(input("\n1 - Alterar\n 2 - voltar ao Menu\n 3 - Finalizar o programa"))
                if escolha4 == 1:
                    self.alterar() # voltar para a função alterar
                elif escolha4 == 2:
                    self.menu()
                else:
                    self.finalizar() # ir para a função de finalizar

            elif escolha4 == 3:
                # voltar para o Menu
                self.menu()
            elif escolha4 == 4:
                #finalizar o programa
                self.finalizar()
            else:
                print(">>> ERRO! <<<")
                print("Após o erro te redirecionamos ao menu!")   
                self.menu()   

        elif escolha2 == 2:
            print("\nAqui vamos alterar um dado do aluno:")
            print("\nO que você deseja alterar?\n 1 - Nome\n 2 - Matrícula")
            escolha3 = int(input("\nEscolha: "))
            if escolha3 == 1:
                # altera o nome do aluno
                self.nome = input("\nNovo nome: ")
                self.CPF = int(input("\nConfirme seu CPF: "))
                try:
                    c = ConexaoDB() # faz a conexão com o banco 
                    sql = f"update aluno " 
                    sql += f"set nome ='{self.nome}' where CPF='{self.CPF}'"
                    c.executarDML(sql)
                    print('\nDados alterados com sucesso!')
                    c.desconectar()
                except SystemError as ex:
                    print('Erro de conexão:', ex)
                    
                print("\ndeseja alterar mais algum dado ?")
                escolha4 = int(input("\n1 - Alterar\n 2 - voltar ao Menu\n 3 - Finalizar o programa"))
                if escolha4 == 1:
                    self.alterar() # voltar para a função alterar
                elif escolha4 == 2:
                    self.menu()
                else:
                    self.finalizar() # ir para a função de finalizarr

            elif escolha3 == 2:
                # altera a matricula do aluno
                self.nome = input("\nNova matricula: ")
                self.CPF = int(input("\nConfime seu CPF: "))
                try:
                    c = ConexaoDB() # faz a conexão com o banco 
                    sql = f"update aluno " 
                    sql += f"set matricula ='{self.nome}' where CPF='{self.CPF}'"
                    c.executarDML(sql)
                    print('\nDados alterados com sucesso!')
                    c.desconectar()
                except SystemError as ex:
                    print('Erro de conexão:', ex)
                    
                print("\ndeseja alterar mais algum dado ?")
                escolha4 = int(input("\n1 - Alterar\n 2 - voltar ao Menu\n 3 - Finalizar o programa"))
                if escolha4 == 1:
                    self.alterar() # voltar para a função alterar
                elif escolha4 == 2:
                    self.menu()
                else:
                    self.finalizar() # ir para a função de finalizarr

            elif escolha3 != 1 or escolha3 != 2: # define que se tiver um numero diferente desses ele vai ser reenviado para o inicio da função read
                print("\nNúmero errado! Digite um número dentro da escolha.\n") 
                self.alterar() 
                
            else:
                print("erro!")

            # Aluno
        elif escolha2 == 3:
            print("\nAqui vamos alterar um dado de curso:")
            print("\nO que você deseja alterar?\n 1 - Nome do curso\n 2 - duração do curso")
            escolha3 = int(input("\nEscolha: "))
            if escolha3 == 1:
                # altera o nome do curso
                self.nomeCurso = input("\nNovo nome: ")
                self.id_curso = int(input("\nconfirme o id do curso: "))
                try:
                    c = ConexaoDB() # faz a conexão com o banco 
                    sql = f"update curso " 
                    sql += f"set nomeCurso ='{self.nomeCurso}' where id_curso='{self.id_curso}'"
                    c.executarDML(sql)
                    print('\nDados alterados com sucesso!')
                    c.desconectar()
                except SystemError as ex:
                    print('Erro de conexão:', ex)
                    
                print("\nDeseja alterar mais algum dado ?")
                escolha4 = int(input("\n1 - Alterar\n 2 - voltar ao Menu\n 3 - Finalizar o programa"))
                if escolha4 == 1:
                    self.alterar() # voltar para a função alterar
                elif escolha4 == 2:
                    self.menu()
                else:
                    self.finalizar() # ir para a função de finalizar

            elif escolha3 == 2:
                # altera a duração do curso
                self.duracao = input("\nNova duração do curso: ")
                self.id_curso = int(input("\nConfime o id do curso: "))
                try:
                    c = ConexaoDB() # faz a conexão com o banco 
                    sql = f"update curso " 
                    sql += f"set duracao ='{self.duracao}' where id_curso='{self.id_curso}'"
                    c.executarDML(sql)
                    print('\nDados alterados com sucesso!')
                    c.desconectar()
                except SystemError as ex:
                    print('Erro de conexão:', ex)
                    
                print("\nDeseja alterar mais algum dado ?")
                escolha4 = int(input("\n1 - Alterar\n 2 - voltar ao Menu\n 3 - Finalizar o programa"))
                if escolha4 == 1:
                    self.alterar() # voltar para a função alterar
                elif escolha4 == 2:
                    self.menu()
                else:
                    self.finalizar() # ir para a função de finalizar

            elif escolha3 != 1 or escolha3 != 2: # define que se tiver um numero diferente desses ele vai ser reenviado para o inicio da função read
                print("\nNúmero errado! Digite um número dentro da escolha.\n") 
                self.alterar() 
                
            else:
                print("erro!")
            # Curso 
        elif escolha2 == 4:
            print("\nAqui vamos alterar um dado de disciplina:")
            print("\nO que você deseja alterar?\n 1 - Nome da disciplina\n 2 - carga horária")
            escolha3 = int(input("\nescolha: "))
            if escolha3 == 1:
                # altera o nome da disciplina
                self.nomeDisciplina = input("\nNovo nome da disciplina: ")
                self.id_disciplina = int(input("\nconfirme o id da disciplina: "))
                try:
                    c = ConexaoDB() # faz a conexão com o banco 
                    sql = f"update disciplina " 
                    sql += f"set nomeDisciplina ='{self.nomeDisciplina}' where id_disciplina ='{self.id_disciplina}'"
                    c.executarDML(sql)
                    print('\nDados alterados com sucesso!')
                    c.desconectar()
                except SystemError as ex:
                    print('Erro de conexão:', ex)
                    
                print("\ndeseja alterar mais algum dado ?")
                escolha4 = int(input("\n1 - Alterar\n 2 - voltar ao Menu\n 3 - Finalizar o programa"))
                if escolha4 == 1:
                    self.alterar() # voltar para a função alterar
                elif escolha4 == 2:
                    self.menu()
                else:
                    self.finalizar() # ir para a função de finalizar

            elif escolha3 == 2:
                # altera o nome do aluno
                self.carga_horaria = input("\nNova carga horária: ")
                self.id_disciplina = int(input("\nconfirme o id da disciplina: "))
                try:
                    c = ConexaoDB() # faz a conexão com o banco 
                    sql = f"update disciplina " 
                    sql += f"set carga_horaria ='{self.carga_horaria}' where id_disciplina ='{self.id_disciplina}'"
                    c.executarDML(sql)
                    print('\nDados alterados com sucesso!')
                    c.desconectar()
                except SystemError as ex:
                    print('Erro de conexão:', ex)
                    
                print("\ndeseja alterar mais algum dado ?")
                escolha4 = int(input("\n1 - Alterar\n 2 - voltar ao Menu\n 3 - Finalizar o programa"))
                if escolha4 == 1:
                    self.alterar() # voltar para a função alterar
                elif escolha4 == 2:
                    self.menu()
                else:
                    self.finalizar() # ir para a função de finalizar
            # Disciplina
        elif escolha2 != 1 or escolha2 != 2 or escolha2 != 3 or escolha2 != 4: # define que se tiver um numero diferente desses
            print("\nNúmero errado! Digite um número dentro da escolha.\n")    # ele vai ser reenviado para o inicio da função alterar
            self.alterar()                                                        
        else: 
            print("erro!")
        
    def finalizar(self):
        print(">>>>>>>> obriagdo por usar nosso código <<<<<<<<<<<")

    def menu(self):
        print("\nEscolha uma das opções para acessá-la.")
        print("\n1 - Mostrar\n2 - Cadastrar\n3 - Deletar\n4 - Alterar\n5 - Finalizar")  # escolha para adentrar ao crud e possibilitar as escolhas informadas
        escolha1 = int(input("\nEscolha: "))

        if escolha1 == 1:
            self.read()
            # realizar consulta 

        elif escolha1 == 2:
            self.registrar()
            # registrar 

        elif escolha1 == 3:
            self.deletar()
            # deletar as informações 

        elif escolha1 == 4:
            self.alterar()
            # alterar as informações
        elif escolha1 == 5:
            self.finalizar()
            # finalizar o programa
        else:
            print("\nerro!")

object = senac()
object.menu()