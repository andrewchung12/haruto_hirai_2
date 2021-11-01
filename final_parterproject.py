#import turtles
import random as rand
import turtle as trtl
spot = trtl.Turtle()
score_writer = trtl.Turtle()
counter =  trtl.Turtle()

#set up fonts and score value
score = 0
font_setup = ("Helvetica", 20, "normal")
spot.hideturtle()
wn = trtl.Screen()
wn.addshape('halloween_picture.gif')
trtl.shape('halloween_picture.gif')
spot.speed(8)

#add shapes for images
wn.addshape('bats.last.gif')
wn.addshape('ghost.gif')
wn.addshape('final_pumpkin.gif')
wn.addshape('start.gif')

#list of shapes and angles
shape_list = ['ghost.gif','ghost.gif','ghost.gif','ghost.gif', 'ghost.gif', 'ghost.gif', 'bats.last.gif', 'final_pumpkin.gif', 'final_pumpkin.gif']
angle_list = [20, 40, 60, 80, 100, 120, 140, 160]

#if right clicked, you get 0 score and skip the object
def right_click(x,y):
  global score
  score +=0
  score_writer.clear()
  score_writer.hideturtle()
  score_writer.goto(-300,200)
  score_writer.write("Score: ", font=font_setup)
  score_writer.goto(-220,200)
  score_writer.write(score, font=font_setup)
  clicked(x,y)

#pumpkin will reset the score
def pumpkin_score(x,y):
  global score
  score -= score
  score_writer.clear()
  score_writer.hideturtle()
  score_writer.goto(-300,200)
  score_writer.write("Score: ", font=font_setup)
  score_writer.goto(-220,200)
  score_writer.write(score, font=font_setup)
  clicked(x,y)

#bat will give you 1 additional score for bonus
def bat_score(x,y):
  global score
  score += 2
  score_writer.clear()
  score_writer.hideturtle()
  score_writer.goto(-300,200)
  score_writer.write("Score: ", font=font_setup)
  score_writer.goto(-220,200)
  score_writer.write(score, font=font_setup)
  clicked(x,y)

#the gost is the normal score(gives 1 score)
def ghost_score(x,y):
  global score
  score += 1
  score_writer.clear()
  score_writer.hideturtle()
  score_writer.goto(-300,200)
  score_writer.write("Score: ", font=font_setup)
  score_writer.goto(-220,200)
  score_writer.write(score, font=font_setup)
  clicked(x,y)

#when it's clicked it will move the turtle to random cordinates (add random angle change later ask teacher)
def clicked(x, y):
  random_shape = rand.randint(0, 8)
  spot.shape(shape_list[random_shape])
  new_xpo = rand.randint(-250,250)
  new_ypo = rand.randint(-140,200)
  spot.penup()
  spot.goto(new_xpo, new_ypo) 
  spot.pendown()
  '''angles = rand.randint(0, 7)
  spot.setheading(angle_list[angles])'''
  #depending on the shape, it will score differently by using the functions
  if random_shape <6:
    spot.onclick(ghost_score)
  elif random_shape == 6:
    spot.onclick(bat_score)
  elif random_shape >6:
    spot.onclick(pumpkin_score)

#displays countdown and end screen
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    wn.addshape('times_upp.gif')
    trtl.shape('times_upp.gif')
    spot.hideturtle()
    spot.clear()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
    
spot.penup()
spot.goto(-100,-300)
spot.write("Bats= +2", font=font_setup)
spot.goto(-120, -350)
spot.write("Ghosts= +1", font=font_setup)
spot.goto(-180,-400)
spot.write("Pumpkin = Resets Score", font=font_setup)
spot.showturtle()

#starting shape is the botton
spot.goto(0,0)
spot.shape('start.gif')

#add random angle changes (ask teacher.)
spot.onclick(clicked, btn=1, add=None)
spot.onclick(right_click, btn=3, add=None)

#timer shower(was on textbook)
score_writer.penup()
timer = 20
counter_interval = 1000   
timer_up = False
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(-150,200)

counter.hideturtle()
counter.penup()
counter.goto(193,200)

#screen
wn.ontimer(countdown, counter_interval) 
wn.mainloop()