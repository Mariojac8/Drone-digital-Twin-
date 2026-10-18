class Drone:
    def __init__(self):
        self.status = "Off"
        self.battery = 100
        self.altitude = 0
        self.speed = 0
        self.location = "Home"

    def start(self):
        self.status = "On"
        print("Drone turned on.")

    def take_off(self):
        if self.status == "On" and self.battery > 0:
            self.altitude = 10
            self.battery -= 10
            print("Drone took off to 10 feet.")
        else:
            print("Drone must be on and have battery to take off.")

    def increase_speed(self):
        if self.altitude > 0:
            self.speed += 5
            self.battery -= 5
            print("Speed increased to", self.speed, "mph.")
        else:
            print("Drone must be flying to increase speed.")

    def move(self):
        if self.altitude > 0:
            self.location = "Soccer Field"
            self.battery -= 10
            print("Drone moved to the", self.location)
        else:
            print("Drone must take off first.")

    def land(self):
        self.altitude = 0
        self.speed = 0
        print("Drone landed.")

    def display_status(self):
        print("Status:", self.status)
        print("Battery:", self.battery, "%")
        print("Altitude:", self.altitude, "feet")
        print("Speed:", self.speed, "mph")
        print("Location:", self.location)
        print()


# Create a drone and try each method
my_drone = Drone()
print("Starting drone simulation")
my_drone.display_status()
my_drone.start()
my_drone.take_off()
my_drone.increase_speed()
my_drone.move()
my_drone.display_status()
my_drone.land()
my_drone.display_status()
