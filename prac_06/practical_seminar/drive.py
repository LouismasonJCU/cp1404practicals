def drive (self,distance):
    """drive a car a given distance if enough fuel."""
    if distance > self.fuel:
        distance = self.fuel
        self.fuel =0
else :
