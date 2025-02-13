class MyList:
  def __init__(self,*args):
      self.ind = 0
      self.arr = []
      for item in args:
          for ele in item:
              self.arr.append(ele)
    
  def __iter__(self):
    return self

  def __next__(self):
    try:
        if self.ind >= len(self.arr):
            raise StopIteration  # Stop iteration when all elements are exhausted
        value = self.arr[self.ind]  # Get the next valu
        self.ind +=1
        return value
        
    except StopIteration:
        raise
n = 5
myclass = MyList([1,2],[3,4],[5])
myiter = iter(myclass)

for x in myiter:
  print(x)
  

