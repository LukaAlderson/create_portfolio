from django.shortcuts import render

def my_profile(request):
    return render(request, "myprofile/profile.html")

