from sys import stdout, set_int_max_str_digits
set_int_max_str_digits (0)


# 1)

def fiboRecursif (nb):

    if nb <= 0:
        exit (1)
        
    return fiboAppels (nb)


def fiboAppels (nb):

    if nb in (1, 2):
        return 1
        
    return fiboAppels (nb - 1) + fiboAppels (nb - 2)
    
    
# 2)

"""
Complexité temporelle : quasi-linéaire en nb
Complexité spatiale : linéaire en nb
"""

def fiboRescencement (nb):

    if nb <= 0:
        exit (1)

    suite = dict ()
    suite[1] = 1
    suite[2] = 1
    
    for index in range (3, nb + 1):
        suite[index] = suite[index - 1] + suite[index - 2]
    
    return suite[nb]
    
    
# 3)

def fiboAmeliore (nb):

    if nb <= 0:
        exit (1)

    dernier = 1
    actuel = 1
    
    for _ in range (nb - 2):
        antepenultieme = dernier
        dernier = actuel
        actuel = dernier + antepenultieme
    
    return actuel
    
    
# 4)

"""
M := (0 1)
     (1 1)
     
M² = (1 1)
     (1 2)
     
M³ = (1 2)
     (2 3)
     
∀ n ∈ ℕ*,
M^n = (fibo (n - 1)     fibo (n)    )
      (fibo (n)         fibo (n + 1))
"""


# 5)

def encodage (nbBase10):

    if nbBase10 <= 0:
        exit (1)

    nbBase2 = ""
    
    while nbBase10 != 0:
    
        bitFaible = nbBase10 % 2
        nbBase2 = str (bitFaible) + nbBase2
        nbBase10 //= 2
        
    return nbBase2


def produit2x2 (a, b):

    hautGauche = a[0][0] * b[0][0] + a[0][1] * b[1][0]
    hautDroite = a[0][0] * b[0][1] + a[0][1] * b[1][1]
    basGauche  = a[1][0] * b[0][0] + a[1][1] * b[1][0]
    basDroite  = a[1][0] * b[0][1] + a[1][1] * b[1][1]
    
    return ((hautGauche, hautDroite), (basGauche, basDroite))
    

def matrice2x2exposant (expose):

    if expose <= 0:
        exit (1)

    impairs = list (encodage (expose))[1:]
    triangulaire = ((0, 1), (1, 1))
    matrice = triangulaire
    
    for impair in impairs:
    
        matrice = produit2x2 (matrice, matrice)
        if impair == '1':
            matrice = produit2x2 (matrice, triangulaire)

    return matrice


# 6)

"""
Complexité temporelle : logarithmique en nb
Complexité spatiale : logarithmique en nb
"""

def fiboMeilleur (nb):

    # Il suffit de renvoyer la case en haut à droite de la matrice exposant nb
    return matrice2x2exposant (nb)[0][1]


# Tests

def main ():

    # Max. : 35
    stdout.write (str (fiboRecursif (30)) + "\n\n")
    
    # Max. : 200 000
    stdout.write (str (fiboRescencement (30)) + "\n\n")
    
    # Max. : 300 000
    stdout.write (str (fiboAmeliore (30)) + "\n\n")
    
    # Max. : 2 000 000
    stdout.write (str (fiboMeilleur (30)) + "\n\n")
    
    """
    Attention :
    au-delà de la valeur limite indiquée,
    il est possible que votre tâche ne réponde plus.
    """
    
    
main ()
