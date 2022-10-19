class Robot:
    def introduce_self(self):
        print("My name is" + self.name) #this is Java

rl = Robot()
rl.name = " Tom"
rl.color = "blue"
rl.weight = "30"

r2 = Robot()
r2.name = " Ichiban"
r2.color = "yellow"
r2.weight = "40"

rl.introduce_self()
r2.introduce_self()


