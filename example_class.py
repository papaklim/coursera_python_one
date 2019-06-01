class Lamp:
    # state = False
    def __init__(self, floor=None):
        self.state = False
        self.floor = floor

    def switch_on(self):
        if self.state:
            return 'Лампа уже включена'
        else:
            self.state = True
            return 'Лампа включилась'


    def switch_off(self):
        if self.state:
            self.state = False
            return "Лампа выключилась"
        else:
            return "Для того, чтобы выключить лампу сначала её нужно включить"


lamp1 = Lamp(1)
lamp2 = Lamp(2)
# print(Lamp.state)
print(lamp1.state)
print(lamp1.floor)
print(lamp2.floor)
print(lamp1.switch_on())
print(lamp1.switch_on())

print(lamp1.state)

print(lamp1.switch_off())
print(lamp1.switch_off())

