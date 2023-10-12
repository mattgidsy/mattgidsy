import turtle

wn = turtle.Screen()

screen_color = input('what color screen would you like?\n')
turtle_color = input('what color turtle would you like?\n')
turtle_size = input('how big do you want that turtle? (0-10)\n')
turtle_name = input('what should we name your turtle?\n')
turtle_str = turtle_name

wn.bgcolor(screen_color)        # set the window background color

turtle_name = turtle.Turtle()
turtle_name.color(turtle_color)              # make tess blue
turtle_name.pensize(turtle_size)                 # set the width of her pen

def draw_square(self):
    turn = 4
    while turn > 0:
        self.forward(150)
        self.left(90)
        turn -= 1
def curve(self):
    for i in range(200):
        # Defining step by step curve motion
        self.right(1)
        self.forward(1)
def draw_heart(self):
    self.left(120)
    self.forward(113)
    curve(self)
    self.left(120)
    curve(self)
    self.forward(112)

def txt(self):
  
  
    turtle_name.up()
    turtle_name.setpos(-68, -100)
    turtle_name.down()
    # Write the specified text in 
    # specified font style and size
    turtle_name.write("I love you", font=(
      "Arial", 24))
        

    
draw_heart(turtle_name)
txt(turtle_name)
print(turtle_str, "made you a drawing")
wn.exitonclick()                # wait for a user click on the canvas