from django.shortcuts import render,redirect
from django.views.generic import View
from bookapp import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from bookapp.models import Book





class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=forms.RegistrationForm()
        return render(request,"registration.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form =forms.RegistrationForm(request.POST)
        if form.is_valid():

            User.objects.create_user(**form.cleaned_data)
            return redirect("signin")
        else:
            return render(request, "registrations.html",{"form": form})


class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=forms.Loginform()
        return render(request,"login.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form=forms.Loginform(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login (request,user)
                print("login success")
                return redirect("Index")
            else:
                print("invalid credientials")
        return render(request, "login.html", {"form": form})


class IndexView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"home.html")

class SignoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")



class BookAddView(View):
    def get(self,request,*args,**kwargs):
        form=forms.BookForm()
        return render(request,"add-book.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=forms.BookForm(request.POST)
        if form.is_valid():
            form.instance.user=request.user
            form.save()
            return redirect("Index")
        else:
            return render(request, "add-book.html", {"form": form})

class BookListView(View):
    def get(self,request,*args,**kwargs):
        all_books=Book.objects.all()
        return render(request,"booklist.html",{"books":all_books})

