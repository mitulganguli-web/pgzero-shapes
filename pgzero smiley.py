import pgzrun
from random import randint

WIDTH=300
HEIGHT=300

def draw():
    for i in range (3):
        r=255
        g=0
        b=randint(50,255)


        radius=100

        screen.draw.circle((150,150),radius,(r,g,b))
        
        radius=20
        
        screen.draw.circle((110,110),radius,(r,g,b))

        screen.draw.circle((200,110),radius,(r,g,b))

        rect=Rect((0,0),(90,20))
        rect.center=150,200
        screen.draw.rect(rect,(r,g,b))
        
pgzrun.go()