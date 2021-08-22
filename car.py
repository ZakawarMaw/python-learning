class Car :
    sterringWheel=1 #Class level attribute
    def __init__ (self,name,wheels):
        self.name=name  # Instance level attribute
        self.wheels=wheels
    def drive(self):
        print(f'{self.name} is driving')

    @classmethod
    def common(cls) :
         print(f'All car have only {Car.sterringWheel} sterring wheel');

# suzuki=Car("BW",4)
# suzuki.drive()
# print(f'Suzuki sterring wheel is {suzuki.sterringWheel}')
# suzuki.common();

# marcedes=Car("Marcedes",4)
# marcedes.drive()
# print(f'Marcedes sterring wheel is {marcedes.sterringWheel}')
# marcedes.common();

# print(Car.sterringWheel);  # call Class level attribute

# Car.common();  # call Class level method