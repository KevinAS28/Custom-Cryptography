class oke:
 def __init__(self, x, y):
  self.x = x
  self.y = y
 def __add__(self, other):
  return oke(self.x + other.y, self.x + other.y)

 class new:
  def __init__(self, x, y):
   self.x = x
   self.y = y


  def encrypt(self, d):
   return self.x + self.y + d

wow = oke.new(10, 5)
print(wow.encrypt(2))
print(wow.encrypt(100))

