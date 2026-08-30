class Avto:
    def __init__(self,model,rang,korobka,narx):
        self.model = model
        self.color = rang
        self.korobka = korobka
        self.cost = narx
        self.km = 0

    def get_info(self):
        return f"Modeli: {self.model}\nRangi: {self.color}\nKorobkasi: {self.korobka}\nNarxi: {self.cost}\nKilometri: {self.km}"   
    def update_km(self,s):
        self.km+=s


avto1 = Avto('nexia','qizil','avtomat','3500')
avto1.update_km(100) 
print(avto1.get_info())  

class Avtosalon:
    def __init__(self,nom,manzil):
        self.nom = nom
        self.manzil = manzil
        self.avtomobillar = []

    def add_avto(self,nomi):
        self.avtomobillar.append(nomi)
    def get_info(self):
        return f"Salon: {self.nom}, Manzil: {self.manzil} Sotuvdagi mashinalar: {self.avtomobillar}"
           

salon1 = Avtosalon("UzAuto Motors", "Toshkent sh.")
salon1.add_avto('Cobalt')
salon1.add_avto('Nexia')    
print(salon1.get_info())

def see_methods(cls):
    return [method for method in dir(cls) if method.startswith('__') is False] #dir(class) shows methods of the class

print(see_methods(Avtosalon))
print(dir(salon1))
print(salon1.__dict__)
print(salon1.__dict__.keys())