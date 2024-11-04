class Circle:

    def __init__(self):
        self.num = [10, 501, 22, 37, 100, 999, 87, 351]

    def read_number(self):
        print(self.num)
value = Circle()
value.read_number()




class MyClass:
    a = 33  
    pi = 3.141

    def __privMeth(self):
        print("I'm inside class MyClass")

    def hello(self):
        print("Private Variable value:", MyClass.a)
foo = MyClass()
foo.hello()
print(foo.a)
print("Value of pi:", MyClass.pi)




class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.141 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.141 * self.radius 

NewCircle = Circle(7)
print("Area:", NewCircle.area())
print("Perimeter:", NewCircle.perimeter())




class TV:
    
    def __init__(self, brand, price, inches):
        self.brand = brand
        self.channel = 1       
        self.price = price
        self.inches = inches
        self.on = False        
        self.volume = 50       

    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False

    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def set_channel(self, channel):
        if 1 <= channel <= 50:
            self.channel = channel

    def reset(self):
        self.channel = 1
        self.volume = 50

    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"

class LedTV(TV):
    def __init__(self, brand, price, inches, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand, price, inches)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def viewing_angle(self):
        return "Viewing angle: 178 degrees"

    def backlight(self):
        return "Backlight: LED"

    def display_details(self):
        return (f"LED TV Details:\n"
                f"Brand: {self.brand}\n"
                f"Price: ${self.price}\n"
                f"Inches: {self.inches}\n"
                f"Screen Thickness: {self.screen_thickness} mm\n"
                f"Energy Usage: {self.energy_usage} W\n"
                f"Lifespan: {self.lifespan} years\n"
                f"Refresh Rate: {self.refresh_rate} Hz\n"
                f"{self.viewing_angle()}\n"
                f"{self.backlight()}")

class PlasmaTV(TV):
    def __init__(self, brand, price, inches, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand, price, inches)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def viewing_angle(self):
        return "Viewing angle: 160 degrees"

    def backlight(self):
        return "Backlight: Plasma"

    def display_details(self):
        return (f"Plasma TV Details:\n"
                f"Brand: {self.brand}\n"
                f"Price: ${self.price}\n"
                f"Inches: {self.inches}\n"
                f"Screen Thickness: {self.screen_thickness} mm\n"
                f"Energy Usage: {self.energy_usage} W\n"
                f"Lifespan: {self.lifespan} years\n"
                f"Refresh Rate: {self.refresh_rate} Hz\n"
                f"{self.viewing_angle()}\n"
                f"{self.backlight()}")

if __name__ == "__main__":
    my_tv = TV("Panasonic", 500, 55)
    my_tv.turn_on()
    my_tv.set_channel(8)
    for _ in range(25):  
        my_tv.increase_volume()
    print(my_tv.status())
    
    led_tv = LedTV("Samsung", 700, 65, 30, 100, 10, 120)
    led_tv.turn_on()
    led_tv.set_channel(5)
    led_tv.increase_volume()
    print(led_tv.status()) 
    print(led_tv.display_details())

    plasma_tv = PlasmaTV("LG", 600, 60, 40, 150, 8, 60)
    plasma_tv.turn_on()
    plasma_tv.set_channel(3)
    plasma_tv.decrease_volume()
    print(plasma_tv.status()) 
    print(plasma_tv.display_details())

