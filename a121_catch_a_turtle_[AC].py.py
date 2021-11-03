#-----import statements-----
import random as rand
import turtle as trtl
spot = trtl.Turtle()
import turtle as score_writer
counter=trtl.Turtle()
wn=trtl.Screen()
spot.showturtle()
spot.shape("circle")
# spot.shapesize(2)
spot.color("red")
spot.speed(8)
score = 0

font_setup = ("Helvetica", 20, "normal")
#def update_score():
different_sizes = [.5, .7, .9, 1.2, 1.4, 1.6, 1.8, 2]
def clicked(x, y):
    size = rand.randint(0,7)
    spot.shapesize(different_sizes[size])
    global score
    score += 1
    new_xpo = rand.randint(-380,380)
    new_ypo = rand.randint(-280,280)
    spot.penup()
    spot.goto(new_xpo, new_ypo) 
    #update_score
    score_writer.clear()
    score_writer.goto(-300,200)
    score_writer.write("score: ", font=font_setup)
    score_writer.goto(-220,200)
    score_writer.write(score, font=font_setup)
def countdown():
  global timer, timer_up
  counter.clear()
  counter.penup()
  counter.hideturtle()
  counter.goto(150,200)
  if timer <= 0:
    counter.write("times up",font=font_setup)
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

spot.onclick(clicked)


#timer shower(was on textbook)
score_writer.penup()
timer = 20
counter_interval = 1000   
timer_up = False
score_writer.penup()
score_writer.hideturtle()

wn.bgcolor("green")
wn.ontimer(countdown, counter_interval)
wn = trtl.Screen()
wn.mainloop()