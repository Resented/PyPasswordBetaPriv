import os
import time
#vars
pathNameLength = len(os.path.basename(__file__))
pathModule = __file__[:-pathNameLength]
path = pathModule+'PPTData/PPT.py'
os.system('cls')
code = ''
s1 = '    '
s2 = '        '
s3 = '            '
s4 = '                '
s5 = '                    '
s6 = '                        '
s7 = '                            '
s8 = '                                '
firstnumber = ''
lastdigit = 0
lastcharacterpos = 0
errorsentence = '<<< --Error--: something went wrong'
commands = '.calc cls help start powershell cmd .r'
print('PPL [version 0.0]')
while True:
    #redefine
    code = input('>>>')
    if code =='help':
        print(s1+'<<<'+'commands:')
        print(s2+'<<<'+'.info: this command will give you info about PPT.')
        print(s2+'<<<'+'.calc: this command is used to calculate stuff.')
        print(s2+'<<<'+'.cls: this command is used to clear everything on the screen.')
        print(s2+'<<<'+'.taskkill: this command is used to close tasks.')
        print(s2+'<<<'+'.open: this command is used to read and write things in a file.')
        print(s2+'<<<'+'.r: this command is used to refresh the program.')
        print(s2+'<<<'+'.cmd: this command is used to start cmd.')
        print(s2+'<<<'+'.powershell: this command is used to open powershell.')
        print(s1+'<<<'+'output:')
        print(s2+'<<<'+'>>> is where the user types stuff')
        print(s2+'<<<'+'<<< is where the terminal writes the outputs to commands')
    if code == '.calc':
        try:
            print('<<<help available')
            calculation = input(s1+'>>>')
            if calculation == 'help':
                print(s1+'<<<'+'help:')
                print(s2+'<<<'+'functionhelp:')
                print('<<<'+s3+'*   this is multiply')
                print('<<<'+s3+'/   this is divide')
                print('<<<'+s3+'+   this is add')
                print('<<<'+s3+'-   this is subtrction')
                print(s2+'<<<'+'numberhelp:')
                print('<<<'+s3+'the first number of your calculation is the number before the function.')
                print('<<<'+s3+'the second number of your calculation is the number after the function.')
            else:
                functionpos=calculation.rfind('+')
                prefunction = '+'
                if functionpos == -1:
                    functionpos=calculation.rfind('*')
                    prefunction = '*'
                    if functionpos == -1:
                        functionpos=calculation.rfind('^')
                        prefunction = '^'
                        if functionpos == -1:
                            functionpos=calculation.rfind('-')
                            prefunction = '-'
                            if functionpos == -1:
                                functionpos=calculation.rfind('/')
                                prefunction = '/'
                firstnum = calculation[0:functionpos]
                presecondnum1 = functionpos+1
                presecondnum2 = len(calculation)
                secondnum = calculation[(functionpos+1):(len(calculation))]
                if prefunction == '+':
                    endsum=(int(firstnum)+int(secondnum))
                elif prefunction == '-':
                    endsum=(int(firstnum)-int(secondnum))
                elif prefunction == '*':
                    endsum=(int(firstnum)*int(secondnum))
                elif prefunction == '^':
                    endsum=(int(firstnum)**int(secondnum))
                elif prefunction == '/':
                    endsum=(int(firstnum)/int(secondnum))          
                if prefunction == '+' or '-' or '*' or '^' or '/':
                    pass
                else:
                    print(errorsentence)
                print('<<<'+str(endsum))
        except Exception:
            print('<<< --Error-- invalid calculation/function input')
    if code == '.cls':
        try:
            os.system('cls')
            print('PPT [version 0.0]')
        except Exception:
            print(errorsentence)
    if '.start' in code:
        try:
            objecttoexecute = input(s1+'>>>')
            os.system('start '+objecttoexecute)
            print('successfull execution')
        except Exception:
            print('<< --Error-- could not find '+objecttoexecute)
    if code == '.r':
            os.system('start py '+pathModule+'PPT.py & taskkill /im python3.8.exe')
            quit()
    if code == '.cmd':
        os.system('start cmd')
    if code == '.powershell':
        os.system('start powershell')
    if '.terminatetask' in code or '.taskkill' in code:
        print(s1+'<<< help available')
        killmethod=input(s1+'>>>')
        if killmethod == 'help':
            print(s2+'<<<help:')
            print(s3+'<<<after you type taskkill it will ask for the killmethod.')
            print(s4+'<<<killmethods:')
            print(s3+'<<<taskname: if you type taskname it will then ask you for the name of the task you want to kill.')
            print(s3+'<<<taskid: it you type taskid it will then ask your for the pid of the task you want to kill.')
            print(s3+'<<<after you have entered the killmethod it will ask you for the taskname or taskid of the task you want to kill.')
            print(s3+'<<<you can get tasks pid by opening cmd and typing tasklist')
            print(s3+'<<<you can get a tasksk name by again, opening cmd and typing tasklist.')
            print(s3+'<<<after you have entered your taskname or taskid, it will ask you for a attribute')
            print(s4+'<<<attributes:')
            print(s3+'<<<force: if your attribute is force it forces the system to kill the task')
            print(s3+'<<<repeat: if your attribute is repeat it will continouisly kill the task')
            print(s3+'<<<examples:')
            print(s3+'<<<')
            print(s3+'<<<')
            print(s3+'>>>.taskkill')
            print(s4+'<<< help available')
            print(s4+'>>>taskname')
            print(s5+'>>>exampletaskname')
            print(s6+'>>>repeat')
            print(s3+'<<<')
            print(s3+'<<<')
            print(s3+'<<<output:')
            print(s4+'<<<success! sent taskkill signal to pid 12523')
            print(s4+'<<<success! sent taskkill signal to pid 12523')
            print(s4+'<<<success! sent taskkill signal to pid 12523')
            print(s4+'<<<success! sent taskkill signal to pid 12523')
            print(s4+'<<<success! sent taskkill signal to pid 12523')
            print(s4+'<<<success! sent taskkill signal to pid 12523')
            print(s4+'<<<success! sent taskkill signal to pid 12523')
            print(s3+'<<<example2:')
            print(s3+'<<<')
            print(s3+'<<<')
            print(s3+'>>>.taskkill')
            print(s4+'<<< help available')
            print(s4+'>>>taskid')
            print(s5+'>>>4579')
            print(s6+'>>>force')
            print(s3+'<<<')
            print(s3+'<<<')
            print(s3+'<<<output:')
            print(s4+'<<<Success! killed task with pid 4579')
        if killmethod == 'taskname':
            taskname = input(s2+'>>>')
            attributes = input(s3+'>>>')
            if attributes == 'force':
                attributes = '/f'
            elif attributes == 'repeat':
                attributes = ''
                command = ('taskkill '+' /im '+taskname)
                for i in range(18446744073709551614):
                    os.system(command)
            if attributes != '':
                command = ('taskkill '+attributes+' /im '+taskname)
                os.system(command)
        if killmethod == 'taskid':
            taskid = input(s2+'>>>')
            attributes = input(s3+'>>>')
            if attributes == 'force':
                attributes = '/f'
            if attributes == 'repeat':
                command = ('taskkill '+' /pid '+taskid)
                for i in range(18446744073709551614):
                    os.system(command)
            command = ('taskkill '+attributes+' /pid '+taskid)
            os.system(command)
    if code == '.open':
        print(s1+'<<<help available')
        filepath = input(s1+'>>>')
        if filepath == 'help':
            print(s2+'<<<help unavailable right now. check later')
        openmode = input(s2+'>>>')
        if openmode == 'read':
            while True:
                openmode = 'r'
                openedfile = open(filepath,openmode)
                readway = input(s3+'>>>')
                if readway == 'readline':
                    linenum = input(s4+'>>>')
                    ttr = 0
                    for line in openedfile:
                        ttr += 1
                        if ttr == int(linenum):
                            print(line)
                if readway == 'all':
                    text = ''
                    for line in openedfile:
                        text += line
                    print(text)
                    text = ''
                if readway == 'search':
                    text = ''
                    substring = input(s4+'>>>')
                    for line in openedfile:
                        text += line
                    if substring in text:
                        substringindex = text.rfind(substring)
                        print(s4+substring+'was found at column '+str(substringindex))
                    else:
                        print('not found')
                if readway == 'exit':
                    break
        elif openmode == 'write':
            openmode = 'w'
            openedfile = open(filepath,'a')
            while True:
                openedfile = open(filepath,'a')
                stringtowrite = input(s2+'>>>')
                if '--nowrite' in stringtowrite:
                    pass
                else:
                    openedfile.write(stringtowrite)
                if stringtowrite == '--nowrite .del':
                    open(filepath,'w').close()
                if stringtowrite == '--nowrite .close':
                    openedfile.close()
                    break
    if code != '.taskkill' or code != 'taskterminate'or code != '.powershell' or code != '.cmd' or code != '.r'or code != '.cls'or code != '.calc' or code !='.open':
        print('<<< --Error-- invalid command')