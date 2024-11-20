from rdflib import Graph, URIRef, Literal, Namespace, RDF

g = Graph()

namespace = Namespace("https://online-game-store.com/")

game_1 = URIRef("https://online-game-store.com/games/fortnite")
game_2 = URIRef("https://online-game-store.com/games/fc-25")
game_3 = URIRef("https://online-game-store.com/games/valorant")
game_4 = URIRef("https://online-game-store.com/games/call-of-duty")
game_5 = URIRef("https://online-game-store.com/games/minecraft")
game_6 = URIRef("https://online-game-store.com/games/red-dead-redemption-2")

company_1 = URIRef("https://online-game-store.com/company/epic-games")
company_2 = URIRef("https://online-game-store.com/company/ea-sports")
company_3 = URIRef("https://online-game-store.com/company/riot-games")
company_4 = URIRef("https://online-game-store.com/company/activision")
company_5 = URIRef("https://online-game-store.com/company/mojang")
company_6 = URIRef("https://online-game-store.com/company/rockstar-games")

genre_1 = URIRef("https://online-game-store.com/genre/battle-royale")
genre_2 = URIRef("https://online-game-store.com/genre/first-person-shooter")
genre_3 = URIRef("https://online-game-store.com/genre/sports")
genre_4 = URIRef("https://online-game-store.com/genre/sandbox")
genre_5 = URIRef("https://online-game-store.com/genre/adventure")

g.add((game_1, RDF.type, namespace.Game))
g.add((game_1, namespace.title, Literal("Fortnite")))
g.add((game_1, namespace.developedBy, company_1))
g.add((game_1, namespace.hasGenre, genre_1))

g.add((game_2, RDF.type, namespace.Game))
g.add((game_2, namespace.title, Literal("FIFA 25")))
g.add((game_2, namespace.developedBy, company_2))
g.add((game_2, namespace.hasGenre, genre_3))

g.add((game_3, RDF.type, namespace.Game))
g.add((game_3, namespace.title, Literal("Valorant")))
g.add((game_3, namespace.developedBy, company_3))
g.add((game_3, namespace.hasGenre, genre_2))

g.add((game_4, RDF.type, namespace.Game))
g.add((game_4, namespace.title, Literal("Call of Duty")))
g.add((game_4, namespace.developedBy, company_4))
g.add((game_4, namespace.hasGenre, genre_2))

g.add((game_5, RDF.type, namespace.Game))
g.add((game_5, namespace.title, Literal("Minecraft")))
g.add((game_5, namespace.developedBy, company_5))
g.add((game_5, namespace.hasGenre, genre_4))
g.add((game_5, namespace.hasGenre, genre_5))

g.add((game_6, RDF.type, namespace.Game))
g.add((game_6, namespace.title, Literal("Red Dead Redemption 2")))
g.add((game_6, namespace.developedBy, company_6))
g.add((game_6, namespace.hasGenre, genre_5))

g.add((company_1, RDF.type, namespace.Company))
g.add((company_1, namespace.name, Literal("Epic Games")))

g.add((company_2, RDF.type, namespace.Company))
g.add((company_2, namespace.name, Literal("EA Sports")))

g.add((company_3, RDF.type, namespace.Company))
g.add((company_3, namespace.name, Literal("Riot Games")))

g.add((company_4, RDF.type, namespace.Company))
g.add((company_4, namespace.name, Literal("Activision")))

g.add((company_5, RDF.type, namespace.Company))
g.add((company_5, namespace.name, Literal("Mojang")))

g.add((company_6, RDF.type, namespace.Company))
g.add((company_6, namespace.name, Literal("Rockstar Games")))

g.add((genre_1, RDF.type, namespace.Genre))
g.add((genre_1, namespace.name, Literal("Battle Royale")))

g.add((genre_2, RDF.type, namespace.Genre))
g.add((genre_2, namespace.name, Literal("First Person Shooter")))

g.add((genre_3, RDF.type, namespace.Genre))
g.add((genre_3, namespace.name, Literal("Sports")))

g.add((genre_4, RDF.type, namespace.Genre))
g.add((genre_4, namespace.name, Literal("Sandbox")))

g.add((genre_5, RDF.type, namespace.Genre))
g.add((genre_5, namespace.name, Literal("Adventure")))

# print(g.serialize(format="turtle"))

query = """
    PREFIX ns: <https://online-game-store.com/>
    SELECT ?gameTitle ?companyName (GROUP_CONCAT(?genreName; SEPARATOR=", ") AS ?genres)
    WHERE {
        ?game ns:title ?gameTitle .
        ?game ns:developedBy ?company .
        ?company ns:name ?companyName .
        ?game ns:hasGenre ?genre .
        ?genre ns:name ?genreName .
    }
    GROUP BY ?gameTitle ?companyName
"""

print("[")
for row in g.query(query):
    print("{\n" + f"    Game: {row.gameTitle}\n"
                  f"    Developer: {row.companyName}\n"
                  f"    Genres: {row.genres}" +
          "\n},")
print("]")