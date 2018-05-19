from tkinter import *
import random



def main():
    global GAME
    if GAME:
        s.moving()
        coords_head = c.coords(s.parts[-1].example)
        x1, y1, x2, y2 = coords_head
        if x2 > WIDTH or x1 < 0 or y1 < 0 or y2 > HEIGHT:
            GAME = False
        
        elif coords_head == c.coords(APPLE):# Eating apples
            s.add()
            c.delete(APPLE)
            creating_apple()
        
        else:
            for i in range(len(s.parts)-1):
                if coords_head == c.coords(s.parts[i].example):
                    GAME = False
        root.after(100, main)
    
    else:#stop game
        c.create_text(WIDTH/2, HEIGHT/2,
                      text="GAME OVER!",
                      font="Arial 20",
                      fill="yellow")


def creating_apple():
    global APPLE
    posx = PART_SIZE * random.randint(1, (WIDTH-PART_SIZE) / PART_SIZE)
    posy = PART_SIZE * random.randint(1, (HEIGHT-PART_SIZE) / PART_SIZE)
    APPLE = c.create_oval(posx, posy,
                          posx+PART_SIZE, posy+PART_SIZE,
                          fill="red")





class Snake_part(object):
    def __init__(self, x, y):
        self.example = c.create_rectangle(x, y,
                                           x+PART_SIZE, y+PART_SIZE,
                                           fill="green")


class Snake(object):
    def __init__(self, parts):
        self.parts = parts
        self.possition = {"Down": (0, 1), "Right": (1, 0),"Up": (0, -1), "Left": (-1, 0)}
        self.begin = self.possition["Right"]

    def add(self):
        fin_part = c.coords(self.parts[0].example)
        x = fin_part[2] - PART_SIZE
        y = fin_part[3] - PART_SIZE
        self.parts.insert(0, Snake_part(x, y))


    def change_vector(self, event):
        if event.keysym in self.possition:
            self.begin = self.possition[event.keysym]
    def moving(self):
        for i in range(len(self.parts)-1):
            part = self.parts[i].example
            x1, y1, x2, y2 = c.coords(self.parts[i+1].example)
            c.coords(part, x1, y1, x2, y2)

        x1, y1, x2, y2 = c.coords(self.parts[-2].example)
        c.coords(self.parts[-1].example,
                 x1+self.begin[0]*PART_SIZE, y1+self.begin[1]*PART_SIZE,
                 x2+self.begin[0]*PART_SIZE, y2+self.begin[1]*PART_SIZE)

    

root = Tk()
root.title("Win_Snake!")

GAME = True
HEIGHT = 650
WIDTH = 900
PART_SIZE = 25

c = Canvas(root, width=WIDTH, height=HEIGHT, bg="#F4C430")
c.grid()
c.focus_set()

parts=[Snake_part(PART_SIZE, PART_SIZE),
            Snake_part(PART_SIZE*2, PART_SIZE),
            Snake_part(PART_SIZE*3, PART_SIZE),
            Snake_part(PART_SIZE*4, PART_SIZE)]
s = Snake(parts)
c.bind("<KeyPress>", s.change_vector)

creating_apple()
main()
root.mainloop()


