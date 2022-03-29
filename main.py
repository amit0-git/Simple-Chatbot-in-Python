from tkinter import *
import json
from PIL import ImageTk, Image


def get_ans(rr):
    with open("ans.json", "r") as f:
        data = f.read()
    data1 = json.loads(data)

    for i in data1:
        if rr.lower() == "":
            break

        elif rr.lower() == "exit":
            # destroy application
            root.destroy()

        elif rr.lower() in i['ques'].lower():
            anss = i['ans']
            t1.insert(END, rr+": "+anss+"\n")
            break

    else:
        t1.insert(END, rr+": "+"Not found!"+"\n")


root = Tk()
root.title("Chatbot")


frim = Image.open('chatbot_business_requirement.png')
frim = frim.resize((200, 100), Image.ANTIALIAS)
frimg = ImageTk.PhotoImage(frim)

canvas = Canvas(root, height=100)
canvas.grid(row=0, column=0, columnspan=2)
canvas.create_image(180, 50, image=frimg)

l1 = Label(root, text="Chatbot", font=("Arial", 30))
l1.grid(row=1, column=0, columnspan=2)

e1 = Entry(root)
e1.grid(row=2, column=0, sticky=E)

b1 = Button(root, text="Enter", command=lambda: get_ans(e1.get()))
b1.grid(row=2, column=1, sticky=W)

t1 = Text(root, font=('Arial', 10))
t1.grid(row=3, column=0, columnspan=2)

root.mainloop()
