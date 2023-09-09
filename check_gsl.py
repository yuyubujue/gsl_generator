with open('uid_list.txt','r') as f:
    lines = f.readlines()

gsl_id = input("uid:")

try:
    if int(gsl_id) in lines:
        print('纯正gsl')
    else:
        print('该id目前不在gsl库中')

except:
    print("请输入uid，目前不支持用户名检索")