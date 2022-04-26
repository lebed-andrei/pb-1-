class x:
    def q(self):
        print("main0")
    def w(self):
        print("main1")
class y(x):
    def e(self):
        print("slave")

print(issubclass(y,x))
print(issubclass(x,y))
