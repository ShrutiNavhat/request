import requests
import json
api="https://api.merakilearn.org/courses"
saral_url=requests.get(api)
# print(saral_url)
data=saral_url.json()

with open("cours_data.json","w")as f:
    json.dump(data,f,indent=4)

print(" ")
print("welcome to navgurukul and learn basic programming language :-")
print(" ")

serial_no=0
for i in data:
    print(serial_no+1 , i["name"],i["id"])
    serial_no=serial_no+1

course_no_1=int(input("enter your number do you want in id :- "))
print(data[course_no_1-1]["name"])
# idd=data[course_no_1-1]["id"]
url2=requests.get("http://api.merakilearn.org/courses/"+str(data[course_no_1-1]["id"])+"/exercises")
var2=url2.json()
with open("topic.json","w")as h:
    json.dump(var2,h,indent=5)
    serial_no2=1

list1=[]
list2=[]
DATA=0
data_1=0
for i in var2["course"]["exercises"]:
    if i["parent_exercise_id"]==None:
        print(serial_no2,i["name"])
        print("   ",serial_no2,i["slug"])
        serial_no2=serial_no2+1
        list1.append(i)
        list2.append(i)

    if ["parent_exercise_id"]==["id"]:
        print(serial_no2,i["name"])
        print("   ",serial_no2,i["name"])
        serial_no2=serial_no2+1
    
    if ["parent_exercise_id"]!=["id"]:
        print(serial_no2,i["name"])
        print("   ",serial_no2,i["name"])
        serial_no2=serial_no2+1
    
topic_no=int(input("choose child no you want:- "))
for l in range (0,len(list2)):
    if topic_no ==l+1:
        print(topic_no,list2[l]["name"])
        # a=list2[l]["parent_exercise_id"]
var=1
var1=[]
var2=[]
for d in range(0,len(list2)): 
    a=list2[l]["parent_exercise_id"]
    if list2[d]["parent_exercise_id"]==a:
        print(" ", var,list1[d]["name"])
        var1.append(list2[d]["name"])
        var2.append(list2[d]["content"])
        var+=1

child_no=int(input("which child you want to print :- "))
print(var2[child_no-1]) 
question=child_no-1
while child_no>0:
    next_question=input("enter the what you want next or previous n/p:-")
    if child_no==len(var2):
        print("next page")
    if next_question=="p":
        if child_no==1:
            print("no more question")
            break
        else:
            child_no=child_no-1        
            print(var2[child_no])
    if next_question=="n":
        if child_no<len(var2):
            index=child_no+1
            print(var2[index-1])
            question=question+1
            child_no=child_no+1
            if question==(len(var2)-1):
                print("next page ")
                break
