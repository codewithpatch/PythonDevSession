class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name)
        print("Im color " + self.color)
        print("My weight is " + str(self.weight))
        print("")
#r1.name = "Tom"
#r1.color = "Red"
#r1.weight = 30

#r2 = Robot()
#r2.name = "Jerry"
#r2.color = "Blue"
#r2.weight = 40

r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)

r1.introduce_self()
r2.introduce_self()