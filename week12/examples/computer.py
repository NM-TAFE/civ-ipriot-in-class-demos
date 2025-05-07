class Computer():
  def __init__(self, operating_system, disk_space):
    self._operating_system = operating_system
    self._disk_space = disk_space

  def on(self):
    print("The computer turned on")

  def compute(self):
    print("beep boop")

  def operating_system(self):
    print(self._operating_system)


class Laptop(Computer):
  pass
    
laptop = Laptop("Windows 11", 256000000000)
print(laptop.compute())


class Lamp():
  # Same "shape", not necessarily due to inheritance
  def on(self):
    print("BRIGHT")

lamp = Lamp()

for device in [lamp, laptop]:
  device.on()