from django.shortcuts import render
from .models import Student,OnlineClass,OnlineTest

def home(request):
	return render(request,'dav_app/home.html')

def online_class(request):
	classes = OnlineClass.objects.all()
	return render(request,'dav_app/class.html',{'classes':classes})

def online_test(request):
	tests = OnlineTest.objects.all()
	return render(request,'dav_app/test.html',{'tests':tests})

def study(request):
	return render(request,'dav_app/study.html')

def payment(request):
	return render(request,'dav_app/payment.html')

def about(request):
	return render(request,'dav_app/about.html')

def academic(request):
	return render(request,'dav_app/academic.html')

def admission(request):
	return render(request,'dav_app/admission.html')