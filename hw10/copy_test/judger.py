import os
import time
import sys
from colorfulPrint import ColorfulPrint

# set names here
# playerName = ['Lancer', 'Archer', 'Rider', 'Caster', 'Assassin', 'Berserker']
# playerName = ['Charles','gx','dt','sj']
# playerName = ['Charles','dt','tjx','tqx','tsx','txx','ygx','thx']
# playerName = ['Charles','dt','tqx','ygx']
playerName = ['Charles','dt']
work_dir='D:\\coding_file\\study\\Lesson\\oo_lesson\\OO\\test\\hw10\\copy_test'
times = []
ans = []
lineNum = []

# set running parameter here
playerNum = len(playerName)
recodeTime = True
displayDetail = True
showTime = True
maxWaCount = 5

def makeLog(num, size, aboutTime = False):
    if aboutTime == False:
        with open('stdin.txt', 'r') as f:
            con = f.read()
        with open('./logWA/stdin' + str(num) + '.txt', 'w') as f:
            f.write(con)
        for i in range(size):
            name1 = 'stdout' + str(i + 1) + '.txt'
            name2 = './logWA/stdout' + str(i + 1) + '_' + str(num) + '.txt'
            with open(name1, 'r') as f:
                con = f.read()
            with open(name2, 'w') as f:
                f.write(con)
    else:
        with open('stdin.txt', 'r') as f:
            con = f.read()
        with open('./logTLE/stdin' + str(num) + '.txt', 'w') as f:
            f.write(con)
        for i in range(size):
            name1 = 'stdout' + str(i + 1) + '.txt'
            name2 = './logTLE/stdout' + str(i + 1) + '_' + str(num) + '.txt'
            with open(name1, 'r') as f:
                con = f.read()
            with open(name2, 'w') as f:
                f.write(con)

def exec(cmd, display = displayDetail):
    if display:
        print('Executing: ' + cmd)
    os.system(cmd)

def init():
    for _ in range(playerNum):
        times.append(0.0)
        ans.append([])

def runAndGetAns(recodeTime):
    for i in range(playerNum):
        name = playerName[i]
        timeBegin = time.time()
        exec('java -jar ' + name + '.jar < stdin.txt > '+name+'_stdout.txt')
        timeEnd = time.time()
        times[i] = timeEnd - timeBegin
        with open(name+'_stdout.txt', 'r') as f:
            ans[i] = f.readlines()
    if recodeTime:
        temp = ''
        for i in range(playerNum):
            temp += str(times[i]) + ','
        temp = temp[:-1]
        temp += '\n'
        with open('time.txt', 'a') as f:
            f.write(temp)

def check():
    waCount = 0
    flag = True
    for i in range(len(ans[0])):
        for j in range(playerNum):
            if j == 0:
                cmp = ans[j][i]
            else:
                if cmp != ans[j][i]:
                    flag = False
                    ColorfulPrint.colorfulPrint('Error in line: ' + str(i + 1) + '!', ColorfulPrint.MODE_BOLD, ColorfulPrint.COLOR_RED)
                    waCount += 1
                    if waCount >= maxWaCount:
                        return False
    return flag

if __name__ == '__main__':
    os.chdir(work_dir)
    init()
    for i in range(int(sys.argv[1])):
        exec('python generate.py > stdin.txt')
        ColorfulPrint.colorfulPrint('>>>>>>>>>> Test ' + str(i + 1) + ' <<<<<<<<<<', ColorfulPrint.MODE_BOLD, ColorfulPrint.COLOR_BLUE)
        runAndGetAns(recodeTime)
        flag = check()
        if flag:
            ColorfulPrint.colorfulPrint('===== Accepted =====', ColorfulPrint.MODE_BOLD, ColorfulPrint.COLOR_GREEN)
        else:
            ColorfulPrint.colorfulPrint('***** Wrong Answer! *****', ColorfulPrint.MODE_BOLD, ColorfulPrint.COLOR_RED)
        if showTime:
            for i in range(playerNum):
                ColorfulPrint.colorfulPrint('>>>>> ' + playerName[i] + ' use time: ' + str(times[i]) + 's <<<<<', ColorfulPrint.MODE_BOLD, ColorfulPrint.COLOR_BLUE)
        if flag == False:
            makeLog(i + 1, playerNum)
            break
        assert flag == True
        