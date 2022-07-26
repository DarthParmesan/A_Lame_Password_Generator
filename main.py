from gui import *
import sys
import os

os.chdir(sys._MEIPASS)
os.system('data/list_a.txt')
os.system('data/list_b.txt')
os.system('data/countries.txt')

if __name__ == '__main__':
    win = gui()
    win.run()

