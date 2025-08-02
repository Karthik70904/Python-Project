import tkinter as tk
from tkinter import messagebox

quiz = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "London", "Paris", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "What is 5 + 7?",
        "options": ["10", "12", "11", "13"],
        "answer": "12"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["Python", "Java", "JavaScript", "C++"],
        "answer": "JavaScript"
    },
    {
        "question": "Who wrote 'Harry Potter'?",
        "options": ["J.R.R. Tolkien", "J.K. Rowling", "Stephen King", "Dan Brown"],
        "answer": "J.K. Rowling"
    }
]

current_q = 0
score = 0

root = tk.Tk()
root.title("Quiz Game")
root.geometry("500x450")
root.resizable(False, False)

question_var = tk.StringVar()

question_label = tk.Label(root, textvariable=question_var, font=('Segoe UI', 16), wraplength=480, pady=20)
question_label.pack()

option_buttons = []

def load_question():
    question = quiz[current_q]
    question_var.set(f"Q{current_q + 1}: {question['question']}")
    for i, opt in enumerate(question['options']):
        option_buttons[i].config(text=opt)

def check_answer(index):
    global current_q, score
    selected = option_buttons[index]['text']
    correct = quiz[current_q]['answer']
    if selected == correct:
        score += 1
    current_q += 1
    if current_q < len(quiz):
        load_question()
    else:
        messagebox.showinfo("Quiz Over", f"Your score: {score}/{len(quiz)}")
        root.destroy()

for i in range(4):
    btn = tk.Button(root, text="", font=('Segoe UI', 14), width=40, height=2, 
                    command=lambda i=i: check_answer(i))
    btn.pack(pady=5)
    option_buttons.append(btn)

load_question()
root.mainloop()
