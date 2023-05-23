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
            print("2")
      elif tipos == 3:
            print("3")
      elif tipos == 4:
            print("4")
      elif tipos == 5:
            print("5")
      elif tipos == 6:
            print("6")
