try:  
    with open("test.txt", mode = 'w') as my_file:
            text = my_file.write(": 0")
            print(text)
except FileNotFoundError as err:
      print("file not found")
      raise err
except IOError as err:
      print("IO Error")
      raise err