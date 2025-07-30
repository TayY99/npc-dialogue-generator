import os #lets you access sytems variables (like API key)
import openai # connects to the AI model 
import random # lets you pick random options
from dotenv import load_dotenv # let you load secrets from .env file

#Reads .env file and load secrete key
load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY")) # creates a client to tak to OpenAI's servers


# if input is left blank these are the random options
mood_types = [
    "angry", "sorrowful", "possessed", "unhinged", "vengeful",
    "paranoid", "whispery", "delusional", "sadistic", "cold"
]
setting_types = [
    "abandoned theme park", "foggy village", "submerged asylum",
    "cursed forest", "deserted hospital", "crumbling cathedral",
    "underground bunker", "rotting mansion", "bloodstained lab"
]

npc_types = [ 
    "ghost",
    "cultist",
    "possessed child",
    "demonic clown",
    "abandoned robot",
    "cursed villager",
    "hollow-eyed priest",
    "forgotten soldier",
    "witch in disguise",
    "insane scientist"
]

#Send prompt to ChatGPT via your function
# heart of the generator
def generate_dialogue(mood, setting):
    prompt = f"Generate a creepy line of dialogue from a {npc_type} NPC. Mood: {mood}. Setting: {setting}."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=60
    )

    return response.choices[0].message.content.strip()
#-------------------------------------------------------------

# Get User Input
mood = input("Enter a mood (e.g., angry, sorrowful, possessed): ")
if mood.strip() == "":
    mood = random.choice(mood_types)
    print(f"Random Mood choosen: {mood}")
setting = input("Enter a setting (e.g., haunted mansion, cursed forest): ")
if setting.strip() == "":
    setting= random.choice(setting_types)
    print(f"Random Setting choosen: {setting}")
npc_type = input("Enter an NPC type (e.g., ghost, cultist, robot, possessed child): ")
if npc_type.strip() == "":
    npc_type = random.choice(npc_types)
    print(f"Random NPC Type choosen: {npc_type}")

while True:
    try:
        count_input = input("How many lines do you want to generate? (Leave blank for random 1–5): ")
        if count_input.strip() == "":
            count = random.randint(1, 5)
            print(f"🎲 Random number of lines: {count}")
        else:
            count = int(count_input)
    except ValueError:
        print("Invalid input. Defaulting to 1 line.")
        count = 1

    print(f"\n📜 Generating {count} creepy line(s)...\n")

    for i in range(count):
        line = generate_dialogue(mood, setting)
        print(f"{i+1}. {line}\n")

    again = input("Generate more lines with same setup? (yes/no): ").strip().lower()
    if again not in ["yes", "y"]:
        print("👋 Exiting. Stay creepy.")
        break



# NPC Dialogue Generator
# Created by TayasJah Young (Tay) | tayyoung99@rocketmail.com
# © 2025 All rights reserved.
# Do not copy or distribute without permission.