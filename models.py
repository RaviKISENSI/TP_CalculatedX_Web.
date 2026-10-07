class Calculatrice:
    def __init__(self):
        self._historique = []

    def addition(self, a, b):
        resultat = a + b
        self._historique.append(f"{a} + {b} = {resultat}")
        return resultat

    def soustraction(self, a, b):
        resultat = a - b
        self._historique.append(f"{a} - {b} = {resultat}")
        return resultat

    def multiplication(self, a, b):
        resultat = a * b
        self._historique.append(f"{a} x {b} = {resultat}")
        return resultat

    def division(self, a, b):
        if b == 0:
            raise ValueError("Division par zéro impossible")
        resultat = a / b
        self._historique.append(f"{a} / {b} = {resultat}")
        return resultat

    def exposant(self, a, b):
        if a == 0 and b < 0:
            raise ValueError("0 ne peut pas avoir d'exposant négatif")
        resultat = a ** b
        self._historique.append(f"{a} ^ {b} = {resultat}")
        return resultat

    def get_historique(self):
        return list(self._historique)


if __name__ == "__main__":
    calc = Calculatrice()

    while True:
        try:
            a = float(input("Premier nombre : "))
            signe = input("Signe (+, -, *, /, ^) : ").strip()
            b = float(input("Deuxième nombre : "))

            if signe == "+":
                print(calc.addition(a, b))
            elif signe == "-":
                print(calc.soustraction(a, b))
            elif signe == "*":
                print(calc.multiplication(a, b))
            elif signe == "/":
                print(calc.division(a, b))
            elif signe == "^":
                print(calc.exposant(a, b))
            else:
                print("Signe inconnu")

        except ValueError as e:
            print(f"Erreur : {e}")
        except ZeroDivisionError:
            print("Erreur : opération impossible (division par zéro)")
        except OverflowError:
            print("Erreur : résultat trop grand")

        if input("Autre calcul ? (o/n) : ").lower() != "o":
            break

    print(calc.get_historique())