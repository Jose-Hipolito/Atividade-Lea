def carla(valor,custo):
    if valor>=custo:
        return "Bem sucessido"
    else :
       return f"Mal Sucedido. Faltam {custo-valor} "
valor=float(input("digite o quanto voce tem: "))
custo=float(input("Digite o custo das compras: "))
print (carla(valor, custo))
