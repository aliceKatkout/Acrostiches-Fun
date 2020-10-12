import random

adjectifs = {
    "A": ["Adorable", "Amical.e", "Agil.e", "Arrogant.e", "Audacieux.se"],
    "B": ["Barbare", "Belle", "Brave"],
    "C": ["Cupide", "Classe", "Comique", "Cocasse" ],
    "D": ["Drole", "Dormeur.se", "Dictateur.trice"],
    "E": ["Exceptionnel.le", "Elégant.e", "Erudit.e"],
    'F': ["Fort.e", "Fantastique", "Frimeur.se"],
    "G": ["Génial.e", "Généreux.se", "Gentil.le"],
    "H": ["Horrible", "Hackeur", "Hospitalié"],
    "I": ["Irresistible", "Idiot.e", "Idilique","Invincible"],
    "J": ["Joyeu.se", "Joli.e", "Joueur.euse"],
    "K": ["Kanon", "Kamikaze","KomiKe"],
    "L": ["Loyal.e", "Logique", "Looping"],
    "M": ["Magnifique", "Mignon.e", "Myope"],
    "N": ["Naif.ve", "Novateur.trice", "Narquois.e","Negatif.ve","Noble","Narratif.ve","Nice"],
    "O": ["Optimiste", "Original.e"],
    "P": ["Parfait.e", "Propre", "Purifié.e" ],
    "Q": ["Qualitatif.ve", "Qomique"],
    "R": ["Responsable", "Résonnable"],
    "S": ["Super", "Sympa", "Salvateur.trice"],
    "T": ["Triste", "Terrifiant.e", "Torturé.e", "Taquin.e", "Trivial.e","Touche a tout","tendre"],
    "U": ["Unique", "Utopiste"],
    "V": ["Vrai.e", "Vénéré.e", "Vaniteux.se"],
    "W": ["Wow", "Waouw", "Wapiti" ],
    "X": ["Xylophone", "Xtra'comme les kellogs","Xtrème"],
    "Y": ["Youpi", "Youhou", "Yougoslave","Yikes"],
    "Z": ["Zinzin", "Zébré", "Zelé"],
}


prenom = input("Tapez votre prénom! ")
prenom_maj = prenom.upper()
lettres = list(prenom_maj)

#nombre_de_lettres = len(lettres)
#accro = adjectifs.get(lettres[0])

for lettre in lettres:
	accro = adjectifs.get(lettre)
	final = random.choice(accro)
	print(final)
	
