
import json
import os
#couleurs pour le terminal
VERT = "\033[92m"
ROUGE = "\033[91m"
JAUNE = "\033[93m"
BLEU = "\033[94m"
RESET = "\033[0m"
GRAS = "\033[1m"

def addition():
    a = float(input("Premier nombre: "))
    b = float(input("Deuxieme nombre: "))
    resultat = a + b
    print(f"{VERT}Resultat:{resultat}{RESET}")

def soustraction():
    a = float(input("Premier nombre: "))
    b = float(input("Deuxieme nombre: "))
    resultat = a - b
    print(f"{VERT}Resultat:{resultat}{RESET}")
def multiplication():
    a = float(input("Premier nombre: "))
    b = float(input("Deuxieme nombre: "))
    resultat = a * b
    print(f"{VERT}Resultat:{resultat}{RESET}") 
def division():
    a = float(input("Premier nombre: "))
    b = float(input("Deuxieme nombre: "))
    if b==0:
        print(f"{ROUGE}Erreur ! Division par zero impossible !{RESET}")
    else:
        resultat = a / b
        print(f"{VERT}Resultat:{resultat}{RESET}")   

while True:
    print(f"\n{BLEU}{'='*30}{RESET}")
    print(f"{GRAS}CALCULATRICE{RESET}")
    print(f"{VERT}1.{RESET} Addition")
    print(f"{VERT}2.{RESET} Soustraction")
    print(f"{VERT}3.{RESET} Multiplication")
    print(f"{VERT}4.{RESET} Division")
    print(f"{VERT}5.{RESET} Quitter")
    print(f"{BLEU}{'='*30}{RESET}")

    choix = input(f"{JAUNE}Ton choix: {RESET}")
    if choix == "1":
        addition()
    elif choix =="2":
        soustraction()
    elif choix =="3":
        multiplication()
    elif choix =="4":
        division()
    elif choix =="5":
        print(f"\n{VERT}{GRAS} Au revoir !{RESET}")
        break
    
    else :
        print(f"{ROUGE}Choix invalide ! Tape 1, 2, 3, 4, ou 5 !{RESET}")
        

