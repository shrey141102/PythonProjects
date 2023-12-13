import pygame
import random

# initialize the pygame
pygame.init()

c = 0
black = (0,0,0)
grey = (150, 150, 150)
white = (255,255,255)
mouse_x =0 # click position x
mouse_y =0 # click position y
sum = 0

# create the screen
screen = pygame.display.set_mode((1000,600))

# Title and icon
pygame.display.set_caption("Num Sherlock")
icon = pygame.image.load('NumSherlock/images/private-detective.png')
pygame.display.set_icon(icon)

# Welcome image
playerImg = pygame.image.load('NumSherlock/images/startimg.png (2).png')
playerX= 400
playerY = 30

def player():
    screen.blit(playerImg, (playerX, playerY)) 

# Last Second slide image
lastsec = pygame.image.load('NumSherlock/images/lastsec1 (1).png')
lastsecX = 375
lastsecY = 30

def lastsecimg():
    screen.blit(lastsec, (lastsecX, lastsecY))

# Last slide image
last = pygame.image.load('NumSherlock/images/last1 (1).png')
lastX = 375
lastY = 30

def lastimg():
    screen.blit(last, (lastX, lastY))


# Game loop
running = True
while running:
    # RGB
    screen.fill((180,190,172))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if (c==0): 
        player()
        text_lines = [
        "Welcome to Num-Sherlock!",
        "Pick any number from 1 to 100",
        "Click NEXT when ready",
        "Don't make it easy for me though ;) !!"
        ]

        line_height = 100

        font = pygame.font.Font('freesansbold.ttf', 32)

        # Render text surfaces and get their dimensions
        text_surfaces = [font.render(line, True, black) for line in text_lines]
        text_rects = [text_surface.get_rect() for text_surface in text_surfaces]

        # Calculate the starting y position to center the text
        y_position = (600 - 150) // 2

        for text_surface, text_rect in zip(text_surfaces, text_rects):
            text_rect.topleft = ((1000 - text_rect.width) // 2, y_position+40)
            screen.blit(text_surface, text_rect)
            y_position += text_rect.height + 10  # Increment y position for the next line

        # Adding button
        button_width = 150
        button_height = 50
        button_x = 427
        button_y = 480

        # Text for the button
        button_text = "NEXT"

        # Draw the button
        pygame.draw.rect(screen, black, (button_x, button_y, button_width, button_height))
    
        # Render button text
        text_surface = font.render(button_text, True, white)
        text_rect = text_surface.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
        screen.blit(text_surface, text_rect)
        
        if(event.type == pygame.MOUSEBUTTONDOWN):
            mouse_x, mouse_y = pygame.mouse.get_pos()
        if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height: # Placeholder action for button click
            c=c+1 
            

    elif(c==1):
            text_lines = [
            "Check for your number and click 'yes' if present or else 'no'",
            " ",
            "16  17  18  19  20  21  22  23",
            "24  25  26  27  28  29  30  31",
            "48  49  50  51  52  53  54  55",
            "56  57  58  59  60  61  62  63",
            "80  81  82  83  84  85  86  87",
            "88  89  90  91  92  93  94  95"
            ]

            line_height = 100

            font = pygame.font.Font('freesansbold.ttf', 32)

            # Render text surfaces and get their dimensions
            text_surfaces = [font.render(line, True, black) for line in text_lines]
            text_rects = [text_surface.get_rect() for text_surface in text_surfaces]

            # Calculate the starting y position to center the text
            y_position = (350 - 310) // 2

            for text_surface, text_rect in zip(text_surfaces, text_rects):
                text_rect.topleft = ((1000 - text_rect.width) // 2, y_position+40)
                screen.blit(text_surface, text_rect)
                y_position += text_rect.height + 10  # Increment y position for the next line

            # Adding buttons

            yes_button_width = 100
            yes_button_height = 50
            yes_button_x = 150
            yes_button_y = 430

            # Text for the button
            yes_button_text = "YES"

            # Draw the button
            pygame.draw.rect(screen, black, (yes_button_x, yes_button_y, yes_button_width, yes_button_height))
    
            # Render button text
            text_surface = font.render(yes_button_text, True, white)
            text_rect = text_surface.get_rect(center=(yes_button_x + yes_button_width // 2, yes_button_y + yes_button_height // 2))
            screen.blit(text_surface, text_rect)
        
            if(event.type == pygame.MOUSEBUTTONDOWN):
                mouse_x, mouse_y = pygame.mouse.get_pos()
            if yes_button_x <= mouse_x <= yes_button_x + yes_button_width and yes_button_y <= mouse_y <= yes_button_y + yes_button_height: # Placeholder action for button click
                c=c+1 
                sum = sum + 16

            no_button_width = 100
            no_button_height = 50
            no_button_x = 150
            no_button_y = 530

            # Text for the button
            no_button_text = "NO"

            # Draw the button
            pygame.draw.rect(screen, black, (no_button_x, no_button_y, no_button_width, no_button_height))
    
            # Render button text
            text_surface = font.render(no_button_text, True, white)
            text_rect = text_surface.get_rect(center=(no_button_x + no_button_width // 2, no_button_y + no_button_height // 2))
            screen.blit(text_surface, text_rect)
        
            if(event.type == pygame.MOUSEBUTTONDOWN):
                mouse_x, mouse_y = pygame.mouse.get_pos()
            if no_button_x <= mouse_x <= no_button_x + no_button_width and no_button_y <= mouse_y <= no_button_y + no_button_height: # Placeholder action for button click
                c=c+1 


    elif(c==2):
            text_lines = [
            "Check for your number and click 'yes' if present or else 'no'",
            " ",
            "02  03  06  07  10  11  14  15",
            "18  19  22  23  26  27  30  31",
            "34  35  38  39  42  43  46  47",
            "50  51  54  55  58  59  62  63",
            "66  67  70  71  74  75  78  79",
            "82  83  86  87  90  91  94  95",
            "98  99"
            ]

            line_height = 100

            font = pygame.font.Font('freesansbold.ttf', 32)

            # Render text surfaces and get their dimensions
            text_surfaces = [font.render(line, True, black) for line in text_lines]
            text_rects = [text_surface.get_rect() for text_surface in text_surfaces]

            # Calculate the starting y position to center the text
            y_position = (300 - 310) // 2

            for text_surface, text_rect in zip(text_surfaces, text_rects):
                text_rect.topleft = ((1000 - text_rect.width) // 2, y_position+40)
                screen.blit(text_surface, text_rect)
                y_position += text_rect.height + 10  # Increment y position for the next line

            # Adding Buttons
            yes_button_width = 100
            yes_button_height = 50
            yes_button_x =250
            yes_button_y = 430

            # Text for the button
            yes_button_text = "YES"

            # Draw the button
            pygame.draw.rect(screen, black, (yes_button_x, yes_button_y, yes_button_width, yes_button_height))
    
            # Render button text
            text_surface = font.render(yes_button_text, True, white)
            text_rect = text_surface.get_rect(center=(yes_button_x + yes_button_width // 2, yes_button_y + yes_button_height // 2))
            screen.blit(text_surface, text_rect)
        
            if(event.type == pygame.MOUSEBUTTONDOWN):
                mouse_x, mouse_y = pygame.mouse.get_pos()
            if yes_button_x <= mouse_x <= yes_button_x + yes_button_width and yes_button_y <= mouse_y <= yes_button_y + yes_button_height: # Placeholder action for button click
                c=c+1 
                sum = sum + 2

            no_button_width = 100
            no_button_height = 50
            no_button_x = 250
            no_button_y = 530

            # Text for the button
            no_button_text = "NO"

            # Draw the button
            pygame.draw.rect(screen, black, (no_button_x, no_button_y, no_button_width, no_button_height))
    
            # Render button text
            text_surface = font.render(no_button_text, True, white)
            text_rect = text_surface.get_rect(center=(no_button_x + no_button_width // 2, no_button_y + no_button_height // 2))
            screen.blit(text_surface, text_rect)
        
            if(event.type == pygame.MOUSEBUTTONDOWN):
                mouse_x, mouse_y = pygame.mouse.get_pos()
            if no_button_x <= mouse_x <= no_button_x + no_button_width and no_button_y <= mouse_y <= no_button_y + no_button_height: # Placeholder action for button click
                c=c+1 

    
    elif(c==3):
            text_lines = [
            "Check for your number and click 'yes' if present or else 'no'",
            " ",
            "64  65  66  67  68  69  70  71",
            "72  73  74  75  76  77  78  79",
            "80  81  82  83  84  85  86  87",
            "88  89  90  91  92  93  94  95",
            "96  97  98  99  100"
            ]

            line_height = 100

            font = pygame.font.Font('freesansbold.ttf', 32)

            # Render text surfaces and get their dimensions
            text_surfaces = [font.render(line, True, black) for line in text_lines]
            text_rects = [text_surface.get_rect() for text_surface in text_surfaces]

            # Calculate the total text height
            #total_text_height = sum(text_rect.height for text_rect in text_rects)

            # Calculate the starting y position to center the text
            y_position = (400 - 310) // 2

            for text_surface, text_rect in zip(text_surfaces, text_rects):
                text_rect.topleft = ((1000 - text_rect.width) // 2, y_position+40)
                screen.blit(text_surface, text_rect)
                y_position += text_rect.height + 10  # Increment y position for the next line

            # Adding buttons
            yes_button_width = 100
            yes_button_height = 50
            yes_button_x = 350
            yes_button_y = 430

            # Text for the button
            yes_button_text = "YES"

            # Draw the button
            pygame.draw.rect(screen, black, (yes_button_x, yes_button_y, yes_button_width, yes_button_height))
    
            # Render button text
            text_surface = font.render(yes_button_text, True, white)
            text_rect = text_surface.get_rect(center=(yes_button_x + yes_button_width // 2, yes_button_y + yes_button_height // 2))
            screen.blit(text_surface, text_rect)
        
            if(event.type == pygame.MOUSEBUTTONDOWN):
                mouse_x, mouse_y = pygame.mouse.get_pos()
            if yes_button_x <= mouse_x <= yes_button_x + yes_button_width and yes_button_y <= mouse_y <= yes_button_y + yes_button_height: # Placeholder action for button click
                c=c+1 
                sum = sum + 64

            no_button_width = 100
            no_button_height = 50
            no_button_x = 350
            no_button_y = 530

            # Text for the button
            no_button_text = "NO"

            # Draw the button
            pygame.draw.rect(screen, black, (no_button_x, no_button_y, no_button_width, no_button_height))
    
            # Render button text
            text_surface = font.render(no_button_text, True, white)
            text_rect = text_surface.get_rect(center=(no_button_x + no_button_width // 2, no_button_y + no_button_height // 2))
            screen.blit(text_surface, text_rect)
        
            if(event.type == pygame.MOUSEBUTTONDOWN):
                mouse_x, mouse_y = pygame.mouse.get_pos()
            if no_button_x <= mouse_x <= no_button_x + no_button_width and no_button_y <= mouse_y <= no_button_y + no_button_height: # Placeholder action for button click
                c=c+1 

    elif(c==4):
            text_lines = [
            "Check for your number and click 'yes' if present or else 'no'",
            " ",
            "32  33  34  35  36  37  38  39",
            "40  41  42  43  44  45  46  47",
            "48  49  50  51  52  53  54  55",
            "56  57  58  59  60  61  62  63",
            "96  97  98  99  100"
            ]

            line_height = 100

            font = pygame.font.Font('freesansbold.ttf', 32)

            # Render text surfaces and get their dimensions
            text_surfaces = [font.render(line, True, black) for line in text_lines]
            text_rects = [text_surface.get_rect() for text_surface in text_surfaces]

            # Calculate the starting y position to center the text
            y_position = (400 - 310) // 2

            for text_surface, text_rect in zip(text_surfaces, text_rects):
                text_rect.topleft = ((1000 - text_rect.width) // 2, y_position+40)
                screen.blit(text_surface, text_rect)
                y_position += text_rect.height + 10  # Increment y position for the next line

            # Adding buttons
            yes_button_width = 100
            yes_button_height = 50
            yes_button_x = 450
            yes_button_y = 430

            # Text for the button
            yes_button_text = "YES"

            # Draw the button
            pygame.draw.rect(screen, black, (yes_button_x, yes_button_y, yes_button_width, yes_button_height))
    
            # Render button text
            text_surface = font.render(yes_button_text, True, white)
            text_rect = text_surface.get_rect(center=(yes_button_x + yes_button_width // 2, yes_button_y + yes_button_height // 2))
            screen.blit(text_surface, text_rect)
        
            if(event.type == pygame.MOUSEBUTTONDOWN):
                mouse_x, mouse_y = pygame.mouse.get_pos()
            if yes_button_x <= mouse_x <= yes_button_x + yes_button_width and yes_button_y <= mouse_y <= yes_button_y + yes_button_height: # Placeholder action for button click
                c=c+1 
                sum = sum + 32

            no_button_width = 100
            no_button_height = 50
            no_button_x = 450
            no_button_y = 530

            # Text for the button
            no_button_text = "NO"

            # Draw the button
            pygame.draw.rect(screen, black, (no_button_x, no_button_y, no_button_width, no_button_height))
    
            # Render button text
            text_surface = font.render(no_button_text, True, white)
            text_rect = text_surface.get_rect(center=(no_button_x + no_button_width // 2, no_button_y + no_button_height // 2))
            screen.blit(text_surface, text_rect)
        
            if(event.type == pygame.MOUSEBUTTONDOWN):
                mouse_x, mouse_y = pygame.mouse.get_pos()
            if no_button_x <= mouse_x <= no_button_x + no_button_width and no_button_y <= mouse_y <= no_button_y + no_button_height: # Placeholder action for button click
                c=c+1 


    elif(c==5):
            text_lines = [
            "Check for your number and click 'yes' if present or else 'no'",
            " ",
            "04  05  06  07  12  13  14  15",
            "20  21  22  23  28  29  30  31",
            "36  37  38  39  44  45  46  47",
            "52  53  54  55  60  61  62  63",
            "68  69  70  71  76  77  78  79",
            "84  85  86  87  92  93  94  95",
            "100"
            ]

            line_height = 100

            font = pygame.font.Font('freesansbold.ttf', 32)

            # Render text surfaces and get their dimensions
            text_surfaces = [font.render(line, True, black) for line in text_lines]
            text_rects = [text_surface.get_rect() for text_surface in text_surfaces]

            # Calculate the starting y position to center the text
            y_position = (300 - 310) // 2

            for text_surface, text_rect in zip(text_surfaces, text_rects):
                text_rect.topleft = ((1000 - text_rect.width) // 2, y_position+40)
                screen.blit(text_surface, text_rect)
                y_position += text_rect.height + 10  # Increment y position for the next line

            # Adding buttons
            yes_button_width = 100
            yes_button_height = 50
            yes_button_x =550
            yes_button_y = 430

            # Text for the button
            yes_button_text = "YES"

            # Draw the button
            pygame.draw.rect(screen, black, (yes_button_x, yes_button_y, yes_button_width, yes_button_height))
    
            # Render button text
            text_surface = font.render(yes_button_text, True, white)
            text_rect = text_surface.get_rect(center=(yes_button_x + yes_button_width // 2, yes_button_y + yes_button_height // 2))
            screen.blit(text_surface, text_rect)
        
            if(event.type == pygame.MOUSEBUTTONDOWN):
                mouse_x, mouse_y = pygame.mouse.get_pos()
            if yes_button_x <= mouse_x <= yes_button_x + yes_button_width and yes_button_y <= mouse_y <= yes_button_y + yes_button_height: # Placeholder action for button click
                c=c+1 
                sum = sum + 4

            no_button_width = 100
            no_button_height = 50
            no_button_x = 550
            no_button_y = 530

            # Text for the button
            no_button_text = "NO"

            # Draw the button
            pygame.draw.rect(screen, black, (no_button_x, no_button_y, no_button_width, no_button_height))
    
            # Render button text
            text_surface = font.render(no_button_text, True, white)
            text_rect = text_surface.get_rect(center=(no_button_x + no_button_width // 2, no_button_y + no_button_height // 2))
            screen.blit(text_surface, text_rect)
        
            if(event.type == pygame.MOUSEBUTTONDOWN):
                mouse_x, mouse_y = pygame.mouse.get_pos()
            if no_button_x <= mouse_x <= no_button_x + no_button_width and no_button_y <= mouse_y <= no_button_y + no_button_height: # Placeholder action for button click
                c=c+1 

    
    elif(c==6):
            text_lines = [
            "Check for your number and click 'yes' if present or else 'no'",
            " ",
            "08  09  10  11  12  13  14  15",
            "24  25  26  27  28  29  30  31",
            "40  41  42  43  44  45  46  47",
            "56  57  58  59  60  61  62  63",
            "72  73  74  75  76  77  78  79",
            "88  89  90  91  92  93  94  95",
            ]

            line_height = 100

            font = pygame.font.Font('freesansbold.ttf', 32)

            # Render text surfaces and get their dimensions
            text_surfaces = [font.render(line, True, black) for line in text_lines]
            text_rects = [text_surface.get_rect() for text_surface in text_surfaces]

            # Calculate the starting y position to center the text
            y_position = (300 - 310) // 2

            for text_surface, text_rect in zip(text_surfaces, text_rects):
                text_rect.topleft = ((1000 - text_rect.width) // 2, y_position+40)
                screen.blit(text_surface, text_rect)
                y_position += text_rect.height + 10  # Increment y position for the next line

            # Adding buttons
            yes_button_width = 100
            yes_button_height = 50
            yes_button_x =650
            yes_button_y = 430

            # Text for the button
            yes_button_text = "YES"

            # Draw the button
            pygame.draw.rect(screen, black, (yes_button_x, yes_button_y, yes_button_width, yes_button_height))
    
            # Render button text
            text_surface = font.render(yes_button_text, True, white)
            text_rect = text_surface.get_rect(center=(yes_button_x + yes_button_width // 2, yes_button_y + yes_button_height // 2))
            screen.blit(text_surface, text_rect)
        
            if(event.type == pygame.MOUSEBUTTONDOWN):
                mouse_x, mouse_y = pygame.mouse.get_pos()
            if yes_button_x <= mouse_x <= yes_button_x + yes_button_width and yes_button_y <= mouse_y <= yes_button_y + yes_button_height: # Placeholder action for button click
                c=c+1 
                sum = sum + 8

            no_button_width = 100
            no_button_height = 50
            no_button_x = 650
            no_button_y = 530

            # Text for the button
            no_button_text = "NO"

            # Draw the button
            pygame.draw.rect(screen, black, (no_button_x, no_button_y, no_button_width, no_button_height))
    
            # Render button text
            text_surface = font.render(no_button_text, True, white)
            text_rect = text_surface.get_rect(center=(no_button_x + no_button_width // 2, no_button_y + no_button_height // 2))
            screen.blit(text_surface, text_rect)
        
            if(event.type == pygame.MOUSEBUTTONDOWN):
                mouse_x, mouse_y = pygame.mouse.get_pos()
            if no_button_x <= mouse_x <= no_button_x + no_button_width and no_button_y <= mouse_y <= no_button_y + no_button_height: # Placeholder action for button click
                c=c+1 

    
    elif(c==7):
            text_lines = [
            "Check for your number and click 'yes' if present or else 'no'",
            " ",
            "01  03  05  07  09  11  13  15",
            "17  19  21  23  25  27  29  31",
            "33  35  37  39  41  43  45  47",
            "49  51  53  55  57  59  61  63",
            "65  67  69  71  73  75  77  79",
            "81  83  85  87  89  91  93  95",
            "97  99"
            ]

            line_height = 100

            font = pygame.font.Font('freesansbold.ttf', 32)

            # Render text surfaces and get their dimensions
            text_surfaces = [font.render(line, True, black) for line in text_lines]
            text_rects = [text_surface.get_rect() for text_surface in text_surfaces]

            # Calculate the starting y position to center the text
            y_position = (300 - 310) // 2

            for text_surface, text_rect in zip(text_surfaces, text_rects):
                text_rect.topleft = ((1000 - text_rect.width) // 2, y_position+40)
                screen.blit(text_surface, text_rect)
                y_position += text_rect.height + 10  # Increment y position for the next line

            # Adding buttons
            yes_button_width = 100
            yes_button_height = 50
            yes_button_x =750
            yes_button_y = 430

            # Text for the button
            yes_button_text = "YES"

            # Draw the button
            pygame.draw.rect(screen, black, (yes_button_x, yes_button_y, yes_button_width, yes_button_height))
    
            # Render button text
            text_surface = font.render(yes_button_text, True, white)
            text_rect = text_surface.get_rect(center=(yes_button_x + yes_button_width // 2, yes_button_y + yes_button_height // 2))
            screen.blit(text_surface, text_rect)
        
            if(event.type == pygame.MOUSEBUTTONDOWN):
                mouse_x, mouse_y = pygame.mouse.get_pos()
            if yes_button_x <= mouse_x <= yes_button_x + yes_button_width and yes_button_y <= mouse_y <= yes_button_y + yes_button_height: # Placeholder action for button click
                c=c+1 
                sum = sum + 1

            no_button_width = 100
            no_button_height = 50
            no_button_x = 750
            no_button_y = 530

            # Text for the button
            no_button_text = "NO"

            # Draw the button
            pygame.draw.rect(screen, black, (no_button_x, no_button_y, no_button_width, no_button_height))
    
            # Render button text
            text_surface = font.render(no_button_text, True, white)
            text_rect = text_surface.get_rect(center=(no_button_x + no_button_width // 2, no_button_y + no_button_height // 2))
            screen.blit(text_surface, text_rect)
        
            if(event.type == pygame.MOUSEBUTTONDOWN):
                mouse_x, mouse_y = pygame.mouse.get_pos()
            if no_button_x <= mouse_x <= no_button_x + no_button_width and no_button_y <= mouse_y <= no_button_y + no_button_height: # Placeholder action for button click
                c=c+1 


    elif (c==8): 
        lastsecimg()
        text_lines = [
        "Hmmm!",
        "That wasn't hard at all :) ",
        "Click REVEAL to see your chosen number"
        ]

        line_height = 100

        font = pygame.font.Font('freesansbold.ttf', 32)

        # Render text surfaces and get their dimensions
        text_surfaces = [font.render(line, True, black) for line in text_lines]
        text_rects = [text_surface.get_rect() for text_surface in text_surfaces]

        # Calculate the starting y position to center the text
        y_position = (700 - 150) // 2

        for text_surface, text_rect in zip(text_surfaces, text_rects):
            text_rect.topleft = ((1000 - text_rect.width) // 2, y_position+40)
            screen.blit(text_surface, text_rect)
            y_position += text_rect.height + 10  # Increment y position for the next line

        # Adding button
        button_width = 230
        button_height = 50
        button_x = 627
        button_y = 480

        # Text for the button
        button_text = "REVEAL >>"

        # Draw the button
        pygame.draw.rect(screen, black, (button_x, button_y, button_width, button_height))
    
        # Render button text
        text_surface = font.render(button_text, True, white)
        text_rect = text_surface.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
        screen.blit(text_surface, text_rect)
        
        if(event.type == pygame.MOUSEBUTTONDOWN):
            mouse_x, mouse_y = pygame.mouse.get_pos()
        if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height: # Placeholder action for button click
            c=c+1 


    else:
            lastimg()
            text_lines = [
            "Your chosen number is ",
            f'{sum}',
            "Isn't it?",
            " ",
            "Thank you"
            ]

            line_height = 100

            font = pygame.font.Font('freesansbold.ttf', 32)

            # Render text surfaces and get their dimensions
            text_surfaces = [font.render(line, True, black) for line in text_lines]
            text_rects = [text_surface.get_rect() for text_surface in text_surfaces]

            # Calculate the starting y position to center the text
            y_position = (900 - 310) // 2

            for text_surface, text_rect in zip(text_surfaces, text_rects):
                text_rect.topleft = ((1000 - text_rect.width) // 2, y_position+40)
                screen.blit(text_surface, text_rect)
                y_position += text_rect.height + 10  # Increment y position for the next line


    pygame.display.update() 
