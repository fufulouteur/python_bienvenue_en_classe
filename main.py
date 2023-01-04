print('Bienvenue! reponds a ces question pour te presenter.')

print('quel est ton prenom ?')
prenom = input()
print(prenom)


print('ta couleur favorite ?')
couleur = input()
print(couleur)

print('ce que tu preferes manger ?')
plat = input()
print(plat)

print('le film favori ?')
film = input()
print(film)
if film == ('pokemon'):
    print('question bonus')
    print('jeux video prefere')
    jeux_video = input()
    print(jeux_video)

print(F"je vous presente {prenom}! " +
      F" {prenom} adore la couleur {couleur}. " +
      F"son plat prefere est {plat}. " +
      F"son film favori est {film}. ")
if prenom == ('fufulouteur') + couleur == ('red') + plat == ('sushi') + film == ('pokemon'):
    print(F" je vous presente le grand, le beau {prenom}! " +
          F" {prenom} adore la couleur {couleur}car c'est une couleur vive. " +
          F" son plat prefere est les {plat} par ce que il aime le poison . " +
          F" il adore {film}, ")



