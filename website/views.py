from django.shortcuts import render , redirect# type: ignore
from django.contrib.auth import authenticate,login,logout # type: ignore
from django.contrib import messages # type:ignore
from .forms import signUpform ,AddRecordForm
from .models import Record

# Create your views here.

def home(request):
    records = Record.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successful')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials')
            return render(request, 'home.html')

    return render(request, 'home.html', {'rec': records})



def logout_user(request):
    logout(request)
    messages.success(request,"You have been Logged out..")
    return render(request,'home.html',{})

def register_user(request):
    if request.method=='POST':
        form=signUpform(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,'Registration Successful')
            return redirect('home')
        else:
            messages.error(request,'Invalid Credentials') 
            return render(request,'register.html',{'form':form})
    else:
        form=signUpform()
        return render(request,'register.html',{'form':form})
 # form is passed to 'form' so now you cha use form in register.html 

def customer_record(request , pk):
    if request.user.is_authenticated:
        #lookup records
        cr= Record.objects.get(id=pk)
        return render(request,'record.html',{'customer_record':cr})
    else:
        messages.error(request,'You must be logged into that page.') 
        return redirect('home')

def delete_record(request , pk):
    if request.user.is_authenticated:
        deleteit= Record.objects.get(id=pk)
        deleteit.delete()
        messages.success(request,'Record Deleted')
        return redirect('home')
    else:
        messages.error(request,'You must be logged into that page.')
        return redirect('home')
    
def add_record(request):
    form=AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method=="POST":
            if form.is_valid():
                add_record=form.save()
                messages.success(request,"Record added...")
                return redirect('home')
        return render(request, 'addrec.html',{'form':form})
    else:
        messages.success(request,"You must be logged in...")
        return render(request,'addrec.html',{})
    
def update_record(request , pk):
    if request.user.is_authenticated:
        current_record= Record.objects.get(id=pk)
        form=AddRecordForm(request.POST or None,instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,'Record has been Updated...')
            return redirect('home')
        return render(request, 'update_record.html',{'form':form})
    else: 
        messages.error(request,'You must be logged into that page.')
        return redirect('home')