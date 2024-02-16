from tires.tires import Tires


class Carrigan(Tires):
    def __init__(self, sensors):
        self.sensors = sensors
        
    def needs_service(self):
        if any(x >= 0.9 for x in self.sensors):
            return True
        else:
            return False