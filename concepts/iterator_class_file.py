import csv 

# with open("iter_lines.csv","r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
        
        
class MyClass:
  def __init__(self):
      self.file_name = "iter_lines.csv"
      self.mode = 'r'
      self.file = open(self.file_name, self.mode)  # Open the file
      self.reader = csv.reader(self.file) 
      
      
  def __iter__(self):
    return self

  def __next__(self):
    try:
      return next(self.reader)  
    except StopIteration:
      raise

n = 5
myclass = MyClass()
myiter = iter(myclass)

for x in myiter:
  print(x)
