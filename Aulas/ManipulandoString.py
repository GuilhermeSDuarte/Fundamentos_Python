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
        opcao = input("Para prosseguir com outros conteúdos digite 10 ou digite 0 para encerrar:\n")