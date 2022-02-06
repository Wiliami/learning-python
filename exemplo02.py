pagina = open("index01.html", "w")
pagina.write("""
<!DOCTYPE html>
<html lang="pt-BR">
    <head>
        <meta charset=UTF-8>
        <title>Como funciona python com html</title>
    </head>
    <body>
    <p>Listar contagem de 10 números!</p>
""")
for l in range(10):
    pagina.write("<p>%d</p>\n" % l)
pagina.write("""
    </body>
</html>
""")
pagina.close()