# Importa as bibliotecas tkinter e pygame
import tkinter as tk
import pygame

# Inicia o mixer de áudio do pygame
pygame.mixer.init()

class Animal:
    def fazer_som(self):
        pass

class Leao(Animal):
    def fazer_som(self):
        pygame.mixer.Sound("leao.mp3").play()
        return "Leão rugindo!"

class Galo(Animal):
    def fazer_som(self):
        pygame.mixer.Sound("galo.mp3").play()
        return "Galo cantando!"

class Elefante(Animal):
    def fazer_som(self):
        pygame.mixer.Sound("elefante.mp3").play()
        return "Elefante trombando!"

def mostrar_som(animal):
    resultado["text"] = animal.fazer_som()

# Interface
janela = tk.Tk()
janela.title("Zoológico Falante")

tk.Label(janela, text="Clique no animal para ouvir seu som!", font=("Arial", 14)).pack(pady=10)

tk.Button(janela, text="Leão", command=lambda: mostrar_som(Leao()), width=20).pack(pady=5)
tk.Button(janela, text="Galo", command=lambda: mostrar_som(Galo()), width=20).pack(pady=5)
tk.Button(janela, text="Elefante", command=lambda: mostrar_som(Elefante()), width=20).pack(pady=5)

resultado = tk.Label(janela, text="", font=("Arial", 16), fg="green")
resultado.pack(pady=20)

janela.mainloop()
