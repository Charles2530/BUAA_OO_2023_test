import sympy
import os

My_path = 'D:/coding_file/study/Lesson/oo_lesson/OO/test/hw1'
names = ['Caster', 'Saber', 'Rider', 'Lancer',
         'Archer', 'Assign']  # other person jar name
# names = ['Caster', 'Lancer',
#          'Archer', 'Assign']  # other person jar name


def judge_equal(expr_in, expr_out, name):
    simpy_in = sympy.core.sympify(expr_in)
    simpy_out = sympy.core.sympify(expr_out)
    if (simpy_in.equals(simpy_out)):
        print("success!!!")
    else:
        print("failed!!!")
        with open(My_path+'/src/error_log.txt', 'a+') as h:
            h.write(str(name)+":error"+"\n")
            h.write("expr_in:"+str(expr_in)+"\n")
            h.write("simpy_in:"+str(simpy_in)+"\n")
            h.write("expr_out:"+str(expr_out)+"\n")
            h.write("simpy_out:"+str(simpy_out)+"\n")
            h.write("---------------------------\n")


num = 1
os.chdir(My_path)
while(num <= 1):
    print('num = ' + str(num))
    i = 0
    # os.system('python production.py')
    while i <= len(names)-1:
        print(">>>>>The comparison result with "+str(names[i]) + " is:")
        os.system('java -jar '+str(names[i])+'.jar < src/in.txt > src/out.txt')
        with open(My_path+'/src/in.txt', 'r+') as f:
            expr_in = f.read().rstrip()
        with open(My_path+'/src/out.txt', 'r+') as g:
            expr_out = g.read().rstrip()
        judge_equal(expr_in, expr_out, names[i])
        i = i+1
    num = num+1
