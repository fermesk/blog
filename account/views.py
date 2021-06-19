from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse
from django.contrib.auth import login



# Create your views here.
def signup(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #log user in
            return HttpResponseRedirect(reverse('article'))
    else:
        form = UserCreationForm()
    return render(request,'account/signup.html',{'form':form})

def signin(request):
    if request.method =='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get.user()
            login(request.user)
            #log user in
            return HttpResponseRedirect(reverse('article'))
    else:
        form = AuthenticationForm()
    return render(request,'account/signin.html',{'form':form})
