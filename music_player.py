from tkinter import *
import pygame
import os



player_name = 'Music player'
root = Tk()
root.title(f'{player_name}')
root.geometry('500x300')

pygame.mixer.init()

songlist = Listbox(root, bg = 'black', fg='white', width=100, height=15)
songlist.pack()

play_btn_image = PhotoImage(file = 'play.png')
pause_btn_image = PhotoImage(file = 'pause.png')
next_btn_image = PhotoImage(file = 'next.png')
prev_btn_image = PhotoImage(file = 'previous.png')

control_frame = Frame(root)
control_frame.pack()

play_btn = Button(control_frame, image = play_btn_image, borderwidth=0)
pause_btn = Button(control_frame, image = pause_btn_image, borderwidth=0)
next_btn = Button(control_frame, image = next_btn_image, borderwidth=0)
prev_btn = Button(control_frame, image = prev_btn_image, borderwidth=0)



root.mainloop()
