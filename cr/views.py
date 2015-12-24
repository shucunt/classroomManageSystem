#-*- coding: UTF-8 -*-
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from models import User, zhengxin, zhizhi, chengyi, zhulou
import string
import datetime

FLAG = 0
class UserForm(forms.Form):
    username = forms.CharField(label='用户名字',max_length=100)
    passworld = forms.CharField(label='密 码',widget=forms.PasswordInput())
    email = forms.EmailField(label='邮 件')
    name = forms.CharField(label='姓 名',max_length=100)
    num = forms.CharField(label='学 号',max_length=100)
    major = forms.CharField(label='学 院',max_length=100)

class LogForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    passworld = forms.CharField(label='密 码',widget=forms.PasswordInput())
    
class PersonForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    passworld = forms.CharField(label='原密码',widget=forms.PasswordInput())
    newpass = forms.CharField(label='新密码',widget=forms.PasswordInput())
    email = forms.EmailField(label='邮 件')
    name = forms.CharField(label='姓 名',max_length=100)
    num = forms.CharField(label='学 号',max_length=100)
    major = forms.CharField(label='学 院',max_length=100)
    
def register(request):
    global FLAG
    userna = []
    if request.method == "POST":
        uf = UserForm(request.POST)
        allusers = User.objects.all()
        for i in range(len(allusers)):
            userna.append(allusers[i].username)
        if uf.is_valid():
        #获取表单信息
            usernames = uf.cleaned_data['username']
            passworlds = uf.cleaned_data['passworld']
            emails = uf.cleaned_data['email']
            names = uf.cleaned_data['name']
            nums = uf.cleaned_data['num']
            majors = uf.cleaned_data['major']
            #将表单写入数据库
            if usernames in userna:
                return render_to_response('rep_user.html',locals())
            else:
                user = User(
                username = usernames,
                password = passworlds,
                email = emails,
                name = names,
                num = nums,
                major = majors
                )
                #user.passworld.create(password=passworlds)
                user.save()
                FLAG = 1
                a1 = 1
                a2 = 2
                a3 = 3
                a4 = 4
                #返回注册成功页面
                return render_to_response('map.html',locals())
    else:
        uf = UserForm()
        return render_to_response('register.html',{'uf':uf})

def login(request):
    global FLAG
    if request.method == "POST":
        uf = LogForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['passworld']
            user = User.objects.get(username = username)
            if user.password == password:
                FLAG = 1
                a1 = 1
                a2 = 2
                a3 = 3
                a4 = 4
                #返回登陆成功页面
                if username == 'admin':
                    return render_to_response('admin.html',locals())
                else:
                    return render_to_response('map.html',locals())
            else:
                 return render_to_response('wrong.html')
        else:
            return render_to_response('wrong.html')
    else:
        uf = LogForm()
        return render_to_response('login.html',{'uf':uf},context_instance=RequestContext(request))

def personal(request):
    global FLAG
    if FLAG == 1:
        if request.method == "POST":
            uf = PersonForm(request.POST)
            if uf.is_valid():
                usernames = uf.cleaned_data['username']
                passworlds = uf.cleaned_data['passworld']
                pers = User.objects.get(username = usernames)
                if pers.password == passworlds:
                    newpassd = uf.cleaned_data['newpass']
                    emails = uf.cleaned_data['email']
                    names = uf.cleaned_data['name']
                    nums = uf.cleaned_data['num']
                    majors = uf.cleaned_data['major']
                    pers.password = newpassd
                    pers.email = emails
                    pers.name = names
                    pers.num = nums
                    pers.major = majors
                    a1 = 1
                    a2 = 2
                    a3 = 3
                    a4 = 4
                    pers.save()
                    return render_to_response('map.html',locals())
                else :
                    return render_to_response('wrong.html')
        else:
            uf = PersonForm()
            return render_to_response('personal.html',{'uf':uf},context_instance=RequestContext(request))
    else:
        return render_to_response('nolog.html')

def result(request, StrID):
    global FLAG
    if FLAG == 1:
        fla = 1
        standard = datetime.datetime.now().strftime("%X")
        time = datetime.datetime.now().strftime("%A")
        hour = datetime.datetime.now().strftime("%H")
        minute = datetime.datetime.now().strftime("%M")
        if StrID == "1":
            zx = zhengxin.objects.all()
            if time == "Monday":
                room1 = []
                room2 = []
                room3 = []
                room4 = []
                rooms = []
                nums = []
                id1 = []
                id2 = []
                id3 = []
                id4 = []
                for i in range (len(zx)):
                    if "1" in zx[i].Monday:
                        room1.append(zx[i].roomID)
                        id1.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "2" in zx[i].Monday:
                        room2.append(zx[i].roomID)
                        id2.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "3" in zx[i].Monday:
                        room3.append(zx[i].roomID)
                        id3.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "4" in zx[i].Monday:
                        room4.append(zx[i].roomID)
                        id4.append({zx[i].roomID:StrID+zx[i].roomID})
                if (string.atoi(hour) == 8) or (string.atoi(hour) == 9 and string.atoi(minute) <= 45) :
                    for i in room1:
                        num = []
                        room = zhengxin.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 10) or (string.atoi(hour) == 11 and string.atoi(minute) <= 45) :
                    for i in room2:
                        num = []
                        room = zhengxin.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 13 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 14) or \
                (string.atoi(hour) == 15 and string.atoi(minute) <= 30) :
                    for i in room3:
                        num = []
                        room = zhengxin.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 15 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 16) or \
                (string.atoi(hour) == 17 and string.atoi(minute) <= 30) :
                    for i in room4:
                        num = []
                        room = zhengxin.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                else:
                    fla = 0
                    for i in range(len(zx)):
                        num = []
                        num.append(zx[i].roomID)
                        num.append(zx[i].num)
                        nums.append(num)
                if fla == 1:
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
                else:
                    nroom="now it is out of class"
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
            if time == "Tuesday":
                room1 = []
                room2 = []
                room3 = []
                room4 = []
                rooms = []
                nums = []
                id1 = []
                id2 = []
                id3 = []
                id4 = []
                for i in range (len(zx)):
                    if "1" in zx[i].Tuesday:
                        room1.append(zx[i].roomID)
                        id1.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "2" in zx[i].Tuesday:
                        room2.append(zx[i].roomID)
                        id2.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "3" in zx[i].Tuesday:
                        room3.append(zx[i].roomID)
                        id3.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "4" in zx[i].Tuesday:
                        room4.append(zx[i].roomID)
                        id4.append({zx[i].roomID:StrID+zx[i].roomID})
                if (string.atoi(hour) == 8) or (string.atoi(hour) == 9 and string.atoi(minute) <= 45) :
                    for i in room1:
                        num = []
                        room = zhengxin.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 10) or (string.atoi(hour) == 11 and string.atoi(minute) <= 45) :
                    for i in room2:
                        num = []
                        room = zhengxin.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 13 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 14) or \
                (string.atoi(hour) == 15 and string.atoi(minute) <= 30) :
                    for i in room3:
                        num = []
                        room = zhengxin.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 15 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 16) or \
                (string.atoi(hour) == 17 and string.atoi(minute) <= 30) :
                    for i in room4:
                        num = []
                        room = zhengxin.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                else:
                    fla = 0
                    for i in range(len(zx)):
                        num = []
                        num.append(zx[i].roomID)
                        num.append(zx[i].num)
                        nums.append(num)
                if fla == 1:
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
                else:
                    nroom="now it is out of class"
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
            if time == "Wednesday":
                room1 = []
                room2 = []
                room3 = []
                room4 = []
                rooms = []
                nums = []
                id1 = []
                id2 = []
                id3 = []
                id4 = []

                for i in range (len(zx)):
                    if "1" in zx[i].Wednesday:
                        room1.append(zx[i].roomID)
                        id1.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "2" in zx[i].Wednesday:
                        room2.append(zx[i].roomID)
                        id2.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "3" in zx[i].Wednesday:
                        room3.append(zx[i].roomID)
                        id3.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "4" in zx[i].Wednesday:
                        room4.append(zx[i].roomID)
                        id4.append({zx[i].roomID:StrID+zx[i].roomID})
                if (string.atoi(hour) == 8) or (string.atoi(hour) == 9 and string.atoi(minute) <= 45) :
                    for i in room1:
                        num = []
                        room = zhengxin.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 10) or (string.atoi(hour) == 11 and string.atoi(minute) <= 45) :
                    for i in room2:
                        num = []
                        room = zhengxin.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 13 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 14) or \
                (string.atoi(hour) == 15 and string.atoi(minute) <= 30) :
                    for i in room3:
                        num = []
                        room = zhengxin.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 15 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 16) or \
                (string.atoi(hour) == 17 and string.atoi(minute) <= 30) :
                    for i in room4:
                        num = []
                        room = zhengxin.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                else:
                    fla = 0
                    for i in range(len(zx)):
                        num = []
                        num.append(zx[i].roomID)
                        num.append(zx[i].num)
                        nums.append(num)
                if fla == 1:
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
                else:
                    nroom="now it is out of class"
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
            if time == "Thursday":
                room1 = []
                room2 = []
                room3 = []
                room4 = []
                rooms = []
                nums = []
                id1 = []
                id2 = []
                id3 = []
                id4 = []

                for i in range (len(zx)):
                    if "1" in zx[i].Thursday:
                        room1.append(zx[i].roomID)
                        id1.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "2" in zx[i].Thursday:
                        room2.append(zx[i].roomID)
                        id2.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "3" in zx[i].Thursday:
                        room3.append(zx[i].roomID)
                        id3.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "4" in zx[i].Thursday:
                        room4.append(zx[i].roomID)
                        id4.append({zx[i].roomID:StrID+zx[i].roomID})
                if (string.atoi(hour) == 8) or (string.atoi(hour) == 9 and string.atoi(minute) <= 45) :
                    for i in room1:
                        num = []
                        room = zhengxin.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 10) or (string.atoi(hour) == 11 and string.atoi(minute) <= 45) :
                    for i in room2:
                        num = []
                        room = zhengxin.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 13 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 14) or \
                (string.atoi(hour) == 15 and string.atoi(minute) <= 30) :
                    for i in room3:
                        num = []
                        room = zhengxin.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 15 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 16) or \
                (string.atoi(hour) == 17 and string.atoi(minute) <= 30) :
                    for i in room4:
                        num = []
                        room = zhengxin.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                else:
                    fla = 0
                    for i in range(len(zx)):
                        num = []
                        num.append(zx[i].roomID)
                        num.append(zx[i].num)
                        nums.append(num)
                if fla == 1:
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
                else:
                    nroom="now it is out of class"
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
            if time == "Friday":
                room1 = []
                room2 = []
                room3 = []
                room4 = []
                rooms = []
                nums = []
                id1 = []
                id2 = []
                id3 = []
                id4 = []

                for i in range (len(zx)):
                    if "1" in zx[i].Friday:
                        room1.append(zx[i].roomID)
                        id1.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "2" in zx[i].Friday:
                        room2.append(zx[i].roomID)
                        id2.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "3" in zx[i].Friday:
                        room3.append(zx[i].roomID)
                        id3.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "4" in zx[i].Friday:
                        room4.append(zx[i].roomID)
                        id4.append({zx[i].roomID:StrID+zx[i].roomID})
                if (string.atoi(hour) == 8) or (string.atoi(hour) == 9 and string.atoi(minute) <= 45) :
                    for i in room1:
                        num = []
                        room = zhengxin.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 10) or (string.atoi(hour) == 11 and string.atoi(minute) <= 45) :
                    for i in room2:
                        num = []
                        room = zhengxin.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 13 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 14) or \
                (string.atoi(hour) == 15 and string.atoi(minute) <= 30) :
                    for i in room3:
                        num = []
                        room = zhengxin.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 15 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 16) or \
                (string.atoi(hour) == 17 and string.atoi(minute) <= 30) :
                    for i in room4:
                        num = []
                        room = zhengxin.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                else:
                    fla = 0
                    for i in range(len(zx)):
                        num = []
                        num.append(zx[i].roomID)
                        num.append(zx[i].num)
                        nums.append(num)
                if fla == 1:
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
                else:
                    nroom="now it is out of class"
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
            if time == "Saturday":
                room1 = []
                room2 = []
                room3 = []
                room4 = []
                rooms = []
                nums = []
                id1 = []
                id2 = []
                id3 = []
                id4 = []

                for i in range (len(zx)):
                    if "1" in zx[i].Saturday:
                        room1.append(zx[i].roomID)
                        id1.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "2" in zx[i].Saturday:
                        room2.append(zx[i].roomID)
                        id2.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "3" in zx[i].Saturday:
                        room3.append(zx[i].roomID)
                        id3.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "4" in zx[i].Saturday:
                        room4.append(zx[i].roomID)
                        id4.append({zx[i].roomID:StrID+zx[i].roomID})
                if (string.atoi(hour) == 8) or (string.atoi(hour) == 9 and string.atoi(minute) <= 45) :
                    for i in room1:
                        num = []
                        room = zhengxin.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 10) or (string.atoi(hour) == 11 and string.atoi(minute) <= 45) :
                    for i in room2:
                        num = []
                        room = zhengxin.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 13 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 14) or \
                (string.atoi(hour) == 15 and string.atoi(minute) <= 30) :
                    for i in room3:
                        num = []
                        room = zhengxin.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 15 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 16) or \
                (string.atoi(hour) == 17 and string.atoi(minute) <= 30) :
                    for i in room4:
                        num = []
                        room = zhengxin.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                else:
                    fla = 0
                    for i in range(len(zx)):
                        num = []
                        num.append(zx[i].roomID)
                        num.append(zx[i].num)
                        nums.append(num)
                if fla == 1:
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
                else:
                    nroom="now it is out of class"
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
            if time == "Sunday":
                room1 = []
                room2 = []
                room3 = []
                room4 = []
                rooms = []
                nums = []
                id1 = []
                id2 = []
                id3 = []
                id4 = []

                for i in range (len(zx)):
                    if "1" in zx[i].Sunday:
                        room1.append(zx[i].roomID)
                        id1.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "2" in zx[i].Sunday:
                        room2.append(zx[i].roomID)
                        id2.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "3" in zx[i].Sunday:
                        room3.append(zx[i].roomID)
                        id3.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "4" in zx[i].Sunday:
                        room4.append(zx[i].roomID)
                        id4.append({zx[i].roomID:StrID+zx[i].roomID})
                if (string.atoi(hour) == 8) or (string.atoi(hour) == 9 and string.atoi(minute) <= 45) :
                    for i in room1:
                        num = []
                        room = zhengxin.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 10) or (string.atoi(hour) == 11 and string.atoi(minute) <= 45) :
                    for i in room2:
                        num = []
                        room = zhengxin.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 13 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 14) or \
                (string.atoi(hour) == 15 and string.atoi(minute) <= 30) :
                    for i in room3:
                        num = []
                        room = zhengxin.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 15 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 16) or \
                (string.atoi(hour) == 17 and string.atoi(minute) <= 30) :
                    for i in room4:
                        num = []
                        room = zhengxin.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                else:
                    fla = 0
                    for i in range(len(zx)):
                        num = []
                        num.append(zx[i].roomID)
                        num.append(zx[i].num)
                        nums.append(num)
                if fla == 1:
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
                else:
                    nroom="now it is out of class"
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
                    
                    
        if StrID == "2":
            zx = zhizhi.objects.all()
            if time == "Monday":
                room1 = []
                room2 = []
                room3 = []
                room4 = []
                rooms = []
                nums = []
                id1 = []
                id2 = []
                id3 = []
                id4 = []
                for i in range (len(zx)):
                    if "1" in zx[i].Monday:
                        room1.append(zx[i].roomID)
                        id1.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "2" in zx[i].Monday:
                        room2.append(zx[i].roomID)
                        id2.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "3" in zx[i].Monday:
                        room3.append(zx[i].roomID)
                        id3.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "4" in zx[i].Monday:
                        room4.append(zx[i].roomID)
                        id4.append({zx[i].roomID:StrID+zx[i].roomID})
                if (string.atoi(hour) == 8) or (string.atoi(hour) == 9 and string.atoi(minute) <= 45) :
                    for i in room1:
                        num = []
                        room = zhizhi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 10) or (string.atoi(hour) == 11 and string.atoi(minute) <= 45) :
                    for i in room2:
                        num = []
                        room = zhizhi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 13 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 14) or \
                (string.atoi(hour) == 15 and string.atoi(minute) <= 30) :
                    for i in room3:
                        num = []
                        room = zhizhi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 15 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 16) or \
                (string.atoi(hour) == 17 and string.atoi(minute) <= 30) :
                    for i in room4:
                        num = []
                        room = zhizhi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                else:
                    fla = 0
                    for i in range(len(zx)):
                        num = []
                        num.append(zx[i].roomID)
                        num.append(zx[i].num)
                        nums.append(num)
                if fla == 1:
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
                else:
                    nroom="now it is out of class"
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
            if time == "Tuesday":
                room1 = []
                room2 = []
                room3 = []
                room4 = []
                rooms = []
                nums = []
                id1 = []
                id2 = []
                id3 = []
                id4 = []
                for i in range (len(zx)):
                    if "1" in zx[i].Tuesday:
                        room1.append(zx[i].roomID)
                        id1.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "2" in zx[i].Tuesday:
                        room2.append(zx[i].roomID)
                        id2.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "3" in zx[i].Tuesday:
                        room3.append(zx[i].roomID)
                        id3.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "4" in zx[i].Tuesday:
                        room4.append(zx[i].roomID)
                        id4.append({zx[i].roomID:StrID+zx[i].roomID})
                if (string.atoi(hour) == 8) or (string.atoi(hour) == 9 and string.atoi(minute) <= 45) :
                    for i in room1:
                        num = []
                        room = zhizhi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 10) or (string.atoi(hour) == 11 and string.atoi(minute) <= 45) :
                    for i in room2:
                        num = []
                        room = zhizhi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 13 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 14) or \
                (string.atoi(hour) == 15 and string.atoi(minute) <= 30) :
                    for i in room3:
                        num = []
                        room = zhizhi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 15 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 16) or \
                (string.atoi(hour) == 17 and string.atoi(minute) <= 30) :
                    for i in room4:
                        num = []
                        room = zhizhi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                else:
                    fla = 0
                    for i in range(len(zx)):
                        num = []
                        num.append(zx[i].roomID)
                        num.append(zx[i].num)
                        nums.append(num)
                if fla == 1:
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
                else:
                    nroom="now it is out of class"
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
            if time == "Wednesday":
                room1 = []
                room2 = []
                room3 = []
                room4 = []
                rooms = []
                nums = []
                id1 = []
                id2 = []
                id3 = []
                id4 = []

                for i in range (len(zx)):
                    if "1" in zx[i].Wednesday:
                        room1.append(zx[i].roomID)
                        id1.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "2" in zx[i].Wednesday:
                        room2.append(zx[i].roomID)
                        id2.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "3" in zx[i].Wednesday:
                        room3.append(zx[i].roomID)
                        id3.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "4" in zx[i].Wednesday:
                        room4.append(zx[i].roomID)
                        id4.append({zx[i].roomID:StrID+zx[i].roomID})
                if (string.atoi(hour) == 8) or (string.atoi(hour) == 9 and string.atoi(minute) <= 45) :
                    for i in room1:
                        num = []
                        room = zhizhi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 10) or (string.atoi(hour) == 11 and string.atoi(minute) <= 45) :
                    for i in room2:
                        num = []
                        room = zhizhi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 13 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 14) or \
                (string.atoi(hour) == 15 and string.atoi(minute) <= 30) :
                    for i in room3:
                        num = []
                        room = zhizhi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 15 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 16) or \
                (string.atoi(hour) == 17 and string.atoi(minute) <= 30) :
                    for i in room4:
                        num = []
                        room = zhizhi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                else:
                    fla = 0
                    for i in range(len(zx)):
                        num = []
                        num.append(zx[i].roomID)
                        num.append(zx[i].num)
                        nums.append(num)
                if fla == 1:
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
                else:
                    nroom="now it is out of class"
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
            if time == "Thursday":
                room1 = []
                room2 = []
                room3 = []
                room4 = []
                rooms = []
                nums = []
                id1 = []
                id2 = []
                id3 = []
                id4 = []

                for i in range (len(zx)):
                    if "1" in zx[i].Thursday:
                        room1.append(zx[i].roomID)
                        id1.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "2" in zx[i].Thursday:
                        room2.append(zx[i].roomID)
                        id2.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "3" in zx[i].Thursday:
                        room3.append(zx[i].roomID)
                        id3.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "4" in zx[i].Thursday:
                        room4.append(zx[i].roomID)
                        id4.append({zx[i].roomID:StrID+zx[i].roomID})
                if (string.atoi(hour) == 8) or (string.atoi(hour) == 9 and string.atoi(minute) <= 45) :
                    for i in room1:
                        num = []
                        room = zhizhi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 10) or (string.atoi(hour) == 11 and string.atoi(minute) <= 45) :
                    for i in room2:
                        num = []
                        room = zhizhi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 13 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 14) or \
                (string.atoi(hour) == 15 and string.atoi(minute) <= 30) :
                    for i in room3:
                        num = []
                        room = zhizhi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 15 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 16) or \
                (string.atoi(hour) == 17 and string.atoi(minute) <= 30) :
                    for i in room4:
                        num = []
                        room = zhizhi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                else:
                    fla = 0
                    for i in range(len(zx)):
                        num = []
                        num.append(zx[i].roomID)
                        num.append(zx[i].num)
                        nums.append(num)
                if fla == 1:
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
                else:
                    nroom="now it is out of class"
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
            if time == "Friday":
                room1 = []
                room2 = []
                room3 = []
                room4 = []
                rooms = []
                nums = []
                id1 = []
                id2 = []
                id3 = []
                id4 = []

                for i in range (len(zx)):
                    if "1" in zx[i].Friday:
                        room1.append(zx[i].roomID)
                        id1.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "2" in zx[i].Friday:
                        room2.append(zx[i].roomID)
                        id2.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "3" in zx[i].Friday:
                        room3.append(zx[i].roomID)
                        id3.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "4" in zx[i].Friday:
                        room4.append(zx[i].roomID)
                        id4.append({zx[i].roomID:StrID+zx[i].roomID})
                if (string.atoi(hour) == 8) or (string.atoi(hour) == 9 and string.atoi(minute) <= 45) :
                    for i in room1:
                        num = []
                        room = zhizhi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 10) or (string.atoi(hour) == 11 and string.atoi(minute) <= 45) :
                    for i in room2:
                        num = []
                        room = zhizhi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 13 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 14) or \
                (string.atoi(hour) == 15 and string.atoi(minute) <= 30) :
                    for i in room3:
                        num = []
                        room = zhizhi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 15 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 16) or \
                (string.atoi(hour) == 17 and string.atoi(minute) <= 30) :
                    for i in room4:
                        num = []
                        room = zhizhi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                else:
                    fla = 0
                    for i in range(len(zx)):
                        num = []
                        num.append(zx[i].roomID)
                        num.append(zx[i].num)
                        nums.append(num)
                if fla == 1:
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
                else:
                    nroom="now it is out of class"
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
            if time == "Saturday":
                room1 = []
                room2 = []
                room3 = []
                room4 = []
                rooms = []
                nums = []
                id1 = []
                id2 = []
                id3 = []
                id4 = []

                for i in range (len(zx)):
                    if "1" in zx[i].Saturday:
                        room1.append(zx[i].roomID)
                        id1.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "2" in zx[i].Saturday:
                        room2.append(zx[i].roomID)
                        id2.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "3" in zx[i].Saturday:
                        room3.append(zx[i].roomID)
                        id3.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "4" in zx[i].Saturday:
                        room4.append(zx[i].roomID)
                        id4.append({zx[i].roomID:StrID+zx[i].roomID})
                if (string.atoi(hour) == 8) or (string.atoi(hour) == 9 and string.atoi(minute) <= 45) :
                    for i in room1:
                        num = []
                        room = zhizhi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 10) or (string.atoi(hour) == 11 and string.atoi(minute) <= 45) :
                    for i in room2:
                        num = []
                        room = zhizhi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 13 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 14) or \
                (string.atoi(hour) == 15 and string.atoi(minute) <= 30) :
                    for i in room3:
                        num = []
                        room = zhizhi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 15 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 16) or \
                (string.atoi(hour) == 17 and string.atoi(minute) <= 30) :
                    for i in room4:
                        num = []
                        room = zhizhi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                else:
                    fla = 0
                    for i in range(len(zx)):
                        num = []
                        num.append(zx[i].roomID)
                        num.append(zx[i].num)
                        nums.append(num)
                if fla == 1:
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
                else:
                    nroom="now it is out of class"
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
            if time == "Sunday":
                room1 = []
                room2 = []
                room3 = []
                room4 = []
                rooms = []
                nums = []
                id1 = []
                id2 = []
                id3 = []
                id4 = []

                for i in range (len(zx)):
                    if "1" in zx[i].Sunday:
                        room1.append(zx[i].roomID)
                        id1.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "2" in zx[i].Sunday:
                        room2.append(zx[i].roomID)
                        id2.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "3" in zx[i].Sunday:
                        room3.append(zx[i].roomID)
                        id3.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "4" in zx[i].Sunday:
                        room4.append(zx[i].roomID)
                        id4.append({zx[i].roomID:StrID+zx[i].roomID})
                if (string.atoi(hour) == 8) or (string.atoi(hour) == 9 and string.atoi(minute) <= 45) :
                    for i in room1:
                        num = []
                        room = zhizhi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 10) or (string.atoi(hour) == 11 and string.atoi(minute) <= 45) :
                    for i in room2:
                        num = []
                        room = zhizhi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 13 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 14) or \
                (string.atoi(hour) == 15 and string.atoi(minute) <= 30) :
                    for i in room3:
                        num = []
                        room = zhizhi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 15 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 16) or \
                (string.atoi(hour) == 17 and string.atoi(minute) <= 30) :
                    for i in room4:
                        num = []
                        room = zhizhi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                else:
                    fla = 0
                    for i in range(len(zx)):
                        num = []
                        num.append(zx[i].roomID)
                        num.append(zx[i].num)
                        nums.append(num)
                if fla == 1:
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
                else:
                    nroom="now it is out of class"
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})


        if StrID == "3":
            zx = chengyi.objects.all()
            if time == "Monday":
                room1 = []
                room2 = []
                room3 = []
                room4 = []
                rooms = []
                nums = []
                id1 = []
                id2 = []
                id3 = []
                id4 = []
                for i in range (len(zx)):
                    if "1" in zx[i].Monday:
                        room1.append(zx[i].roomID)
                        id1.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "2" in zx[i].Monday:
                        room2.append(zx[i].roomID)
                        id2.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "3" in zx[i].Monday:
                        room3.append(zx[i].roomID)
                        id3.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "4" in zx[i].Monday:
                        room4.append(zx[i].roomID)
                        id4.append({zx[i].roomID:StrID+zx[i].roomID})
                if (string.atoi(hour) == 8) or (string.atoi(hour) == 9 and string.atoi(minute) <= 45) :
                    for i in room1:
                        num = []
                        room = chengyi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 10) or (string.atoi(hour) == 11 and string.atoi(minute) <= 45) :
                    for i in room2:
                        num = []
                        room = chengyi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 13 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 14) or \
                (string.atoi(hour) == 15 and string.atoi(minute) <= 30) :
                    for i in room3:
                        num = []
                        room = chengyi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 15 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 16) or \
                (string.atoi(hour) == 17 and string.atoi(minute) <= 30) :
                    for i in room4:
                        num = []
                        room = chengyi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                else:
                    fla = 0
                    for i in range(len(zx)):
                        num = []
                        num.append(zx[i].roomID)
                        num.append(zx[i].num)
                        nums.append(num)
                if fla == 1:
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
                else:
                    nroom="now it is out of class"
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
            if time == "Tuesday":
                room1 = []
                room2 = []
                room3 = []
                room4 = []
                rooms = []
                nums = []
                id1 = []
                id2 = []
                id3 = []
                id4 = []
                for i in range (len(zx)):
                    if "1" in zx[i].Tuesday:
                        room1.append(zx[i].roomID)
                        id1.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "2" in zx[i].Tuesday:
                        room2.append(zx[i].roomID)
                        id2.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "3" in zx[i].Tuesday:
                        room3.append(zx[i].roomID)
                        id3.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "4" in zx[i].Tuesday:
                        room4.append(zx[i].roomID)
                        id4.append({zx[i].roomID:StrID+zx[i].roomID})
                if (string.atoi(hour) == 8) or (string.atoi(hour) == 9 and string.atoi(minute) <= 45) :
                    for i in room1:
                        num = []
                        room = chengyi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 10) or (string.atoi(hour) == 11 and string.atoi(minute) <= 45) :
                    for i in room2:
                        num = []
                        room = chengyi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 13 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 14) or \
                (string.atoi(hour) == 15 and string.atoi(minute) <= 30) :
                    for i in room3:
                        num = []
                        room = chengyi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 15 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 16) or \
                (string.atoi(hour) == 17 and string.atoi(minute) <= 30) :
                    for i in room4:
                        num = []
                        room = chengyi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                else:
                    fla = 0
                    for i in range(len(zx)):
                        num = []
                        num.append(zx[i].roomID)
                        num.append(zx[i].num)
                        nums.append(num)
                if fla == 1:
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
                else:
                    nroom="now it is out of class"
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
            if time == "Wednesday":
                room1 = []
                room2 = []
                room3 = []
                room4 = []
                rooms = []
                nums = []
                id1 = []
                id2 = []
                id3 = []
                id4 = []

                for i in range (len(zx)):
                    if "1" in zx[i].Wednesday:
                        room1.append(zx[i].roomID)
                        id1.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "2" in zx[i].Wednesday:
                        room2.append(zx[i].roomID)
                        id2.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "3" in zx[i].Wednesday:
                        room3.append(zx[i].roomID)
                        id3.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "4" in zx[i].Wednesday:
                        room4.append(zx[i].roomID)
                        id4.append({zx[i].roomID:StrID+zx[i].roomID})
                if (string.atoi(hour) == 8) or (string.atoi(hour) == 9 and string.atoi(minute) <= 45) :
                    for i in room1:
                        num = []
                        room = chengyi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 10) or (string.atoi(hour) == 11 and string.atoi(minute) <= 45) :
                    for i in room2:
                        num = []
                        room = chengyi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 13 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 14) or \
                (string.atoi(hour) == 15 and string.atoi(minute) <= 30) :
                    for i in room3:
                        num = []
                        room = chengyi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 15 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 16) or \
                (string.atoi(hour) == 17 and string.atoi(minute) <= 30) :
                    for i in room4:
                        num = []
                        room = chengyi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                else:
                    fla = 0
                    for i in range(len(zx)):
                        num = []
                        num.append(zx[i].roomID)
                        num.append(zx[i].num)
                        nums.append(num)
                if fla == 1:
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
                else:
                    nroom="now it is out of class"
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
            if time == "Thursday":
                room1 = []
                room2 = []
                room3 = []
                room4 = []
                rooms = []
                nums = []
                id1 = []
                id2 = []
                id3 = []
                id4 = []

                for i in range (len(zx)):
                    if "1" in zx[i].Thursday:
                        room1.append(zx[i].roomID)
                        id1.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "2" in zx[i].Thursday:
                        room2.append(zx[i].roomID)
                        id2.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "3" in zx[i].Thursday:
                        room3.append(zx[i].roomID)
                        id3.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "4" in zx[i].Thursday:
                        room4.append(zx[i].roomID)
                        id4.append({zx[i].roomID:StrID+zx[i].roomID})
                if (string.atoi(hour) == 8) or (string.atoi(hour) == 9 and string.atoi(minute) <= 45) :
                    for i in room1:
                        num = []
                        room = chengyi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 10) or (string.atoi(hour) == 11 and string.atoi(minute) <= 45) :
                    for i in room2:
                        num = []
                        room = chengyi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 13 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 14) or \
                (string.atoi(hour) == 15 and string.atoi(minute) <= 30) :
                    for i in room3:
                        num = []
                        room = chengyi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 15 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 16) or \
                (string.atoi(hour) == 17 and string.atoi(minute) <= 30) :
                    for i in room4:
                        num = []
                        room = chengyi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                else:
                    fla = 0
                    for i in range(len(zx)):
                        num = []
                        num.append(zx[i].roomID)
                        num.append(zx[i].num)
                        nums.append(num)
                if fla == 1:
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
                else:
                    nroom="now it is out of class"
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
            if time == "Friday":
                room1 = []
                room2 = []
                room3 = []
                room4 = []
                rooms = []
                nums = []
                id1 = []
                id2 = []
                id3 = []
                id4 = []

                for i in range (len(zx)):
                    if "1" in zx[i].Friday:
                        room1.append(zx[i].roomID)
                        id1.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "2" in zx[i].Friday:
                        room2.append(zx[i].roomID)
                        id2.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "3" in zx[i].Friday:
                        room3.append(zx[i].roomID)
                        id3.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "4" in zx[i].Friday:
                        room4.append(zx[i].roomID)
                        id4.append({zx[i].roomID:StrID+zx[i].roomID})
                if (string.atoi(hour) == 8) or (string.atoi(hour) == 9 and string.atoi(minute) <= 45) :
                    for i in room1:
                        num = []
                        room = chengyi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 10) or (string.atoi(hour) == 11 and string.atoi(minute) <= 45) :
                    for i in room2:
                        num = []
                        room = chengyi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 13 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 14) or \
                (string.atoi(hour) == 15 and string.atoi(minute) <= 30) :
                    for i in room3:
                        num = []
                        room = chengyi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 15 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 16) or \
                (string.atoi(hour) == 17 and string.atoi(minute) <= 30) :
                    for i in room4:
                        num = []
                        room = chengyi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                else:
                    fla = 0
                    for i in range(len(zx)):
                        num = []
                        num.append(zx[i].roomID)
                        num.append(zx[i].num)
                        nums.append(num)
                if fla == 1:
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
                else:
                    nroom="now it is out of class"
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
            if time == "Saturday":
                room1 = []
                room2 = []
                room3 = []
                room4 = []
                rooms = []
                nums = []
                id1 = []
                id2 = []
                id3 = []
                id4 = []

                for i in range (len(zx)):
                    if "1" in zx[i].Saturday:
                        room1.append(zx[i].roomID)
                        id1.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "2" in zx[i].Saturday:
                        room2.append(zx[i].roomID)
                        id2.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "3" in zx[i].Saturday:
                        room3.append(zx[i].roomID)
                        id3.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "4" in zx[i].Saturday:
                        room4.append(zx[i].roomID)
                        id4.append({zx[i].roomID:StrID+zx[i].roomID})
                if (string.atoi(hour) == 8) or (string.atoi(hour) == 9 and string.atoi(minute) <= 45) :
                    for i in room1:
                        num = []
                        room = chengyi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 10) or (string.atoi(hour) == 11 and string.atoi(minute) <= 45) :
                    for i in room2:
                        num = []
                        room = chengyi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 13 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 14) or \
                (string.atoi(hour) == 15 and string.atoi(minute) <= 30) :
                    for i in room3:
                        num = []
                        room = chengyi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 15 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 16) or \
                (string.atoi(hour) == 17 and string.atoi(minute) <= 30) :
                    for i in room4:
                        num = []
                        room = chengyi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                else:
                    fla = 0
                    for i in range(len(zx)):
                        num = []
                        num.append(zx[i].roomID)
                        num.append(zx[i].num)
                        nums.append(num)
                if fla == 1:
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
                else:
                    nroom="now it is out of class"
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
            if time == "Sunday":
                room1 = []
                room2 = []
                room3 = []
                room4 = []
                rooms = []
                nums = []
                id1 = []
                id2 = []
                id3 = []
                id4 = []

                for i in range (len(zx)):
                    if "1" in zx[i].Sunday:
                        room1.append(zx[i].roomID)
                        id1.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "2" in zx[i].Sunday:
                        room2.append(zx[i].roomID)
                        id2.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "3" in zx[i].Sunday:
                        room3.append(zx[i].roomID)
                        id3.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "4" in zx[i].Sunday:
                        room4.append(zx[i].roomID)
                        id4.append({zx[i].roomID:StrID+zx[i].roomID})
                if (string.atoi(hour) == 8) or (string.atoi(hour) == 9 and string.atoi(minute) <= 45) :
                    for i in room1:
                        num = []
                        room = chengyi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 10) or (string.atoi(hour) == 11 and string.atoi(minute) <= 45) :
                    for i in room2:
                        num = []
                        room = chengyi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 13 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 14) or \
                (string.atoi(hour) == 15 and string.atoi(minute) <= 30) :
                    for i in room3:
                        num = []
                        room = chengyi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 15 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 16) or \
                (string.atoi(hour) == 17 and string.atoi(minute) <= 30) :
                    for i in room4:
                        num = []
                        room = chengyi.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                else:
                    fla = 0
                    for i in range(len(zx)):
                        num = []
                        num.append(zx[i].roomID)
                        num.append(zx[i].num)
                        nums.append(num)
                if fla == 1:
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
                else:
                    nroom="now it is out of class"
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})


        if StrID == "4":
            zx = zhulou.objects.all()
            if time == "Monday":
                room1 = []
                room2 = []
                room3 = []
                room4 = []
                rooms = []
                nums = []
                id1 = []
                id2 = []
                id3 = []
                id4 = []
                for i in range (len(zx)):
                    if "1" in zx[i].Monday:
                        room1.append(zx[i].roomID)
                        id1.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "2" in zx[i].Monday:
                        room2.append(zx[i].roomID)
                        id2.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "3" in zx[i].Monday:
                        room3.append(zx[i].roomID)
                        id3.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "4" in zx[i].Monday:
                        room4.append(zx[i].roomID)
                        id4.append({zx[i].roomID:StrID+zx[i].roomID})
                if (string.atoi(hour) == 8) or (string.atoi(hour) == 9 and string.atoi(minute) <= 45) :
                    for i in room1:
                        num = []
                        room = zhulou.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 10) or (string.atoi(hour) == 11 and string.atoi(minute) <= 45) :
                    for i in room2:
                        num = []
                        room = zhulou.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 13 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 14) or \
                (string.atoi(hour) == 15 and string.atoi(minute) <= 30) :
                    for i in room3:
                        num = []
                        room = zhulou.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 15 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 16) or \
                (string.atoi(hour) == 17 and string.atoi(minute) <= 30) :
                    for i in room4:
                        num = []
                        room = zhulou.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                else:
                    fla = 0
                    for i in range(len(zx)):
                        num = []
                        num.append(zx[i].roomID)
                        num.append(zx[i].num)
                        nums.append(num)
                if fla == 1:
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
                else:
                    nroom="now it is out of class"
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
            if time == "Tuesday":
                room1 = []
                room2 = []
                room3 = []
                room4 = []
                rooms = []
                nums = []
                id1 = []
                id2 = []
                id3 = []
                id4 = []
                for i in range (len(zx)):
                    if "1" in zx[i].Tuesday:
                        room1.append(zx[i].roomID)
                        id1.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "2" in zx[i].Tuesday:
                        room2.append(zx[i].roomID)
                        id2.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "3" in zx[i].Tuesday:
                        room3.append(zx[i].roomID)
                        id3.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "4" in zx[i].Tuesday:
                        room4.append(zx[i].roomID)
                        id4.append({zx[i].roomID:StrID+zx[i].roomID})
                if (string.atoi(hour) == 8) or (string.atoi(hour) == 9 and string.atoi(minute) <= 45) :
                    for i in room1:
                        num = []
                        room = zhulou.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 10) or (string.atoi(hour) == 11 and string.atoi(minute) <= 45) :
                    for i in room2:
                        num = []
                        room = zhulou.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 13 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 14) or \
                (string.atoi(hour) == 15 and string.atoi(minute) <= 30) :
                    for i in room3:
                        num = []
                        room = zhulou.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 15 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 16) or \
                (string.atoi(hour) == 17 and string.atoi(minute) <= 30) :
                    for i in room4:
                        num = []
                        room = zhulou.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                else:
                    fla = 0
                    for i in range(len(zx)):
                        num = []
                        num.append(zx[i].roomID)
                        num.append(zx[i].num)
                        nums.append(num)
                if fla == 1:
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
                else:
                    nroom="now it is out of class"
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
            if time == "Wednesday":
                room1 = []
                room2 = []
                room3 = []
                room4 = []
                rooms = []
                nums = []
                id1 = []
                id2 = []
                id3 = []
                id4 = []

                for i in range (len(zx)):
                    if "1" in zx[i].Wednesday:
                        room1.append(zx[i].roomID)
                        id1.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "2" in zx[i].Wednesday:
                        room2.append(zx[i].roomID)
                        id2.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "3" in zx[i].Wednesday:
                        room3.append(zx[i].roomID)
                        id3.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "4" in zx[i].Wednesday:
                        room4.append(zx[i].roomID)
                        id4.append({zx[i].roomID:StrID+zx[i].roomID})
                if (string.atoi(hour) == 8) or (string.atoi(hour) == 9 and string.atoi(minute) <= 45) :
                    for i in room1:
                        num = []
                        room = zhulou.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 10) or (string.atoi(hour) == 11 and string.atoi(minute) <= 45) :
                    for i in room2:
                        num = []
                        room = zhulou.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 13 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 14) or \
                (string.atoi(hour) == 15 and string.atoi(minute) <= 30) :
                    for i in room3:
                        num = []
                        room = zhulou.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 15 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 16) or \
                (string.atoi(hour) == 17 and string.atoi(minute) <= 30) :
                    for i in room4:
                        num = []
                        room = zhulou.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                else:
                    fla = 0
                    for i in range(len(zx)):
                        num = []
                        num.append(zx[i].roomID)
                        num.append(zx[i].num)
                        nums.append(num)
                if fla == 1:
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
                else:
                    nroom="now it is out of class"
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
            if time == "Thursday":
                room1 = []
                room2 = []
                room3 = []
                room4 = []
                rooms = []
                nums = []
                id1 = []
                id2 = []
                id3 = []
                id4 = []

                for i in range (len(zx)):
                    if "1" in zx[i].Thursday:
                        room1.append(zx[i].roomID)
                        id1.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "2" in zx[i].Thursday:
                        room2.append(zx[i].roomID)
                        id2.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "3" in zx[i].Thursday:
                        room3.append(zx[i].roomID)
                        id3.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "4" in zx[i].Thursday:
                        room4.append(zx[i].roomID)
                        id4.append({zx[i].roomID:StrID+zx[i].roomID})
                if (string.atoi(hour) == 8) or (string.atoi(hour) == 9 and string.atoi(minute) <= 45) :
                    for i in room1:
                        num = []
                        room = zhulou.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 10) or (string.atoi(hour) == 11 and string.atoi(minute) <= 45) :
                    for i in room2:
                        num = []
                        room = zhulou.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 13 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 14) or \
                (string.atoi(hour) == 15 and string.atoi(minute) <= 30) :
                    for i in room3:
                        num = []
                        room = zhulou.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 15 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 16) or \
                (string.atoi(hour) == 17 and string.atoi(minute) <= 30) :
                    for i in room4:
                        num = []
                        room = zhulou.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                else:
                    fla = 0
                    for i in range(len(zx)):
                        num = []
                        num.append(zx[i].roomID)
                        num.append(zx[i].num)
                        nums.append(num)
                if fla == 1:
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
                else:
                    nroom="now it is out of class"
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
            if time == "Friday":
                room1 = []
                room2 = []
                room3 = []
                room4 = []
                rooms = []
                nums = []
                id1 = []
                id2 = []
                id3 = []
                id4 = []

                for i in range (len(zx)):
                    if "1" in zx[i].Friday:
                        room1.append(zx[i].roomID)
                        id1.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "2" in zx[i].Friday:
                        room2.append(zx[i].roomID)
                        id2.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "3" in zx[i].Friday:
                        room3.append(zx[i].roomID)
                        id3.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "4" in zx[i].Friday:
                        room4.append(zx[i].roomID)
                        id4.append({zx[i].roomID:StrID+zx[i].roomID})
                if (string.atoi(hour) == 8) or (string.atoi(hour) == 9 and string.atoi(minute) <= 45) :
                    for i in room1:
                        num = []
                        room = zhulou.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 10) or (string.atoi(hour) == 11 and string.atoi(minute) <= 45) :
                    for i in room2:
                        num = []
                        room = zhulou.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 13 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 14) or \
                (string.atoi(hour) == 15 and string.atoi(minute) <= 30) :
                    for i in room3:
                        num = []
                        room = zhulou.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 15 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 16) or \
                (string.atoi(hour) == 17 and string.atoi(minute) <= 30) :
                    for i in room4:
                        num = []
                        room = zhulou.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                else:
                    fla = 0
                    for i in range(len(zx)):
                        num = []
                        num.append(zx[i].roomID)
                        num.append(zx[i].num)
                        nums.append(num)
                if fla == 1:
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
                else:
                    nroom="now it is out of class"
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
            if time == "Saturday":
                room1 = []
                room2 = []
                room3 = []
                room4 = []
                rooms = []
                nums = []
                id1 = []
                id2 = []
                id3 = []
                id4 = []

                for i in range (len(zx)):
                    if "1" in zx[i].Saturday:
                        room1.append(zx[i].roomID)
                        id1.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "2" in zx[i].Saturday:
                        room2.append(zx[i].roomID)
                        id2.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "3" in zx[i].Saturday:
                        room3.append(zx[i].roomID)
                        id3.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "4" in zx[i].Saturday:
                        room4.append(zx[i].roomID)
                        id4.append({zx[i].roomID:StrID+zx[i].roomID})
                if (string.atoi(hour) == 8) or (string.atoi(hour) == 9 and string.atoi(minute) <= 45) :
                    for i in room1:
                        num = []
                        room = zhulou.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 10) or (string.atoi(hour) == 11 and string.atoi(minute) <= 45) :
                    for i in room2:
                        num = []
                        room = zhulou.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 13 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 14) or \
                (string.atoi(hour) == 15 and string.atoi(minute) <= 30) :
                    for i in room3:
                        num = []
                        room = zhulou.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 15 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 16) or \
                (string.atoi(hour) == 17 and string.atoi(minute) <= 30) :  
                    for i in room4:
                        num = []
                        room = zhulou.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                else:
                    fla = 0
                    for i in range(len(zx)):
                        num = []
                        num.append(zx[i].roomID)
                        num.append(zx[i].num)
                        nums.append(num)
                if fla == 1:
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
                else:
                    nroom="now it is out of class"
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
            if time == "Sunday":
                room1 = []
                room2 = []
                room3 = []
                room4 = []
                rooms = []
                nums = []
                id1 = []
                id2 = []
                id3 = []
                id4 = []

                for i in range (len(zx)):
                    if "1" in zx[i].Sunday:
                        room1.append(zx[i].roomID)
                        id1.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "2" in zx[i].Sunday:
                        room2.append(zx[i].roomID)
                        id2.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "3" in zx[i].Sunday:
                        room3.append(zx[i].roomID)
                        id3.append({zx[i].roomID:StrID+zx[i].roomID})
                    if "4" in zx[i].Sunday:
                        room4.append(zx[i].roomID)
                        id4.append({zx[i].roomID:StrID+zx[i].roomID})
                if (string.atoi(hour) == 8) or (string.atoi(hour) == 9 and string.atoi(minute) <= 45) :
                    for i in room1:
                        num = []
                        room = zhulou.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 10) or (string.atoi(hour) == 11 and string.atoi(minute) <= 45) :
                    for i in room2:
                        num = []
                        room = zhulou.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 13 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 14) or \
                (string.atoi(hour) == 15 and string.atoi(minute) <= 30) :
                    for i in room3:
                        num = []
                        room = zhulou.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                elif (string.atoi(hour) == 15 and string.atoi(minute) >= 45) or\
                (string.atoi(hour) == 16) or \
                (string.atoi(hour) == 17 and string.atoi(minute) <= 30) :
                    for i in room4:
                        num = []
                        room = zhulou.objects.get(roomID = i)
                        num.append(i)
                        num.append(room.num)
                        nums.append(num)
                    nums.sort(key = lambda x:x[1])
                else:
                    fla = 0
                    for i in range(len(zx)):
                        num = []
                        num.append(zx[i].roomID)
                        num.append(zx[i].num)
                        nums.append(num)
                if fla == 1:
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})
                else:
                    nroom="now it is out of class"
                    for i in range (len(nums)):
                        rooms.append({nums[i][0]:StrID+nums[i][0]})

        a1 = 1
        a2 = 2
        a3 = 3
        a4 = 4
        return render_to_response('result.html', locals())
    else:
        return render_to_response('nolog.html')

def aboutus(request):
    global FLAG
    if FLAG == 1:
        return render_to_response('about_us.html')
    else:
        return render_to_response('nolog.html')

def tomap(request):
    global FLAG
    if FLAG == 1:
        return render_to_response('map.html')
    else:
        return render_to_response('nolog.html')

def detail(request, Id):
    global FLAG
    if FLAG == 1:
        struct = Id[0]
        roomId = str(Id[1:])
        if struct == "1":
            poepleNum = zhengxin.objects.get(roomID = roomId).num
        elif struct == "2":
            poepleNum = zhizhi.objects.get(roomID = roomId).num
        elif struct == "3":
            poepleNum = chengyi.objects.get(roomID = roomId).num
        elif struct == "4":
            poepleNum = zhulou.objects.get(roomID = roomId).num
        return render_to_response('detail.html', locals())
    else:
        return render_to_response('nolog.html')      

def logout(request):
    global FLAG
    FLAG = 0
    return HttpResponseRedirect('http://127.0.0.1:8000/')

def submit(request,Id):
    global FLAG
    if FLAG == 1:
        struct = Id[0]
        roomId = str(Id[1:])
        if struct == "1":
            pn = zhengxin.objects.get(roomID = roomId).num 
            pn += 1
            classroom = zhengxin.objects.get(roomID = roomId)
            classroom.num = pn
            classroom.save()
            poepleNum = zhengxin.objects.get(roomID = roomId).num
        elif struct == '2':
            pn = zhizhi.objects.get(roomID = roomId).num 
            pn += 1
            classroom = zhizhi.objects.get(roomID = roomId)
            classroom.num = pn
            classroom.save()
            poepleNum = zhizhi.objects.get(roomID = roomId).num
        elif struct == '3':
            pn = chengyi.objects.get(roomID = roomId).num 
            pn += 1
            classroom = chengyi.objects.get(roomID = roomId)
            classroom.num = pn
            classroom.save()
            poepleNum = chengyi.objects.get(roomID = roomId).num
        elif struct == '4':
            pn = zhulou.objects.get(roomID = roomId).num 
            pn += 1
            classroom = zhulou.objects.get(roomID = roomId)
            classroom.num = pn
            classroom.save()
            poepleNum = zhulou.objects.get(roomID = roomId).num
        return render_to_response('detail.html',locals())
    else:
        return render_to_response('nolog.html')

def select(request):
    global FLAG
    if FLAG == 1:
        a1 = 1
        a2 = 2
        a3 = 3
        a4 = 4
        return render_to_response('map.html',locals())
    else:
         return render_to_response('nolog.html')

def add(request, id):
    a1 = 1
    a2 = 2
    a3 = 3
    a4 = 4
    strucName = "正心楼"
    if id == '1':
        strucName = "正心楼"
    if id == '2':
        strucName = "致知楼" 
    if id == '3':
        strucName = "诚意楼"
    if id == '4':
        strucName = "主楼"    
    return render_to_response('adminAdd.html',locals())

def finishAdd(request, id):
    roomid = request.GET['roomid']
    mon = request.GET['mon']
    tue = request.GET['tue']
    wed = request.GET['wed']
    thu = request.GET['thu']
    fri = request.GET['fri']
    sat = request.GET['sat']
    sun = request.GET['sun']
    if id == '1':
        roomExist = zhengxin.objects.filter(roomID = roomid)
        if  roomExist:
            roomExist[0].delete()
        roomDetail = zhengxin(roomID = roomid, Monday = mon,Tuesday = tue,\
        Wednesday = wed,Thursday = thu, Friday = fri,\
        Saturday = sat, Sunday = sun, num = 0)
        roomDetail.roomID = roomid
        roomDetail.Monday = mon
        roomDetail.Tuesday = tue
        roomDetail.Wednesday = wed
        roomDetail.Thursday = thu
        roomDetail.Friday = fri
        roomDetail.Saturday = sat
        roomDetail.Sunday = sun
        roomDetail.num = 0
        roomDetail.save()
    if id == '2':
        roomExist = zhizhi.objects.filter(roomID = roomid)
        if  roomExist:
            roomExist[0].delete()
        roomDetail = zhizhi(roomID = roomid, Monday = mon,Tuesday = tue,\
        Wednesday = wed,Thursday = thu, Friday = fri,\
        Saturday = sat, Sunday = sun, num = 0)
        roomDetail.roomID = roomid
        roomDetail.Monday = mon
        roomDetail.Tuesday = tue
        roomDetail.Wednesday = wed
        roomDetail.Thursday = thu
        roomDetail.Friday = fri
        roomDetail.Saturday = sat
        roomDetail.Sunday = sun
        roomDetail.num = 0
        roomDetail.save()
    if id == '3':
        roomExist = chengyi.objects.filter(roomID = roomid)
        if  roomExist:
            roomExist[0].delete()
        roomDetail = chengyi(roomID = roomid, Monday = mon,Tuesday = tue,\
        Wednesday = wed,Thursday = thu, Friday = fri,\
        Saturday = sat, Sunday = sun, num = 0)
        roomDetail.roomID = roomid
        roomDetail.Monday = mon
        roomDetail.Tuesday = tue
        roomDetail.Wednesday = wed
        roomDetail.Thursday = thu
        roomDetail.Friday = fri
        roomDetail.Saturday = sat
        roomDetail.Sunday = sun
        roomDetail.num = 0
        roomDetail.save()
    if id == '4':
        roomExist = zhulou.objects.filter(roomID = roomid)
        if  roomExist:
            roomExist[0].delete()
        roomDetail = zhulou(roomID = roomid, Monday = mon,Tuesday = tue,\
        Wednesday = wed,Thursday = thu, Friday = fri,\
        Saturday = sat, Sunday = sun, num = 0)
        roomDetail.roomID = roomid
        roomDetail.Monday = mon
        roomDetail.Tuesday = tue
        roomDetail.Wednesday = wed
        roomDetail.Thursday = thu
        roomDetail.Friday = fri
        roomDetail.Saturday = sat
        roomDetail.Sunday = sun
        roomDetail.num = 0
        roomDetail.save() 
    a1 = 1
    a2 = 2
    a3 = 3
    a4 = 4
    return render_to_response('admin.html',locals()) 

def delete(request, id):
    roomid = request.GET['roomidd']
    if id == '1':
        roomExist = zhengxin.objects.filter(roomID = roomid)
        if  roomExist:
            for room in roomExist:
                room.delete()
    if id == '2':
        roomExist = zhizhi.objects.filter(roomID = roomid)
        if  roomExist:
            for room in roomExist:
                room.delete()
    if id == '3':
        roomExist = chengyi.objects.filter(roomID = roomid)
        if  roomExist:
            for room in roomExist:
                room.delete()
    if id == '4':
        roomExist = zhulou.objects.filter(roomID = roomid)
        if  roomExist:
            for room in roomExist:
                room.delete() 
    a1 = 1
    a2 = 2
    a3 = 3
    a4 = 4
    return render_to_response('admin.html',locals())

def showall(request, id):
    if id == '1':
        roomExist = zhengxin.objects.all()
    if id == '2':
        roomExist = zhizhi.objects.all()
    if id == '3':
        roomExist = chengyi.objects.all()
    if id == '4':
        roomExist = zhulou.objects.all()
    a1 = 1
    a2 = 2
    a3 = 3
    a4 = 4
    return render_to_response('showall.html',locals())