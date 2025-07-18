class Logger:
    def log(self,msg):
        pass

class ConsoleLogger(Logger):
    def log(self,msg):
        print(f"[Console Log]{msg}")

class FileLogger(Logger):
    def log(self,msg):
        with open ("logger.txt","a",encoding="utf-8") as file:
            file.write(f"{msg}\n")
class Payment:
    def __init__(self,logger):
        self.logger=logger

    def payment(self,amount):
        self.logger.log(f" Payment of ₹{amount}")
print("Using Console Logger:")
consolelog=ConsoleLogger()
pay=Payment(consolelog)
pay.payment(5000)

print("\nUsing File Logger (check log.txt): ")
filelog=FileLogger()
pay=Payment(filelog)
pay.payment(8000)
              