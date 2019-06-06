# demander al'utilisateur de rentrer ses  films preferes
continuer = 'o'
listeDeFilms = []
while continuer == 'o':
    userFilm = str(raw_input('ajouter vos films preferes: '))
    # gerer les doublons
    #ce_film = listeDeFilms.count(userFilm)
    # on regarde si un film existe deja
    # on va maintenant convertir les films que l'utilisateur a rentre 
    # en minuscule avec la comprehension de liste
    if userFilm.lower() in [film.lower() for film in listeDeFilms]:
        print('le film {0} est deja dans votre liste de film'.format(userFilm))
        continuer = str(raw_input('voulez vous ajouter un autre film ? o/n: '))
        print('')
    else:
        listeDeFilms.append(userFilm)
        continuer = str(raw_input('voulez vous ajouter un autre film ? o/n: '))
        print('')
    

# nous allons maintenant classes les films par ordre alphabetique
listeDeFilms.sort()
#et ensuite les affiches
print(listeDeFilms)

