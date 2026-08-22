import json
import os
#Couleurs pour le terminal
VERT = "\033[92m"
ROUGE = "\033[91m"
JAUNE = "\033[93m"
BLEU = "\033[94m"
RESET = "\033[0m"
GRAS = "\033[1m"

contacts = []

def sauvegarder():
    with open("contacts.json", "w") as f:
        json.dump(contacts, f , indent=4)

def charge():
    global contacts
    try:
        with open("contacts.json", "r") as f:
            contacts = json.load(f)
    except:
        contacts = []

def valider_telephone(telephone):
    return telephone.isdigit() and len(telephone) >= 8

def valider_email(email):
    return "@" in email and "." in email
def ajouter_contact():
    print(f"\n{BLEU}=== AJOUTER UN CONTACT ==={RESET}")
    nom = input("Nom: ").strip()
    if not nom:
        print(f"{ROUGE} le nom ne peut pas etre vide !{RESET}")
        return
    telephone = input("Telephone: ").strip()
    if not valider_telephone(telephone):
        print(f"{ROUGE}Numero invalide ! Minimum 8 chiffre !{RESET}")
        return
    email = input("Email: ").strip()
    if not valider_email(email):
        print(f"{ROUGE}Email invalide !{RESET}")
        return
    contact ={ "nom": nom,
                "telephone": telephone,
                "email": email}
    contacts.append(contact)
    sauvegarder()
    print(f"{VERT} Contact {nom} ajoute avec succes !{RESET}")

def affiche_contacts():
    if len(contacts)==0:
        print(f"{JAUNE}Aucun contact trouve !{RESET}")
        return
    for i, contact in enumerate(contacts, 1):
        print(f"\n{ROUGE}Contact #{i}{RESET}")
        print(f" Nom : {VERT}{contact["nom"]}{RESET}")
        print(f" Telephone : {contact["telephone"]}")
        print(f" Email : {contact["email"]}")
        print(f" {"-"*30}")

def rechercher_contact():
    print(f"\n{BLEU}=== LISTE DES CONTACTS ==={RESET}")
    terme = input("Non a rechercher: ").strip().lower()
    resultats = [c for c in contacts if terme in c["nom"].lower()]
    if not resultats:
        print(f"{ROUGE}Aucun contact trouve pour '{terme}' !{RESET}")
        return
    print(f"\n{VERT}{len(resultats)} contact(s) trouve(s) :{RESET}")
    for contact in resultats:
        print(f"\n Nom: {VERT}{contact['nom']}{RESET}")
        print(f"   telephone: {contact['telephone']}")
        print(f"   email: {contact['email']}")

def supprimer_contact():
    print(f"\n{BLEU}=== SUPPRIMER UN CONTACT ==={RESET}")
    nom = input("Nom a supprimer: ").strip()
    for contact in contacts:
        if contact["nom"].lower() == nom.lower():
            confirmation = input(f"{JAUNE}Confirmer la suppression de {nom}? (oui/non): {RESET}")
            if confirmation.lower() == "oui":
                contacts.remove(contact)
                sauvegarder()
                print(f"{VERT} {nom} supprime avec succes !{RESET}")
            else:
                print(f"{JAUNE}Suppression annulee !{RESET}")
                return
        print(f"{ROUGE}Contact '{nom}' non trouve !{RESET}")

def modifier_contact():
    print(f"\n{BLEU}=== MODIFIER UN CONTACT ==={RESET}")
    nom = input("Nom a modifier: ").strip()
    for contact in contacts:
        if contact["nom"].lower() == nom.lower():
            print(f"{JAUNE}Laisse vide pour garder la valeur actuelle{RESET}")
            nouveau_nom = input(f"Nouveau nom ({contact['nom']}): ").strip()
            nouveau_tel = input(f"Nouveau telephone ({contact['telephone']}): ").strip()
            nouveau_email = input(f"Nouveau email ({contact['email']}): ").strip()
            if nouveau_nom:
                contact["nom"] = nouveau_nom
            if nouveau_tel:
                if valider_telephone(nouveau_tel):
                    contact["telephone"] = nouveau_tel
                else:
                    print(f"{ROUGE}Numero invalide - non modifie !{RESET}")
            if nouveau_email:
                if valider_email(nouveau_email):
                    contact["email"] = nouveau_email
                else:
                    print(f"{ROUGE}Email invalide - non modifie !{RESET}")
            sauvegarder()
            print(f"{VERT} Contact modifie avec succes !{RESET}")
            return
        print(f"{ROUGE}Contact '{nom}' non trouve !{RESET}")

def trier_contacts():
    contacts.sort(key=lambda x: x["nom"].lower())
    sauvegarder()
    print(f"{VERT} Contacts tries alphabetiquement !{RESET}")
    affiche_contacts()

def exporter_contacts():
    with open("contacts.txt","w" , encoding="utf-8") as f:
        f.write("="* 40 + "\n")
        f.write("  LISTE DE CONTACTS\n")
        f.write("="* 40 + "\n\n")
        for i, contact in enumerate(contacts, 1):
            f.write(f"Contact #{i}\n")
            f.write(f" Nom:{contact['nom']}\n")
            f.write(f" Telephone:{contact['telephone']}\n")
            f.write(f" Email:{contact['email']}\n")
            f.write("=" * 30 + "\n")
    print(f"{VERT} Contacts exportes dans contacts.txt !{RESET}")

def afficher_menu():
    print(f"\n{BLEU}{'='*35}{RESET}")
    print(f"{GRAS}   GESTIONNAIRE DE CONTACTS{RESET}")
    print(f"{BLEU}{'='*35}{RESET}")
    print(f" {VERT}1.{RESET}Ajouter un contact")
    print(f" {VERT}2.{RESET}Afficher les contacts")
    print(f" {VERT}3.{RESET}Rechercher un contact")
    print(f" {VERT}4.{RESET}Supprimer un contact")
    print(f" {VERT}5.{RESET}Modifier un contact")
    print(f" {VERT}6.{RESET}Trier les contacts")
    print(f" {VERT}7.{RESET}Exporter les contacts")
    print(f" {VERT}8.{RESET}Nombre de contacts")
    print(f" {VERT}9.{RESET} Quitter")
    print(f"{BLEU}{'='*35}{RESET}")

# Programme principal
charge()
print(f"{VERT}{GRAS}Bienvenue dans le Gestionnaire de contacts !{RESET}")
while True:
    afficher_menu()
    choix = input(f"\n{JAUNE}Ton choix: {RESET}").strip()

    if choix == "1":
        ajouter_contact()
    elif choix == "2":
        affiche_contacts()
    elif choix == "3":
        rechercher_contact()
    elif choix == "4":
        supprimer_contact()
    elif choix == "5":
        modifier_contact()
    elif choix == "6":
        trier_contacts()
    elif choix == "7":
        exporter_contacts()
    elif choix == "8":
        print(f"\n{VERT} Tu as {GRAS}{len(contacts)}{RESET}{VERT} contact(s) !{RESET}")
    elif choix == "9":
        print(f"\n{VERT}{GRAS}Au revoir ! Bonne continuation ! {RESET}")
        break
    else:
        print(f"{ROUGE}Choix invalide ! Tape un nombre entre 1 et 9{RESET}")





