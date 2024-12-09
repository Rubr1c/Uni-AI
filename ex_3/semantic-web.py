"""
Online Game Store Semantic Web Implementation

This module implements a semantic web model for an online game store using RDF (Resource Description Framework).
The ontology represents relationships between video games, their developers, genres, and additional metadata.

Ontology Design:
1. Core Entities:
   - Games: Individual video game titles
   - Companies: Game development companies
   - Genres: Game categories/genres

2. Properties:
   - title: Name of the game
   - name: Name of company or genre
   - price: Numeric value in USD
   - rating: ESRB rating (E, T, M, etc.)
   - releaseDate: Date of initial release
   - playerCount: Number of supported players
"""

import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    __import__("rdflib")
except ImportError:
    print(f"rdflib not found. Installing...")
    install("rdflib")


from rdflib import Graph, URIRef, Literal, Namespace, RDF
from datetime import datetime

g = Graph()

namespace = Namespace("https://online-game-store.com/")

game_1 = URIRef("https://online-game-store.com/games/fortnite")
game_2 = URIRef("https://online-game-store.com/games/fc-25")
game_3 = URIRef("https://online-game-store.com/games/valorant")
game_4 = URIRef("https://online-game-store.com/games/call-of-duty")
game_5 = URIRef("https://online-game-store.com/games/minecraft")
game_6 = URIRef("https://online-game-store.com/games/red-dead-redemption-2")
game_7 = URIRef("https://online-game-store.com/games/rocket-league")
game_8 = URIRef("https://online-game-store.com/games/league-of-legends")

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
g.add((game_1, namespace.hasPrice, Literal(0.0)))
g.add((game_1, namespace.hasRating, Literal("T")))
g.add((game_1, namespace.hasReleaseDate, Literal("2017-07-25")))
g.add((game_1, namespace.hasPlayerCount, Literal("100")))

g.add((game_2, RDF.type, namespace.Game))
g.add((game_2, namespace.title, Literal("FIFA 25")))
g.add((game_2, namespace.developedBy, company_2))
g.add((game_2, namespace.hasGenre, genre_3))
g.add((game_2, namespace.hasPrice, Literal(69.99)))
g.add((game_2, namespace.hasRating, Literal("E")))  # Everyone
g.add((game_2, namespace.hasReleaseDate, Literal("2024-09-27")))
g.add((game_2, namespace.hasPlayerCount, Literal("4")))

g.add((game_3, RDF.type, namespace.Game))
g.add((game_3, namespace.title, Literal("Valorant")))
g.add((game_3, namespace.developedBy, company_3))
g.add((game_3, namespace.hasGenre, genre_2))
g.add((game_3, namespace.hasPrice, Literal(0.0)))  # Free to play
g.add((game_3, namespace.hasRating, Literal("T")))
g.add((game_3, namespace.hasReleaseDate, Literal("2020-06-02")))
g.add((game_3, namespace.hasPlayerCount, Literal("10")))

g.add((game_4, RDF.type, namespace.Game))
g.add((game_4, namespace.title, Literal("Call of Duty")))
g.add((game_4, namespace.developedBy, company_4))
g.add((game_4, namespace.hasGenre, genre_2))
g.add((game_4, namespace.hasPrice, Literal(59.99)))
g.add((game_4, namespace.hasRating, Literal("M")))  # Mature
g.add((game_4, namespace.hasReleaseDate, Literal("2023-11-10")))
g.add((game_4, namespace.hasPlayerCount, Literal("150")))

g.add((game_5, RDF.type, namespace.Game))
g.add((game_5, namespace.title, Literal("Minecraft")))
g.add((game_5, namespace.developedBy, company_5))
g.add((game_5, namespace.hasGenre, genre_4))
g.add((game_5, namespace.hasGenre, genre_5))
g.add((game_5, namespace.hasPrice, Literal(29.99)))
g.add((game_5, namespace.hasRating, Literal("E10+")))  # Everyone 10+
g.add((game_5, namespace.hasReleaseDate, Literal("2011-11-18")))
g.add((game_5, namespace.hasPlayerCount, Literal("8")))

g.add((game_6, RDF.type, namespace.Game))
g.add((game_6, namespace.title, Literal("Red Dead Redemption 2")))
g.add((game_6, namespace.developedBy, company_6))
g.add((game_6, namespace.hasGenre, genre_5))
g.add((game_6, namespace.hasPrice, Literal(59.99)))
g.add((game_6, namespace.hasRating, Literal("M")))
g.add((game_6, namespace.hasReleaseDate, Literal("2018-10-26")))
g.add((game_6, namespace.hasPlayerCount, Literal("32")))

g.add((game_7, RDF.type, namespace.Game))
g.add((game_7, namespace.title, Literal("Rocket League")))
g.add((game_7, namespace.developedBy, company_1))
g.add((game_7, namespace.hasGenre, genre_3))
g.add((game_7, namespace.hasPrice, Literal(19.99)))
g.add((game_7, namespace.hasRating, Literal("E")))
g.add((game_7, namespace.hasReleaseDate, Literal("2015-07-07")))
g.add((game_7, namespace.hasPlayerCount, Literal("8")))

g.add((game_8, RDF.type, namespace.Game))
g.add((game_8, namespace.title, Literal("League of Legends")))
g.add((game_8, namespace.developedBy, company_3))
g.add((game_8, namespace.hasGenre, genre_3))
g.add((game_8, namespace.hasPrice, Literal(0.0)))
g.add((game_8, namespace.hasRating, Literal("T")))
g.add((game_8, namespace.hasReleaseDate, Literal("2009-10-27")))
g.add((game_8, namespace.hasPlayerCount, Literal("10")))

g.add((company_1, RDF.type, namespace.Company))
g.add((company_1, namespace.name, Literal("Epic Games")))
g.add((company_1, namespace.foundedYear, Literal("1991")))
g.add((company_1, namespace.headquarters, Literal("Cary, North Carolina")))

g.add((company_2, RDF.type, namespace.Company))
g.add((company_2, namespace.name, Literal("EA Sports")))
g.add((company_2, namespace.foundedYear, Literal("1991")))
g.add((company_2, namespace.headquarters, Literal("Redwood City, California")))

g.add((company_3, RDF.type, namespace.Company))
g.add((company_3, namespace.name, Literal("Riot Games")))
g.add((company_3, namespace.foundedYear, Literal("2006")))
g.add((company_3, namespace.headquarters, Literal("Los Angeles, California")))

g.add((company_4, RDF.type, namespace.Company))
g.add((company_4, namespace.name, Literal("Activision")))
g.add((company_4, namespace.foundedYear, Literal("1979")))
g.add((company_4, namespace.headquarters, Literal("Santa Monica, California")))

g.add((company_5, RDF.type, namespace.Company))
g.add((company_5, namespace.name, Literal("Mojang")))
g.add((company_5, namespace.foundedYear, Literal("2009")))
g.add((company_5, namespace.headquarters, Literal("Stockholm, Sweden")))

g.add((company_6, RDF.type, namespace.Company))
g.add((company_6, namespace.name, Literal("Rockstar Games")))
g.add((company_6, namespace.foundedYear, Literal("1998")))
g.add((company_6, namespace.headquarters, Literal("New York City, New York")))

g.add((genre_1, RDF.type, namespace.Genre))
g.add((genre_1, namespace.name, Literal("Battle Royale")))
g.add((genre_1, namespace.description, Literal("Last-player-standing gameplay where multiple players compete in an arena")))

g.add((genre_2, RDF.type, namespace.Genre))
g.add((genre_2, namespace.name, Literal("First Person Shooter")))
g.add((genre_2, namespace.description, Literal("Action game where the player views the game world from a first-person perspective")))

g.add((genre_3, RDF.type, namespace.Genre))
g.add((genre_3, namespace.name, Literal("Sports")))
g.add((genre_3, namespace.description, Literal("Games that simulate traditional sports")))

g.add((genre_4, RDF.type, namespace.Genre))
g.add((genre_4, namespace.name, Literal("Sandbox")))
g.add((genre_4, namespace.description, Literal("Open-world games with emphasis on player freedom and creativity")))

g.add((genre_5, RDF.type, namespace.Genre))
g.add((genre_5, namespace.name, Literal("Adventure")))
g.add((genre_5, namespace.description, Literal("Story-driven games focusing on exploration and problem-solving")))


def print_query_results(query_name, results):
    """
    Print query results in a nicely formatted way
    
    Parameters:
            query_name (str): name for the query
            results (query.Result): results outputed from the query 
    """
    print(f"\n=== {query_name} ===")
    
    # Get the column names from the first result
    if results:
        columns = results.vars
        
        # Print header
        header = " | ".join(str(col).upper() for col in columns)
        print("-" * len(header))
        print(header)
        print("-" * len(header))
        
        # Print rows
        for row in results:
            values = [str(row[col]) for col in columns]
            print(" | ".join(values))
        print("-" * len(header))

# Query 1: Find all free-to-play games
query1 = """
    PREFIX ns: <https://online-game-store.com/>
    SELECT ?title ?rating ?playerCount
    WHERE {
        ?game ns:title ?title ;
              ns:hasPrice ?price ;
              ns:hasRating ?rating ;
              ns:hasPlayerCount ?playerCount .
        FILTER(?price = 0.0)
    }
"""

# Query 2: Find games by genre with their companies
query2 = """
    PREFIX ns: <https://online-game-store.com/>
    SELECT ?title ?genre ?company ?releaseDate
    WHERE {
        ?game ns:title ?title ;
              ns:hasGenre ?genreUri ;
              ns:developedBy ?companyUri ;
              ns:hasReleaseDate ?releaseDate .
        ?genreUri ns:name ?genre .
        ?companyUri ns:name ?company .
    }
    ORDER BY ?genre ?releaseDate
"""

# Query 3: Find companies and their game count
query3 = """
    PREFIX ns: <https://online-game-store.com/>
    SELECT ?company (COUNT(?game) as ?gameCount)
    WHERE {
        ?game ns:developedBy ?companyUri .
        ?companyUri ns:name ?company .
    }
    GROUP BY ?company
    ORDER BY DESC(?gameCount)
"""

if __name__ == "__main__":
    print_query_results("Free-to-Play Games", g.query(query1))
    print_query_results("Games by Genre", g.query(query2))
    print_query_results("Company Game Counts", g.query(query3))