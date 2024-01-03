class Student:
    def __init__(self, nom, prenom, numero_etudiant, credits=0):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = credits

    
    def get_nom(self):
        return self.__nom

    def get_prenom(self):
        return self.__prenom

    def get_numero_etudiant(self):
        return self.__numero_etudiant

    def get_credits(self):
        return self.__credits

    
    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
        else:
            print("Erreur : Le nombre de crédits doit être supérieur à zéro.")


etudiant = Student("John", "Doe", 145)


etudiant.add_credits(10)
etudiant.add_credits(10)
etudiant.add_credits(10)


print(f"Total de crédits de {etudiant.get_nom()} {etudiant.get_prenom()} : {etudiant.get_credits()}")
