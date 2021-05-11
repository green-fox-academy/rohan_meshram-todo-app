from tkinter import *
#from wanderer.Hero import Hero
from wanderer.Hero import Hero
from wanderer.Skeleton import Skeleton
from wanderer.Boss import Boss
#from wanderer.Game_charcter import Game_charcter

#import random

#def d6():
 #   d6 = random.randint(1,6)
  #  return d6

level = 1

IMG_SIZE = 72
WIDTH = 10 * IMG_SIZE
HEIGHT = 10 * IMG_SIZE

hero = Hero()
skeleton_1 = Skeleton(9,5)
skeleton_2 = Skeleton(0,9)
skeleton_3 = Skeleton(9,0)
boss = Boss(9,9)

root = Tk()
root.title('Wanderer Game')
canvas = Canvas(root, width = WIDTH, height = HEIGHT)
canvas.pack()

list1 = [[1,1,1,1,0,1,1,1,1,1],
         [1,1,0,1,0,0,0,1,0,1],
         [1,1,0,1,0,1,1,1,0,1],
         [0,0,0,1,0,0,0,1,0,0],
         [1,1,1,1,1,1,1,1,1,1],
         [1,0,0,0,0,1,0,0,1,0],
         [1,1,1,1,0,1,0,0,1,0],
         [1,0,0,1,0,1,1,1,1,1],
         [1,0,0,1,0,1,0,0,0,1],
         [1,1,1,1,1,1,1,1,1,1]
         ]

def draw_screen():
    canvas.delete("all")
    for i in range(len(list1)):
        for j in range(len(list1)):
            if list1[i][j] == 1:
                canvas.create_image(i*IMG_SIZE, j*IMG_SIZE, image=root.floor, anchor=NW)
            else:
                canvas.create_image(i * IMG_SIZE, j * IMG_SIZE, image=root.wall, anchor=NW)
    canvas.create_image(hero.x * IMG_SIZE, hero.y * IMG_SIZE, image=getattr(root, hero.img), anchor=NW)
    canvas.create_image(skeleton_1.x * IMG_SIZE, skeleton_1.y * IMG_SIZE, image=getattr(root, skeleton_1.img), anchor=NW)
    canvas.create_image(skeleton_2.x * IMG_SIZE, skeleton_2.y * IMG_SIZE, image=getattr(root, skeleton_2.img), anchor=NW)
    canvas.create_image(skeleton_3.x * IMG_SIZE, skeleton_3.y * IMG_SIZE, image=getattr(root, skeleton_3.img), anchor=NW)
    canvas.create_image(boss.x * IMG_SIZE, boss.y * IMG_SIZE, image=getattr(root, boss.img), anchor=NW)


def load_images():
    dir = "images/"
    root.floor = PhotoImage(file=dir + "floor.png")
    root.wall = PhotoImage(file=dir + "wall.png")
    root.hero_down = PhotoImage(file=dir + "hero-down.png")
    root.hero_up = PhotoImage(file=dir + "hero-up.png")
    root.hero_right = PhotoImage(file=dir + "hero-right.png")
    root.hero_left = PhotoImage(file=dir + "hero-left.png")
    root.skeleton = PhotoImage(file=dir + "skeleton.png")
    root.boss = PhotoImage(file=dir + "boss.png")

load_images()

class attack:
    pass

class defend:
    pass

# Binding keyboard key events to functions
def leftKey(event):
    if hero.x >0:
        hero.move(x = -1)

def rightKey(event):
    hero.move(x = 1)

def upKey(event):
    hero.move(y = -1)

def downKey(event):
    hero.move(y = 1)

def spacekey(event):
    hero.attack(space= 1)
root.bind('<Left>', leftKey)
root.bind('<Right>', rightKey)
root.bind('<Up>', upKey)
root.bind('<Down>', downKey)

root.bind('<space>', spacekey)

while True:
    draw_screen()
    root.update_idletasks()
    root.update()
