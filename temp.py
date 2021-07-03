import cv2
import random

imgCookie = cv2.imread('cookie.png')   #Loading Images

imgHeart = cv2.imread("heart.png")

imgBroc = cv2.imread('art.png')

cam = cv2.VideoCapture(1)    #Setting screne display. dont need for pynq board
cam.set(3, 1980)
cam.set(4, 1080)

frame_count = 0   #used to create retro looking speed

cookie_point_across_one = random.randint(50, 1770)   #spawn in objects
cookie_point_across_two = random.randint(50,1770)
cookie_point_across_three = random.randint(50,1770)
broc_point_across_one = random.randint(50,1770)
broc_point_across_two = random.randint(50,1770)

        
allgood = True
        
while(allgood):
    if abs(cookie_point_across_two-cookie_point_across_one) < 75:   #checking no collisions between cookies
        cookie_point_across_two = random.randint(50,1770)
    if abs(cookie_point_across_one-cookie_point_across_three) < 75:
        cookie_point_across_three = random.randint(50,1770)
    elif abs(cookie_point_across_two-cookie_point_across_three) < 75:
        cookie_point_across_three = random.randint(50,1770)
    else:
        allgood = False
            
allgood = True

while(allgood):   #checking no collisions between cookies and broc
    if abs(broc_point_across_one-cookie_point_across_one) < 75 or abs(broc_point_across_one-cookie_point_across_two) < 75 or abs(broc_point_across_one-cookie_point_across_three) < 75:
        broc_point_across_one = random.randint(50,1770)
    if abs(broc_point_across_two-cookie_point_across_one) < 75 or abs(broc_point_across_two-cookie_point_across_two) < 75 or abs(broc_point_across_two-cookie_point_across_three) < 75:
        broc_point_across_two = random.randint(50,1770)
    elif abs(broc_point_across_two-broc_point_across_one) < 75:
        broc_point_across_two = random.randint(50,1770)
    else:
        allgood = False
            
cookie_point_down_one = 0    #spawning cookies at the top
cookie_point_down_two = 0   
cookie_point_down_three = 0
broc_point_down_one = 0
broc_point_down_two = 0
#lower is faster
cookie_speed = 6    
lives_one = 3
lives_two = 3
score_one = 0
score_two = 0

player_one_x = 70
player_one_y = 600         #these will change with inputs from the cpp code
player_one_length = 300

player_two_x = 1300
player_two_y = 600
player_two_length = 300

while(True):
    
    ret_val, frame = cam.read()    #takes camera in
    
    #setting up the two players
     
    player_one_x_end =  player_one_x+player_one_length       
    player_two_x_end =  player_two_x+player_two_length
    
    player_one_middle = player_one_x+(0.5*player_one_length)
    player_two_middle = player_two_x+(0.5*player_two_length)
         
    cv2.line(frame,(player_one_x, player_one_y), (player_one_x_end, player_one_y), (255,0,0), 2)    #don't have these in final game
    cv2.line(frame,(player_two_x, player_two_y), (player_two_x_end, player_two_y), (0,0,255), 2)    #will have puppets, just for testing
    
    #Setting up variables for dimensions of objects
    
    cookie_h, cookie_w, cookie_c = imgCookie.shape
    broc_h, broc_w, broc_c = imgBroc.shape
    
    broc_bottom_one = broc_point_down_one + broc_h
    broc_bottom_two = broc_point_down_two + broc_h
    
    broc_left_one = broc_point_across_one + broc_w
    broc_left_two = broc_point_across_two + broc_w
    
    cookie_bottom_one = cookie_h + cookie_point_down_one
    cookie_bottom_two = cookie_h + cookie_point_down_two
    cookie_bottom_three = cookie_h + cookie_point_down_three
    
    cookie_left_one = cookie_point_across_one + cookie_w
    cookie_left_two = cookie_point_across_two + cookie_w
    cookie_left_three = cookie_point_across_three + cookie_w
    
    cookie_middle_y_one = cookie_bottom_one-(0.5*cookie_h)
    cookie_middle_y_two = cookie_bottom_two-(0.5*cookie_h)
    cookie_middle_y_three = cookie_bottom_three-(0.5*cookie_h)
    
    cookie_middle_x_one = cookie_point_across_one+(0.5*cookie_w)
    cookie_middle_x_two = cookie_point_across_two+(0.5*cookie_w)
    cookie_middle_x_three = cookie_point_across_three+(0.5*cookie_w)
    
    #Setting up Collisions with player_one
    
    broc_coll_one = False
    broc_coll_two = False

    if (cookie_point_across_one) >= (player_one_x-40) and (cookie_left_one) <= (player_one_x_end+40) and abs(cookie_bottom_one-player_one_y) <= 15 :
        score_one = score_one + 10
        cookie_point_down_one = 0
        if lives_one > 0 and lives_two > 0:
            cookie_point_across_one = random.randint(50,1770)
            allgood = True
            while(allgood):
                if abs(cookie_point_across_one-cookie_point_across_two) > 75 and abs(cookie_point_across_one-cookie_point_across_three) > 75:
                    allgood = False
                else:
                    cookie_point_across_one = random.randint(50,1770)

    if (cookie_point_across_two) >= (player_one_x-40) and (cookie_left_two) <= (player_one_x_end+40) and abs(cookie_bottom_two-player_one_y) <= 15 :
        score_one = score_one + 10
        cookie_point_down_two = 0
        if lives_one > 0 and lives_two > 0:
            cookie_point_across_two = random.randint(50,1770)
            allgood = True
            while(allgood):
                if abs(cookie_point_across_two-cookie_point_across_one) > 75 and abs(cookie_point_across_two-cookie_point_across_three) > 75:
                    allgood = False
                else:
                    cookie_point_across_two = random.randint(50,1770)
                    
    if (cookie_point_across_three) >= (player_one_x-40) and (cookie_left_three) <= (player_one_x_end+40) and abs(cookie_bottom_three-player_one_y) <= 15 :
        score_one = score_one + 10
        cookie_point_down_three = 0
        if lives_one > 0 and lives_two > 0:
            cookie_point_across_threed = random.randint(50,1770)
            allgood = True
            while(allgood):
                if abs(cookie_point_across_three-cookie_point_across_one) > 75 and abs(cookie_point_across_three-cookie_point_across_two) > 75:
                    allgood = False
                else:
                    cookie_point_across_three = random.randint(50,1770)
                    
    if (broc_point_across_one) >= (player_one_x-40) and (broc_left_one) <= (player_one_x_end+40) and abs(broc_bottom_one-player_one_y) <= 15 :
        lives_one = lives_one - 1
        broc_point_down_one = 0
        allgood = True
        broc_coll_one = True
        while(allgood):
            broc_point_across_one = random.randint(50,1770)
            if abs(broc_point_across_one-cookie_point_across_one) > 75 and abs(broc_point_across_one-cookie_point_across_two) > 75 and abs(broc_point_across_one-cookie_point_across_three) > 75:
                allgood = False
            else:
                broc_point_across_one = random.randint(50,1770)
                
    if (broc_point_across_two) >= (player_one_x-40) and (broc_left_two) <= (player_one_x_end+40) and abs(broc_bottom_two-player_one_y) <= 15 :
        lives_one = lives_one - 1
        broc_point_down_two = 0
        broc_coll_two = True
        allgood = True
        while(allgood):
            broc_point_across_two = random.randint(50,1770)
            if abs(broc_point_across_two-cookie_point_across_one) > 75 and abs(broc_point_across_two-cookie_point_across_two) > 75 and abs(broc_point_across_two-cookie_point_across_three) > 75:
                allgood = False
            else:
                broc_point_across_two = random.randint(50,1770)
                
    if broc_coll_one:
        if abs(broc_point_across_two-broc_point_across_one) < 75:
            broc_point_across_one = random.randint(50,1770)
            
    if broc_coll_two:
        if abs(broc_point_across_two-broc_point_across_one) < 75:
            broc_point_across_two = random.randint(50,1770)

    #Setting up Collisions with player_two
    
    broc_coll_one = False
    broc_coll_two = False

    if (cookie_point_across_one) >= (player_two_x-30) and (cookie_left_two) <= (player_two_x_end+30) and abs(cookie_bottom_two-player_one_y) <= 15 :
        score_two = score_two + 10
        cookie_point_down_one = 0
        if lives_one > 0 and lives_two > 0:
            cookie_point_across_one = random.randint(50,1770)
            allgood = True
            while(allgood):
                if abs(cookie_point_across_one-cookie_point_across_two) > 75 and abs(cookie_point_across_one-cookie_point_across_three) > 75:
                    allgood = False
                else:
                    cookie_point_across_one = random.randint(50,1770)

    if (cookie_point_across_two) >= (player_two_x-30) and (cookie_left_two) <= (player_two_x_end+30) and abs(cookie_bottom_two-player_two_y) <= 15 :
        score_two = score_two + 10
        cookie_point_down_two = 0
        if lives_one > 0 and lives_two > 0:
            cookie_point_across_two = random.randint(50,1770)
            allgood = True
            while(allgood):
                if abs(cookie_point_across_two-cookie_point_across_one) > 75 and abs(cookie_point_across_two-cookie_point_across_three) > 75:
                    allgood = False
                else:
                    cookie_point_across_two = random.randint(50,1770)
                    
    if (cookie_point_across_three) >= (player_two_x-30) and (cookie_left_three) <= (player_two_x_end+30) and abs(cookie_bottom_three-player_two_y) <= 15 :
        score_two = score_two + 10
        cookie_point_down_three = 0
        if lives_one > 0 and lives_two > 0:
            cookie_point_across_threed = random.randint(50,1770)
            allgood = True
            while(allgood):
                if abs(cookie_point_across_three-cookie_point_across_one) > 75 and abs(cookie_point_across_three-cookie_point_across_two) > 75:
                    allgood = False
                else:
                    cookie_point_across_three = random.randint(50,1770)
                    
    if (broc_point_across_one) >= (player_two_x-30) and (broc_left_one) <= (player_two_x_end+30) and abs(broc_bottom_one-player_two_y) <= 15 :
        lives_two = lives_two - 1
        broc_point_down_one = 0
        allgood = True
        broc_coll_one = True
        while(allgood):
            broc_point_across_one = random.randint(50,1770)
            if abs(broc_point_across_one-cookie_point_across_one) > 75 and abs(broc_point_across_one-cookie_point_across_two) > 75 and abs(broc_point_across_one-cookie_point_across_three) > 75:
                allgood = False
            else:
                broc_point_across_one = random.randint(50,1770)
                
    if (broc_point_across_two) >= (player_two_x-30) and (broc_left_two) <= (player_two_x_end+30) and abs(broc_bottom_two-player_two_y) <= 15 :
        lives_two = lives_two - 1
        broc_point_down_two = 0
        allgood = True
        broc_coll_two = True
        while(allgood):
            broc_point_across_two = random.randint(50,1770)
            if abs(broc_point_across_two-cookie_point_across_one) > 75 and abs(broc_point_across_two-cookie_point_across_two) > 75 and abs(broc_point_across_two-cookie_point_across_three) > 75:
                allgood = False
            else:
                broc_point_across_two = random.randint(50,1770)
                
    if broc_coll_one:
        if abs(broc_point_across_two-broc_point_across_one) < 75:
            broc_point_across_one = random.randint(50,1770)
            
    if broc_coll_two:
        if abs(broc_point_across_two-broc_point_across_one) < 75:
            broc_point_across_two = random.randint(50,1770)

            
    #Setting up speed
        
    if score_one%50 == 0 or score_two%50 == 0:
            if cookie_speed > 2 and score_one > 0 and score_two > 0:
                cookie_speed = cookie_speed - 1
    
    if frame_count%cookie_speed == 0:
        cookie_point_down_one = cookie_point_down_one+20
        cookie_point_down_two = cookie_point_down_two+20
        cookie_point_down_three = cookie_point_down_three+20
        broc_point_down_one = broc_point_down_one+20
        broc_point_down_two = broc_point_down_two+20

        
    #Setting up bottom collision
    
    broc_coll_one = False
    broc_coll_two = False

        
    if cookie_bottom_one >= 1050:
        distance_one = ((player_one_y-cookie_middle_y_one)**2)+((player_one_middle-cookie_middle_x_one)**2)
        distance_two = ((player_two_y-cookie_middle_y_one)**2)+((player_two_middle-cookie_middle_x_one)**2)
        if distance_one<distance_two:
            lives_one = lives_one-1
        if distance_one>distance_two:
            lives_two = lives_two -1
        if lives_one > 0 and lives_two > 0:
            cookie_point_across_one = random.randint(50,1770)
            allgood = True
            while(allgood):
                if abs(cookie_point_across_one-cookie_point_across_two) > 75 and abs(cookie_point_across_one-cookie_point_across_three) > 75:
                    allgood = False
                else:
                    cookie_point_across_one = random.randint(50,1770)
            cookie_point_down_one = 0
    
    if cookie_bottom_two >= 1050:
        distance_one = ((player_one_y-cookie_middle_y_two)**2)+((player_one_middle-cookie_middle_x_two)**2)
        distance_two = ((player_two_y-cookie_middle_y_two)**2)+((player_two_middle-cookie_middle_x_two)**2)
        if distance_one<distance_two:
            lives_one = lives_one-1
        if distance_one>distance_two:
            lives_two = lives_two -1
        if lives_one > 0 and lives_two > 0:
            cookie_point_across_two = random.randint(50,1770)
            allgood = True
            while(allgood):
                if abs(cookie_point_across_two-cookie_point_across_one) > 75 and abs(cookie_point_across_two-cookie_point_across_three) > 75:
                    allgood = False
                else:
                    cookie_point_across_three = random.randint(50,1770)
            cookie_point_down_two = 0
            
    if cookie_bottom_three >= 1050:
        distance_one = ((player_one_y-cookie_middle_y_three)**2)+((player_one_middle-cookie_middle_x_three)**2)
        distance_two = ((player_two_y-cookie_middle_y_three)**2)+((player_two_middle-cookie_middle_x_three)**2)
        if distance_one<distance_two:
            lives_one = lives_one-1
        if distance_one>distance_two:
            lives_two = lives_two -1
        if lives_one > 0 and lives_two > 0:
            cookie_point_across_three = random.randint(50,1770)
            allgood = True
            while(allgood):
                if abs(cookie_point_across_three-cookie_point_across_one) > 75 and abs(cookie_point_across_three-cookie_point_across_two) > 75:
                    allgood = False
                else:
                    cookie_point_across_three = random.randint(50,1770)
            cookie_point_down_three = 0
            
    if broc_bottom_one > 1020:
        allgood = True
        broc_coll_one = True
        broc_point_across_one = random.randint(50,1770)
        while(allgood):
            if abs(broc_point_across_one-cookie_point_across_one) > 75 and abs(broc_point_across_one-cookie_point_across_two) > 75 and abs(broc_point_across_one-cookie_point_across_three) > 75:
                allgood = False
            else:
                broc_point_across_one = random.randint(50,1770)
        broc_point_down_one = 0
        
    if broc_bottom_two > 1020:
        allgood = True
        broc_coll_two = True
        broc_point_across_two = random.randint(50,1770)
        while(allgood):
            if abs(broc_point_across_two-cookie_point_across_one) > 75 and abs(broc_point_across_two-cookie_point_across_two) > 75 and abs(broc_point_across_two-cookie_point_across_three) > 75:
                allgood = False
            else:
                broc_point_across_two = random.randint(50,1770)
        broc_point_down_two = 0
        
    if broc_coll_one:
        if abs(broc_point_across_two-broc_point_across_one) < 75:
            broc_point_across_one = random.randint(50,1770)
            
    if broc_coll_two:
        if abs(broc_point_across_two-broc_point_across_one) < 75:
            broc_point_across_two = random.randint(50,1770)


        
    
    heart_h, heart_w, heart_c = imgHeart.shape
    
    #Printing the hearts
    
        
    
    frame_h, frame_w, frame_c = frame.shape
    
    cv2.rectangle(frame, (1920,0), (1770,50), (0,0,0), -1)
    cv2.rectangle(frame, (1920,70), (1770,120), (0,0,0), -1)
    
    y_off=0
    if lives_one == 3:
        x_off=1870
        frame[y_off:y_off+imgHeart.shape[0], x_off:x_off+imgHeart.shape[1]] = imgHeart   
        x_off=1820
        frame[y_off:y_off+imgHeart.shape[0], x_off:x_off+imgHeart.shape[1]] = imgHeart       
        x_off=1770
        frame[y_off:y_off+imgHeart.shape[0], x_off:x_off+imgHeart.shape[1]] = imgHeart
                
                
    if lives_one == 2:
        x_off=1870
        frame[y_off:y_off+imgHeart.shape[0], x_off:x_off+imgHeart.shape[1]] = imgHeart   
        x_off=1820
        frame[y_off:y_off+imgHeart.shape[0], x_off:x_off+imgHeart.shape[1]] = imgHeart 
        
            
     
    if lives_one == 1:
        x_off=1870
        frame[y_off:y_off+imgHeart.shape[0], x_off:x_off+imgHeart.shape[1]] = imgHeart 
        
    y_off=70
    if lives_two == 3:
        x_off=1870
        frame[y_off:y_off+imgHeart.shape[0], x_off:x_off+imgHeart.shape[1]] = imgHeart   
        x_off=1820
        frame[y_off:y_off+imgHeart.shape[0], x_off:x_off+imgHeart.shape[1]] = imgHeart       
        x_off=1770
        frame[y_off:y_off+imgHeart.shape[0], x_off:x_off+imgHeart.shape[1]] = imgHeart
                
                
    if lives_two == 2:
        x_off=1870
        frame[y_off:y_off+imgHeart.shape[0], x_off:x_off+imgHeart.shape[1]] = imgHeart   
        x_off=1820
        frame[y_off:y_off+imgHeart.shape[0], x_off:x_off+imgHeart.shape[1]] = imgHeart 
        
            
     
    if lives_two == 1:
        x_off=1870
        frame[y_off:y_off+imgHeart.shape[0], x_off:x_off+imgHeart.shape[1]] = imgHeart 
    
            
        
    #Printing the cookies and broc
    
    if lives_one > 0 and lives_two > 0:
        x_off = cookie_point_across_one
        y_off = cookie_point_down_one
        frame[y_off:y_off+imgCookie.shape[0], x_off:x_off+imgCookie.shape[1]] = imgCookie          
        x_off = cookie_point_across_two
        y_off = cookie_point_down_two
        frame[y_off:y_off+imgCookie.shape[0], x_off:x_off+imgCookie.shape[1]] = imgCookie
        x_off = cookie_point_across_three
        y_off = cookie_point_down_three
        frame[y_off:y_off+imgCookie.shape[0], x_off:x_off+imgCookie.shape[1]] = imgCookie
                
        x_off = broc_point_across_one
        y_off = broc_point_down_one
        frame[y_off:y_off+imgBroc.shape[0], x_off:x_off+imgBroc.shape[1]] = imgBroc
        x_off = broc_point_across_two
        y_off = broc_point_down_two
        frame[y_off:y_off+imgBroc.shape[0], x_off:x_off+imgBroc.shape[1]] = imgBroc
        
        
    frame = cv2.flip(frame,1)
    
    while (lives_one <= 0):
        ret_val, frame = cam.read()
        frame = cv2.flip(frame,1)
        font = cv2.FONT_HERSHEY_TRIPLEX
        cv2.putText(frame, 'GAME OVER - PLAYER TWO WINS', (150, 500), font, 3, (255,255,255), 2, cv2.LINE_AA)
        cv2.imshow('my webcam', frame)         
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    while (lives_two <= 0):
        ret_val, frame = cam.read()
        frame = cv2.flip(frame,1)
        font = cv2.FONT_HERSHEY_TRIPLEX
        cv2.putText(frame, 'GAME OVER - PLAYER ONE WINS', (150, 500), font, 3, (255,255,255), 2, cv2.LINE_AA)
        cv2.imshow('my webcam', frame)         
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
         
          
    cv2.putText(frame, str(score_one), (1800,50), cv2.FONT_HERSHEY_TRIPLEX, 2, (0,0,0), 2, cv2.LINE_AA)
    cv2.putText(frame, str(score_two), (1800,100), cv2.FONT_HERSHEY_TRIPLEX, 2, (0,0,0), 2, cv2.LINE_AA)   
    
    cv2.putText(frame, "PLAYER 1 - COOKIE MONSTER", (700,50), cv2.FONT_HERSHEY_TRIPLEX, 1, (0,0,0), 2, cv2.LINE_AA)
    cv2.putText(frame, "PLAYER 2 - ELMO", (700,100), cv2.FONT_HERSHEY_TRIPLEX, 1, (0,0,0), 2, cv2.LINE_AA)
        
    cv2.imshow('my webcam', frame)
    
    frame_count = frame_count + 1
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cam.release()
cv2.destroyAllWindows()
