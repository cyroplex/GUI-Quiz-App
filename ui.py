from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_input=QuizBrain):
        self.quiz = quiz_input
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)
        self.score = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 10, "bold"))
        self.score.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, borderwidth=0,
                                  command=self.true_pressed)
        self.true_button.grid(column=0, row=2)
        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, borderwidth=0,
                                   command=self.false_pressed)
        self.false_button.grid(column=1, row=2)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")
        self.score.config(text=f"Score: {self.quiz.score}")
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer(user_answer="True"))


    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer(user_answer="False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)




