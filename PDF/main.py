from os import system
from db import add_pregunta, add_correcta
import readline
clear = system("clear")
sep = ';'

evaluacion = input("Nombre de la evaluación: ")
unidad=input("Unidad: ")
n_preguntas = int(input("Desde: "))
fin_preguntas = int(input("Hasta: "))
c_alternativas = int(input("Cantidad de alternativas: "))

for i in range(n_preguntas, fin_preguntas+1):
    alternativas = ""
    enunciado = input(f"{i}. ")
    for j in range(97, 97 + c_alternativas):
        alternativas += f"{sep}{chr(j)}. {input(f"{chr(j)}. ")}"
    alternativas = alternativas[1:]
    figura = False if input("Figura (0 ó 1): ") == "0" else True
    add_pregunta(evaluacion=evaluacion, enunciado=enunciado, numero=i, alternativas=alternativas, correcta="", figura=figura, unidad=unidad)
    system("clear")

for i in range(n_preguntas, fin_preguntas+1):
    correcta = input(f"Correcta en pregunta {i}. ")
    add_correcta(evaluacion=evaluacion, numero=i, correcta=correcta)
    system("clear")