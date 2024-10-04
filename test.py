# Definice slovníku
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

# Kontrola, jestli je hodnota 'Alice' ve slovníku
if 'Alice' in my_dict.values():
    print("Hodnota 'Alice' je obsažena ve slovníku.")
else:
    print("Hodnota 'Alice' není ve slovníku.")

# Kontrola, jestli je hodnota 30 ve slovníku
if 30 in my_dict.values():
    print("Hodnota 30 je obsažena ve slovníku.")
else:
    print("Hodnota 30 není ve slovníku.")

# Kontrola, jestli je dvojice ('name', 'Alice') ve slovníku
if ('name', 'Alice') in my_dict.items():
    print("Dvojice ('name', 'Alice') je obsažena ve slovníku.")
else:
    print("Dvojice ('name', 'Alice') není ve slovníku.")

# Kontrola, jestli je dvojice ('age', 25) ve slovníku
if ('age', 25) in my_dict.items():
    print("Dvojice ('age', 25) je obsažena ve slovníku.")
else:
    print("Dvojice ('age', 25) není ve slovníku.")

# Projití slovníku pomocí cyklu for
print("\nProcházím slovník:")
for key, value in my_dict.items():  # Procházíme každou dvojici klíč-hodnota
    print(f"Klíč: {key}, Hodnota: {value}")  # Vytiskneme klíč a odpovídající hodnotu

# Alternativní přístup - procházení pouze klíčů
print("\nProcházím pouze klíče:")
for key in my_dict.keys():  # Procházíme všechny klíče
    print(f"Klíč: {key}")  # Vytiskneme každý klíč

# Alternativní přístup - procházení pouze hodnot
print("\nProcházím pouze hodnoty:")
for value in my_dict.values():  # Procházíme všechny hodnoty
    print(f"Hodnota: {value}")  # Vytiskneme každou hodnotu
