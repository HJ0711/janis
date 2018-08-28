#-*-coding:utf8-*-
import sys,os,copy

class datas:
    def __init__(self,datas):
        self.datas = datas
        self.datas1 = copy.deepcopy(datas) #정보는 같지만 주소값이 다르게 복사된 리스트
        self.stid = [datas[i][0] for i in range(len(self.datas))] #학번리스트
        self.stname = [datas[i][1] for i in range(len(self.datas))]#이름리스트
        self.mids = [self.datas[i][2] for i in range(len(self.datas))]#중간점수 리스트
        self.fins = [self.datas[i][3] for i in range(len(self.datas))]#기말점수 리스트
        self.search_id = 0

    def gradecheck(self):
        self.points_info = []
        self.grades_info = []
        for i in range(len(self.datas1)):
            self.averages = '%.1f' % (float(self.mids[i]) * 0.5 + float(self.fins[i]) * 0.5)
            if float(self.averages) >= 90:
                self.grade = 'A'
            elif float(self.averages) >= 80:
                self.grade = 'B'
            elif float(self.averages) >= 70:
                self.grade = 'C'
            elif float(self.averages) >= 60:
                self.grade = 'D'
            else:
                self.grade = 'F'
            self.points_info.append(self.averages)
            self.grades_info.append(self.grade)
        datas1 = []
        for i,(a,b) in enumerate(zip(self.points_info,self.grades_info)):
            datas1.append(self.datas1[i]+[a]+[b])
        datas1.sort(key=lambda e: e[4], reverse=True)
        return datas1
        self.datas1 = datas1
    def show(self,d):
        dlist = d
        fw = open('grade.txt', 'w')
        title = [['Student', 'Name', 'Midterm', 'Final','Average','Grade']]
        line = [['------------', '------------', '------------', '------------','------------','------------']]
        form = title + line + dlist
        print '\n'
        if len(dlist[0]) == 4 :
            for k in range(len(form)):
                for m in range(len(form[2])):
                    print'%-15s' % form[k][m],
                print'\n'
        else:
            for k in range(len(form)):
                for m in range(len(form[0])):
                    print'%-15s' % form[k][m],
                    a = '%-15s' % form[k][m]
                    if len(d)>1 :
                        fw.write(a,)
                print'\n'
                if len(dlist)>1:
                    fw.write('\n')
        self.datas1 = dlist
    def search(self,id,datass):
        listid=[i for i in datass if id == i[0]]
        return listid

def changescore(dd):
    datach = copy.deepcopy(dd)
    search_id = raw_input("Student ID: ")
    if not search_id in info.stid:
        print "NO SUCH PERSON"
    else:
        mf = raw_input("Mid? / Final? ")
        if mf.upper()=='MID' or mf.upper()=='FINAL' :
            new_score = raw_input("Input new Score: ")
            if not float(new_score) <= 100:
                return
            if mf.upper() =='MID':
                for k in datach:
                    if search_id == k[0]:
                        k[2] = int(new_score)
            elif mf.upper() =='FINAL':
                for k in datach:
                    if search_id == k[0]:
                        k[3] = int(new_score)
    info.mids = [datach[i][2] for i in range(len(datach))]
    info.fins = [datach[i][3] for i in range(len(datach))]
    return search_id,datach
def add():
    newid = raw_input('Student ID: ')
    if newid in info.stid:
        print 'ALREADY EXISTS.'
        return
    else:
        new = []
        update = []
        new.append(newid)
    newname = raw_input('Name: ')
    new.append(newname)
    newmid = raw_input('Midterm score: ')
    new.append(newmid)
    info.mids.append(newmid)
    newfin = raw_input('Final score: ')
    new.append(newfin)
    info.fins.append(newfin)
    print 'Student added.'
    return new
def searchgrade():
    grades = []
    scgrades = []
    grades = ['A','B', 'C', 'D', 'F']
    x = raw_input('Grade to search: ')
    if not x.upper() in grades:
        'NO RESULTS'
    scgrades = [ i for i in info.datas1 if x.upper() == i[5]]
    return scgrades

def remove():
    pass
def quit():
    sys.exit()

#main
if not sys.argv[0] == 'project11.py':#11->1
    print 'no such file'
elif len(sys.argv) == 2 and sys.argv[0] == 'project11.py':
    file = sys.argv[1]
    f = open(file, 'r')
    stlist = [i.strip() for i in f]
    stlist = [i.split() for i in stlist]
    stlist = [[stlist[k][0], stlist[k][1] +' '+ stlist[k][2], stlist[k][3], stlist[k][4]] for k in range(len(stlist))]
elif len(sys.argv) == 1 and sys.argv[0] == 'project11.py':
    file = 'students.txt'
    f = open(file, 'r')
    stlist = [i.strip() for i in f]
    stlist = [i.split() for i in stlist]
    stlist = [[stlist[k][0],stlist[k][1]+' '+stlist[k][2],stlist[k][3],stlist[k][4]] for k in range(len(stlist))]
f.close()

info = datas(stlist)
info.show(stlist)

while True:
    command = raw_input("#")
    if command.upper() == 'SEARCH' or command.upper() == 'CHANGESCORE' or command.upper() == 'ADD' or command.upper() == "SEARCHGRADE" or command.upper() == "REMOVE" or command.upper() == "QUIT" or command.upper() =="SHOW":
        if command.upper() == "SHOW":
            dd = info.gradecheck()
            info.show(dd)
        elif command.upper() == "SEARCH":
            stid = raw_input('Student ID: ')
            if not stid in info.stid :
                print 'NO SUCH PERSON.'
            else:
                dds = info.search(stid,dd)
                info.show(dds)
                info.datas1 = dd
        elif command.upper() == "CHANGESCORE":
            ddi,chdatas = changescore(dd)
            oid= info.search(ddi,dd)
            info.show(oid)
            print '****Score changed****'
            chdatas = [chdatas[i][:4] for i in range(len(chdatas))]
            info.datas1 = chdatas
            point =info.gradecheck()
            chid = info.search(ddi,point)
            info.show(chid)
            info.datas1 = chdatas
        elif command.upper() == "ADD":
            newlist = add()
            addedlist = [info.datas1[i][:4] for i in range(len(info.datas1))]
            addedlist.append(newlist)
            info.datas1 = addedlist
            pointadd = info.gradecheck()
            pointadd.sort(key=lambda e: e[5])
            info.datas1 = pointadd
        elif command.upper() == "SEARCHGRADE":
            scgrades = searchgrade()
            info.show(scgrades)
            #searchgrade 이후 show를 하면 남아있지 않은 문제
        elif command.upper() == "REMOVE":
            removeid = raw_input('Student ID: ')
            if not stid in info.stid:
                print 'NO SUCH PERSON.'
            else:
                remove()
        elif command.upper() == "QUIT":
            quit()