import random

adjectifs = {
	"A": ["Adorable", "Authentique", "Audacieu.x.se"],
	"B": ["Barbare", "Brave", "Bocal"],
	"C": ["Créati.f.ve", "Calme", "Carré.e"],
	"D": ["Drôle", "Délirant.e", "Docile"],
	"E": ["Extraordinaire", "Eclatant.e", "Enthousiaste"],
	"F": ["Fabuleu.x.se", "Formidable", "Fort.e"],
	"G": ["Génial.e", "Grand.e", "Glauque"],
	"H": ["Horrible", "Horripilant.e", "Hospitalier"],
	"I": ["Irrépressible", "Ivre", "Irrésistible"],
	"J": ["Joyeu.x.se", "Joueu.r.se", "Joli.e"],
	"K": ["Kamikaze", "Karatéka", "Komique"],
	"L": ["Lardon", "Loyal", "Lessive"],
	"M": ["Marrant.e", "Mauvais.e", "Merveilleu.x.se"],
	"N": ["Nyctalope", "Narquois.e", "Net.te"],
	"O": ["Optimiste", "Original.e", "Organisé.e"],
	"P": ["Provoquant.e", "Parfait.e", "Périlleu.x.se"],
	"Q": ["Quadrilatère", "Qualitati.f.ve"],
	"R": ["Rêveu.r.se", "Royal.e", "Rébarbati.f.ve"],
	"S": ["Sympathique", "Souriant.e", "Stupide"],
	"T": ["Talentueu.x.se", "Taquin.e", "Télépathe"],
	"U": ["Unique", "Utopiste"],
	"V": ["Véritable", "Vénérable", "Vénéneu.x.se"],
	"W": ["Wagon", "Wolksvagen", "VraiValeureu.x.se"],
	"X": ["X-trême", "Xylophone"],
	"Y": ["Youhou", "Youpi"],
	"Z": ["Zoyeu.x.se", "Zinzin", "Zoli.e"]
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
	
