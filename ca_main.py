# -*- coding: iso-8859-1 -*-
from PIL import Image, ImageDraw
from random import randint
import sys

def iterate(calist, rule):
    '''updates calist based on rule ( left XOR right here )'''
    temp = len(calist)*[0]
    n = len(calist)

    rule = bin(rule)
    rule = rule.lstrip('0b')
    rule = rule.zfill(8)

    for i in range(1,n-1):

        if   (calist[i-1:i+2] == [0,0,0]):
            temp[i] = int(rule[7])
        elif (calist[i-1:i+2] == [0,0,1]):
            temp[i] = int(rule[6])
        elif (calist[i-1:i+2] == [0,1,0]):
            temp[i] = int(rule[5])
        elif (calist[i-1:i+2] == [0,1,1]):
            temp[i] = int(rule[4])
        elif (calist[i-1:i+2] == [1,0,0]):
            temp[i] = int(rule[3])
        elif (calist[i-1:i+2] == [1,0,1]):
            temp[i] = int(rule[2])
        elif (calist[i-1:i+2] == [1,1,0]):
            temp[i] = int(rule[1])
        elif (calist[i-1:i+2] == [1,1,1]):
            temp[i] = int(rule[0])
    return temp


def run_ca(rule, size, rand_seed):

    arr = []

    #size = 20
    
    if rand_seed:
        calist = [randint(0,1) for _ in range(size)]
    else:
        calist = [0]*size
        calist[size//2] = 1

    for i in range(size//2):
        arr.append(calist)
        #if i < 5:
        #    p(calist)
        calist = iterate(calist, rule)
        
        print(str(i) + ' ', end='')

    draw_ca(rule, arr, size)

def p(calist):
    '''This function prints calist with 'A' for 1 and ' ' for 0 value.''' 
    print('')
    for each in calist:
       if each == 1:
           print('.', end=''),
       else:
           print(' ', end=''),

def draw_ca(rule, arr, size):

    print('\nnow drawing')
    
    # scale factor:
    s = 4 
    
    img = Image.new("RGB", (size*s, size//2*s), "white")
    draw = ImageDraw.Draw(img)

    y = 0

    for row in arr:
        print(str(y//s) + ' ', end='')

        y = y + s
        x = 0

        for column in row:

            x = x + s

            if column == 1:
                #print(str(x) + ' ' + str(y))
                #self.cv.create_line(x, y, x + 1, y, fill = 'black')
                draw.rectangle(((x, y), (x+s-1, y+s-1)), fill="black")
                #draw.point((x,y), fill="black")

    # save picture
    #self.cv.postscript(file="mylines.ps", colormode='color')
    img.save(str(rule) + '_' + str(size) + '_' + str(randint(0,1234)) + ".png", "PNG")


def start_ca (text):
    if text.isdigit():
        if 0 <= int(text) < 256:
            run_ca(int(text))
    else:
        print(text + ' is not a number')



if __name__ == "__main__":
    
    a = sys.argv
    print(a)
    #app = simpleapp_tk(None)
    #app.title('my application')
    #run_ca(75, 2000, 1)
    run_ca(int(a[1]), int(a[2]), int(a[3]))
    #app.mainloop()
