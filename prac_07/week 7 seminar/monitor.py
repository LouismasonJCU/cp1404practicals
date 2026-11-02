class monitor:
    """represent a monitor with its width and height"""
    def __init__(self,model: str,width:int,height:int):
        """intitialize all the attributes"""
        self.model = model
        self.width = width
        self.height = height

    def __str__(self) :
        return f"{self.model} {self.width} x {self.height}"

    def get_resolution (self):
        """returns the tuples with width and height"""
        return self.width,self.height

    def get_total_pixels (self):
        """get the total number of pixels"""
        return self.width * self.height

    def __eq__(self, other):
        self.width,self.height = other.get_resolution()