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
        self.ship_limit = 2 

        # Bullet settings 
        self.bullet_speed = 5 
        self.bullet_width = 5 
        self.bullet_height = 25 
        self.bullet_color = (125, 249, 255) 
        self.bullets_allowed = 2000 

        # Alien settings 
        self.alien_speed = 0.050 
        self.fleet_drop_speed = 20 
        # fleet_direction of 1 represents right; -1 represnts left. 
        self.fleet_direction = 1 