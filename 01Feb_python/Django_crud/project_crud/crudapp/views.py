from django.shortcuts import render,redirect,get_object_or_404
from .models import Student
# Create your views here.
def index(request):
    return render(request,'index.html')






def reg(request):

    if request.method=='POST':
        
        if request.POST['user_id']!="":
            user_id = request.POST['user_id']
            data = request.POST
            select_user = Student.objects.get(id=user_id)
            select_user.uname = data.get('uname')
            select_user.email = data.get('email')
            select_user.password = data.get('password')
            select_user.gender = data.get('gender')
            
            str_lan = ",".join(str(element) for element in request.POST.getlist("lng"))
            
            print(str_lan)
                      
            select_user.country = data.get('country')
                                 
            try:    
                    select_user.lang=str_lan
                    select_user.img = request.FILES['img']
                    select_user.save()
            except:
                    select_user.lang=str_lan
                    select_user.save1()
            return redirect('reg')
        else:
            data = request.POST
            uname = data.get('uname')
            email = data.get('email')
            password = data.get('password')
            gender = data.get('gender')
            lang = data.getlist('lng')
            country = data.get('country')
            img = request.FILES.get('img')

        
            lng=""
            j=0
            for i in lang:
                if j==0:
                    lng=lng+i
                else:
                    lng=lng+","+i
                j=j+1
          

            Student.objects.create(uname=uname,email=email,password=password,gender=gender,lang=lng,country=country,img=img)
            alldata = Student.objects.all()
            context = {'alldata':alldata}
            return render(request,'reg.html',context)
    else:
        alldata = Student.objects.all()
        context = {'alldata':alldata}
        return render(request,'reg.html',context)

def editUser(request,user_id):
       
    select_user = Student.objects.get(id=user_id)
    alldata = Student.objects.all()
    return render(request,"reg.html",{"select_user":select_user,'alldata':alldata})

def deleteUser(request,user_id):
    deletedata=Student.objects.get(id=user_id)
    deletedata.delete()
    return redirect('reg')