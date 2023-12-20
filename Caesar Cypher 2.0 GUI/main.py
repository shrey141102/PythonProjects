import sys
import pygame

pygame.init()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

wndow = (255,191,128)
black = (0,0,0)
white = (255,255,255)
c = 0
mouse_x=0
mouse_y=0
typee = ""
final = ""
shift_num =0

screen = pygame.display.set_mode((1000,600))

pygame.display.set_caption("Caesar Cipher")
icon = pygame.image.load('Caesar Cypher 2.0 GUI/image/encrypted.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('Caesar Cypher 2.0 GUI/image/welcome (1).png')
playerX= 350
playerY = 100

def player():
    screen.blit(playerImg, (playerX, playerY))

def font(size):
    font_path = pygame.font.match_font('berlinsansfb')  
    font = pygame.font.Font(font_path, size)
    line_height = 100
    return font

intext = ""
shift=""
shift_box= pygame.Rect(75,75,100,50)
inputfont = font(25)
shift_font = font(32)
intext_box = pygame.Rect(75,75,250,50)
active = False
color = pygame.Color('brown')
clock = pygame.time.Clock()

def caesar(plainText, shift): 
    cipherText = ""
    for ch in plainText:
        if ch.isalpha():
            apolo = ch
            stayInAlphabet = ord(ch.lower()) + shift 
            if stayInAlphabet > ord('z'):
                stayInAlphabet -= 26
            if stayInAlphabet < ord('a'):
                stayInAlphabet +=26
            if apolo.isupper():
                finalLetter = chr(stayInAlphabet-32)
            else:
                finalLetter = chr(stayInAlphabet)
            cipherText += finalLetter
        if ch.isspace():
            cipherText += " "
        if not(ch.isspace() or ch.isalpha()):
            cipherText += ch
    return cipherText

def dicaesar(plaintext,shift):
    return caesar(plaintext,-shift)

running = True
while running:
    screen.fill(wndow)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if typee == "encode":
                print("ENCRYPTED TEXT : ",final)
            else:
                print("DECRYPTED TEXT : ",final)
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if intext_box.collidepoint(event.pos):
                active = True
            else:
                active = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if shift_box.collidepoint(event.pos):
                passive = True
            else:
                passive = False

        if event.type == pygame.KEYDOWN:
            if(active):
                if event.key == pygame.K_BACKSPACE:
                    intext = intext[:-1]
                elif event.key == pygame.K_RETURN:  
                    intext += "\n"  
                else:
                    intext += event.unicode

        if event.type == pygame.KEYDOWN:
            if(passive):
                if event.key == pygame.K_BACKSPACE:
                    shift = intext[:-1]
                elif event.key == pygame.K_RETURN: 
                    shift += "\n"  
                else:
                    shift += event.unicode

    if (c==0): 
        text_lines = [
        "WELCOME TO CAESAR CIPHER!!"
        ]

        weltext = font(50)
        text_surfaces = [weltext.render(line, True, black) for line in text_lines]
        text_rects = [text_surface.get_rect() for text_surface in text_surfaces]

        y_position = (150 - 150) // 2

        for text_surface, text_rect in zip(text_surfaces, text_rects):
            text_rect.topleft = ((1000 - text_rect.width) // 2, y_position+40)
            screen.blit(text_surface, text_rect)
            y_position += text_rect.height + 10  

        player()
        
        text_lines = [
        "Click on 'Encode' to encrypt",
        "or 'Decode' to decrypt your text"
        ]

        msg = font(35)
        text_surfaces = [msg.render(line, True, black) for line in text_lines]
        text_rects = [text_surface.get_rect() for text_surface in text_surfaces]

        y_position = (750 - 150) // 2

        for text_surface, text_rect in zip(text_surfaces, text_rects):
            text_rect.topleft = ((1000 - text_rect.width) // 2, y_position+40)
            screen.blit(text_surface, text_rect)
            y_position += text_rect.height + 10  

        yes_button_width = 150
        yes_button_height = 50
        yes_button_x = 300
        yes_button_y = 480
        
        yes_button_text = "ENCODE"

        pygame.draw.rect(screen, black, (yes_button_x, yes_button_y, yes_button_width, yes_button_height))
    
        butt = font(30)
        text_surface = butt.render(yes_button_text, True, white)
        text_rect = text_surface.get_rect(center=(yes_button_x + yes_button_width // 2, yes_button_y + yes_button_height // 2))
        screen.blit(text_surface, text_rect)
        
        if(event.type == pygame.MOUSEBUTTONDOWN):
            mouse_x, mouse_y = pygame.mouse.get_pos()
        if yes_button_x <= mouse_x <= yes_button_x + yes_button_width and yes_button_y <= mouse_y <= yes_button_y + yes_button_height: 
            c=c+1 
            
        no_button_width = 150
        no_button_height = 50
        no_button_x = 550
        no_button_y = 480

        no_button_text = "DECODE"

        pygame.draw.rect(screen, black, (no_button_x, no_button_y, no_button_width, no_button_height))
    
        text_surface = butt.render(no_button_text, True, white)
        text_rect = text_surface.get_rect(center=(no_button_x + no_button_width // 2, no_button_y + no_button_height // 2))
        screen.blit(text_surface, text_rect)
        
        if(event.type == pygame.MOUSEBUTTONDOWN):
            mouse_x, mouse_y = pygame.mouse.get_pos()
        if no_button_x <= mouse_x <= no_button_x + no_button_width and no_button_y <= mouse_y <= no_button_y + no_button_height: 
            c=c+2
            
    if (c==1): 
        text_lines = [
        "Type your text in the text box",
        "that you want to encrypt and click on NEXT:"
        ]

        weltext = font(40)
        text_surfaces = [weltext.render(line, True, black) for line in text_lines]
        text_rects = [text_surface.get_rect() for text_surface in text_surfaces]

        y_position = (150 - 150) // 2

        for text_surface, text_rect in zip(text_surfaces, text_rects):
            text_rect.topleft = ((1000 - text_rect.width) // 2, y_position+40)
            screen.blit(text_surface, text_rect)
            y_position += text_rect.height + 10  

        if active:
            color = pygame.Color('brown')
        else:
            color = pygame.Color('black')

        intext_box.x = 100
        intext_box.y = 175

        pygame.draw.rect(screen, color, intext_box,4)
        
        surf = inputfont.render(intext,True,'black')
        screen.blit(surf,(intext_box.x +5, intext_box.y +5))
        intext_box.w = max(250, surf.get_width()+10)
        intext_box.h = max(50,surf.get_height()+20)
        clock.tick(50)

        typee = "encode"

        button_width = 150
        button_height = 50
        button_x = 600
        button_y = 400

        button_text = "NEXT >>"

        pygame.draw.rect(screen, black, (button_x, button_y, button_width, button_height))
    
        text_surface = butt.render(button_text, True, white)
        text_rect = text_surface.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
        screen.blit(text_surface, text_rect)
        
        if(event.type == pygame.MOUSEBUTTONDOWN):
            mouse_x, mouse_y = pygame.mouse.get_pos()
        if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height: 
            c=5    

    if (c==2): 
        text_lines = [
        "Type your text in the text box",
        "that you want to decrypt and click on NEXT:"
        ]

        weltext = font(40)
        text_surfaces = [weltext.render(line, True, black) for line in text_lines]
        text_rects = [text_surface.get_rect() for text_surface in text_surfaces]

        y_position = (150 - 150) // 2

        for text_surface, text_rect in zip(text_surfaces, text_rects):
            text_rect.topleft = ((1000 - text_rect.width) // 2, y_position+40)
            screen.blit(text_surface, text_rect)
            y_position += text_rect.height + 10  

        if active:
            color = pygame.Color('brown')
        else:
            color = pygame.Color('black')

        intext_box.x = 100
        intext_box.y = 175

        pygame.draw.rect(screen, color, intext_box,4)
        
        surf = inputfont.render(intext,True,'black')
        screen.blit(surf,(intext_box.x +5, intext_box.y +5))
        intext_box.w = max(250, surf.get_width()+10)
        intext_box.h = max(50,surf.get_height()+20)
        clock.tick(50)
        
        typee = "decode"

        button_width = 150
        button_height = 50
        button_x = 600
        button_y = 400

        button_text = "NEXT >>"

        pygame.draw.rect(screen, black, (button_x, button_y, button_width, button_height))
    
        text_surface = butt.render(button_text, True, white)
        text_rect = text_surface.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
        screen.blit(text_surface, text_rect)
        
        if(event.type == pygame.MOUSEBUTTONDOWN):
            mouse_x, mouse_y = pygame.mouse.get_pos()
        if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height: 
            c=5
            
    if (c==5): 
        text_lines = [
        "Type the shiftkey in the text box",
        "(can be anything between 1-10)"
        ]

        weltext = font(40)
        text_surfaces = [weltext.render(line, True, black) for line in text_lines]
        text_rects = [text_surface.get_rect() for text_surface in text_surfaces]

        y_position = (150 - 150) // 2

        for text_surface, text_rect in zip(text_surfaces, text_rects):
            text_rect.topleft = ((1000 - text_rect.width) // 2, y_position+40)
            screen.blit(text_surface, text_rect)
            y_position += text_rect.height + 10  

        if passive:
            color = pygame.Color('brown')
        else:
            color = pygame.Color('black')

        shift_box.x = 450
        shift_box.y = 175

        pygame.draw.rect(screen, color, shift_box,4)
        
        sirf = shift_font.render(shift,True,'black')
        screen.blit(sirf,(shift_box.x +5, shift_box.y +5))
        
        clock.tick(50)

        button_width = 200
        button_height = 50
        button_x = 550
        button_y = 350

        button_text = "CONTINUE >>"

        pygame.draw.rect(screen, black, (button_x, button_y, button_width, button_height))
    
        text_surface = butt.render(button_text, True, white)
        text_rect = text_surface.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
        screen.blit(text_surface, text_rect)
        
        if(event.type == pygame.MOUSEBUTTONDOWN):
            mouse_x, mouse_y = pygame.mouse.get_pos()
        if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height: 
            c=7

    if (c==7): 
        if typee == "encode":
            final = caesar(intext,int(shift))
        else:
            final = dicaesar(intext,int(shift))

        if typee == "encode":
            text_lines = [
            "Encrypted text is:",
            f'"{final}"',
            " ",
            "(check the terminal for ",
            "copying the encrypted text)"
            ]
        elif typee == "decode":
            text_lines = [
            "Decrypted text is:",
            f'"{final}"',
            " ",
            "(check the terminal for ",
            "copying the decrypted text)"
            ]
        
        weltext = font(40)
        text_surfaces = [weltext.render(line, True, black) for line in text_lines]
        text_rects = [text_surface.get_rect() for text_surface in text_surfaces]

        y_position = (350 - 150) // 2

        for text_surface, text_rect in zip(text_surfaces, text_rects):
            text_rect.topleft = ((1000 - text_rect.width) // 2, y_position+40)
            screen.blit(text_surface, text_rect)
            y_position += text_rect.height + 10  
        
    pygame.display.flip()

pygame.quit()
sys.exit()

