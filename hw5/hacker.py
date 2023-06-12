import os

My_path = 'D:/coding_file/study/Lesson/oo_lesson/OO/test/hw5'
# names = ['Caster', 'Saber', 'Rider', 'Lancer',
#          'Archer', 'Assign']  # other person jar name
names = ['code']  # other person jar name

os.chdir(My_path)
i = 0
# os.system('python production.py')
while i <= len(names)-1:
    print(">>>>>The comparison result with "+str(names[i]) + " is:")
    os.system('.\datainput_student_win64.exe | java -jar '+str(names[i])+'.jar > stdout.txt')
    os.system('python outputChecker.py')
    i = i+1
