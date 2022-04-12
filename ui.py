from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"



class UI:

    def __init__(self,quiz_bro:QuizBrain):

        self.quiz=quiz_bro
        self.windows = Tk()
        self.windows.title("quizz")
        self.windows.config(padx=20, pady=20, bg=THEME_COLOR)

        self.text_1=Label(text="Score",fg="white", bg=THEME_COLOR)
        self.text_1.grid(column=1,row=0)

        self.canvas = Canvas(width=300, height=250,bg="white")
        self.question_Text=self.canvas.create_text(150,125,text="questions",fill=THEME_COLOR,font=("Arial",20,"italic"),width=280)
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)

        true_photo=PhotoImage(file="images/true.png")
        self.true_button=Button(image=true_photo,highlightthickness=0,command=self.true_1)
        self.true_button.grid(column=0,row=2)

        false_photo=PhotoImage(file="images/false.png" )
        self.false_button=Button(image=false_photo,highlightthickness=0,command=self.false)
        self.false_button.grid(column=1,row=2)
        self.get_next_question()






        self.windows.mainloop()



    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.text_1.config(text=f"Score:{self.quiz.score}")

            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_Text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_Text,text="You have reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_1(self):
        q_true = self.quiz.check_answer("True")
        self.feedback(q_true)

    def false(self):
        q_true = self.quiz.check_answer("False")
        self.feedback(q_true)


    def feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")
        self.windows.after(1000,self.get_next_question )



