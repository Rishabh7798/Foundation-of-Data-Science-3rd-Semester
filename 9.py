#Design a python program for Recommendation System.

import random as r

genre = input("Hello! Choose your genre and I'll recommend you a great movie!\n1)Action\n2)Anime\n3)Comedy\n4)Horror\n5)Sci-Fi\n6)Romance\n7)Thriller\n\n")
genre = genre.upper()

movies = {
    "ACTION" : ["The Gray Man", "Top Gun: Maverick", "Jungle Cruise", "Mission Impossible", "Doctor Strange in the Multiverse of Madness"], 
    "ANIME" : ["Flavors of Youth", "Drifting Home", "A Whisker Away", "Stand by Me Doraemon 2", "Whisper of the Heart"], 
    "COMEDY" : ["The King's Man", "Thor: Love and Thunder", "Murder Mystery", "Bullet Train", "Violent Night"], 
    "HORROR" : ["The Conjuring", "The Nun", "The Incantation", "Prey for the Devil", "Orphan : First Kill"], 
    "SCI-FI" : ["Oxygen", "Moonfall", "The Adam Project", "Jurassic World Dominion", "Godzilla vs Kong"], 
    "ROMANCE" : ["Fifty Shades of Grey", "Marry Me", "After Ever Happy", "Dear Zindagi", "Always Be My Maybe"], 
    "THRILLER" : ["The Guilty", "The Pale Blue Eye", "Cuttputlli", "A Thursday", "Welcome Home"]
    }
print("Recommended", genre.lower(), "movie for you is \'",movies[genre][r.choice([0,4])],"\'.")



