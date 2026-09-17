import tkinter as tk

from data import question_data
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.root = tk.Tk()
        self.root.title("Quizzler")
        self.root.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = tk.Label(
            text=f"Score: 0/{len(question_data)}",
            bg=THEME_COLOR,
            fg="white",
            font=("Arial", 17, "bold"),
        )
        self.score.grid(column=1, row=0)

        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 17, "italic"),
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_image = tk.PhotoImage(file="day-34-gui-quiz-app/images/true.png")
        self.true_button = tk.Button(
            image=true_image, highlightthickness=0, command=self.true_pressed
        )
        self.true_button.grid(row=2, column=0)

        false_image = tk.PhotoImage(file="day-34-gui-quiz-app/images/false.png")
        self.false_button = tk.Button(
            image=false_image, highlightthickness=0, command=self.false_pressed
        )
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.root.mainloop()

    def get_next_question(self):
        self.true_button.config(state="normal")
        self.false_button.config(state="normal")
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_text, fill="black")

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've gotten to the end!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        self.score.config(text=f"Score: {self.quiz.score}/{len(question_data)}")
        self.canvas.itemconfig(self.question_text, fill="white")
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

        if is_right:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")

        self.root.after(1000, self.get_next_question)
