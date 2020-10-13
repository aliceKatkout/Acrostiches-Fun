import random

adjectifs = {
    "A": ["Adorable", "Amical.e", "Agil.e", "Arrogant.e", "Audacieux.se","Attentive", "Authentique"],
    "B": ["Barbare", "Belle", "Brave", "Bocal"],
    "C": ["Cupide", "Classe", "Comique", "Cocasse", "Créatif.ve", "Calme", "Carré.e"],
    "D": ["Drôle", "Dormeur.se", "Dictateur.trice", "Délirant.e", "Docile"],
    "E": ["Exceptionnel.le", "Elégant.e", "Erudit.e", "Extraordinaire", "Eclatant.e", "Enthousiaste"],
    'F': ["Fort.e", "Fantastique", "Frimeur.se", "Fabuleux.se", "Formidable"],
    "G": ["Génial.e", "Généreux.se", "Gentil.le", "Grand.e", "Glauque"],
    "H": ["Horrible", "Hackeur", "Hospitalier"],
    "I": ["Irresistible", "Idiot.e", "Idyllique","Invincible", "Irrépressible"],
    "J": ["Joyeu.se", "Joli.e", "Joueur.euse"],
    "K": ["Kanon", "Kamikaze", "Karatéka"],
    "L": ["Loyal.e", "Logique", "Looping", "Lardon"],
    "M": ["Magnifique", "Mignon.ne", "Myope", "Marrant.e", "Merveilleux.se"],
    "N": ["Naif.ve", "Novateur.trice", "Narquois.e","Negatif.ve","Noble","Narratif.ve","Nice", "Net.te", "Nyctalope"],
    "O": ["Optimiste", "Original.e", "Organisé.e", "Orage"],
    "P": ["Parfait.e", "Propre", "Purifié.e", "Provoquant.e", "Périlleux.se"],
    "Q": ["Qualitatif.ve", "Qomique", "Quadrilatère"],
    "R": ["Responsable", "Raisonnable", "Rieur.euse", "Rêveur.se", "Royal.e"],
    "S": ["Super", "Sympathique", "Salvateur.trice", "Souriant.e", "Stupide"],
    "T": ["Triste", "Terrifiant.e", "Torturé.e", "Taquin.e", "Trivial.e","Touche-à-tout", "Tendre", "Talentueux.se", "Taquin.e", "Télépathe"],
    "U": ["Unique", "Utopiste", "Usurpateur.trice"],
    "V": ["Vrai.e", "Vénéré.e", "Vaniteux.se", "Vénéneux.se", "Véritable"],
    "W": ["Wow", "Waouw", "Wapiti", "Wolksvagen" ],
    "X": ["Xylophone", "Xtra'comme les kellogs","Xtrème"],
    "Y": ["Youpi", "Youhou", "Yougoslave","Yikes"],
    "Z": ["Zinzin", "Zébré.e", "Zelé.e", "Zoyeux.se"],
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
