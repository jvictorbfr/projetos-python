#CALCULADORA SIMPLES by Jvictor

#OBTENÇÃO DOS DADOS
n1=int(input("Digite o primeiro número inteiro: "))
n2=int(input("Digite o segundo número inteiro: "))

#SÍMBOLO DAS OPERAÇÕES
print("\nOperações:")
print("Soma (+)")
print("Subtração (-)")
print("Multiplicação (*)")
print("Divisão (/)")
op=input("\nDigite o símbolo da operação que você deseja executar: ")

#PROCESSAMENTO DOS DADOS
soma=n1+n2
sub=n1-n2
mul=n1*n2
div=n1/n2

#SAÍDA DOS RESULTADOS
if(op=="+"):
    print("\nO resultado da soma desses números é",soma,".")
if(op=="-"):
    print("\nO resultado da subtração desses números é",sub,".")
if(op=="*"):
    print("\nO resultado da multiplicação desses números é",mul,".")
if(op=="/"):
    print("\nO resultado da divisão desses números é",div,".")