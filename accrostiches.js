const adjectifs = {
	A: "Adorable",
	B: "Barbare",
	C: "Créati.f.ve",
	D: "Drôle",
	E: "Extraordinaire",
	F: "Fabuleu.x.se",
	G: "Génial.e",
	H: "Horrible",
	I: "Irrépressible",
	J: "Joyeu.x.se",
	K: "Kamikaze",
	L: "Lardon",
	M: "Marrant.e",
	N: "Nyctalope",
	O: "Optimiste",
	P: "Provoquant.e",
	Q: "Quadrilatère",
	R: "Rêveu.r.se",
	S: "Sympathique",
	T: "Talentueu.x.se",
	U: "Unique",
	V: "Véritable",
	W: "Wagon",
	X: "X-trême",
	Y: "Youhou",
	Z: "Zoyeu.x.se"
}

let prenom = "Alice" ;
let prenom_maj = prenom.toUpperCase();
let liste_lettres = Array.from(prenom_maj);

for (let lettre of liste_lettres) {
	let acro = adjectifs[lettre];
	console.log(acro);
}
