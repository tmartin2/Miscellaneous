import random
import math 
import sys
import time


# these are the lists for the holes 
# x,       y,       radius,  value,   score-sheet
# list[0]  list[1]  list[2]  list[3]  list[5]
# score sheet is 0 because we want to increment it
top = [24,5,4,40,0]
mid = [24,26,5,30,0] 
bot = [24,38,6,20,0]
big = [24,38,18,10,0]


simulating = True  
while simulating:
    getting_input = True
    while getting_input:
        print("Remember to press the letter ""\"q""\" if you'd like to exit.\n")
        try:
            balls = input("How many throws would you like to simulate?: ")
            if str(balls) == 'q':
                sys.exit()
            elif int(balls) < 1:
                raise Exception("Sorry, that's too few balls")
            else:
                balls = int(balls)
                getting_input = False
        except Exception as error_message:
            print(error_message)
            continue
    start_time = time.time()
    thrown_balls = 0
    misses = 0
    while thrown_balls < balls:
        x_cord = random.randint(0,48)
        y_cord = random.randint(0,60)
        top_dist = math.sqrt( (x_cord - top[0])**2  +  (y_cord - top[1])**2 )
        mid_dist = math.sqrt( (x_cord - mid[0])**2  +  (y_cord - mid[1])**2 )
        bot_dist = math.sqrt( (x_cord - bot[0])**2  +  (y_cord - bot[1])**2 )
        big_dist = math.sqrt( (x_cord - big[0])**2  +  (y_cord - big[1])**2 )
        if top_dist < top[2]: top[4] += 1
        if mid_dist < mid[2]: mid[4] += 1
        if bot_dist < bot[2]: bot[4] += 1
        if big_dist < big[2] and bot_dist > bot[2] and mid_dist > mid[2]:
            big[4] += 1
        if top_dist > top[2] and big_dist > big[2]:
            misses += 1
        thrown_balls += 1
    output = (
    f"\nDone!\nExecution time: {round((time.time() - start_time),2)} secs\n\n"
    f"* Total throws:  {balls}{' '*3}{(balls/balls)*100}%\n"
    f"* Misses:        {misses}{' '*((len(str(balls))+3)-len(str(misses)))}{round((misses/balls),3)*100}%\n"
    f"* 10 points:     {big[4]}{' '*((len(str(balls))+3)-len(str(big[4])))}{round((big[4]/balls),2)*100}%\n"
    f"* 20 points:     {bot[4]}{' '*((len(str(balls))+3)-len(str(bot[4])))}{round((bot[4]/balls),2)*100}%\n"
    f"* 30 points:     {mid[4]}{' '*((len(str(balls))+3)-len(str(mid[4])))}{round((mid[4]/balls),2)*100}%\n"
    f"* 40 points:     {top[4]}{' '*((len(str(balls))+3)-len(str(top[4])))}{round((top[4]/balls),2)*100}%\n"
    )
    print(output)
    
    



            



 
