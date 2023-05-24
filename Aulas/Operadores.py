tipos = 10
while tipos != 0:
      print("Nesse menu você vai escolher sobre qual operador deseja aprender:\n"
            "1 - Aritméticos\n"
            "2 - Comparação\n"
            "3 - Atribuição\n"
            "4 - Lógico\n"
            "5 - Identidade\n"
            "6 - Associação")
      tipos = int(input("Escolha o tipo de operador ou digite 0 para encerrar:"))
      if tipos == 1:
            print("Os operadores aritméticos que o Python e outras linguagens possuem são:\n")
            print("Adição = 2 + 2 =",2+2,"\n")
            print("Subtração = 3 - 1 = ",3-1,"\n")
            print("Multiplicação = 2 * 3 =",2*3,"\n")
            print("Divisão = 8 / 4 = ",8/4,
                  "ou "
                  "8 // 4 = ",8//4,"\n")
            print("Resto = 8 % 4 = ",8%4,"\n")
            print("Exponenciação = 2 ** 3 = ",2**3,"\n")
            while tipos != 0 and tipos != 10:
                  fim = input("Se desejar encerrar digite 0 e para prosseguir vendo outros operadores 10:")
                  if fim == "10" or fim == "0":
                        tipos = int(fim)
      elif tipos == 2:
            print("Os operadores de comparação que o Python e outras linguagens possuem são:\n")
            print("Igualdade ==\n")
            print("Diferença !=\n")
            print("Maior que > e Maior ou igual >=\n")
            print("Menor que < e Meno ou igual <=\n")
            print("Todas essas comparações retornam valores booleanos, sendo assim True e False.\n")
            while tipos != 0 and tipos != 10:
                  fim = input("Se desejar encerrar digite 0 e para prosseguir vendo outros operadores 10:")
                  if fim == "10" or fim == "0":
                        tipos = int(fim)
      elif tipos == 3:
            print("Os operadores de atribuição que o Python e outras linguagens possuem são:\n")
            print("Atribuição simples =\n")
            print("Atribuição com Adição +=\n")
            print("Atribuição com Subtração -=\n")
            print("Atribuição com Divisão /=\n")
            print("Atribuição com Módulo %=\n")
            print("Atribuição com Exponenciação **=\n")
            print("Essas são as formas de atribuir um dado há um objeto do sistema.\n")
            while tipos != 0 and tipos != 10:
                  fim = input("Se desejar encerrar digite 0 e para prosseguir vendo outros operadores 10:")
                  if fim == "10" or fim == "0":
                        tipos = int(fim)
      elif tipos == 4:
            print("Os operadores lógicos que o Python possui são:\n")
            print("Operador E and\n")
            print("Operador Ou or\n")
            print("Operador de Negação not\n")
            print("Parênteses ()\n")
            print("Esses são operadores que geralmente servem para tratar algum tipo de comparação, são usados principalmente para montar expressão lógica.\n")
            while tipos != 0 and tipos != 10:
                  fim = input("Se desejar encerrar digite 0 e para prosseguir vendo outros operadores 10:")
                  if fim == "10" or fim == "0":
                        tipos = int(fim)
      elif tipos == 5:
            print("Os operadores de identidade que o Python possui são:\n")
            print("Operador is, sendo assim ele verifica se a variavel possui a mesma posição de memoria.\n")
            print("Operador is not, esse ele verifica se a variavel não possui a mesma posição de memoria.\n")
            print("Esses são operadores utilizados para comparar se dois objetos testados ocupam a mesma posição na memória.\n")
            while tipos != 0 and tipos != 10:
                  fim = input("Se desejar encerrar digite 0 e para prosseguir vendo outros operadores 10:")
                  if fim == "10" or fim == "0":
                        tipos = int(fim)
      elif tipos == 6:
            print("Os operadores de associação que o Python possui são:\n")
            print("Operador in, sendo assim ele verifica se o objeto está na variavel ou variaveis.\n")
            print("Operador in not, esse ele verifica se o objeto não está na variavel ou variaveis.\n")
            print("Esses são operadores utilizados para verificar se um objeto está dentro de algo ou variavel.\n")
            while tipos != 0 and tipos != 10:
                  fim = input("Se desejar encerrar digite 0 e para prosseguir vendo outros operadores 10:")
                  if fim == "10" or fim == "0":
                        tipos = int(fim)
