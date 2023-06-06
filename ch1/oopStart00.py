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

    def getShot(self):
        if self.sensorType == 'Digital':
            print(f'Your {self.model} takes a shot! Your jpeg file is ready')
        elif self.sensorType == 'Analog':
            print(f'Your analog granny {self.model} takes a shot! You need to find film laboratory for film develop')
        else:
            print("I don't understand, what do you want?")

    def getBuy(self, cash):
        if self.price == cash:
            return f'Give me your {cash} and take this camera, my dear customer'
            print(f'Give me your {cash} and take this camera, my dear customer')
        elif self.price < cash:
            return 'Take your new camera and yours ' + str(cash - self.price) + '$! My congrats!'
            print('Take your new camera and yours ' + str(cash - self.price) + '$! My congrats!')
        elif self.price > cash:
            return 'You need some money. How about ' + str(self.price - cash) + '$?'
            print('You need some money. How about ' + str(self.price - cash) + '$?')
        else:
            return "I don't understand, what do you want?"
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
# print(fujifilmX100v.__dict__)



canon5DIII = Camera('Canon', '5D Mark III', 'Full-Frame', 'Digital', 'FX', 1.0, 500)

# canon5DIII.getShot()
# fujifilmX100v.getBuy(1000)
# canon5DIII.getBuy(300)

def test_buying_exist_camera():
    """testing Camera class getBuy method"""

    tSumEq = 1000
    t1 = f"Give me your {tSumEq} and take this camera, my dear customer"
    t2 = fujifilmX100v.getBuy(1000)
    assert t1 == t2

def test_buying_new_camera_eq():
    """testing Camera class getBuy method"""

    pentaxMX1 = Camera('Pentax', 'MX-1', '1/1.5', 'Digital', 'None', 2.5, 250)

    x = 250
    t1 = f"Give me your {pentaxMX1.price} and take this camera, my dear customer"
    t2 = pentaxMX1.getBuy(x)
    assert t1 == t2


def test_buying_new_camera_more():
    """testing Camera class getBuy method"""

    pentaxMX1 = Camera('Pentax', 'MX-1', '1/1.5', 'Digital', 'None', 2.5, 250)

    x = 300
    t1 = 'Take your new camera and yours ' + str(x - pentaxMX1.price) + '$! My congrats!'
    t2 = pentaxMX1.getBuy(x)
    assert t1 == t2

def test_buying_new_camera_not_enough():
    """testing Camera class getBuy method"""

    pentaxMX1 = Camera('Pentax', 'MX-1', '1/1.5', 'Digital', 'None', 2.5, 250)

    x = 100
    t1 = 'You need some money. How about ' + str(pentaxMX1.price - x) + '$?'
    t2 = pentaxMX1.getBuy(x)
    assert t1 == t2

# nikon = Camera('Nikon', '3100', '1/1:4', 'Digital', 'None', 3, 100)
# nikon.getBuy(200)