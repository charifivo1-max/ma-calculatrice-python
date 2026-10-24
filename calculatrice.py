
print("=== Ma calculatrice Python ===")

a = float(input("Premier nombre : "))
b = float(input("Deuxième nombre : "))

print("Somme :", a + b)
print("Différence :", a - b)
print("Produit :", a * b)

if b != 0:
    print("Quotient :", a / b)
else:
    print("Division impossible : division par zéro.")
