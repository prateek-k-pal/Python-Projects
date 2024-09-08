import pygame
import sys

def draw_grid(screen, x, y, y_extra, line_length, line_width, padding):
    pygame.draw.lines(screen, "white", True, [(0, 0), (x - line_width, 0), (x - line_width, y - line_width), (0, y - line_width)],line_width)
    
    pygame.draw.line(screen, "white", (padding + 1 + line_length/3, y_extra + line_width + padding), (padding + 1 + line_length/3, line_length + y_extra + line_width + padding),line_width)
    pygame.draw.line(screen, "white", (padding + 1 + (line_length/3)*2, y_extra + line_width + padding), ((line_length/3)*2 + padding + 1, line_length + y_extra + line_width + padding),line_width)
    pygame.draw.line(screen, "white", (padding + line_width + 1, line_length/3 + y_extra + padding), ( line_width + padding + 1 + line_length, line_length/3 + y_extra + padding),line_width)
    pygame.draw.line(screen, "white", (padding + line_width + 1, (line_length/3)*2 + y_extra + padding), ( line_width + padding + 1 + line_length , (line_length/3)*2 + y_extra + padding),line_width)
    
def place_is_empty(block_flag, line_width, padding, y_extra, line_length):
    cur_pos = pygame.mouse.get_pos()
    
    if cur_pos[0] >= (line_width + padding) and cur_pos[0] <= (padding + line_length/3):
        if cur_pos[1] >= (line_width + padding + y_extra) and cur_pos[1] <= (padding + y_extra + line_length/3):
            if(block_flag['block_1'] == 0):
                return True, 'block_1'
            else:
                return False, None
            
        elif cur_pos[1] >= (line_width + padding + y_extra + line_length/3) and cur_pos[1] <= (padding + y_extra + (line_length/3)*2):
            if(block_flag['block_2'] == 0):
                return True, 'block_2'
            else:
                return False, None
            
        elif cur_pos[1] >= (line_width + padding + y_extra + (line_length/3)*2) and cur_pos[1] <= (padding + y_extra + line_length):
            if(block_flag['block_3'] == 0):
                return True, 'block_3'
            else:
                return False, None
            
    elif cur_pos[0] >= (line_width + padding + line_length/3) and cur_pos[0] <= (padding + (line_length/3)*2) :
        if cur_pos[1] >= (line_width + padding + y_extra) and cur_pos[1] <= (padding + y_extra + line_length/3):
            if(block_flag['block_4'] == 0):
                return True, 'block_4'
            else:
                return False, None
            
        elif cur_pos[1] >= (line_width + padding + y_extra + line_length/3) and cur_pos[1] <= (padding + y_extra + (line_length/3)*2):
            if(block_flag['block_5'] == 0):
                return True, 'block_5'
            else:
                return False, None
            
        elif cur_pos[1] >= (line_width + padding + y_extra + (line_length/3)*2) and cur_pos[1] <= (padding + y_extra + line_length):
            if(block_flag['block_6'] == 0):
                return True, 'block_6'
            else:
                return False, None
            
    elif cur_pos[0] >= (line_width + padding + (line_length/3)*2) and cur_pos[0] <= (padding + line_length):
        if cur_pos[1] >= (line_width + padding + y_extra) and cur_pos[1] <= (padding + y_extra + line_length/3):
            if(block_flag['block_7'] == 0):
                return True, 'block_7'
            else:
                return False, None
            
        elif cur_pos[1] >= (line_width + padding + y_extra + line_length/3) and cur_pos[1] <= (padding + y_extra + (line_length/3)*2):
            if(block_flag['block_8'] == 0):
                return True, 'block_8'
            else:
                return False, None
            
        elif cur_pos[1] >= (line_width + padding + y_extra + (line_length/3)*2) and cur_pos[1] <= (padding + y_extra + line_length):
            if(block_flag['block_9'] == 0):
                return True, 'block_9'
            else:
                return False, None

def draw_crosses_circles(block_flag, screen):
    for i in block_flag.keys():
        match i:
            case 'block_1':
                if block_flag[i] == 1:
                    pygame.draw.line(screen, "red", (25, 226), (115, 316), 3)
                    pygame.draw.line(screen, "red", (115, 226), (25, 316), 3)
                elif block_flag[i] == 2:
                    pygame.draw.circle(screen, "green", (70, 271), 43, 2)
                    
            case 'block_2':
                if block_flag[i] == 1:
                    pygame.draw.line(screen, "red", (25, 336), (115, 426), 3)
                    pygame.draw.line(screen, "red", (115, 336), (25, 426), 3)
                elif block_flag[i] == 2:
                    pygame.draw.circle(screen, "green", (70, 381), 43, 2)
                    
            case 'block_3':
                if block_flag[i] == 1:
                    pygame.draw.line(screen, "red", (25, 456), (115, 546), 3)
                    pygame.draw.line(screen, "red", (115, 456), (25, 546), 3)
                elif block_flag[i] == 2:
                    pygame.draw.circle(screen, "green", (70, 501), 43, 2)
                    
            case 'block_4':
                if block_flag[i] == 1:
                    pygame.draw.line(screen, "red", (130, 226), (230, 316), 3)
                    pygame.draw.line(screen, "red", (230, 226), (130, 316), 3)
                elif block_flag[i] == 2:
                    pygame.draw.circle(screen, "green", (180, 271), 43, 2)
                    
            case 'block_5':
                if block_flag[i] == 1:
                    pygame.draw.line(screen, "red", (130, 336), (230, 426), 3)
                    pygame.draw.line(screen, "red", (230, 336), (130, 426), 3)
                elif block_flag[i] == 2:
                    pygame.draw.circle(screen, "green", (180, 381), 43, 2)
                    
            case 'block_6':
                if block_flag[i] == 1:
                    pygame.draw.line(screen, "red", (130, 456), (230, 546), 3)
                    pygame.draw.line(screen, "red", (230, 456), (130, 546), 3)
                elif block_flag[i] == 2:
                    pygame.draw.circle(screen, "green", (180, 501), 43, 2)
                    
            case 'block_7':
                if block_flag[i] == 1:
                    pygame.draw.line(screen, "red", (245, 226), (335, 316), 3)
                    pygame.draw.line(screen, "red", (335, 226), (245, 316), 3)
                elif block_flag[i] == 2:
                    pygame.draw.circle(screen, "green", (290, 271), 43, 2)
                    
            case 'block_8':
                if block_flag[i] == 1:
                    pygame.draw.line(screen, "red", (245, 336), (335, 426), 3)
                    pygame.draw.line(screen, "red", (335, 336), (245, 426), 3)
                elif block_flag[i] == 2:
                    pygame.draw.circle(screen, "green", (290, 381), 43, 2)
                    
            case 'block_9':
                if block_flag[i] == 1:
                    pygame.draw.line(screen, "red", (245, 456), (335, 546), 3)
                    pygame.draw.line(screen, "red", (335, 456), (245, 546), 3)
                elif block_flag[i] == 2:
                    pygame.draw.circle(screen, "green", (290, 501), 43, 2)
                                
def check_for_win(block_flag, screen):
    if(block_flag["block_1"] != 0 or block_flag["block_2"] != 0 or block_flag["block_3"] != 0 or block_flag["block_4"] != 0 or block_flag["block_7"] != 0):
        if(block_flag["block_1"] == block_flag["block_2"] == block_flag["block_3"] != 0):
            if block_flag["block_1"] == 1:
                pygame.draw.line(screen, "white", (69, 226), (69, 546), 3)
                return 1
            else:
                pygame.draw.line(screen, "white", (69, 226), (69, 546), 3)
                return 2
        
        elif(block_flag["block_4"] == block_flag["block_5"] == block_flag["block_6"] != 0):
            if block_flag["block_4"] == 1:
                pygame.draw.line(screen, "white", (179, 226), (179, 546), 3)
                return 1
            else:
                pygame.draw.line(screen, "white", (179, 226), (179, 546), 3)
                return 2
            
        elif(block_flag["block_7"] == block_flag["block_8"] == block_flag["block_9"] != 0):
            if block_flag["block_7"] == 1:
                pygame.draw.line(screen, "white", (289, 226), (289,546), 3)
                return 1
            else:
                pygame.draw.line(screen, "white", (289, 226), (289,546), 3)
                return 2
            
        elif(block_flag["block_1"] == block_flag["block_4"] == block_flag["block_7"] != 0):
            if block_flag["block_1"] == 1:
                pygame.draw.line(screen, "white", (25, 270), (335, 270), 3)
                return 1
            else:
                pygame.draw.line(screen, "white", (25, 270), (335, 270), 3)
                return 2
            
        elif(block_flag["block_2"] == block_flag["block_5"] == block_flag["block_8"] != 0):
            if block_flag["block_2"] == 1:
                pygame.draw.line(screen, "white", (25, 380), (335, 380), 3)
                return 1
            else:
                pygame.draw.line(screen, "white", (25, 380), (335, 380), 3)
                return 2
            
        elif(block_flag["block_3"] == block_flag["block_6"] == block_flag["block_9"] != 0):
            if block_flag["block_3"] == 1:
                pygame.draw.line(screen, "white", (25, 500), (335, 500), 3)
                return 1
            else:
                pygame.draw.line(screen, "white", (25, 500), (335, 500), 3)
                return 2
            
        elif(block_flag["block_1"] == block_flag["block_5"] == block_flag["block_9"] != 0):
            if block_flag["block_1"] == 1:
                pygame.draw.line(screen, "white", (25, 226), (335, 546), 3)
                return 1
            else:
                pygame.draw.line(screen, "white", (25, 226), (335, 546), 3)
                return 2
            
        elif(block_flag["block_7"] == block_flag["block_5"] == block_flag["block_3"] != 0):
            if block_flag["block_7"] == 1:
                pygame.draw.line(screen, "white", (335, 226), (25 , 546), 3)
                return 1
            else:
                pygame.draw.line(screen, "white", (335, 226), (25 , 546), 3)
                return 2
        elif(all(values!=0 for values in block_flag.values())):
            return 3
        else:
            return 0
            
    else:
        return 0

def text_input(screen, player, color_font, p_x, p_y, b_x, b_y):
    font = pygame.font.Font(None, 40)
    head = font.render(player, True, color_font)
    screen.blit(head, (p_x, p_y))
    
    input_box =  pygame.Rect(b_x, b_y, 150, 60)
    color_inactive = pygame.Color('gray')
    color_active = pygame.Color('white')
    color = color_inactive
    active = False
    text = ''
    txt_surface = font.render(text, True, color)
    width = max(200, txt_surface.get_width() + 10)
    input_box.w = width
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print('Text entered', text)
                        running = False
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    elif len(text) < 12:
                        text += event.unicode
                    txt_surface = font.render(text, True, color)
                    width = max(200, txt_surface.get_width() + 10)
                    input_box.w = width
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
                
        pygame.draw.rect(screen, color, input_box)
        txt_surface = font.render(text, True, "black")
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)
        
        pygame.display.flip()
        
    return text

def main():
    pygame.init()

    x = 370
    y = 650
    y_extra = 202
    screen = pygame.display.set_mode((x,y))
    
    line_width = 4
    padding = 15
    line_length = 330
    pygame.display.set_caption("Tic-Tac-Toe")
    font = pygame.font.Font(None, 50)
    player1 = "Player 1"
    player2 = "Player 2"
    win = False
    
    block_flag = {"block_1":0, "block_2":0, "block_3":0, "block_4":0, "block_5":0, "block_6":0, "block_7":0, "block_8":0, "block_9":0 }
    turn = 1
    clock = pygame.time.Clock()
    running = True
    menu = True
    reset = False
    
    while(menu):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
        
        temp = pygame.font.Font(None, 25)
        
        heading_font = pygame.font.Font(None, 100)
        screen.fill("black")
        heading = heading_font.render("Tic", False, "red")
        screen.blit(heading, (15, 50))
        heading = heading_font.render("Tac", False, "green")
        screen.blit(heading, (120, 50))
        heading = heading_font.render("Toe", False, "red")
        screen.blit(heading, (240, 50))
        text = temp.render("Enter name in blank and press Enter.", True, 'white')
        screen.blit(text, (33, 150))
        
        pygame.display.flip()
        player1 = text_input(screen, player1, "red", 130, 200, 85, 240)
        player2 = text_input(screen, player2, "green", 130, 320, 85, 360)
        
        if player1 != "Player 1" and player2 != "Player 2":
            menu = False

    while(running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        reset = False
        
        screen.fill("black")
        temp = pygame.font.Font(None, 30)
        
        if (check_for_win(block_flag, screen) == 0 and win == False):
            if turn == 1:
                player1_text = font.render(player1 + "     Turn", True, 'white', None)
                player2_text = font.render(player2, True, 'white', None)
                screen.blit(player1_text, (25, 25))
                screen.blit(player2_text, (25, 95))
            elif turn == 2:
                player1_text = font.render(player1, True, 'white', None)
                player2_text = font.render(player2 + "     Turn", True, 'white', None)
                screen.blit(player1_text, (25, 25))
                screen.blit(player2_text, (25, 95))
                
            draw_grid(screen, x, y, y_extra, line_length, line_width, padding)
            
            if(pygame.mouse.get_pressed()[0]):
                try:
                    empty, present = place_is_empty(block_flag, line_width, padding, y_extra, line_length)    
                    if(empty):
                        block_flag[present] = turn
                        if turn == 1:
                            turn = 2
                        else:
                            turn = 1
                            
                except TypeError:
                    print("Clicked at the wrong place.")
                        
            draw_crosses_circles(block_flag,screen)
            pygame.display.flip()
        
        elif(check_for_win(block_flag, screen) == 1 and win == False):
            
            draw_grid(screen, x, y, y_extra, line_length, line_width, padding)
            draw_crosses_circles(block_flag,screen)
            
            print("player 1 wins")
            player1_text = font.render(player1 + "      Win", True, 'white', None)
            player2_text = font.render(player2 + "     Lose", True, 'white', None)
            screen.blit(player1_text, (25, 25))
            screen.blit(player2_text, (25, 95))
            
            screen.blit(temp.render("Press ESC to close.", True, 'white'), (25, 150))
            
            reset_button = pygame.Rect(260 , 580, 73, 30)
            pygame.draw.rect(screen, 'white', reset_button)
            screen.blit(temp.render("Reset", True, 'black'), (270, 585))
            
            pygame.display.flip()
            
            while(win == False and reset == False):
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if reset_button.collidepoint(event.pos):
                            print("Resetting")
                            block_flag = {"block_1":0, "block_2":0, "block_3":0, "block_4":0, "block_5":0, "block_6":0, "block_7":0, "block_8":0, "block_9":0 }
                            turn = 1
                            reset = True
                    if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                        if event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
                            win = True
                            break
                    
                
        elif(check_for_win(block_flag, screen) == 2 and win == False):
            draw_grid(screen, x, y, y_extra, line_length, line_width, padding)
            draw_crosses_circles(block_flag,screen)
            
            print("player 2 wins")
            player1_text = font.render(player1 + "     Lose", True, 'white', None)
            player2_text = font.render(player2 + "      Win", True, 'white', None)
            screen.blit(player1_text, (25, 25))
            screen.blit(player2_text, (25, 95))
            
            screen.blit(temp.render("Press ESC to close.", True, 'white'), (25, 150))
            
            reset_button = pygame.Rect(260 , 580, 73, 30)
            pygame.draw.rect(screen, 'white', reset_button)
            screen.blit(temp.render("Reset", True, 'black'), (270, 585))
            
            pygame.display.flip()
            while(win == False and reset == False):
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if reset_button.collidepoint(event.pos):
                            print("Resetting")
                            block_flag = {"block_1":0, "block_2":0, "block_3":0, "block_4":0, "block_5":0, "block_6":0, "block_7":0, "block_8":0, "block_9":0 }
                            turn = 1
                            reset = True
                    if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                        if event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
                            win = True
                            break
            
            
        elif(check_for_win(block_flag, screen) == 3 and win == False):
            draw_grid(screen, x, y, y_extra, line_length, line_width, padding)
            draw_crosses_circles(block_flag,screen)
            
            print("draw in both players")
            player1_text = font.render(player1 + "     Draw", True, 'white', None)
            player2_text = font.render(player2 + "     Draw", True, 'white', None)
            screen.blit(player1_text, (25, 25))
            screen.blit(player2_text, (25, 95))
            
            screen.blit(temp.render("Press ESC to close.", True, 'white'), (25, 150))
            
            reset_button = pygame.Rect(260 , 580, 73, 30)
            pygame.draw.rect(screen, 'white', reset_button)
            screen.blit(temp.render("Reset", True, 'black'), (270, 585))
            
            pygame.display.flip()
            while(win == False and reset == False):
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if reset_button.collidepoint(event.pos):
                            print("Resetting")
                            block_flag = {"block_1":0, "block_2":0, "block_3":0, "block_4":0, "block_5":0, "block_6":0, "block_7":0, "block_8":0, "block_9":0 }
                            turn = 1
                            reset = True
                    if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                        if event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
                            win = True
                            break
        
        else:
            running = False
            break        
        
        clock.tick(60)


    pygame.quit()


if __name__ == "__main__":
    main()