from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from urllib.request import urlopen
import json
from tkinter import END, Image
import urllib.request
import base64
import io
from PIL import ImageTk, Image      
import time
import sys


root = tk.Tk()
root.title("Tomato_Game")
root.geometry("1240x650+50+25")
root.resizable(False, False)


class Tomato_Game:
    def __init__(self, quesn, soln):
        self.quesn = quesn
        self.soln = soln
        self.score = 0
        self.username = sys.argv[0]
        self.imagelab = tk.Label(root)
        self.imagelab.grid(padx=275, pady=120)
        self.score_res = None

        logout = Button(
            root,
            text="Log Out",
            command=self.logout_function,
            cursor="hand2",
            font=("Helvetica 15"),
            bg="red",
            fg="white",
            activebackground="white",
            bd=0,
        )
        logout.place(x=1080, y=600, width=120)

        title = Label(
            root,
            text=f"Welcome to Tomato Game",
            font=("Sans Serif", 36, "bold"),
            fg="Red",
        )
        title.place(x=360, y=30)

        title = Label(
            root,
            text="Next question in 30 seconds.",
            font=("Sans Serif", 20, "bold"),
            fg="red",
        )
        title.place(x=500, y=80)

        # Entry Input
        self.answer = Entry(root, font=("Sans Serif", 14), bg="lightgray")
        self.answer.place(x=475, y=500, width=200, height=50)

        result = Button(
            root,
            text="Submit",
            cursor="hand2",
            command=self.result_function,
            font=("Sans Serif", 14),
            bg="red",
            fg="white",
        )
        result.place(x=700, y=505, width=120)

        self.score_res = tk.Label(root, font=("Sans Serif", 16), fg="red")
        self.score_res.place(x=30, y=90)
        self.score_res.config(text=f"Total correct score  {str(self.score)}")
        self.show_image()

    # functionality

    def show_image(self):

        self.quesn, self.soln = Tomato_Game.create_image()

        with urllib.request.urlopen(self.quesn) as u:
            raw_data = u.read()
        self.image = tk.PhotoImage(data=base64.encodebytes(raw_data))
        image = Image.open(io.BytesIO(raw_data))
        self.image = ImageTk.PhotoImage(image)
        self.imagelab.config(image=self.image)
        root.after(1000 * 30, self.show_image)

    def logout_function(self):
        time.sleep(0)
        root.destroy()
        

    
        

    @staticmethod
    def create_image():
        api_url = "http://marcconrad.com/uob/tomato/api.php"
        response = urlopen(api_url)
        TomatoJson = json.loads(response.read())
        question = TomatoJson["question"]
        solution = TomatoJson["solution"]

        return question, solution

    def result_function(self):
        if self.answer.get() == "":
            messagebox.showerror("Error", "Enter a number", parent=root)
        elif self.answer.get() != str(self.soln):
            messagebox.showerror("Error", "Game Over!", parent=root)
            self.answer.delete(0, END)
        else:
            messagebox.showinfo("Success", "Correct Answer!!!!", parent=root)
            self.score += 1
            self.answer.delete(0, END)
            self.score_res.config(text=f"Your current score  is {str(self.score)}")
            self.show_image()


if __name__ == "__main__":
    quesn, soln = Tomato_Game.create_image()
    print(quesn, soln)
    img = Tomato_Game(quesn, soln)
    root.mainloop()
