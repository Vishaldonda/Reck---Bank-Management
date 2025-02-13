# open file write context manger 
#     - print "file is opening " - enter operation
#     - exited __exit__ - exit operation

#     prob: Write a simple context manager that opens a file,
# writes some text into it,
# and then automatically closes it
# when the context is exited.
# Use the with statement to manage the file handling.

class FileManager():
    def __init__(self,file_name,mode):
        self.file_name = file_name
        self.mode = mode
        self.file  = None
         
    def __enter__(self):
        self.file = open(self.file_name,self.mode)
        print("file opened")
        return self.file
     
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()
        print('file closed')
 
with FileManager("iter_lines.csv",'a') as file:
    print("Writing into file...")
    file.write("\nAdded line via context manager")