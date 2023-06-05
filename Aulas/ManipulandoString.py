opcao = "10"

while opcao != "0":
    if opcao == "10":
        print(f"""Escolha uma das formas de manipular Strings:
    1 - Métodos que podem ser utilizados com a classe String;
    2 - Interpolando variáveis;
    3 - Fatiamento de String;
    4 - String de múltiplas linhas;\n""")
    opcao = input("Escolha uma das opções acima para prosseguir ou digite 0 para encerrar:\n")
    if opcao == "1":
        print(f"""  Os primeiros métodos que são possíveis usar para manipular uma String são upper, lower
e title:

    upper() - tem a função de deixar toda a String maiuscula;
    lowe() - tem a função de deixar toda a String minuscula;
    title() - tem a função de deixar somente a primeira letra maiuscula.

    Outros métodos que podemos utilizar são de eliminar espaçõs em branco em escritas:

    strip() - tira os espaços em branco antes e após a primeira e ultima palavra;
    lstrip() - tira somente o espaço da esquerda;
    rstrip() - tira somente o espaço da direita.
    
    Alem de métodos de eliminar espaços ou de manipular a string, temos tambem lagumas que podem centralizar e 
adicionar outras informações:

    center() - função utilizada para centralizar a String de acordo com a quantidade de vetores na variavel;
    joint() - função que adiciona informações na String.
""")
        while opcao != "10" and opcao != "0":
            opcao = input("Para prosseguir com outros conteúdos digite 10 ou digite 0 para encerrar:\n")
    if opcao == "2":
        print(f"""Aqui você vai ver como fazer uma interpolação de variáveis em uma String:

    %s/%d/%f - esse é um método antigo para que adicione objetos a String, onde %s são para incluir valores do tipo
String, %d para valores do tipo Inteiro e %f para pontos flutuantes, exemplo: print("Olá, me chamo %s. Eu tenho %d
anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissão, liguagem));
    
    .format - esse método utilizamos chaves nos locais onde desejamos adicionar as variaveis, usando esse método não
precisamos necessariamente informar as variaveis na ordem em que devem ser colocadas, podemos informar a posição do
objeto;

    f-string - esse método é o mais simples, pois só precisamos informar a variavel entre chaves.
""")
        while opcao != "10" and opcao != "0":
            opcao = input("Para prosseguir com outros conteúdos digite 10 ou digite 0 para encerrar:\n")
    if opcao == "3":
        print(f"""Esse método de agora veremos como fazer o fatiamento da String de uma variavel:
    
    [][:][::] - essas são as formas no qual podemos informar qual o vetor que desejamos buscar na String, por
exemplo: podemos ter uma variavel com um nome nela, dessa variavel queremos buscar apenas uma letra, para isso só
colocar [] e o indicador da area que deseja extrair a informação entre colchetes.
""")
        while opcao != "10" and opcao != "0":
            opcao = input("Para prosseguir com outros conteúdos digite 10 ou digite 0 para encerrar:\n")
    if opcao == "4":
        print(f"""Esse método é o mais simples e que facilita na hora da escrita de alguma mensagem no print:
    
    Esse é só a gente observar o código, pois essa parte de 

""")