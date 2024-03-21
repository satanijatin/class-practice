from django.shortcuts import render,redirect
from .models import Student
import os
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout





def index(request):
    return render(request,'index.html')


def loginpage(request):
    if request.method=='POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')


        user =  authenticate(username=username,password=password)
        print(user)
        if user is None:
            messages.info(request,"Invalid credentials")
            return redirect('login')
        else:
           login(request,user)
           return redirect('reg')


    return render(request,'login.html')

def SignupPage(request):
    if request.method=='POST':
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        username = data.get('username')
        password = data.get('password')

        if User.objects.filter(username=username).exists():
             messages.info(request,"User alredy exist !!!")
             return redirect('/')

        user = User(first_name=first_name,last_name=last_name,username=username)
        user.set_password(password)
        user.save()
        messages.info(request,"Registration successfully done !!!")
        return redirect('login')

    return render(request,'signup.html')
  
  
def LogoutPage(request):
    logout(request)
    return redirect('/')
    

@login_required(login_url='/')
def reg(request): 
    if request.method=='POST':
        if request.POST['form_type']=="insert":
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
                                    
                # try:    
                #         select_user.lang=str_lan
                #         os.remove(select_user.img.path)
                #         select_user.img = request.FILES['img']
                    
                #         select_user.save()
                # except:
                #         select_user.lang=str_lan
                #         select_user.save()
                
                if len(request.FILES) !=0 :
                        if select_user.img != "":
                            os.remove(select_user.img.path)
                            select_user.img = request.FILES.get('img')
                        else:
                            select_user.img = request.FILES.get('img')
                else:
                    select_user.img=select_user.img
                        
                select_user.save()
                        
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
                return redirect('reg')
        else:
            
            global datas 
        
            uname = request.POST['uname']
            email = request.POST['email']

                
            q_objects = Q()
    
            if uname!="":
                    q_objects &= Q(uname__icontains=uname)
            if email!="":
                    q_objects &= Q(email__icontains=email)
              
            
            
            datas = Student.objects.filter(q_objects)          
                      
            p = Paginator(datas, 4) 
            page_number = request.POST.get('pageno')
            try:
                page_obj = p.get_page(page_number) 
            except PageNotAnInteger:
                    
                    page_obj = p.page(1)
            except EmptyPage:
                    page_obj = p.page(p.num_pages)
                
            context =  {
                        'alldata':datas,
                        'page_obj': page_obj,
                        "uname":uname,
                        "email":email,
                        'total_page':range(1, page_obj.paginator.num_pages+1)
                    }
           
            return render(request, 'regajax.html', context)            
    else:
         return render(request,'reg.html')

def editUser(request,user_id):
       
        select_user = Student.objects.get(id=user_id)
        alldata = Student.objects.all()
        p = Paginator(alldata, 4) 
        page_number = request.POST.get('pageno')
        try:
            page_obj = p.get_page(page_number) 
        except PageNotAnInteger:
       
            page_obj = p.page(1)
        except EmptyPage:
      
            page_obj = p.page(p.num_pages)
        
        context =  {
            'alldata':alldata,
            'page_obj': page_obj,
            "select_user":select_user,
            'action':"edit",
            'total_page':range(1, page_obj.paginator.num_pages+1)
         }
    
        return render(request,"reg.html",context)

def deleteUser(request,user_id):
    deletedata=Student.objects.get(id=user_id)
    os.remove(deletedata.img.path)
    deletedata.delete()
    return redirect('reg')




  
        
    
    