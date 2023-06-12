import random
import sys

My_path = 'D:\\coding_file\\study\\Lesson\\oo_lesson\\OO\\test\\hw1'

Var = ['x', 'y', 'z']
Op = ['+', '-']
cnt = 3
maxi = sys.maxsize
# maxi = 2
poly_num = 1


class get_Code:
    def __init__(self):
        self.get_Exp()
        self.main()
        self.get_Con()
        self.get_Factor()
        self.get_Expr()
        self.get_Poly()
        self.get_Mono()
        self.get_Var()

    def get_Poly(self):
        s = self.get_Mono()
        num = random.randint(0, poly_num)
        i = 0
        for i in range(num):
            random2 = random.randint(0, len(Op)-1)
            op = Op[random2]
            s += str(op)+self.get_Mono()
            i = i + 1
        return s

    def get_Mono(self):
        s = self.get_Factor()
        num = random.randint(0, 2*poly_num)
        i = 0
        for i in range(num):
            # s += "*"+str(Op[random.randint(0, len(Op)-1)])+self.get_Factor()
            s += "*"+self.get_Factor()
            i = i+1
        return s

    def get_Exp(self):
        base = random.randint(-1*maxi, maxi)
        exp = random.randint(0, 8)
        random1 = random.randint(0, len(Var)-1)
        var = Var[random1]
        return str(base)+" *"+str(var)+"** +"+str(exp)

    def get_Con(self):
        base = random.randint(-1*maxi, maxi)
        return str(base)

    def get_Var(self):
        base = random.randint(-1*maxi, maxi)
        random2 = random.randint(0, len(Var)-1)
        var = Var[random2]
        return str(base)+" *"+str(var)

    def get_Factor(self):
        # Factor_list = [self.get_Con(), self.get_Exp(), self.get_Expr()]
        Factor_list = [self.get_Con(), self.get_Exp(), self.get_Var()]
        ans = random.randint(0, len(Factor_list)-1)
        return Factor_list[ans]

    def get_Expr(self):
        return "("+self.get_Poly()+")"

    def main(self):
        R = ['+', '-', '*']
        self.code = self.get_Poly()
        i = 0
        for i in range(0, 5):
            ran = random.randint(0, len(R)-1)
            self.code = self.code+str(R[ran])+self.get_Expr()
            i += 1


with open(My_path+'\\src\\in.txt', 'w+') as f:
    a = get_Code()
    f.write(a.code)
    # print(a.code)
