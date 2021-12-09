class Waterjug:
    def __init__(self,am,bm,a,b,g):
        self.a_max = am;
        self.b_max = bm;
        self.a = a;
        self.b = b;
        self.goal = g;
    def emptyA(self):
        self.a = 0;
        print ('(', self.a, ',', self.b, ')', "- Applied RULE 1: Empty Jug 1")
    def emptyB(self):
        self.b = 0;
        print ('(', self.a, ',', self.b, ')', "- Applied RULE 2: Empty Jug 2")
    def fillA(self):
        self.a = self.a_max;
        print ('(', self.a, ',',self.b, ')', "- Applied RULE 3: Pour water in Jug 1")
    def fillB(self):
        self.b = self.b_max;
        print ('(', self.a, ',', self.b, ')', "- Applied RULE 4: Pour water in Jug 2")
    def transferAtoB(self):
        while (True):
            self.a = self.a - 1
            self.b = self.b + 1
            if (self.a == 0 or self.b == self.b_max):
                break
        print ('(', self.a, ',', self.b, ')', "- Applied RULE 5: Pour water from Jug 1 to Jug 2")
    def transferBtoA(self):
        while (True):
            self.a = self.a + 1
            self.b = self.b - 1
            if (self.b == 0 or self.a == self.a_max):
                break
        print ('(', self.a, ',', self.b, ')', "- Applied RULE 6: Pour water from Jug 2 to Jug 1")
    def main(self):
        print("Initial State: (0,0)")
        print("Capacity: (",self.a_max,",",self.b_max,")")
        print("Required: (",self.goal,",","y)")
        print("\nStates:")
        while (True):
            if (self.a == self.goal or self.b == self.goal):
                break
            if (self.a == 0):
                self.fillA()
            elif (self.a > 0 and self.b != self.b_max):
                self.transferAtoB()
            elif (self.a > 0 and self.b == self.b_max):
                self.emptyB()
waterjug=Waterjug(5,2,0,0,1);
waterjug.main();
