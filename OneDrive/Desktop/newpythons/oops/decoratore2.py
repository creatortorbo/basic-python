# here using decorators 
def nolove(fx):
    def mfx():
         print("Good Morning ")
         fx()
         print("Thanks for using this funtion")
         return mfx 
@hello
def hello():
    print("I am happey")
hello()