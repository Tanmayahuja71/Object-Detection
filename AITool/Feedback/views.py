from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def feedback(request):
    #message = request.GET['message']
    try:
        firstName = request.GET['firstName']
        lastName = request.GET['lastName']
        email = request.GET['email']
        gender = request.GET['gender']
        rating = request.GET['rating']
        send_mail(
            'feedback succesfully submited',
            'firstName',
            'objectdetectionsystem@gmail.com',
            ['surajpandey7493@gmail.com','tanmay.ahuja71a@gmail.com']


        )
        send_mail(
            'feedback succesfully submited',
            'firstName',
            'objectdetectionsystem@gmail.com',
            [email]

        )
    except:
        print('error')
    return render(request,'feedback.html')