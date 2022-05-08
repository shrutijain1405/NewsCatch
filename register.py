import json

User = input("Username:") 
PW = input("Password:")
PW1 = input("Confirm Password:")

if(PW == PW1):
    print("Registration successfully.")    
    f=open('LoginSystemData.json', 'r')
    data=json.load(f)
    y={		
        "username": User,
        "password": PW  
    }
    print(y)
    data.append(y)
    with open('LoginSystemData.json','w') as f1:
       json.dump(data,f1)
    f.close()            
else:
    print("Registration failed! Please confirm your Password correctly.") 