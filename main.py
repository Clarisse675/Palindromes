#### Fonction secondaire
""" Vérifie si une chaîne de caractères est un palindrome """


def ispalindrome(p):
    """ Retourne True si p est un palindrome, False sinon """
    p = p.lower()
    p = p.translate(str.maketrans("éèêëàâîïôùûüç", "eeeeaaiiouuuc"))
    p = ''.join(c for c in p if c.isalnum())
    return p == p[::-1]


#### Fonction principale


def main():
    """ Permet de tester la fonction ispalindrome """
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
