import explorerhat


class Car:
    def __init__(self, speed=100):
        self.speed = speed

    def drive_forwards(self):
        explorerhat.motor.one.forwards(self.speed)
        explorerhat.motor.two.forwards(self.speed)

    def drive_backwards(self):
        explorerhat.motor.one.backwards(self.speed)
        explorerhat.motor.two.backwards(self.speed)

    def turn_right(self):
        explorerhat.motor.one.forwards(self.speed)
        explorerhat.motor.two.stop()

    def turn_left(self):
        explorerhat.motor.one.stop()
        explorerhat.motor.two.forwards(self.speed)

    def set_speed(self, speed):
        self.speed = speed

    @staticmethod
    def stop():
        explorerhat.motor.one.stop()
        explorerhat.motor.two.stop()
