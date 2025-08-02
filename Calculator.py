import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("420x520")
root.resizable(False, False)
root.configure(bg="#f4f4f4")

expression = ""

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equalpress():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

equation = tk.StringVar()
entry = tk.Entry(root, textvariable=equation, font=('Segoe UI', 22),
                 bd=5, relief='groove', bg="#ffffff", justify='right')
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, padx=10, pady=20, sticky="we")

btn_font = ('Segoe UI', 16)
btn_kwargs = {
    "font": btn_font,
    "width": 4,
    "height": 2,
    "bg": "#e6e6e6",
    "fg": "#333",
    "bd": 1,
    "relief": "ridge",
    "activebackground": "#dcdcdc"
}

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

for i, row in enumerate(buttons):
    for j, btn in enumerate(row):
        action = lambda x=btn: press(x) if x not in ('C', '=') else (clear() if x == 'C' else equalpress())
        tk.Button(root, text=btn, command=action, **btn_kwargs).grid(row=i+1, column=j, padx=5, pady=5)

root.mainloop()