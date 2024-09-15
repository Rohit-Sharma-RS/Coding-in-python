import tkinter

THEME_COLOR = "#375362"
FONT_NAME = 'Arial'

from tkinter import *
from quiz_brain import QuizBrain


class UserInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0

        def click_true():
            is_right = self.quiz.check_answer('True')
            self.label.config(text=f"Score : {self.quiz.score}")
            self.give_feedback(is_right)

        def click_false():
            is_right = self.quiz.check_answer('False')
            self.label.config(text=f"Score : {self.quiz.score}")
            self.give_feedback(is_right)

        self.window = Tk()
        self.window.title = "Quizzler"

        self.window.config(padx=20,pady=20, background=THEME_COLOR)

        self.label = Label(text=f"Score : {self.quiz.score}", font=("Bold",20,"bold"), background=THEME_COLOR, fg="white")
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg ="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some question",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        self.true = PhotoImage(file='images/true.png')
        self.false = PhotoImage(file='images/false.png')
        self.true_button = Button(image=self.true, highlightthickness=0, command=click_true)
        self.false_button = Button(image=self.false, highlightthickness=0, command=click_false)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.get_question()

        self.window.mainloop()

    def get_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"The quiz has ended \nYour score is {self.quiz.score}/10")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(500, self.get_question)
