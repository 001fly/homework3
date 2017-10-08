import sys
def wages_salary(username): #查询员工工资
    wages=open("wages.txt","r",encoding="utf-8")
    wages_list=wages.readlines()
    wages.dic={}
    for item in wages_list:
        item_list=item.split(":")
        wages.dic[item_list[0]]=item_list[1]
        if username in wages.dic:
            salary=wages.dic[username]
    print("%s 的工资是 %s"%(username,salary))

def change_message(change_me): #修改员工工资
    wages = open("wages.txt", "r+", encoding="utf-8")
    if change_me in wages.read():
        wages = open("wages.txt", "r", encoding="utf-8")
        wages_r = wages.readlines()
        print(wages_r)
        salary = input("请输入旧工资：")
        if change_me + ":" + salary + "\n" in wages_r:# 判断员工信息是否正确
            newsalary = input("输入新工资：")
            wages_t = open("wages.txt", "r", encoding="utf-8")
            wabak = open("wabak.txt", "w+", encoding="utf-8")
            for line in wages_t: # 打开2个文件，把修改好的信息读取写入wabak文件，在吧wabak文件信息覆盖wages文件信息
                if change_me + ":" + salary in line:
                    line = line.replace(change_me + ":" + salary, change_me + ":" + newsalary)
                wabak.write(line)
        print("%s修改好工资是%s" % (change_me, newsalary))
    wabak = open("wabak.txt", "r", encoding="utf-8")
    wages_t = open("wages.txt", "w", encoding="utf-8")
    wages_t.write(wabak.read())




while True:
    display='''-----------------------
             1.查询员工工资
             2.修改员工工资
             3.添加新员工与工资
             4.退出
             -----------------------'''
    print(display)
    choise=input(">>>:")
    if choise=="1":
        username=input("员工姓名：")
        wages=open("wages.txt","r",encoding="utf-8") #打开员工工资信息
        q_wages=wages.read()
        if username in q_wages:# 员工名字在文件中就查询员工工资
            wages_salary(username)
        else:
            print("输入有误，请重新输入！")
    elif choise=="2":
        change_me=input("请输入员工姓名如（alex）：")
        change=open("wages.txt","r",encoding="utf-8")
        change_r=change.read()
        if change_me in change_r:
            change_message(change_me)
            change.close()
    elif choise=="3":  #添加新用户
        newname=input("输入新建用户名：")
        newname_o=open("wages.txt","r",encoding="utf-8")
        newname_list=newname_o.read()
        if newname in newname_list:
            print("员工已存在！请重新输入！")
        else:
            newsalary=input("请输入工资：")
            newname_o = open("wages.txt", "a+", encoding="utf-8")
            newname_o.write("\n")
            newname_o.write("%s:%s" % (newname, newsalary))
            print("%s已创建，工资是%s" % (newname, newsalary))
            newname_o.close()
    elif choise=="4":
        print("再见!")
        sys.exit()
    else:
        print("请输入“1-4”")
        continue










