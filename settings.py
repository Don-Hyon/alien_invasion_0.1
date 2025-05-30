class Settings: 
    """A class to store all settings for Alien Invasion.""" 

    def __init__(self): 
        """Game's static settings initialized.""" 
        # Screen settings 
        self.screen_width = 960 
        self.screen_height = 960 
        self.bg_color = (0, 12, 25) 

        # Ship settings 
        self.ship_limit = 2 

        # Bullet settings 
        self.bullet_width = 5 
        self.bullet_height = 25 
        self.bullet_color = (125, 249, 255) 
        self.bullets_allowed = 2000 

        # Alien settings 
        self.fleet_drop_speed = 20 

        # How quickly the game speeds up 
        self.speedup_scale = 1.2 

        self.initialize_dynamic_settings() 
    
    def initialize_dynamic_settings(self): 
        """Init settings that change throughout the game"""
        self.ship_speed = 0.5 
        self.bullet_speed = 2.00 
        self.alien_speed = 0.10 

        # Fleet_direction of 1 represents right; -1 represnts left. 
        self.fleet_direction = 1 
    
    def increase_speed(self): 
        """Increase speed settings.""" 
        self.ship_speed *= self.speedup_scale 
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale 
