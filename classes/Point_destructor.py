class Vehicle:
    def __init__(self):
        print('Vehicle created.')

    def __del__(self):
        print('Destructor called, vehicle deleted.')

car = Vehicle()
del car
