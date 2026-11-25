ig = int(input("Digite o número na tabuada que deseja: "))
i=int
i=1
if (ig>=10):
    print("Número maior que 10, digite outro valor!")
    il = int(input("Digite outro valor: "))
else:
    while i<=10:
        print(ig,"x",i,"=",ig*i)
        i+= 1