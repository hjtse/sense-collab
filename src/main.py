from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
sense.clear()

#Set color values
r = (255,0,0)
g = (100,0,200)
#g = (0,255,0)
b = (0,0,0)
o = (255, 255, 0)
w = (255,255,255)

#Initiate variables
x = 0
y = 0

pos = 2
time = 0
limit = 10

x_win = randint(0,7)
y_win = randint(0,7)

#Basic start screen
init_maze = [[b,b,b,b,b,b,b,b],
		[b,b,b,b,b,b,b,b],
		[b,b,b,b,b,b,b,b],
		[b,b,b,b,b,b,b,b],
		[b,b,b,b,b,b,b,b],
		[b,b,b,b,b,b,b,b],
		[b,b,b,b,b,b,b,b],
		[b,b,b,b,b,b,b,b]]

maze = init_maze


#Animations for crash
explode1 = [[w,w,w,r,w,w,w,w],
			[w,w,r,r,r,w,w,w],
			[w,r,r,r,o,r,w,w],
			[w,r,o,o,o,o,r,r],
			[r,r,o,r,r,o,r,r],
			[r,r,o,o,r,o,r,r],
			[w,r,r,o,o,r,r,w],
			[w,w,r,r,r,r,r,w]]

explode2 = [[w,w,w,w,w,r,w,w],
			[w,w,w,r,r,r,w,w],
			[w,w,r,r,o,o,r,w],
			[w,r,r,o,o,o,r,r],
			[r,r,r,o,r,o,r,r],
			[r,r,r,o,r,o,r,r],
			[w,r,r,r,o,r,r,w],
			[w,w,r,r,r,r,r,w]]

def move_marble(pitch,roll,x,y):
	new_x = x
	new_y = y
	if 1 < pitch < 179 and x != 0:
		new_x -= 1
	elif 359 > pitch > 179 and x != 7 :
		new_x += 1
	if 1 < roll < 179 and y != 7:
		new_y += 1
	elif 359 > roll > 179 and y != 0 :
		new_y -= 1
	x,y = check_wall(x,y,new_x,new_y)
	return x,y


def check_wall(x,y,new_x,new_y):
#    if maze[new_y][new_x] != g:
#        return new_x, new_y
#    elif maze[new_y][x] != g:
#        return x, new_y
#    elif maze[y][new_x] != g:
#        return new_x, y
	return new_x,new_y

'''
def check_lose():
	#move player down if caught by wall
#    if maze[y][x] == g:
#        y += 1
	#if player is pushed offscreen or hits a red dot, end game
	if time == 100:
		sense.set_pixels(sum(explode1,[]))
		sleep(.75)
		sense.set_pixels(sum(explode2,[]))
		sleep(.75)
		sense.show_message("YOU LOSE!!!", scroll_speed=.04)
		sense.show_message("YOU LOSE!!!", scroll_speed=.04)
#        sense.show_message(str(time/10), scroll_speed=0.2, text_colour=[0,0,255])
		#wait for joystick input before starting new game
		sense.stick.wait_for_event()
		x,y = reset(x, y)
	return x, y
'''

def check_win(x,y):
	#if player is on winning spot
	if x == x_win and y == y_win:
		sense.set_pixels(sum(explode1,[]))
		sleep(.75)
		sense.set_pixels(sum(explode2,[]))
		sleep(.75)
		sense.show_message("Score:", scroll_speed=.04)
		sense.show_message(str(100-time/10), scroll_speed=0.2, text_colour=[0,0,255])
		#wait for joystick input before starting new game
		sense.stick.wait_for_event()
		x,y = reset(x,y)
	#if player runs out of time
	elif time == 100:
		sense.set_pixels(sum(explode1,[]))
		sleep(.75)
		sense.set_pixels(sum(explode2,[]))
		sleep(.75)
		sense.show_message("YOU LOSE !!!", scroll_speed=.04)
		sense.show_message("YOU LOSE !!!", scroll_speed=.04)
		#wait for joystick input before starting new game
		sense.stick.wait_for_event()
		x,y = reset(x,y)
	return x,y

def reset(x,y):
	global pos, time, limit, maze, x_win, y_win
	x = 0
	y = 0
	pos = 2
	time = 0
	limit = 10
	x_win = randint(0,7)
	y_win = randint(0,7)
	maze = [[b,b,b,b,b,b,b,b],
		[b,b,b,b,b,b,b,b],
		[b,b,b,b,b,b,b,b],
		[b,b,b,b,b,b,b,b],
		[b,b,b,b,b,b,b,b],
		[b,b,b,b,b,b,b,b],
		[b,b,b,b,b,b,b,b],
		[b,b,b,b,b,b,b,b]]
	return x,y

def add_turn(pos, maze): 
	#three possible ways for tunnel to go: left, right, straight
	direction = randint(1, 3)
	#randomly place red dots
#    obstacle = randint(1, 15)
	#move tunnel left or right as long as it doesn't make it go off screen
#    if direction == 1:
#        pos = max(0, pos - 1)
#    elif direction == 2:
#        pos = min(3, pos + 1)
	##new row goes at top, put in red dots and blanks
#    new_row = [g,g,g,g,g,g,g,g]
#    new_row[pos + 1] = (r if obstacle == 1 else b)
#    new_row[pos + 2] = (r if obstacle == 2 else b)
#    new_row[pos + 3] = (r if obstacle == 3 else b)
#    maze.insert(0, new_row)
	##remove last row
#    maze.pop()
	return pos,maze


while True:
	pitch = sense.get_orientation()['pitch']
	roll = sense.get_orientation()['roll']
	x,y = move_marble(pitch, roll, x, y)
	#limit determines speed - starts at 10 and moves down every 100 cycles
#    if time % limit == 0:
#		pos,maze = add_turn(pos, maze)
#    if time % 100 == 0:
#        limit = max (1, limit - 1)
#    print "Your location: ", x, y
#    print "Winning location: ", x_win, y_win
	x,y = check_win(x, y)
	maze[y_win][x_win] = g
	maze[y][x] = w
	sense.set_pixels(sum(maze,[]))
	sleep(0.10)
	time += 1
	#clear previous player location
	maze[y][x] = b
