import tkinter as tk

def get_values():
    num1 = int(num_entry_1.get())
    num2 = int(num_entry_2.get())
    return num1, num2

def insert_values(value):
    num_entry_answer.delete(0, 'end')
    num_entry_answer.insert(0, value)

def plus():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)

def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)

def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)

def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)

window = tk.Tk()
window.title('Calculator')
window.geometry("350x450")
window.resizable(False, False)
window.configure(background="#66B2FF")

button_plus = tk.Button(window, text="+", font='Times 10', fg='#000020', width=10, height=3, borderwidth=5, command=plus)
button_plus.place(x=75, y=180)
button_plus.configure(background="#99CC99", relief='ridge')

button_minus = tk.Button(window, text="-", font='Times 10', fg='#000020', width=10, height=3, borderwidth=5, command=sub)
button_minus.place(x=75, y=260)
button_minus.configure(background="#99CC99", relief='ridge')

button_multi = tk.Button(window, text="*", font='Times 10', fg='#000020', width=10, height=3, borderwidth=5, command=mul)
button_multi.place(x=180, y=180)
button_multi.configure(background="#99CC99", relief='ridge')

button_div = tk.Button(window, text="/", font='Times 10', fg='#000020', width=10, height=3, borderwidth=5, command=div)
button_div.place(x=180, y=260)
button_div.configure(background="#99CC99", relief='ridge')

num_entry_1 = tk.Entry(window, width=30, font='Times 10', fg='#660000') # Окно для первого числа
num_entry_1.place(x=75, y=65)
label_1 = tk.Label(window, text='Enter first number', background='#66B2FF', font='Times 15')
label_1.place(x=95, y=30)

num_entry_2 = tk.Entry(window, width=30, font='Times 10', fg='#660000') # Окно для второго числа
num_entry_2.place(x=75, y=130)
label_2 = tk.Label(window, text='Enter second number', background='#66B2FF', font='Times 15')
label_2.place(x=85, y=95)

num_entry_answer = tk.Entry(window, width=30, font='Times 10', fg='#660000') # Окно для ответа
num_entry_answer.place(x=75, y=370)
label_answer = tk.Label(window, text='Result', background='#66B2FF', font='Times 15')
label_answer.place(x=135, y=340)

window.mainloop()