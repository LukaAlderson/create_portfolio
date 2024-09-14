from django.db import models

from regist.models import Registration

class MainForm(models.Model):
    
    def set_default_data():
        name = Registration.name
        surname = Registration.surname
        birthday = Registration.birthday
        email = Registration.email
        return name, surname, birthday, email

    #if user choice default data -> set_default_data. Make later... 
    if 1 == 1: 
        set_default_data()


    live_addres = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=10)
    about_me = models.TextField()

    