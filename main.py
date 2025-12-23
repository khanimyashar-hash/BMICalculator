from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("BMI Calculator")
window.minsize(width = 350, height = 350)

def caculate_bmi():
    weight = my_entry.get()
    height = my_entry2.get()

    if height == "" or weight == "":
        result_label.config(text = "Error: Please enter both height and weight in cm!")
    else:
        try:
            bmi = float(weight) / (float(height) / 100 )** 2
            result_string = write_result(bmi)
            result_label.config(text = result_string)
        except:
            result_label.config(text = "Enter a valid number!")

#label
my_label =Label(window, text = "BMI Calculator",  font = ("Arial",15,"normal"))
my_label.config(fg = "Black")
my_label.config(padx = 20, pady = 20)
my_label.pack()

#label2
my_label2 = Label(text = "Enter your weight (kg)", font = ("Arial",13,"normal"))
my_label2.config(padx = 20, pady = 20)
my_label2.pack()

#entry
my_entry = Entry(window, width = 20)
my_entry.pack()

#label3
my_label3 = Label(text = "Enter your height (cm)", font = ("Arial",13,"normal"))
my_label3.config(padx = 20, pady = 20)
my_label3.pack()

#entry2
my_entry2 = Entry(window, width = 20)
my_entry2.pack()

#button
my_button = Button(text = "Calculate BMI", font = ("Arial",13,"normal"), command = caculate_bmi)
my_button.config(bg = "green", fg = "white")
my_button.config(padx = 20, pady = 20)
my_button.pack(pady = 20)

#resultLabel
result_label = Label()
result_label.pack()

def write_result(bmi):
    result_string = f"Your BMI is: {round(bmi,2)}. You are"
    if bmi <= 16:
        result_string += " severely thin ! "
    elif 16 < bmi <= 17:
        result_string += " moderately thin! "
    elif 17 < bmi <= 18.5:
        result_string += " mild thin! "
    elif 18.5 < bmi <= 25:
        result_string += " normal! "
    elif 25 < bmi <= 30:
        result_string += " overweight! "
    elif 30 < bmi <= 35:
        result_string += " obese class 1"
    elif 35 < bmi <= 40:
        result_string += " obese class 2"
    else:
        result_string += " obese class 3"
    return result_string

window.mainloop()