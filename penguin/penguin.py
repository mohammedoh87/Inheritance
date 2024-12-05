class bird:
    def __init__(self):
        print("Bird is ready")
    def who(self):
        print("Bird")
    def swim(self):
        print("swim faster")

class penguin(bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")
    def who(self):
        print("Penguin")
    def run(self):
        print("run faster")

ob1 = penguin()
ob1.who()
ob1.swim()
ob1.run()