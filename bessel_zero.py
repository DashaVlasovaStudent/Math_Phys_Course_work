import tkinter.messagebox
import matplotlib.pyplot as plt
import scipy as sp
import numpy as np
from tkinter import *


def graph_r():
    try:
        global n_r
        global k_r
        global t_r
        n = int(n_r.get())
        k_bessel = int(k_r.get())
        t = float(t_r.get())
        t_array = np.array([0, 0.25 * t, 0.5 * t, 0.75 * t, t])
        R = 6
        r = np.linspace(0, R, n)
        l = 0.5
        k = 0.59
        c = 1.65
        alpha = 0.006
        fig, axes = plt.subplots()
        for j in range(0, 5):
            y = 0
            for i in range(1, k_bessel + 1):
                t = t_array[j]
                mu_array = sp.special.jn_zeros(0, i)
                mu = mu_array[-1]
                yi = np.exp((-((2 * alpha) / (l * k) + (mu / R) ** 2)) * (k * t / c)) * sp.special.j0(
                    mu * r / R) * sp.special.j1(
                    mu * 0.1) / (mu * (sp.special.j1(mu)) ** 2)
                y = y + yi
            y = 4 * y
            axes.plot(r, y, label="t=" + str(t))
        axes.grid()
        axes.legend()
        axes.set_xlabel("Ось r")
        axes.set_ylabel("Ось w(r,t)")
        fig.show()
    except Exception as ex:
        tkinter.messagebox.showerror(title="Error", message=ex)

def graph_t():
    try:
        global n_t
        global k_t
        global r_t
        n = int(n_t.get())
        k_bessel = int(k_t.get())
        r = float(r_t.get())
        r_array = np.array([0, 0.25 * r, 0.5 * r, 0.75 * r, r])
        T = 150
        R = 6
        t = np.linspace(0, T, n)
        l = 0.5
        k = 0.59
        c = 1.65
        alpha = 0.006
        fig, axes = plt.subplots()
        for j in range(0, 5):
            y = 0
            for i in range(1, k_bessel + 1):
                r = r_array[j]
                mu_array = sp.special.jn_zeros(0, i)
                mu = mu_array[-1]
                yi = np.exp((-((2 * alpha) / (l * k) + (mu / R) ** 2)) * (k * t / c)) * sp.special.j0(
                    mu * r / R) * sp.special.j1(
                    mu * 0.1) / (mu * (sp.special.j1(mu)) ** 2)
                y = y + yi
            y = 4 * y
            axes.plot(t, y, label="r=" + str(r))
        axes.grid()
        axes.legend()
        axes.set_xlabel("Ось t")
        axes.set_ylabel("Ось w(r,t)")
        fig.show()
    except Exception as ex:
        tkinter.messagebox.showerror(title="Error", message=ex)

root = Tk()
root['bg'] = 'pink'
root.title('График функции')
root.geometry('570x140')
root.resizable(width=False, height=False)

title_r = Label(root, text='График по r', bg='pink')
title_r.grid(row=0, column=1)
title1 = Label(root, text='количество точек графика', bg='pink')
title1.grid(row=1, column=0)
n_r = Entry(root, bg='white')
n_r.grid(row=2, column=0)

title2 = Label(root, text='количество членов ряда', bg='pink')
title2.grid(row=1, column=1)
k_r = Entry(root, bg='white')
k_r.grid(row=2, column=1)

title3 = Label(root, text='момент времени', bg='pink')
title3.grid(row=1, column=2)
t_r = Entry(root, bg='white')
t_r.grid(row=2, column=2)

button_r = Button(root, text='построить график', bg='green', command=graph_r)
button_r.grid(row=2, column=3)

# -----------------------------------------------------------------------------------------

title_t = Label(root, text='График по t', bg='pink')
title_t.grid(row=3, column=1)
title1 = Label(root, text='количество точек графика', bg='pink')
title1.grid(row=4, column=0)
n_t = Entry(root, bg='white')
n_t.grid(row=5, column=0)

title2 = Label(root, text='количество членов ряда', bg='pink')
title2.grid(row=4, column=1)
k_t = Entry(root, bg='white')
k_t.grid(row=5, column=1)

title3 = Label(root, text='расстояние', bg='pink')
title3.grid(row=4, column=2)
r_t = Entry(root, bg='white')
r_t.grid(row=5, column=2)

button_t = Button(root, text='построить график', bg='green', command=graph_t)
button_t.grid(row=5, column=3)

root.mainloop()

