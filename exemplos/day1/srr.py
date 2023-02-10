# carregar os dados
dados = [
    {"nome": "Cassiano", "cidade": "Campinas"},
    {"nome": "João", "cidade": "Campinas"}
    ]

# processar
template = """\
<html>
<body>
    <ul>
        <li> Nome: {dados[nome]} </li>
        <li> Cidade: {dados[cidade]} </li>
    </ul>
</body>
</html>
"""

# renderizar
for item in dados:
    print(template.format(dados=item))