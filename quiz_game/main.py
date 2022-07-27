from question_model import Question
from data import question_data
from quiz_brain import QuestionBrain

question_bank = []
for item in question_data:
    question = Question(item['question'], item['correct_answer'])
    question_bank.append(question)

quiz = QuestionBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the Quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
