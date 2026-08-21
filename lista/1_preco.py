produto= "Livro"
quantidade= 5
preço= 50.00

total_da_compra= preço * quantidade

print() 
if total_da_compra >= 200:
    print(f"Valor final com 10% de desconto: R${total_da_compra * 0.9:.2f}")
    print() 
else:
    print(f"Valor final: R${total_da_compra:.2f}")