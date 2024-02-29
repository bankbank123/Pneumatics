import secrets
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from PnHyWeb.models import Role, Student
from django.views.decorators.csrf import csrf_exempt
import pdb



def home(request):
    return render(request,'homepage.html')
    
def index(request):
    return render(request,'login.html')

def register(request):
   return render(request,'register.html')

def competency(request):
    return render(request, 'competency.html')

def unit1(request):
    return render(request, 'unit1.html')

def unit2(request):
    return render(request, 'unit2.html')

def unit3(request):
    return render(request, 'unit3.html')

def test(request):
    return render(request, 'test.html')

def pretest(request):
    return render(request, 'pretest.html')

@csrf_exempt
def register_post(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id') 
        if Student.objects.filter(student_id=student_id).exists():
            error_message = "Student ID already exists"
            return render(request, 'register.html', {'error_message': error_message})

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        token = secrets.token_urlsafe(100)
        if student_id == '' or first_name == '' or last_name == '' or email == '' or password == '' or confirm_password == '':
            error_message = "Please fill in complete information."
            return render(request, 'register.html', {'error_message': error_message})
        if password != confirm_password:
            error_message = "Passwords do not match"
            return render(request, 'register.html', {'error_message': error_message})
        if len(password) < 8:  
            error_message = "Password must be at least 8 characters long"
            return render(request, 'register.html', {'error_message': error_message})

        # Retrieve the role object for 'student'
        student_role = Role.objects.get(role_id='2')

        # Create the student object with the retrieved role object
        student = Student(student_id=student_id, password=password, email=email, first_name=first_name, last_name=last_name, token=token, role=student_role)
        student.save()
        success_message = "Register Successful"
        return render(request, 'register.html', {'success_message' : success_message, 'token' : token})
    else:
        return HttpResponse("Only POST requests are allowed", status=405)

    

@csrf_exempt
def postLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        user = Student.objects.filter(first_name=username).first() \
                or Student.objects.filter(student_id=username).first() \
                or Student.objects.filter(email=username).first()
        if user:
            if user.token:
                return JsonResponse({'token': user.token})
            else:
                token = secrets.token_urlsafe(100)
                user.token = token
                user.save()
                return JsonResponse({'token': token})
            
@csrf_exempt
def postLogout(request):
    if request.method == 'POST':
        token = request.POST.get('token')
        user = Student.objects.filter(token=token).first()
        if user:
            if user.token:
                user.token = ''
                user.save()
    
@csrf_exempt
def get_user(request):
    # pdb.set_trace() ไว้ Debugger
    if request.method == 'POST':
        token = request.POST.get('token')
        if Student.objects.filter(token=token).exists():
            user = Student.objects.get(token=token)
            first_name = user.first_name
            last_name = user.last_name
            return JsonResponse({'first_name': first_name, 'last_name': last_name})
    else:
        return HttpResponse("Only POST requests are allowed", status=405)

