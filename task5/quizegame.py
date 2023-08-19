from tkinter import *
from tkinter import messagebox
import json

class Quiz:
    def __init__(self):
        self.q_no=0
        self.display_question()
        self.opt_selected=IntVar()
        self.opts=self.radio_buttons()
        self.display_options()
        self.buttons()
        self.data_size=len(question)
        self.correct=0
    def display_result(self):
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
        
        messagebox.showinfo("Result", f"{result}\n{correct}\n{wrong}")

    def check_ans(self, q_no):
        if self.opt_selected.get() == answer[q_no]:
            return True

    def next_btn(self):
        if self.check_ans(self.q_no):
            self.correct += 1
        self.q_no += 1
        if self.q_no==self.data_size:
            self.display_result()
            gui.destroy()
        else:
            self.display_question()
            self.display_options()

    def buttons(self):
        next_button = Button(gui, text="Next",command=self.next_btn,
        width=13,bg="mediumseagreen",fg="white",font=("ariel",12,"bold"))
        next_button.place(x=350,y=380)
        
        submit_button = Button(gui, text="Submit", command=gui.destroy,
        width=10,bg="crimson", fg="white",font=("ariel",12," bold"))
        submit_button.place(x=700,y=20)

    def display_options(self):
        val=0
        self.opt_selected.set(0)
        
        for option in options[self.q_no]:
            self.opts[val]['text']=option
            val+=1

    def display_question(self):
        q_no = Label(gui, text=question[self.q_no], width=60,
        font=( 'ariel' ,13, 'bold' ), anchor= 'w' )
        q_no.place(x=70, y=100)

    def radio_buttons(self):
        q_list = []
        y_pos = 150
        while len(q_list) < 4:
            radio_btn = Radiobutton(gui,text=" ",variable=self.opt_selected,
            value = len(q_list)+1,font = ("ariel",12))
            q_list.append(radio_btn)
            radio_btn.place(x = 100, y = y_pos)
            y_pos += 40 
        return q_list

gui = Tk()
gui.configure(bg="gainsboro")
gui.title("Quiz")
gui.geometry("850x450")
with open('./task5/questions.json') as f:
    data = json.load(f)

question = (data['question'])
options = (data['options'])
answer = (data[ 'answer'])
quiz = Quiz()
gui.mainloop()