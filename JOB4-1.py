class Student:
    def __init__(self, nom, prenom, numero_etudiant, credits=0):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = credits
        self.__level = self.__studentEval()  

    
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
            self.__level = self.__studentEval()  
        else:
            print("Erreur : Le nombre de crédits doit être supérieur à zéro.")

    
    def __studentEval(self):
        if self.__credits >= 170:
            return "Excellent"
        elif self.__credits >= 150:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    
    def studentInfo(self):
        print(f"Nom : {self.__nom}, Prénom : {self.__prenom}, Identifiant : {self.__numero_etudiant}, Niveau : {self.__level}")


etudiant = Student("John", "Doe", 145)


etudiant.add_credits(30)
etudiant.add_credits(40)
etudiant.add_credits(20)


etudiant.studentInfo()
