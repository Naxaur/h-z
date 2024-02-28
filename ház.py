class House:
    def __init__(self, terület, ertek, telepules, tipus, szobak):
        self.terület = terület
        self.ertek = ertek
        self.telepules = telepules
        self.tipus = tipus
        self.szobak = szobak 

t = int(input("Add meg a területet: "))
penz = int(input("Add meg a ház értékét: "))
telepules = int(input("Add meg a települést: "))
tipus = int(input("Add meg a ház típusát: "))
szoba = int(input("Add meg a szobák számát: "))

def __str__(self):
    return(f"A ház{self.terület} területű, értéke {self.ertek} millió forint, {self.telepules} területen van, {self.tipus} típusú, {self.szobakszama} darab szobája van.")

haz = House(terület, ertek, telepules, tipus, szoba)
print(haz)


