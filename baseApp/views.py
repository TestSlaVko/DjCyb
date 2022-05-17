

import email
from itertools import count
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .models import podatoci,coursevi,UserCourses


def taskList(request):
    return HttpResponse("hello my friend")
def FindCoursesPg(request):
    allCourses = coursevi.objects.all()
   
    zapisani = UserCourses.objects.get(user=request.session['mail'])
    krajnaNiza=[]
    for somet in allCourses:
        if somet.title in zapisani.courses:
            pass
        else:
            krajnaNiza.append(somet.title)
       
    if request.method=="POST":
        select = request.POST.get('testoj',False)
        korisnik = request.session['mail']
        najaven = UserCourses.objects.get(user=korisnik)
        if select in najaven.courses:
           pass
        else:
            najaven.courses = najaven.courses + select + ','
            
            najaven.save()
           
        return render(request,'baseApp/FindCourses.html',{'potr':krajnaNiza})

    return render(request,'baseApp/FindCourses.html',{'potr':krajnaNiza})
def ViewCoursesPg(request):
    broj1 = request.session['mail']
    broj2 = request.session['first']
    return render(request,'baseApp/ViewCourses.html',{'broj1':broj1,
    'broj2':broj2})
def HomePg(request):
   
   return render(request, 'baseApp/home.html')
def IndexPg(request):
    if request.method =="POST":
        title = request.POST.get('title',False)
        duration = request.POST.get('duration',False)
        desc = request.POST.get('description',False)
        courses = coursevi()
        courses.title = title
        courses.duration = duration
        courses.description = desc
        courses.save()
    return render(request,'baseApp/index.html')
def NotesPg(request):
    broj1 = request.session['mail']
    broj2 = request.session['first']
    return render(request,'baseApp/notes.html',{'broj1':broj1,
    'broj2':broj2})    
def CertificationsPg(request):
    broj1 = request.session['mail']
    broj2 = request.session['first']
    return render(request,'baseApp/certifications.html',{'broj1':broj1,
    'broj2':broj2})
def AnalyticsPg(request):
    broj1 = request.session['mail']
    broj2 = request.session['first']
    return render(request,'baseApp/analytics.html',{'broj1':broj1,
    'broj2':broj2}
    )    
def ProfilePg(request):
    broj1 = request.session['mail']
    broj2 = request.session['first']
    broj3 = request.session['last']
    broj4 = request.session['country']
    broj5 = request.session['age']

   
    return render(request,'baseApp/profile.html',{'broj1':broj1,
    'broj2':broj2,
    'broj3':broj3,
    'broj4':broj4,
    'broj5':broj5
    
    
    })
def CoursesPg(request):
    broj1 = request.session['mail']
    broj2 = request.session['first']
    korisnik = request.session['mail']
    najaven = UserCourses.objects.get(user=korisnik)
    
    niza = najaven.courses.split(',')
    niza.remove('')
    return render(request,'baseApp/courses.html',{'broj1':broj1,
    'broj2':broj2,
    'najaven':niza
    })      


def LoginPg(request):
    if request.method == "POST":
        Lemail = request.POST.get('logMail',False)
        Lpass = request.POST.get('logPass',False)

        user = authenticate(username=Lemail,password=Lpass)
        
        if user is not None:
            login(request,user)
            fname = user.first_name
            pod = podatoci.objects.get(email=Lemail) 
            request.session['mail'] = pod.email
            request.session['first'] = pod.firstName
            request.session['last'] = pod.lastName
            request.session['country'] = pod.country
            request.session['age'] = pod.Age
            

            return redirect('/profile')
        else:
            greska = 'invalid credentials'
            return render(request,'baseApp/login.html',{'greska':greska})



    return render(request, 'baseApp/login.html')

def RegisterPg(request):
   if request.method == "POST":
        fname = request.POST.get('fname',False)
        lname = request.POST.get('lname',False)
        email = request.POST.get('email',False)
        pass1 = request.POST.get('pass1',False)
        country = request.POST.get('country',False)
        age = request.POST.get('Age',False)
        
        myuser = User.objects.create_user(email,fname,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
       
        myuser.save()

        podatok = podatoci()
        podatok.poId = 1
        podatok.firstName = fname
        podatok.lastName = lname
        podatok.country = country
        podatok.email = email
        podatok.Age = age
        

        podatok.save()

        UserCasovi = UserCourses()
        UserCasovi.user = email
        UserCasovi.courses=''
        UserCasovi.save()

        
        return redirect('/login')
   else:
        return render(request,'baseApp/register.html')

            
   
  
   

   




 

   
  
  
