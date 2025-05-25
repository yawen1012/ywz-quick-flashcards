import random

# Welcome message
print("Welcome to YWZ Quick Flashcards!")
print("Created by Yawen Zhai, your personal learning buddy!\n")

# Flashcard class
class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

# Encouragement messages
encouragements = [
    "Keep it up, superstar!",
    "You're doing great, Yawen style!",
    "Ouch! Try again, but you're still awesome!",
    "Nice one! On your way to greatness!",
    "Fun fact: Flashcards make you smarter!"
]

# Function: ask a question and check the answer
def ask_question(card, player):
    answer = input(f"{player}, {card.question}: ").strip().lower()
    if answer == card.answer.lower():
        print("Correct!")
        print(random.choice(encouragements) + "\n")
        return 1
    else:
        print(f"Wrong! The correct answer is: {card.answer}")
        print(random.choice(encouragements) + "\n")
        return 0

# Function: run the quiz
def run_quiz(cards, players):
    scores = {player: 0 for player in players}
    for i in range(5):
        player = players[i % len(players)]
        card = random.choice(cards)
        scores[player] += ask_question(card, player)
    return scores

# Function: save scores to a file
def save_scores(scores):
    with open("ywz_scores_log.txt", "a") as f:
        for player, score in scores.items():
            f.write(f"{player}: {score} points - Logged by Yawen Zhai\n")

def main():
    players = [input("Enter Player 1 name: ")]
    if input("Add Player 2? (y/n): ").strip().lower() == 'y':
        players.append(input("Enter Player 2 name: "))
    else:
        print("Single-player mode\n")

    # Flashcard deck
    cards = [
        Flashcard("What is 'apple' in Chinese?", "苹果"),
        Flashcard("Translate 'hello' to French", "bonjour"),
        Flashcard("What is 5+7?", "12"),
        Flashcard("What color is the sky?", "blue"),
        Flashcard("How do you say 'thank you' in Japanese?", "arigato"),
    ]

    scores = run_quiz(cards, players)
    print("\nResults:")
    for player, score in scores.items():
        print(f"{player}: {score} points")
        if score == 5:
            print("🏆 Perfect score! You're a flashcard master!")
        elif score >= 3:
            print("👍 Great job! Keep practicing!")
        else:
            print("📚 Keep going! Learning never stops!")
    save_scores(scores)

    again = input("\nPlay again? (y/n): ").strip().lower()
    if again == 'y':
        print("\nHere we go again! 🚀\n")
        main()
    else:
        print("\nThanks for playing YWZ Quick Flashcards!")
        print("~ Yawen Zhai's Signature Project ~")

if __name__ == '__main__':
    main()