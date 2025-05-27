class Settings: 
    """A class to store all settings for Alien Invasion.""" 

    def __init__(self): 
        """Game's settings initialized.""" 
        # Screen settings 
        self.screen_width = 960 
        self.screen_height = 960 
        self.bg_color = (0, 12, 25) 

        # Ship settings 
        self.ship_speed = 0.5 

        # Bullet settings 
        self.bullet_speed = 2 
        self.bullet_width = 3 
        self.bullet_height = 15 
        self.bullet_color = (125, 249, 255) 
        self.bullets_allowed = 2000 