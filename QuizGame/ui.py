from tkinter import *
from question_brain import QuestionBrain

THEME_COLOR = "#375362"

class Quiz:

    def __init__(self, question_brain: QuestionBrain):
        self.quiz = question_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score:0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Some question text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image=PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0)
        self.true_button.grid(row=2, column=0)

        false_image=PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text= q_text)