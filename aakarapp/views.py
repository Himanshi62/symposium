from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, redirect
from allauth.socialaccount.models import SocialAccount

## import data tables from database
from .models import Submission


# Create your views here.

def home(request):
    return render(request, "home.html")
def submission(request):
    return render(request, "submission.html")


def submitted(request):
    if request.method == "POST":
        user = request.user
        author = request.POST.get('author', '')
        email = user.email
        colgName = request.POST.get('colgName', '')
        degree = request.POST.get('degree', '')
        mobileNo = request.POST.get('mobileNo', '')
        co1 = request.POST.get('co1', '')
        mail1 = request.POST.get('mail1', '')
        co2 = request.POST.get('co2', '')
        mail2 = request.POST.get('mail2', '')
        co3 = request.POST.get('co3', '')
        mail3 = request.POST.get('mail3', '')
        field = request.POST.get('field', '')
        title = request.POST.get('title', '')
        others = request.POST.get('others', '')
        abstract = request.POST.get('abstract', '')
        authentication = request.POST.get('authentication', '')

        response = Submission(author=author, email=email, colgName=colgName,  degree=degree, mobileNo=mobileNo,
                              co1=co1, mail1=mail1, co2=co2, mail2=mail2, co3=co3, mail3=mail3, field=field, title=title, others=others, abstract=abstract, authentication=authentication)
        response.save()

    return  redirect('home')

