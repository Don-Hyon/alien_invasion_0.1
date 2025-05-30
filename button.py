import pygame.font 

class Button: 

    def __init__(self, ai_game, msg): 
        """"Init. button attributes.""" 
        self.screen = ai_game.screen 
        self.screen_rect = self.screen.get_rect() 

        # Set dimensions and properties of the button. 
        self.width, self.height = 300, 75 
        self.button_color = (228, 77, 46) # RGB of cinnabar (trigonal/alpha HgS). 
        self.text_color = (255, 255, 255) 
        self.font = pygame.font.SysFont(None, 48) 

        # Build Button's rect object and center it. 
        self.rect = pygame.Rect(0, 0, self.width, self.height) 
        self.rect.center = self.screen_rect.center 

        # Button message needs to be prepped only once. 
        self._prep_msg(msg) 
    
    def _prep_msg(self, msg): 
        """Turn msg into rendered image and center text on button.""" 
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color) 
        self.msg_image_rect = self.msg_image.get_rect() 
        self.msg_image_rect.center = self.rect.center 
    
    def draw_button(self): 
        # Draw blank button and draw message. 
        self.screen.fill(self.button_color, self.rect) 
        self.screen.blit(self.msg_image, self.msg_image_rect) 