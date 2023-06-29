from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Producer
from django.template import loader
from .forms import Producer, NewUserForm


# Create your views here.
def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())


def company(request):
    template = loader.get_template("company.html")
    return HttpResponse(template.render())


def contact(request):
    template = loader.get_template("contact.html")
    return HttpResponse(template.render())


def partner(request):
    template = loader.get_template("partner.html")
    return HttpResponse(template.render())


def graph1(request):
    template_name = "graph1.html"
    return render(request, template_name)


# def home_view(request):
#     template_name = "home.html"

#     return render(request, template_name)


def register_request(request):
    if request.method == "POST":
        user_form = NewUserForm(request.POST or None, request.FILES or None)
        profile_form = Producer(request.POST or None, request.FILES or None)
        if user_form.is_valid():
            print("USER FORM is valid")
        else:
            print("USER FORM is nottttttttt valid")

        if profile_form.is_valid():
            print("PROFILE FORM is valid")
        else:
            print("PROFILE FORM is nottttttttt valid")

        if user_form.is_valid() and profile_form.is_valid():
            print("F O R M is VALID")

            user = user_form.save()
            profile = profile_form.save(commit=False)

            # assign user to your profile

            profile.user = user
            profile.save()

            return redirect("/greenhouses/login")
    else:
        user_form = NewUserForm()
        profile_form = Producer()
    return render(
        request, "register.html", {"user_form": user_form, "profile_form": profile_form}
    )
