import requests

from question_model import Question
from quiz_brain import QuizBrain

api_url = "https://opentdb.com/api.php?amount=10&difficulty=hard&type=boolean"

response = requests.get(api_url)
response.raise_for_status()  # Will raise an error for bad status codes

# print(response.status_code)
# print(response.text)

question_data = response.json()

question_bank = []

for question in question_data["results"]:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"your final score was: {quiz.score}/{quiz.question_number}")
