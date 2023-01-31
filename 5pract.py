# Design a Python program for creating a random story generator
import random

# List of potential story elements
characters = ["pirate", "princess", "dragon", "knight", "wizard"]
locations = ["desert island", "enchanted forest", "underwater kingdom", "mountain fortress", "magical academy"]
actions = ["rescue", "steal", "fight", "discover", "escape"]
objects = ["treasure", "priceless artifact", "mystical weapon", "secret map", "enchanted jewel"]

# Generate a random story
def generate_story():
    character = random.choice(characters)
    location = random.choice(locations)
    action = random.choice(actions)
    obj = random.choice(objects)
    story = "Once upon a time, a brave " + character + " set off on a quest to " + action + " the " + obj + " in the " + location + "."
    return story

# Generate and print 5 random stories
for i in range(5):
    print(generate_story())
