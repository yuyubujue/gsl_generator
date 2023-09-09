with open('uid_list.txt','r') as f:
    lines = f.readlines()

gsl_id = input("uid:")

cnt = 0
try:
    for i in lines:
        if int(gsl_id) == int(i):
            cnt+=1
        else:
            pass
    if cnt!=0:
        print('纯正gsl')
    else:
        print('该id目前不在gsl库中')
        insert_gsl = input("是否录入其为gsl(y/n)")
        if insert_gsl == "y" or insert_gsl == "Y":
            with open('uid_list.txt', 'a') as f:
                f.write("\n%s" % gsl_id)
            print("已录入")
            f.close()
        elif insert_gsl == "n" or insert_gsl == "N":
            print("不录入")
        else:
            print("请输入y/n")

except:
    print("请输入uid，目前不支持用户名检索")


