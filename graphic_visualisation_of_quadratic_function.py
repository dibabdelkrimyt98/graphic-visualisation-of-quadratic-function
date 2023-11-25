import matplotlib.pyplot as plt #declaration de la bibliotheque matplot   
import numpy as np #declaration de la bibliothque numpy

def calculer_delta (a,b,c): #la fct calculcer delta 
    return pow(b,2) - 4*a*c #la fct retourner la valeur de delta 

def les_valeurs_des_racines (a,b,c): #declaration du fct les valeurs des racines 
    delta = calculer_delta(a,b,c) #affectation de la variable delta de el sort que la variable prend la valeur de delta 
    if delta < 0: #la condition de delta 
        return None #si la condion est vrai la fct les valeurs des racines  return non
    elif delta == 0: #si delta egale a 0 
        x = (-b)/(2*a) #on affecte a la variable x une valeur  
        return x #si la condition est vrai en retourn la valeur de x
    else: #si les condions de if et elif sont fausse donc en va entree a else 
        x_1 = (((-b) + (np.sqrt(delta))) / (2*a)) #l'affectation de x1 
        x_2 = (((-b) - (np.sqrt(delta))) / (2*a))#l'affectation de x2 
        return x_1, x_2 #dans ce cas la fct va retournee la valeur de x1 et x2 
    
def afficher_les_resultats (a,b,c): #declaration de la fct d'affichage des resultats 
    delta = calculer_delta(a,b,c) #affectation de delta 
    print(f"delta : {delta}") #afficher la valeur de delta 

    racines = les_valeurs_des_racines (a,b,c) #affectation de la variable racines
    if racines is None: #si la fct les_valeurs_des_racines (a,b,c) return none 
                        #implique que la varible racines return none donc racines is none 
        print("Pas des racines reels !") #afficher pas des racines 
    else: #si racines a une valeur 
        print(f"Les racines sont: {racines}") #afficher la valeur des racines 
def afficher_le_graphe (a,b,c): #declaration de la fct qui affiche les graphes 
    x = np.linspace(-10, 10, 400) #la fct np.linspace permet de cree un tableau avec une valeur de depart et une valeur de fin 
    y = a*pow(x,2) + 2*b + c #affectation de y 
    plt.plot(x, y, label=f"{a}x^2 + {b}x + {c}") #instruction plot nous permet de tracer la courbe 
    plt.axhline(0, color='black', linewidth=0.5) #utilisé pour ajouter une ligne horizontale sur l’axe.
    plt.axvline(0, color='black', linewidth=0.5) #utilisé pour ajouter une ligne horizontale sur l’axe.
    plt.grid(color='gray', linestyle='--', linewidth=0.5) 
    plt.legend()
    plt.title("Graphique de la fonction quadratique") #ttire de graphe 
    plt.xlabel("x") 
    plt.ylabel("y")
    plt.show() #voir le graphe 
def main():
    try:
        print("Entrez les coefficients de la fonction quadratique ax^2 + bx + c :")
        a = float(input("Coefficient a : "))
        b = float(input("Coefficient b : "))
        c = float(input("Coefficient c : "))
        
        afficher_les_resultats(a, b, c)
        afficher_le_graphe(a, b, c)
        
    except ValueError:
        print("Erreur : Veuillez entrer des coefficients valides.")

if __name__ == "__main__":
    main()  