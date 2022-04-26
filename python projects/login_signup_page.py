import re
import json
import os
file = os.path.exists('name.json')
if file ==False:
    user=input("login or signup ")
    if user=="signup":
        list=[]
        dic={}
        name=input("enter the name : ")
        password=input("enter the passward : ")
        if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
            print("strong password")
            confirm_password=input("enter the confirm_password : ")
            if confirm_password==password:
                print("right")
                date_of_birth=input("enter the date_of_birth : ")
                dict={"name":name,"password":password,"do_birth":date_of_birth}
                list.append(dict)
                dic.update({password:list})
                with open("name.json","a")as f:
                    b=json.dump(dic,f,indent=4)
                
            
        else:
            print("wrong password")
elif file==True:
    user=input("login or signup : ")
    if user=="signup":
        list=[]
        dic={}
        name=input("enter the name : ")
        
        passwrd=input("enter the password : ")
        if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', passwrd):
            print("strong password")
            confirm_password=input("enter the confirm_passward : ")
            if confirm_password==passwrd:
                print("right")                   
                date_of_birth=input("enter the date_of_birth : ")
                dict={"name":name,"password":passwrd,"do_birth":date_of_birth}
                list.append(dict)
                dic.update({passwrd:list})
                with open("name.json","a")as f:
                    b=json.dump(dic,f,indent=4)
                
            
        else:
            print("wrong password")
    else:
        
        if user=="login":
            user_name=input("enter the user name")  
            confrm_passward=input("enter the password")
            with open("name.json","r")as f:
                b=json.load(f)
                if confrm_passward==b['@Anshika'][0]["passward"]:
                    print("login succesfully")
                    print(b)
        else:
            print("your deatils is wrong")