from django.shortcuts import render
from django.shortcuts import render,redirect
from core.moody import expression
from django.contrib import messages

faceRecognition = expression()

def home(request):
    return render(request,'Mudics/home.html')

def login(request):
    face_id = faceRecognition.detection()
    print(face_id)
    return redirect('greeting' ,str(face_id))

def Greeting(request,face_id):
    return render(request,'mudics/greeting.html')
# Create your views here.
