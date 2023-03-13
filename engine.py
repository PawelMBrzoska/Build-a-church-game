import sqlite3
import pandas as pd
import random
from tkinter import *
from tkinter import ttk
import os
import sys

#Setting directory
os.chdir(os.path.dirname(sys.argv[0]))

def Saint_add(DB):
  #Choosing a name for a new Saint
  name = random.choice(open('data/Saint_names.txt').read().splitlines())
  who = "who "+ random.choice(open('data/Saint_who1.txt').read().splitlines()) +" "+ random.choice(open('data/Saint_who2.txt').read().splitlines())
  new_name = 'Saint ' + name
  points = random.randint(20, 200)
  conn = sqlite3.connect(DB)
  c = conn.cursor()
  c.execute("INSERT INTO Saints (name, who, points) VALUES(?,?,?)", ([new_name, who, points]))
  conn.commit() 
  conn.close()

def Saints_print(DB):
  conn = sqlite3.connect(DB)
  c = conn.cursor()
  items = c.execute("Select name, who FROM Saints")
  for i in items:
    print("the " + i[0] + " " + i[1])
  conn.commit() 
  conn.close()

def Saints_reset(DB):
  conn = sqlite3.connect(DB)
  c = conn.cursor()
  c.execute("DROP TABLE Saints")
  conn.commit()
  c.execute("""CREATE TABLE Saints (
   id INTEGER primary key AUTOINCREMENT,
   name TEXT,
   points SMALLINT,
   who TEXT)"""
   )
  conn.commit() 
  conn.close()
  
def Artifact_add(DB):
  #Choosing a name for a new Artifact
  new_name = random.choice(open('data/Art_Names1.txt').read().splitlines())+" "+random.choice(open('data/Art_Names2.txt').read().splitlines())
  that = "that "+ random.choice(open('data/Art_which1.txt').read().splitlines()) +" "+ random.choice(open('data/Art_which2.txt').read().splitlines())
  points = random.randint(50, 120)
  conn = sqlite3.connect(DB)
  c = conn.cursor()
  Saints_number=c.execute("SELECT COUNT(*) FROM Saints").fetchone()[0]
  whose = random.randint(1, Saints_number)
  c.execute("INSERT INTO Artifacts (name, that, Saint_id, points) VALUES(?,?,?,?)", ([new_name, that, whose, points]))
  conn.commit() 
  conn.close()

def Artifact_print(DB):
  conn = sqlite3.connect(DB)
  c = conn.cursor()
  items = c.execute("""Select Artifacts.name, Saints.name, Artifacts.that FROM Artifacts 
  JOIN Saints on Saints.id = Artifacts.Saint_id  
  """)
  for i in items:
    print("the "+i[1]+"'s "+i[0]+" "+i[2])
  conn.commit() 
  conn.close()

def Artifact_reset(DB):
  conn = sqlite3.connect(DB)
  c = conn.cursor()
  c.execute("DROP TABLE Artifacts")
  conn.commit()
  c.execute("""CREATE TABLE Artifacts (
   id INTEGER primary key AUTOINCREMENT,
   name TEXT,
   that TEXT,
   points SMALLINT,
   Saint_id INTEGER)"""
   )
  conn.commit() 
  conn.close()

#def Start(DB):
#  while True:
#    print("""
#    What you want to do?')
#    1 - Reset")
#    2 - add a Saint")
#    3 - add an Artifact")
#    4 - print Saints")
#    5 - print Artifacts
#    """)
#    choice = int(input('Choose: '))
#    print("  ")
#    if choice == 1:
#      Saints_reset(DB)
#      Artifact_reset(DB)
#      print("The game has been reseted")
#    if choice == 2: 
#      Saint_add(DB)
#      print("done!")
#    if choice == 3:
#      Artifact_add(DB)
#      print("done!")
#    if choice == 4:
#      Saints_print(DB)
#    if choice == 5:
#      Artifact_print(DB)


def get_ready(DB):
  Saints_reset(DB)
  Artifact_reset(DB)
  for i in range(4):
    Saint_add(DB)
  for i in range(2):
    Artifact_add(DB)
  Run_game('data/ex1.db')
  

def Run_game(DB):
  Window = Tk()
  
  def click():
    print("test")

  def click1():
    Artifact_add(DB)
    print("added a new artifact")

  def click2():
    Saint_add(DB)
    print("added a new Saint")

  def click3():
    Saints_print(DB)
  
  def click4():
    Artifact_print(DB)

  frm = ttk.Frame(Window, padding=10)
  frm.grid()

  ttk.Label(frm, text="Test").grid(column=1, row=1)

  ttk.Button(frm, text="Add an artifact", command=click1).grid(column=1, row=2)
  ttk.Button(frm, text="Add a Saint", command=click2).grid(column=1, row=3)
  ttk.Button(frm, text="Quit", command=Window.destroy).grid(column=2, row=1)
  ttk.Button(frm, text="Print Saints", command=click3).grid(column=1, row=4)
  ttk.Button(frm, text="Print Artifacts", command=click4).grid(column=1, row=5)

  Window.mainloop()

if __name__ == '__main__':
  get_ready('data/ex1.db')

  
  
