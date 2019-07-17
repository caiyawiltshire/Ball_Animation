ball_y = 100
ball_x = 100
ball_a = 400
ball_b = 100
y_speed = 4
x_speed = 4
a_speed = 4
b_speed = 4


def setup(): #setup runs only once
    size (500,500)
    background (128,128,128)
    
def draw(): #draw runs multiple times
    global ball_y
    global ball_x
    global ball_a
    global ball_b
    global y_speed
    global x_speed
    global a_speed
    global b_speed
    background (252, 255, 194)
    ellipse (ball_x,ball_y,100,100)
    ellipse (ball_a, ball_b,100,100)
    line (0,400,500,400)
    ball_y = ball_y + y_speed # OR ball_y += 1
    ball_x = ball_x + x_speed
    ball_a = ball_a + a_speed
    ball_b = ball_b + b_speed
    
    #Ball bouncing off top and bottom of the screen
    #1st ball
    if ball_y >= 350:
        y_speed = - y_speed
        fill(random(255),random(255), random(255))
    if ball_y <= 50:
        y_speed = - y_speed
        fill(random(255),random(255), random(255))
    if ball_x >= 450:
        x_speed = -x_speed
        fill(random(255),random(255), random(255))
    if ball_x <= 50:
        x_speed = -x_speed
        fill(random(255),random(255), random(255))
        #2nd ball
    if ball_a >= 450:
        a_speed = - a_speed
        #fill(random(255),random(255), random(255))
    if ball_a <= 50:
        a_speed = - a_speed
        #fill(random(255),random(255), random(255))
    if ball_b >= 350:
        b_speed = -b_speed
        #fill(random(255),random(255), random(255))
    if ball_b <= 50:
        b_speed = -b_speed
        #fill(random(255),random(255), random(255))
    
        
    
        
    
    
    
