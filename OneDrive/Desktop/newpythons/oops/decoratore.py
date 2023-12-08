def greet(fx) :
   def mfx ():
      print("good morning ")
      fx()
      print("Thanks for using this funtion")
      return mfx 



@greet 
def hello ():
   print("hello world ")

hello()