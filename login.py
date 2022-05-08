import json

user = input("Username:") 
passwd = input("Password:")
success = False
f=open('LoginSystemData.json', 'r')
data=json.load(f)
##print("hii")
found = False
for i in data:
    a = i['username']
    b = i['password']
    if(a==user and b==passwd):
        print("Login successful")
        found = True
        break

if(found == False):
    print("login not successful")
f.close() 
    
    
