class x:
    def q(self):
        print("main0")
    def w(self):
        print("main1")


class y(x):
    def e(self):
        print("slave")
    def q(self):
        print("slave1")

a=x()
b=y()

a.q()
b.q()



