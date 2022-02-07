movies = ['A era do gelo', 'Nárnia', 'Homem Aranha', 'Deus não está morto']
pagina = open('movies.html', 'w')
pagina.write("""
<!DOCTYPE html>
<html lang="pt-BR">
    <head>
        <meta charset=UTF-8>
        <title>Lista de filmes com python</title>
    </head>
    <body>
""")
for movie in movies:
   print(movie)
pagina.write("""
    </body>
</html>
""")
pagina.close()