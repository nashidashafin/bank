from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import District,Branch
from django.views.generic import ListView
from . forms import AccountOpeningForm
from django.http import JsonResponse

# Create your views here.

def home(request):
    return render(request,'index.html')

def login(request):
    if request.method=='POST':
       username=request.POST['username']
       password=request.POST['password']
       user=auth.authenticate(username=username,password=password)
       if user is not None:
           auth.login(request,user)
           return redirect('btn')
       else:
           messages.info(request,"Invalid username or password")
           return redirect('login')

    return render(request,"login.html")


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already existed")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()

                print("User created")
                return redirect('login')

        else:
            messages.info(request,"Password is not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")

def btn(request):
    return render(request,'btn.html')

def form(request):
    district=District.objects.all()
    branch=Branch.objects.all()
    return render(request, 'form.html', {'district':district,'branch':branch})


def get_branches(request, district_id):
    branches = Branch.objects.filter(district_id=district_id)
    data = [{'id': branch.id, 'name': branch.name} for branch in branches]
    return JsonResponse(data, safe=False)




# def load_branch(request):
#     district_id = request.GET.get('district')
#     branch = Branch.objects.filter(district_id=district_id).order_by('name')
#     return render(request, 'form.html', {'branch': branch})

# class PersonCreateView(CreateView):
#     model = Person
#     fields = ('name', 'birthdate', 'country', 'city')
#     success_url = reverse_lazy('person_changelist')

def logout(request):
    auth.logout(request)
    return redirect('/')