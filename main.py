def register(name,passwd):
    file =open("database.txt")
    for i in file:
        x, b = i.split(",")
        b = b.strip()
        if x!=name:
            file=open("database.txt","a")
            file.write("\n"+name+","+passwd)
            file.close()
        else:
            print("name alread exist")
def access(option):
    if option =="REG":
        def check():
            global email
            email = input("Pls enter email adress you want to sigin in with:")
            if "@" not in email :
                print("@ not present")
                check()
            if "." not in email:
                print("dot(.) should be there in Email")
                check()
            for i in range(len(email)):
                if email[i]=="@":
                    d=i
                    for j in range(d):
                        if email[j]==".":
                            print("dot(.) should be after @")
                            check()
                            break
                        if email[d+1]==".":
                            print("@ should not be just followed by dot(.),RE Enter details")
                            check()
                            break
                if email[0] in "[@_!#$%^&*()<>?/\|}{~:]1234567890":
                    print("first word of email should only starts with alphabet,RE Enter details")
                    check()
                    break
            def password():
                global passwd
                passwd=input("Enter Password:")
                if len(passwd) < 5:
                    print("password length too short,Re-enter password")
                    password()
                elif len(passwd) > 16:
                    print("password length out of range,Re-enter password")
                    password()
                else:
                    a = 0;b = 0;c = 0;dd = 0;e = 0
                    for i in passwd:
                        if i.islower():
                            a = 1
                        elif i.isupper():
                            b = 1
                        elif i in "[@_!#$%^&*()<>?/\|}{~:]":
                            dd = 1
                        elif i in "1234567890":
                            e = 1
                    if a == 1 and b == 1 and dd == 1 and e == 1:
                        register(email,passwd)
                    else:
                        print("Password must have one upper one lower case, especial character and one numeric value,RE-Enter password")
                        password()
            password()
        check()
    else:
        name = input("pls enter name:")
        passwrd = input("pls enter your pwd:")
        def loggin(name, passwrd):
            file = open("database.txt")
            for i in file:
                x, b = i.split(",")
                b = b.strip()
                if x != name:
                    print("USER NOT FOUND,kindly sign up")
                    access("REG")
                if x == name and b != passwrd:
                    forget = input("do you want to login again or forget password(login) or (new-password) or (forget password):")
                    if forget == "login":
                        access(option)
                    else:
                        if forget == "new-password":
                            def paar():
                                global passwd
                                passwd = input("Enter Password:")
                                if len(passwd) < 5:
                                    print("password length too short,Re-enter password")
                                    paar()
                                elif len(passwd) > 16:
                                    print("password length out of range,Re-enter password")
                                    paar()
                                else:
                                    a = 0;b = 0;c = 0;dd = 0;e = 0
                                    for i in passwd:
                                        if i.islower():
                                            a = 1
                                        elif i.isupper():
                                            b = 1
                                        elif i in "[@_!#$%^&*()<>?/\|}{~:]":
                                            dd = 1
                                        elif i in "1234567890":
                                            e = 1
                                    if a == 1 and b == 1 and dd == 1 and e == 1:
                                        f = open("database.txt", "a")
                                        file.write("\n" + name + "," + passwd)
                                        file.close()
                                    else:
                                        print("Password must have one upper one lower case, especial character and one numeric value,RE-Enter password")
                                        paar()
                            paar()
                        else:
                            print("your old password is:", b)
                        break
                if x == name and b == passwrd:
                    print("successful!!")
                    file.close()
                    break
        loggin(name, passwrd)
def begin():
    global option
    print("kindly input lgoin or register")
    option=input("login or register(LOG,REG):")
    if option !="LOG" and option!="REG":
        print("pls kindly provide REG for REGESTRATION or LOG for login")
        begin()
begin()
access(option)
