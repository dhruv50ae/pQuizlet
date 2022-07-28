from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quizBrain: QuizBrain):
        self.quiz = quizBrain
        self.window = Tk()
        self.window.title("Quizlet")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.scoreLabel = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.scoreLabel.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.questionText = self.canvas.create_text(150, 125, width=280, text="Some question text", fill=THEME_COLOR,
                                                    font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        trueImage = PhotoImage(file="images/true.png")
        self.trueButton = Button(image=trueImage, highlightthickness=0, command=self.truePressed)
        self.trueButton.grid(row=2, column=1)

        falseImage = PhotoImage(file="images/false.png")
        self.falseButton = Button(image=falseImage, highlightthickness=0, command=self.falsePressed)
        self.falseButton.grid(row=2, column=0)

        self.getNextQuestion()

        self.window.mainloop()

    def getNextQuestion(self):
        qText = self.quiz.next_question()
        self.canvas.itemconfig(self.questionText, text=qText)

    def truePressed(self):
        self.quiz.check_answer("True")

    def falsePressed(self):
        self.quiz.check_answer("False")
