class Persona:
    def __init__(self,nombre, apellido, tamagotchi):
        self.nombre = nombre
        self.apellido = apellido
        self.tamagotchi = tamagotchi

    def jugar_con_tamagotchi(self): #juega e invoca el método de tamagotchi jugar()
        self.tamagotchi.jugar()
        return self
    
    def darle_comida(self): #le da de comer su tamagotchi invocando al método de tamagotchi comer()
        self.tamagotchi.comer()
        return self
    
    def curarlo(self): #sana las heridas de su tamagotchi invocando al método de tamagotchi curar()
        self.tamagotchi.curar()
        return self