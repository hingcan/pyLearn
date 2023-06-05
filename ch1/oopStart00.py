"""
class Cameras:
    brend = "Default"
    model = "Default"
    format = "Default"
    type = "Default"
    cropFactor = 1.0
    price = 0

class Optics:
    brend = "Default"
    model = "Default"
    autofocus = False



#fujiX100V = Cameras("Fujifilm", "X100V", "APS-C", "Digital", 1000)

canon = Cameras


freetime = True

if freetime:
    print("Axpers, let's go to have a lunch!")

else:
    print("Sorry, axpers, i'm so busy")
"""


class Camera(object):
    """Cameras class include: brand, model, sensorSize, sensorType, bayonet, cropFactor, price"""

    def __init__(self, brand='Null', model='Null', sensorSize='Null', sensorType='Null', bayonet='Null', cropFactor='Null', price='Null'):
        super(Camera, self).__init__()
        self.brand = brand
        self.model = model
        self.sensorSize = sensorSize
        self.sensorType = sensorType
        self.bayonet = bayonet
        self.cropFactor = cropFactor
        self.price = price

    def get_shot(self, model):
        if self.sensorType == 'Digital':
            print(f'Your {model} takes a shot! Your jpeg file is ready')
        elif self.sensorType == 'Analog':
            print(f'Your analog granny {model} takes a shot! You need to find film laboratory for film develop')
        else:
            print("I don't understand, what do you want?")



class Objective(object):
    """Cameras class include: brand, model, autoFocus, focusLength, bayonet, stabilizer, price"""

    def __init__(self, brand, model, autoFocus, focusLength, apperture, bayonet, stabilizer, price):
        super(Objective, self).__init__()
        self.brand = brand
        self.model = model
        self.autoFocus = autoFocus
        self.focusLength = focusLength
        self.apperture = apperture
        self.bayonet = bayonet
        self.stabilizer = stabilizer
        self.price = price


fujifilmX100v = Camera('Fujifilm', 'X100F', 'APS-C', 'Digital', 'Fixed', 1.5, 1000)

canon50mm14 = Objective('Canon', '50 USM 1.4', True, 50, 1.4, 'FX', False, 200)
print(fujifilmX100v.__dict__)



canon5DIII = Camera('Canon', '5D Mark III', 'Full-Frame', 'Digital', 'FX', 1.0, 500)
canon5DIII.get_shot('5D Mark III')
