# 👻 NPC Dialogue Generator

A creepy dialogue generator for horror games that creates NPC lines based on **mood**, **setting**, and **character type**.

Built with Python and the OpenAI API, this tool is great for developers, writers, or anyone needing eerie one-liners for their next spooky project.

---

## 🎮 Features
- User selects or randomizes:
  - Mood (e.g. angry, sorrowful, possessed)
  - Setting (e.g. abandoned hospital, foggy village)
  - NPC type (e.g. cultist, ghost, robot)
- Option to generate multiple lines
- Loop feature: keep generating more with the same setup
- Random fallback if input is left blank

---

## 🛠️ Tech Stack
- Python
- OpenAI API (`gpt-3.5-turbo`)
- `dotenv` for API key handling
- `random` module for creative variety

---

## 🧪 Sample Output

> **Mood**: angry  
> **Setting**: abandoned theme park  
> **NPC**: possessed clown 

"Welcome to the carnival of screams. Your soul's the prize for tonight's final act."
"Laugh while you can, because when the lights go out, I'm the one who plays."
"You think you're brave, but even courage melts in my funhouse."

## 🚀 How to Run

1. Clone the repo  
2. Create a virtual environment  
3. Install dependencies  
4. Create a `.env` file and add your OpenAI API key  
5. Run the script
