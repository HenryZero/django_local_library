from django.shortcuts import render
from .models import Accountdb
from django.urls import path
from accountdb.models import Accountdb


def accountdb_index(request):
    usrpwd_file = open(r"/home/zero/django_local_library/interData/usrpwd.txt", "r+")

    day = []
    time = []
    port = []
    username = []
    password = []
    website = []
    delete = []

    for line in usrpwd_file.readlines():

        line = "nothing,"+line+"fordelete"
        da, ti, po, us, pa, we, de = line.strip().split(',')
#https://www.thinbug.com/q/48615477 
#https://www.delftstack.com/zh-tw/howto/python/how-to-remove-last-character-from-string-in-python/       

#string hide to star *
        if len(str(us)) <= 3:
            star_us=str(us)
            final_us = star_us[:-len(us)]+"*"*(len(us))
            print(final_us)
        elif len(str(us)) <= 4:
            star_us=str(us)
            final_us = star_us[:-2]+"*"*(int(len(us)/2))
            print(final_us)
        elif len(str(us)) > 4:
            star_us=str(us)
            final_us = star_us[:-(int(len(us)/2))]+"*"*(int(len(us)/2)+1)

        if len(str(pa)) <= 3:
            star_pa=str(pa)
            final_pa = star_pa[:-len(pa)]+"*"*(len(pa))
            print(final_pa)
        elif len(str(pa)) == 4:
            star_pa=str(pa)
            final_pa = star_pa[:-2]+"*"*(int(len(pa)/2))
            print(final_pa)
        elif len(str(pa)) > 4:
            star_pa=str(pa)
            final_pa = star_pa[:-(int(len(pa)/2))]+"*"*(int(len(pa)/2)+1)



        day.append(da)
        time.append(ti)
        port.append(po)
        username.append(final_us)
        password.append(final_pa)
        website.append(we)



        accountdb = Accountdb.objects.create(day=da, time=ti, port=po, username=final_us, password=final_pa, website=we)
        accountdb.save()

        #counter = 0
        #for item in usrpwd_file:
        #    usrpwd_file_object = Day(day=day[counter], time=time[counter],port=port[counter],username=username[counter],password=password[counter],website=website[counter])
        #    usrpwd_file_object.save()
        #    print(usrpwd_file_object)
        #    counter = counter + 1
        #    print(counter)

    with open(r"/home/zero/django_local_library/interData/usrpwd.txt", "r+") as f:
        f.truncate()
        read_data = f.read()
        f.truncate()
    accountdb_list = Accountdb.objects.all()  # 把所有 Vendor 的資料取出來
    context = {'accountdb_list': accountdb_list}
    return render(request, 'test.html', context)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  






