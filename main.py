# INFO 607 - TP2 - Exercice 1 : Tri recursif par fusion
# Une liste = une liste Python normale []

import time
import random
import sys

# Q1.1 - Operations de base

# Entree : rien
# Sortie : liste vide []
# Role   : cree une liste vide
def creer_liste():
    return []

# Entree : liste
# Sortie : True ou False
# Role   : dit si la liste est vide
def vide(liste):
    return liste == []

# Entree : liste non vide
# Sortie : le premier element
# Role   : retourne le premier element de la liste
def premier(liste):
    return liste[0]

# Entree : liste non vide
# Sortie : liste sans le premier element
# Role   : retourne la liste sans son premier element
def reste(liste):
    return liste[1:]

# Entree : un element, une liste
# Sortie : liste avec l'element ajoute au debut
# Role   : ajoute un element au debut de la liste
def prefixer(element, liste):
    return [element] + liste

# Entree : un element, une liste
# Sortie : liste avec l'element ajoute a la fin
# Role   : ajoute un element a la fin de la liste
def suffixer(element, liste):
    return liste + [element]


# Q1.2 - FUSION recursive

# Entree : A et B, deux listes triees
# Sortie : une seule liste triee contenant tous les elements de A et B
# Role   : compare les premiers elements et prend le plus petit,
#          recommence jusqu'a ce que l'une des listes soit vide
def FUSION(A, B):
    if vide(A):
        return B
    if vide(B):
        return A

    if premier(A) <= premier(B):
        return prefixer(premier(A), FUSION(reste(A), B))
    else:
        return prefixer(premier(B), FUSION(A, reste(B)))


# Q1.3 - SSC recursive

# Entree : une liste A
# Sortie : la premiere sous-suite croissante de A
# Role   : avance dans la liste tant que les elements augmentent,
#          s'arrete des qu'un element est plus petit que le precedent
#          ex: SSC([a,e,f,c,g,h]) = [a,e,f]
def SSC(A):
    if vide(A) or vide(reste(A)):
        return A

    if premier(reste(A)) >= premier(A):
        return prefixer(premier(A), SSC(reste(A)))
    else:
        return [premier(A)]


# Q1.4 - COMP recursive

# Entree : A debut de B, B liste complete
# Sortie : la partie de B qui vient apres A
# Role   : enleve le debut A de B et retourne ce qui reste
#          ex: COMP([r,y,f], [r,y,f,n,d,z]) = [n,d,z]
def COMP(A, B):
    if vide(A):
        return B

    return COMP(reste(A), reste(B))


# Q1.5 - TRI recursif

# Entree : une liste A non triee
# Sortie : la liste A triee
# Role   : 1. prend la premiere sous-suite croissante
#          2. trie le reste
#          3. fusionne les deux
def TRI(A):
    if vide(A) or vide(reste(A)):
        return A

    suite = SSC(A)
    comp  = COMP(suite, A)

    if vide(comp):
        return A

    return FUSION(suite, TRI(comp))


# Q1.6 - Versions iteratives

# Entree : A et B, deux listes triees
# Sortie : une seule liste triee
# Role   : meme chose que FUSION mais avec une boucle while
def FUSION_iter(A, B):
    resultat = []
    i = 0
    j = 0

    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            resultat.append(A[i])
            i += 1
        else:
            resultat.append(B[j])
            j += 1

    while i < len(A):
        resultat.append(A[i])
        i += 1
    while j < len(B):
        resultat.append(B[j])
        j += 1

    return resultat


# Entree : une liste A
# Sortie : la premiere sous-suite croissante de A
# Role   : meme chose que SSC mais avec une boucle for
def SSC_iter(A):
    if len(A) == 0:
        return []

    suite = [A[0]]

    for i in range(1, len(A)):
        if A[i] >= A[i - 1]:
            suite.append(A[i])
        else:
            break

    return suite


# Entree : A debut de B, B liste complete
# Sortie : la partie de B apres A
# Role   : meme chose que COMP, on coupe apres len(A) elements
def COMP_iter(A, B):
    return B[len(A):]


# Entree : une liste A non triee
# Sortie : la liste A triee
# Role   : meme chose que TRI mais sans recursion
#          etape 1 : decoupe A en sous-suites croissantes
#          etape 2 : fusionne les sous-suites deux par deux jusqu'a la fin
def TRI_iter(A):
    if len(A) <= 1:
        return A

    file = []
    i = 0
    while i < len(A):
        sous_suite = [A[i]]
        while i + 1 < len(A) and A[i + 1] >= A[i]:
            i += 1
            sous_suite.append(A[i])
        file.append(sous_suite)
        i += 1

    while len(file) > 1:
        nouvelle_file = []
        j = 0
        while j < len(file):
            if j + 1 < len(file):
                nouvelle_file.append(FUSION_iter(file[j], file[j + 1]))
                j += 2
            else:
                nouvelle_file.append(file[j])
                j += 1
        file = nouvelle_file

    return file[0]


# Q1.7 - Comparaison des performances

# Entree : taille (int), nombre d'elements dans la liste de test
# Sortie : affiche les temps d'execution
# Role   : compare la version recursive et iterative sur une liste aleatoire
def comparer_performances(taille=2000):
    liste_aleatoire = [random.randint(0, 10000) for _ in range(taille)]

    print(f"\n--- Comparaison sur {taille} elements ---")

    sys.setrecursionlimit(100000)
    copie1 = liste_aleatoire[:]
    debut = time.time()
    TRI(copie1)
    fin = time.time()
    print(f"Recursif  : {fin - debut:.4f} secondes")

    copie2 = liste_aleatoire[:]
    debut = time.time()
    TRI_iter(copie2)
    fin = time.time()
    print(f"Iteratif  : {fin - debut:.4f} secondes")


# Tests

if __name__ == "__main__":
    print("=== Tests de base ===")
    L = prefixer(1, prefixer(2, prefixer(3, creer_liste())))
    print("Liste :", L)
    print("Premier :", premier(L))
    print("Reste :", reste(L))
    print("Vide ?", vide(L))
    print("Suffixer 4 :", suffixer(4, L))

    print("\n=== FUSION ===")
    print(f"FUSION([1,3,5], [2,4,6]) = {FUSION([1,3,5], [2,4,6])}")

    print("\n=== SSC ===")
    print(f"SSC(['a','e','f','c','g','h']) = {SSC(['a','e','f','c','g','h'])}")
    print(f"SSC(['e','b','n','j','y','g']) = {SSC(['e','b','n','j','y','g'])}")

    print("\n=== COMP ===")
    print(f"COMP(['r','y','f'], ['r','y','f','n','d','z']) = {COMP(['r','y','f'], ['r','y','f','n','d','z'])}")

    print("\n=== TRI recursif ===")
    liste_test = [5, 3, 8, 1, 9, 2, 7]
    print(f"TRI({liste_test}) = {TRI(liste_test)}")

    print("\n=== TRI iteratif ===")
    print(f"TRI_iter({liste_test}) = {TRI_iter(liste_test)}")

    print("\n=== Performances ===")
    comparer_performances(2000)



    print(f"\n--- Comparaison sur 10 000 elements iteratif ---")
    liste_10000 = [random.randint(0, 10000) for _ in range(10000)]
    copie2 = liste_10000[:]
    debut = time.time()
    TRI_iter(copie2)
    fin = time.time()
    print(f"Iteratif  10000 : {fin - debut:.4f} secondes")

    print(f"\n--- Comparaison sur 10 000 000 elements iteratif ---")
    liste_10000000 = [random.randint(0, 10000) for _ in range(10000000)]
    copie2 = liste_10000000[:]
    debut = time.time()
    TRI_iter(copie2)
    fin = time.time()
    print(f"Iteratif  10 000 000 : {fin - debut:.4f} secondes")