opcao = int
while opcao != "0":
    print("Nesse menu você vai ver as estruturas condicionais e de repetição.\n"
          "1 - Estruturas Condicionais;\n"
          "2 - Estruturas de Repetição;")
    opcao = input("Digite qual das estruturas deseja verificar ou 0 para encerrar:\n")
    if opcao == "1":
        print("As estruturas de condição possuem três formas de serem feitas:\n"
              "A primeira é com somente 'if', onde a estrutura só vai executar se condição for verdadeira;\n"
              "A segunda é com o 'if' e 'else', a estrutura executa if se a condição for verdadeira se não for ele executa else independente da condição;\n"
              "A terceira e ultima é com elif, com o elif é possível criar outras condições alem do if, então sempre que houver a necessidade de informar outras condições pode se construir a estrutura com elif.")
        opcao = input("Digite qualquer outra coisa para voltar ao menu ou 0 para encerrar:\n")
    if opcao == "2":
        print("As estruturas de repetição e alguns comandos extras:\n"
              "Primeiro temos o While, essa estrutura de repetição você coloca uma condição que vai se repitir enquanto ela não for atendida, mas alem da condição do próprio laço há outros comandinhos que podem ser feitos, como:\n"
              "Break - Esse comando tem a função de parar a execução da estrutura;\n"
              "Continue - Esse comando tem a função de pular uma condição, por exemplo, se fossemos fazer uma estrutura onde imprima digitos numéricos de 0 a 10 e não queremos que exiba por exemplo o numeral 5, adicionamos a condição que quando a variavel for igual a 5 ele vai possuir o comando continue onde ai fazer com que a estrutura de repetição vai pular aquela execução.\n"
              "Segundo temos o for onde utilizamos para percorrer um objeto interavel, é ideal utilizar quando sabemos o tamanho que vamos percorrer no laço de repetição podemos usar outras funções tambem, como:\n"
              "range - Onde definimos um tamanho (numeral) para quantidade de vetores que o laço vai percorrer. Exemplo 'for numero in range(0,100), ele vai percorrer de 0 a 99'.")
        opcao = input("Digite qualquer outra coisa para voltar ao menu ou 0 para encerrar:\n")