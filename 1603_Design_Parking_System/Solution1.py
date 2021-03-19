class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.type2slots_count = {
            1: big,
            2: medium,
            3: small,
        }

    def addCar(self, carType: int) -> bool:
        if self.type2slots_count[carType] <= 0:
            return False

        self.type2slots_count[carType] -= 1
        return True


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

def test1():
    obj = ParkingSystem(1, 1, 0)
    res1 = obj.addCar(1)  # True
    res2 = obj.addCar(2)  # True
    res3 = obj.addCar(3)  # False
    res4 = obj.addCar(1)  # False
    if (res1, res2, res3, res4) == (True, True, False, False):
        print('test1 success.')
    else:
        print('test1 failed.')


if __name__ == '__main__':
    test1()

