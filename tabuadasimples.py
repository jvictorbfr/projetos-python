tabuada=int(input("Digite um número para exibir a tabuada: "))

print("\nTabuada do número", tabuada,":")
for numero in range(1,11,1):
    print("\n", tabuada,"x", numero, "=", tabuada*numero)