import json
import random

class QuizGame:
    def __init__(self, questions_file):
        self.questions = self.load_questions(questions_file)
        self.players = []

    def load_questions(self, questions_file):
        with open(questions_file, 'r') as file:
            data = json.load(file)
            return data

    def add_player(self, player_name):
        self.players.append({"name": player_name, "score": 0})

    def display_question(self, question):
        print(f"\nQuestion: {question['question']}")
        for i, option in enumerate(question['options'], 1):
            print(f"{i}. {option}")

    def play_game(self):
        for player in self.players:
            print(f"\n{player['name']}'s turn:")
            score = 0
            random.shuffle(self.questions)

            for i, q in enumerate(self.questions):
               self.display_question(q)
               user_answer = int(input("Your answer: "))
               ans=q['options'].index(q['correct_answer']) + 1
               if ans == user_answer:
                   print("Correct!\n")
                   score += 1
               else:
                    print(f"Wrong! The correct answer is: {q['correct_answer']}\n")

            player['score'] = score
            print(f"{player['name']}'s score: {score}/{len(self.questions)}")   

           


quiz = QuizGame('quiz_questions.json')

quiz.add_player("Player 1")
quiz.add_player("Player 2")

quiz.play_game()

