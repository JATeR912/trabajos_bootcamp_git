class Tamagotchi:

    def __init__(self, nombre, color, salud, felicidad, energia): 
        self.nombre = nombre
        self.color = color
        self.salud = salud
        self.felicidad = felicidad
        self.energia = energia

    def estado(self):
        print(f"Estado de {self.nombre}:")
        print(f"Salud: {self.salud}")
        if self.salud <= 0:
            print(f"{self.nombre} ha fallecido.")
        elif self.salud < 30:
            print(f"{self.nombre} está enfermo(╯︵╰,).")
        elif self.salud < 60:
            print(f"{self.nombre} está un poco enfermo(╯-╰,).")
        else:
            print(f"{self.nombre} está saludable(｡°w°｡).")  

        print(f"Felicidad: {self.felicidad}")
        if self.felicidad < 10:
            print(f"{self.nombre} está muy triste ( ╥_╥ ).")
        elif self.felicidad < 50:
            print(f"{self.nombre} está un poco triste(´•-•̀ ).")
        elif self.felicidad < 80:
            print(f"{self.nombre} está feliz( °v° ).")
        else:
            print(f"{self.nombre} está muy feliz(っ＾▿＾)❤.")
            

        print(f"Energia: {self.energia}")
        if self.energia <= 0:
            print(f"{self.nombre} está agotado y necesita energía (╯︵╰,).")
        elif self.energia < 40: 
            print(f"{self.nombre} tiene poca energía(╯-╰,).")
        elif self.energia < 80:
            print(f"{self.nombre} tiene energía(｡°v°｡).") 
        else:
            print(f"{self.nombre} tiene mucha energía(｡°w°｡).")
        print() 
    
    def jugar(self): #incrementa la felicidad el 10, disminuye la salud en 5 - energia menos 10.
        self.felicidad += 10
        self.limite_felicidad()
        self.salud -= 5
        self.energia -= 10
        print(f"{self.nombre} está jugando. Felicidad aumento en 10, salud disminuye en 5")
        self.estado()
        return self
    
    def comer(self): #incrementa la felicidad en 5, aumenta la salud en 10 - energia menos 5.
        self.felicidad += 5
        self.limite_felicidad()
        self.salud += 10
        self.limite_salud()
        self.energia -= 5
        print(f"{self.nombre} está comiendo. Felicidad aumento en 5 y salud en 10")
        self.estado()
        return self
    
    def curar(self): #incrementa la salud en 20, disminuye la felicidad en 5 - energia menos 5.
        self.salud += 20
        self.limite_salud()
        self.felicidad -= 5
        self.energia -= 5
        print(f"{self.nombre} está siendo curado. Salud aumento en 20, felicidad disminuye en 5")
        self.estado()
        return self
    
    def limite_felicidad(self):
        if self.felicidad >= 100:
            self.felicidad = 100
    
    def limite_salud(self):
        if self.salud >= 100:
            self.salud = 100
    
    def limite_energia(self):
        if self.energia >= 100:
            self.energia = 100
  
class Mametchi(Tamagotchi):
    def __init__(self, nombre, color, salud=100, felicidad=100, energia=100): # valores por defecto en maximo
        super().__init__(nombre, color, salud, felicidad, energia)
        self.tipo = "Mametchi"

    def estado(self):
        print(f"Tamgochi de tipo {self.tipo}")
        super().estado()
        return self