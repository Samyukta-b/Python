from tkinter import *
from tkinter import messagebox
import random
from tkinter import font
import enchant

root1 = Tk()

root1.title('Cows and Bulls')
root1.geometry('800x500')

f1 = Frame(root1, bd=50)
f1.place(x=100, y=250)

f2 = Frame(root1, bg='white')
f2.place(x=200, y=80)

f3 = Frame(root1, bd=50)
f3.place(x=400, y=250)

global game
global word
chances = 10
chances_left = 10

def hb_word():

    root = Tk()
    root.title('Cows and Bulls: Words')
    root.geometry('750x600')

    frame1 = Frame(root)  # frame containing start and info button
    frame1.place(x=10, y=10)

    frame2 = Frame(root, bd=50)  # frame containing entry widget and chances left
    frame2.place(x=10, y=40)

    frame3 = Frame(root)  # frame containing cow bull
    frame3.place(x=350, y=50)

    frame4 = Frame(root, bd=20)
    frame4.place(x=10, y=500)

    label1 = Label(frame1, text="Cows and Bulls: Words", font=('MingLiU-ExtB', 20, 'bold'))
    label1.pack(pady=1)

    def lvl_buttons():
        global lvl_easy
        global lvl_hard
        startbutton.destroy()

        global chances
        chances = 10

        lvlch = Label(frame2, text='1.Easy Level: Food and Drinks\n 2.Hard Level: Random Words', font=('Helvetica', 12))
        lvlch.grid(row=1, column=0)

        lvl_easy = Button(frame2, text='Easy level', font=('Helvetica', 13), command=easy_lvl)
        lvl_easy.grid(row=2, column=0)

        lvl_hard = Button(frame2, text='Hard level', font=('Helvetica', 13), command=hard_lvl)
        lvl_hard.grid(row=3, column=0, pady=5)

    def easy_lvl():
        lvl_hard.destroy()
        lvl_easy.destroy()

        global game
        global word
        global g

        game = ['corn', 'lime', 'pear', 'rice', 'cake', 'loaf', 'date', 'plum', 'chip', 'milk', 'okra', 'coke', 'soup', 'wine', 'taco']
        word = random.choice(game)

        note = Label(frame2, text='Enter 4 letter word:', font=('Ink Free', 15), fg='#0B10AB')
        note.grid(row=4, column=0)

        g = Entry(frame2, width=5, font=('Helvetica', 15))
        g.grid(row=5, column=0, pady=10)

        root.bind('<Return>', cow_bull)

        easy = Label(frame3, text=f'Easy Level\nChances=10', font=('Helvetica', 13))
        easy.pack()

    def hard_lvl():

        lvl_hard.destroy()
        lvl_easy.destroy()

        global game
        global word
        global g

        note = Label(frame2, text='Enter 4 letter word:', font=('Ink Free', 15), fg='#0B10AB')
        note.grid(row=4, column=0)

        root.bind('<Return>', cow_bull)

        g = Entry(frame2, width=5, font=('Helvetica', 15))
        g.grid(row=5, column=0, pady=10)

        game = ['vein', 'gasp', 'cyst', 'clay', 'icon', 'phew', 'lynx', 'know', 'awry', 'lakh', 'orca', 'tofu']
        word = random.choice(game)

        hard = Label(frame3, text=f'Hard Level', font=('Helvetica', 13))
        hard.pack()

    def cow_bull(x):
        global chances
        d = enchant.Dict("en_US")

        if len(g.get()) != 4:
            messagebox.showerror("Error", 'Only 4 letter words!')

        elif not d.check(g.get()):
            messagebox.showerror("Error", 'Word entered is meaningless!')

        elif g.get() == word:
            cor = Label(frame3, text=f'YAY! You guessed correctly!\n The word is {word}', font=('Helvetica', 14))
            cor.pack()
            g.config(state="disabled")

        elif chances == 0:
            end = Label(frame3, text=f'Game over! The secret word = {word}', font=('Helvetica', 14))
            end.pack()
            g.config(state="disabled")

        else:
            chances -= 1
            cow, bull = 0, 0
            i = 0
            for x in word:
                j = 0
                i += 1
                while j < 4:
                    if x == g.get()[j]:
                        if i == (j + 1):
                            bull += 1
                        else:
                            cow += 1
                        j += 1
                    else:
                        j += 1
            count = Label(frame3, text=f'{g.get()}    Bull={bull}   Cow={cow}', font=('Ink Free', 15, 'bold'))
            count.pack()
            ch = Label(frame2, text=f'Chances Left={chances}', font=('Ink Free', 15, 'bold'),  fg='#f00030')
            ch.grid(row=6, column=0)
        g.delete(0, END)

    def info():
        messagebox.showinfo("showinfo", """Guess the four letter word. 
    You will be given two hints-Cow and Bull.
    'Cow': number of correct letters in the wrong position.
    'Bull': number of correct letter in the correct position.
    The guess word should not have repeated letters.""")

    startbutton = Button(frame1, text='Start', font=('Helvetica', 13), command=lvl_buttons)  # button to generate entry box and go button
    startbutton.pack()

    instructions = Button(frame4, text='How to Play', font=('Helvetica', 13), command=info)  # instructions are displayed
    instructions.pack(side='left', padx=10)

    exitb = Button(frame4, text="Exit", font=('Helvetica', 13), command=root.destroy)
    exitb.pack(side='left', padx=30)

    root1.destroy()
    root.mainloop()

def hb_num():

    root = Tk()
    root.title('Cows and Bulls: Numbers')
    root.geometry('600x600')

    frame1 = Frame(root)  # frame containing start and go button
    frame1.place(x=10, y=10)

    frame2 = Frame(root, bd=10)  # frame containing entry widget
    frame2.place(x=10, y=60)

    frame3 = Frame(root, bd=10)  # frame containing cow bull and chances left
    frame3.place(x=10, y=140)

    z = []  # generates a list of 4 digit numbers without repeated digits
    for x in range(1000, 9999):
        y = str(x)
        if len(y) == len(set(y)):
            z.append(y)

    s = random.choice(z)  # randomly chooses the secret number

    def entrybox():
        global e
        global chances_left
        chances_left = 10
        startbutton.destroy()

        l = Label(frame2, text='Enter a 4 digit number:', font=('Ink Free', 17, 'bold'), fg='#0B10AB')
        e = Entry(frame2, width=5, font=('Helvetica', 20))
        l.grid(row=1, column=1)
        e.grid(row=1, column=2, padx=30)
        root.bind('<Return>', cow_bull)

    def cow_bull(event):
        global chances_left
        bullcount = 0
        cowcount = 0

        if not (e.get()).isdigit():
            messagebox.showerror("Error", f'Enter a number {s}')

        elif len(e.get()) != 4:
            messagebox.showerror("Error", 'Number should be 4 digits')

        elif len(set(e.get())) != len(e.get()):
            messagebox.showerror("Error", 'Number should not contain repeated digits')

        elif e.get() == s:
            cor = Label(frame3, text=f'YOU WIN! Congratulations! The number is {s}', font=('Helvetica', 14))
            cor.pack()
            e.config(state="disabled")

        elif chances_left == 0:
            messagebox.showerror("GAME OVER!", f'GAME OVER! \nThe number is {s} ')
            e.config(state="disabled")

        else:
            chances_left -= 1

            for i in range(4):
                if (e.get()[i]) in s:
                    if e.get()[i] != s[i]:
                        cowcount += 1
                    else:
                        bullcount += 1
            counts = Label(frame3, text=f'{e.get()}         Bull = {bullcount}     Cow = {cowcount} ', font=('Ink Free', 17, 'bold'))
            counts.pack()
            chance = Label(frame2, text=f'Chances left={chances_left}', font=('Ink Free', 17, 'bold'),  fg='#f00030')
            chance.grid(row=1, column=3)

            if chances_left == 0:
                messagebox.showerror("GAME OVER!", f'GAME OVER! \nthe number is {s} ')
                e.config(state="disabled")

        e.delete(0, END)

    def info():  # instructions
        messagebox.showinfo("showinfo",
                            'Guess the 4 digit number! '
                            'Cow is the number of correct digits in the wrong position.'
                            'Bull is the number of correct digits in the correct position.')

    titlelabel = Label(frame1, text='Cow and Bull : Numbers', font=('Tempus Sans ITC', 30))
    titlelabel.pack()
    instructions = Button(root, text='Instructions', command=info, font=('Ink Free', 17))  # instructions are displayed
    instructions.place(x=10, y=545)
    startbutton = Button(root, text='Start', command=entrybox, font=('Ink Free', 17))  # button to generate entry box and go button
    startbutton.place(x=270, y=545)
    exitbutton = Button(root, text="Exit", command=root.destroy, font=('Ink Free', 17))
    exitbutton.place(x=490, y=545)
    root1.destroy()
    root.mainloop()


hb = Label(f2, text='WELCOME TO \nCOWS & BULLS!', font=('Broadway', 40))
hb.pack()

hb_w = Button(f1, text='Play with Word', height=3, width=13, font=('Ink Free', 17, 'bold'), command=hb_word)   #button to calculate the cow and bulls
hb_w.pack()

hb_n = Button(f3, text='Play with Number', height=3, width=13, font=('Ink Free', 17, 'bold'), command=hb_num)   #button to calculate the cow and bulls
hb_n.pack()

root1.mainloop()
