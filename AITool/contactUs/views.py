from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def contactUs(request):
    try:
        name = request.GET['name']
        email = request.GET['email']
        message = request.GET['message']
        print(name,email,message)
        # if name!=None and email!=None and message!=None:
        send_mail(
            'user want contact with you',
            'name',
            'rockstarahuja99@gmail.com',
            ['surajpandey7493@gmail.com']

        )
        send_mail(
            'sucesfully submit contactUs page',
            'name',
            'rockstarahuja99@gmail.com',
            [email]

        )
    except:
        # pass
        print("error")
    return render(request,'contactUs.html')
