def __init__(self):
    self.bindings = {"up": pygame.K_UP,
                     "down":  pygame.K_DOWN,
                     "left":  pygame.K_LEFT,
                     "right":   pygame.K_RIGHT,
                     "lp":  pygame.K_a,
                     "mp":  pygame.K_s,
                     "hp":  pygame.K_d,
                     "lk":  pygame.K_z,
                     "mk":  pygame.K_x,
                     "hk":  pygame.K_c,
                     "pause":   pygame.K_RETURN}

    self.inputState = {"up": False,
                   "down": False,
                   "right": False,
                   "left": False,
                   "lp": False,
                   "mp": False,
                   "hp": False,
                   "lk": False,
                   "mk": False,
                   "hk": False,
                   "pause": False}
