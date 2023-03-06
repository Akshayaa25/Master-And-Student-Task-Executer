from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student,Master,Task,StudentAnswer

# Create your views here.
def zero(func=None):
    if func is None:
        return 0
    else:
        return func(0)

def one(func=None):
    if func is None:
        return 1
    else:
        return func(1)

def two(func=None):
    if func is None:
        return 2
    else:
        return func(2)

def three(func=None):
    if func is None:
        return 3
    else:
        return func(3)

def four(func=None):
    if func is None:
        return 4
    else:
        return func(4)

def five(func=None):
    if func is None:
        return 5
    else:
        return func(5)

def six(func=None):
    if func is None:
        return 6
    else:
        return func(6)

def seven(func=None):
    if func is None:
        return 7
    else:
        return func(7)

def eight(func=None):
    if func is None:
        return 8
    else:
        return func(8)

def nine(func=None):
    if func is None:
        return 9
    else:
        return func(9)

def plus(num):
    def func(x):
        return x + num
    return func

def minus(num):
    def func(x):
        return x - num
    return func

def times(num):
    def func(x):
        return x * num
    return func

def divided_by(num):
    def func(x):
        return x // num
    return func

def calculate(request, op1, operator, op2):
    num1 = int(op1)
    num2 = int(op2)
    if operator == 'plus':
        result = num1(plus(num2))
    elif operator == 'minus':
        result = num1(minus(num2))
    elif operator == 'times':
        result = num1(times(num2))

def home(request):
    return render(request,'home.html')

def masterLogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        try:
            master = Master.objects.get(username=username)
            if master.password == password1:
                response = redirect('masterDashboard')
                response.set_cookie('user', 'master')
                response.set_cookie('username', username)
                response.set_cookie('password1', password1)
                return response
            else:
                return render(request,'login.html',{'user':'master','error':'Incorrect password'})
        except Master.DoesNotExist:
            return render(request,'login.html',{'user':'master','error':'Invalid user'})
    return render(request,'login.html',{'user':'master'})

def studentLogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        try:
            student = Student.objects.get(username=username)
            if student.password == password1:
                response = redirect('studentDashboard')
                response.set_cookie('user', 'student')
                response.set_cookie('username', username)
                response.set_cookie('password1', password1)
                return response
            else:
                context = {
                    'user':'student',
                    'error':'Incorrect password'
                }
                return render(request,'login.html',context)
        except Student.DoesNotExist:
            return render(request,'login.html',{'user':'student','error':'Invalid user'})
    return render(request,'login.html',{'user':'student'})

def masterSignup(request):
    if request.method=='POST':
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1!=password2:
            return render(request,'signup.html',{'user':'master','error':'Password mismatch'})
        else:
            myuser = Master()
            myuser.username=username
            myuser.password=password1
            myuser.confirmpassword=password2
            myuser.save()
            return redirect('masterLogin')
    return render(request,'signup.html',{'user':'master'})

def studentSignup(request):
    if request.method=='POST':
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1!=password2:
            return render(request,'signup.html',{'user':'student','error':'Password mismatch'})
        else:
            myuser = Student()
            myuser.username=username
            myuser.password=password1
            myuser.confirmpassword=password2
            myuser.save()
            return redirect('studentLogin')
    return render(request,'signup.html',{'user':'student'})

def logout(request):
    response = redirect('home')
    response.delete_cookie('user')
    response.delete_cookie('username')
    response.delete_cookie('password1')
    return response


def masterDashboard(request):
    # if (request.COOKIES.get('username') and request.COOKIES.get('password1')):
    #     return render(request,'masterdashboard.html')
    # else:
    #     return redirect('home')
    return render(request,'masterdashboard.html')

def createTask(request):
    if request.method=='POST':
        task=request.POST['task']
        ans = eval(task)
        mytask = Task()
        mytask.task = task
        mytask.result = ans
        mytask.save()
    return render(request,'masterdashboard.html',{'link':'createTask'})

def taskList(request):
    mylist = Task.objects.all()
    return render(request,'masterdashboard.html',{'mylist':mylist,'link':'taskList'})

def studentAnswer(request):
    mydata = StudentAnswer.objects.all()
    context = {
        'mydata':mydata,
        'link':'studentAnswer'
    }
    return render(request,'masterdashboard.html',context)


def studentDashboard(request):
    # if (request.COOKIES.get('username') and request.COOKIES.get('password1')):
    #     return render(request,'masterdashboard.html')
    # else:
    #     return redirect('home')
    username = request.COOKIES.get('username')
    return render(request,'studentdashboard.html',{'username':username})

def viewTask(request,id):
    mytask = Task.objects.get(id=id)
    context = {
        'mytask':mytask,
        'link':'viewTask'
    }
    return render(request,'studentdashboard.html',context)

def taskSolve(request):
    return render(request,'studentdashboard.html',{'link':'taskSolve'})

def solveTask(request,id):
    mytask = Task.objects.get(id=id)
    if request.method=='POST':
        username = request.COOKIES.get('username')
        task = mytask.task
        answer=request.POST['answer']
        result = mytask.result

        studentans=StudentAnswer()
        studentans.username = username
        studentans.task = task
        studentans.answer = answer
        studentans.result = result
        studentans.save()
        return redirect ('listoftask')

    context = {
        'task':mytask,
        'link':'solveTask'
    }
    return render(request,'studentdashboard.html',context)

def listoftask(request):
    mylist = Task.objects.all()
    return render(request,'studentdashboard.html',{'mylist':mylist,'link':'listoftask'})

def activity(request):
    mydata = StudentAnswer.objects.all()
    context = {
        'mydata':mydata,
        'link':'activity'
    }
    return render(request,'studentdashboard.html',context)