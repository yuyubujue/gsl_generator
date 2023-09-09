import random

with open('uid_list.txt','r') as f:
    lines = f.readlines()
print(lines)
rad_int = random.randint(0,len(lines))
gsl_id = lines[rad_int]
gsl_link = 'https://space.bilibili.com/' + gsl_id.strip()
print(gsl_link)

f.close()
