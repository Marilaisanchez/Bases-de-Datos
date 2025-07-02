import speech 
import random as r
import time
levels = {
    "easy": ["hi", "food", "thanks", "bye"],
    "medium":["available", "thoughtful", "itinerary", "placement"],
    "hard": ["jewelry", "lieutenant", "curtain", "sequel"]
}

def play_game(level):
    words = levels.get(level,[])

    if not words:
        print("Nivel de dificultad incorrecto.")
        return
    score = 0
    attemps = 3

    for _ in range(len(words)):
        r_word = r.choice(words)
        print(f"Pronuncie esta palabra: {r_word}")
        rec_word = speech.speech_es()
        print(f"Usted dijo: {rec_word}")

        if r_word == rec_word:
            print("¡¡Bien hecho!!")
            score =+1
        else:
            print(f"La palabra era: {r_word}")

        time.sleep(2)
    print(f"El juego termino, tu puntuación es: {score}/{len(words)}")

select_level = input("Selecciona un nivel(Easy / Medium / Hard)").lower().strip()
play_game(select_level)

