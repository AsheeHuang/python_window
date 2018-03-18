import tkinter
from random import random
from math import sqrt,pow
import math

real_pi = math.pi
def dist(x1,y1,x2,y2) :
    return sqrt(pow(x1-x2,2) + pow(y1-y2,2))

if __name__ == "__main__" :
    r = 300
    total = 0
    in_circle = 0
    record_pi = 0
    tk = tkinter.Tk()
    tk.title("Pi")

    canvas = tkinter.Canvas(bg = 'black',height = 2*r,width = 2*r+2)
    circle = canvas.create_oval(0,0,2*r,2*r,fill = 'black', outline= 'white',width = 1)

    label = tkinter.Label(tk, text="" )
    label.config(bg= 'black',fg = 'white')
    label.config(width = 46)
    label.config(font=("Courier", 16))
    label.pack(side = tkinter.BOTTOM)
    while(1) :

        x = random()*2*r
        y = random()*2*r
        distance = dist(x,y,r,r) #distance from dot to frame center
        total += 1
        # print(distance,r)
        if distance >= r :
            canvas.create_oval(x - 1, y - 1, x + 1, y + 1, fill="#0AF")
        else :
            canvas.create_oval(x - 1, y - 1, x + 1, y + 1, fill="#0FA")
            in_circle += 1

        pi = 4 * (float(in_circle)/float(total))
        diff1 = abs(pi - real_pi)
        diff2 = abs(record_pi - real_pi)
        if diff2 > diff1:
            record_pi = pi
            label.config(text = "PI = "+str(pi))
            print(pi)

        canvas.pack()
        tk.update()