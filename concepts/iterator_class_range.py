class MyNumbers:
  def __init__(self,start=0,end=1):
      self.i = start
      self.end = end
      
  def __iter__(self):
    return self

  def __next__(self):
    if self.end == 0:
        print("Provide the end argument")
    if self.i < self.end:
      curr = self.i
      self.i += 1
      return curr
    else:
      raise StopIteration

n = 5
myclass = MyNumbers(end=n)
# myclass = MyNumbers(start = 2, end=5)

myiter = iter(myclass)

for x in myiter:
  print(x)
  


