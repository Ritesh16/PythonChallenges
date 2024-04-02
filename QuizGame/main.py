from question_model import Question
from data import question_data
from question_brain import QuestionBrain
from ui import Quiz

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz_brain = QuestionBrain(question_bank)
quiz_ui = Quiz(quiz_brain)
#while quiz.still_has_questions():
#    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score was: {quiz_brain.score}/{quiz_brain.question_number}")