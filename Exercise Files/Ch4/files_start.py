#
# Read and write files using the built-in Python file methods
#

def main():  
  # Open a file for writing and create it if it doesn't exist
  # The second argument in the open function call determines the mode (write, read, append, etc.)
  #f = open("textfile.txt", "w+")

  # Open the file for appending text to the end
  f = open("textfile.txt", "r")

  # write some lines of data to the file
  # for i in range(10):
  #   f.write("This is line " + str(i) + "\n")
  
  # close the file when done
  #f.close()
  
  # Open the file back up and read the contents
  if f.mode == 'r':
    #contents = f.read()
    fl = f.readlines()
    for x in fl:
      print(x)
    #print(contents)
    
if __name__ == "__main__":
  main()
