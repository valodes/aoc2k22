# On initialise les variables suivantes :
# - formes_cailloux : une liste de formes de cailloux
# - index_caillou_actuel : un entier qui indique l'index du caillou actuel dans la liste formes_cailloux
# - jets : le contenu du fichier './src/day_17/input.txt'
# - index_jet_actuel : un entier qui indique l'index du jet actuel dans la liste jets
# - tour_en_cours : un ensemble de points représentant la tour en cours de construction
# - cache_cycles : un dictionnaire qui stocke les cycles détectés dans la construction de la tour
formes_cailloux, index_caillou_actuel = [
    (0,1,2,3), 
    (1,0+1j,2+1j,1+2j), 
    (0,1,2,2+1j,2+2j), 
    (0,0+1j,0+2j,0+3j), 
    (0,1,0+1j,1+1j)
], 0
jets, index_jet_actuel = open('./src/day_17/input.txt').read(), 0
tour_en_cours, cache_cycles = {-1}, {}

# On définit une fonction vide qui prend en argument un point p
# et retourne vrai si p est dans les limites du jeu (dans l'intervalle des réels entre 0 et 6, 
# et supérieur à 0 en imaginaire) et n'appartient pas à la tour actuelle.
def est_vide(p):
    return p.real in range(7) and p.imag > 0 and p not in tour_en_cours

# On itère sur un intervalle allant de 0 à 1e12 (un très grand nombre).
# Pour chaque itération de la boucle :
for i in range(int(1e12)):
    # On calcule la hauteur de la tour en prenant la partie imaginaire (la partie en j) la plus grande parmi les éléments de la tour.
    hauteur_tour = max(x.imag for x in tour_en_cours)
    
    # On initialise un point de départ en haut de la tour avec une valeur de 2 pour la partie réelle (la partie en x) 
    # et 4 de plus que la hauteur de la tour pour la partie imaginaire.
    point_depart = complex(2, hauteur_tour + 4)
    
    # Si i est égal à 2022, on imprime la hauteur de la tour.
    if i == 2022:
        print(hauteur_tour)

        # On stocke un tuple contenant les valeurs de index_caillou_actuel et index_jet_actuel dans key.
    # Si key est déjà présent dans le dictionnaire cache_cycles, cela signifie qu'un cycle a été détecté.
    key = (index_caillou_actuel, index_jet_actuel)
    if key in cache_cycles:
        # On récupère les valeurs de n et h stockées dans le dictionnaire pour le cycle en cours.
        n_debut_cycle, hauteur_debut_cycle = cache_cycles[key]
        
        # On calcule le nombre de tours restantes jusqu'à 1e12 et le reste de la division de ce nombre par la différence de tours entre le début du cycle et la position actuelle.
        tours_restantes = int(1e12) - i
        reste_division = tours_restantes % (n_debut_cycle - i)
        
        # Si le reste de la division est égal à zéro, cela signifie que la hauteur de la tour à 1e12 peut être prédite de manière exacte.
        # On imprime la hauteur de la tour à 1e12 et on termine la boucle.
        if reste_division == 0:
            print(hauteur_tour + (hauteur_debut_cycle - hauteur_tour) * (tours_restantes // (n_debut_cycle - i)))
            break
    # Si key n'est pas présent dans le dictionnaire cache_cycles, on stocke les valeurs de i et h dans le dictionnaire pour être utilisées lors de l'itération suivante.
    else:
        cache_cycles[key] = (i, hauteur_tour)
        
    # On récupère le caillou suivant à partir de la liste formes_cailloux en utilisant l'index index_caillou_actuel.
    caillou_actuel = formes_cailloux[index_caillou_actuel]
    
    # On incrémente index_caillou_actuel et on le modulo par la longueur de la liste formes_cailloux 
    # pour s'assurer qu'il reste dans les limites de la liste.
    index_caillou_actuel = (index_caillou_actuel + 1) % len(formes_cailloux)
    
    # On entre dans une boucle infinie.
    while True:
        # On récupère le jet suivant à partir de la liste jets en utilisant l'index index_jet_actuel.
        # Si le jet est '>', on initialise jet_actuel avec 1, sinon on l'initialise avec -1.
        jet_actuel = +1 if jets[index_jet_actuel] == '>' else -1
        # On incrémente index_jet_actuel et on le modulo par la longueur de la liste jets 
        # pour s'assurer qu'il reste dans les limites de la liste.
        index_jet_actuel = (index_jet_actuel + 1) % len(jets)
        
        # On vérifie si tous les points de caillou_actuel décalés de jet_actuel sont vides.
        # Si c'est le cas, on déplace le point de départ de jet_actuel sur la gauche ou la droite.
        if all(est_vide(point_depart + jet_actuel + point_caillou) for point_caillou in caillou_actuel):
            point_depart += jet_actuel
            
        # On vérifie si tous les points de caillou_actuel décalés d'un complexe avec une partie imaginaire négative sont vides.
        # Si c'est le cas, on déplace le point de départ d'un complexe avec une partie imaginaire négative (vers le bas).
        if all(est_vide(point_depart - 1j + point_caillou) for point_caillou in caillou_actuel):
            point_depart -= 1j
        # Si aucun des déplacements précédents n'a été possible, on sort de la boucle infinie.
        else:
            break
    
    # On ajoute les points de caillou_actuel décalés de point_depart à l'ensemble tour_en_cours.
    tour_en_cours |= {point_depart + point_caillou for point_caillou in caillou_actuel}

