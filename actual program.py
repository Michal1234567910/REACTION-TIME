from ctypes.wintypes import SIZE
from pyclbr import Function
from tkinter import Button
from turtle import bgcolor
from guizero import *
import random
import time  
import pickle
def start():
    global startstart, waffle, a, b, start_timetime, timetimetime
    app.hide()
    game.show()
    ben.hide()

    start_timetime = time.time()
    a = random.randint(0,8)
    b = random.randint(0,8) 
    startstart.after(timetimetime, show)

    
def xy(x,y):
    global a,b,what_to_say,text,start_timetime,total_time, timetimetime
    if a == x and b == y:
        
        end_timme = time.time()
        total_time = end_timme - start_timetime
        new_rounded_time = total_time-timetimetime/1000
        rounded_time = round(new_rounded_time,2)
        text.value = "good job, your time was " + str(rounded_time)
        leaderboard.show()
        age.show()
        waffle.hide()
        agetext.show()
        ben.show()

    else:
        text.value = "try again"  

def endend():
    
    game.hide()
    app.show()
    leaderboard_real()

def show():
    global a,b
    waffle.pixel(a,b).color = "green"

def leaderboard_real():
    global total_time, leaderboard_times, age, ben
    i = 0
    old_rounded_time = round(total_time,2)
    rounded_time = old_rounded_time-3
    for i in range(len(leaderboard_times)):
        if rounded_time < leaderboard_times[i][0]:
            new_rounded_time = [rounded_time, ben.value , age.value]
            leaderboard_times.insert(i, new_rounded_time)
            save_oliver()
            print (leaderboard_times)
            print (leaderboard_times[0][0])
            print ("hello")
            restart()
            break
        else:   
            i += 1
            print (leaderboard_times)
            print (i)

def restart():
    global a,b,start_timetime,total_time,ben
    start_timetime = 0
    total_time = 0
    age.hide()
    ben.hide()
    waffle.show()
    waffle.pixel(a,b).color ="white"
    ben.value =""

def open_oliver():
    global leaderboard_times
    try:
        with open("test.pickle","rb") as infile:
            leaderboard_times = pickle.load(infile)
    except FileNotFoundError:
        pass

def save_oliver():
    try:
        with open ("test.pickle", "wb") as outfile:
            pickle.dump (leaderboard_times,outfile)
    except FileNotFoundError:
        pass


        
def show_leaderboard():
    global leaderboard_text_1, leaderboard_value, leaderboard_text_2
    print (leaderboard_value)
    
    i = 0 
    for i in range (len(leaderboard_times)):
        
        reversed_time = leaderboard_times.reverse 
        if leaderboard_times [i][2] == leaderboard_value:
            print (leaderboard_times [i][2], leaderboard_value)
            rounder_leader_times = round(leaderboard_times[i][0],2)
            leaderboard_text_1.value = "the best time was " + str(rounder_leader_times) + " scored by " +  str(leaderboard_times[i][1])
            break
        
        
    
        else:
            pass
        

    
def leaderboard_value_real():
    global leaderboard_value
    print ("a")
    leaderboard_app.show()
    leaderboard_value = leaderboard_slider.value
    show_leaderboard()

    
def age():
    age = leaderboard_slider.value



leaderboard_times = []
open_oliver()
print("Leaderboard after reloading", leaderboard_times)
app = App(title="main app", width="2560", height="1440")
app.set_full_screen()
app.bg = "#E0A2AB"
game = Window(app, title="main menu",width=2560,height=1440)
game.set_full_screen()
picture = Picture(app, image="test.gif",) 
game.bg ="#E0A2AB"
leaderboard_app = Window(app, title="leaderboard", width=2560,height=1440)
leaderboard_app.bg="#E0A2AB"
leaderboard_app.set_full_screen()
leaderboard_app.hide()
a = 0
b = 0
start_timetime = 0
total_time = 0
game.hide()

text = Text(game,text="start")    
leaderboard =  PushButton(game, text="add time to leaderboard",command=endend, align="top", width = 20)
leaderboard.bg="#9FDEED"
leaderboard.hide() 
leaderboard_box = Box(app, align="bottom",height=150,width="20") 
ben = TextBox(game, width=100 , height="40")  
agetext = Text(game,align="top",text="Age?")
age = Slider(game, align="top",width=400,end=18,start=10)
age.bg ="#9FDEED"
waffle = Waffle(game,height=9 , width=9, pad=60, command=xy)
leaderboard_box_1 = Box(leaderboard_app,height=30,width=1,align="top")
leaderboard_slider = Slider(leaderboard_app,align="top", start=10, end=18)
leaderboard_slider.when_left_button_released = leaderboard_value_real
leaderboard_value = 0
leaderboard_box_3 = Box(leaderboard_app, align="top",height=2,width=400, border=20)
leaderboard_text_1 = Text(leaderboard_app, text ="nothig here")
leaderboard_box_3 = Box(leaderboard_app, align="top",height=2,width=400, border=20)

leaderboard_button = PushButton(app,text="leaderboard",command = leaderboard_value_real,align="bottom", width = 20, height= 4)
box_uno = Box(app,width=650,height=10, align="left")
startstart = Picture(app, image="start.gif",align="left")
startstart.when_clicked = start 

agetext.hide()
age.hide()
timetimetime = random.randint(1000, 5000)
app.display()
