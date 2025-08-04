from tamagotchi import Tamagotchi,Mametchi
from persona import Persona

if __name__ == "__main__":
    tama1 = Tamagotchi("Rex", "Rojo",50,50,50)
    persona1 = Persona("Juan", "Perez", tama1)
    mametchi1 = Mametchi("Milu", "Azul")
    persona2 = Persona("Ana", "Lopez", mametchi1) #valores por defecto en 100

    persona1.darle_comida().curarlo().jugar_con_tamagotchi()
    persona2.jugar_con_tamagotchi().darle_comida().curarlo()