import sympy
import os

My_path = 'D:/coding_file/study/Lesson/oo_lesson/OO/test/hw2'


def judge_equal(expr_in, expr_out):
    simpy_in = sympy.core.sympify(expr_in)
    simpy_out = sympy.core.sympify(expr_out)
    if (simpy_in.equals(simpy_out)):
        print(">>>>>The comparison result is:")
        print("success!!!")
    else:
        print(">>>>>The comparison result is:")
        print("failed!!!")
        with open(My_path+'/src/error_log.txt', 'a+') as h:
            h.write("expr_in:"+str(expr_in)+"\n")
            h.write("simpy_in:"+str(simpy_in)+"\n")
            h.write("expr_out:"+str(expr_out)+"\n")
            h.write("simpy_out:"+str(simpy_out)+"\n")
            h.write("---------------------------\n")


os.chdir(My_path)
os.system('java -jar Archer.jar < src/in.txt > src/out.txt')
with open(My_path+'/src/in.txt', 'r+') as f:
    f.readline()
    expr_in = f.read().rstrip()
with open(My_path+'/src/out.txt', 'r+') as g:
    expr_out = g.read().rstrip()
print(expr_out)
