from mailsend import settings
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def contactus(request):
    return render(request,'contactus.html')

def sendmail(request):
    if request.method=='POST':
        subject=request.POST.get('csubject')
        email=request.POST.get('cemail')
        message=request.POST.get('cmessage')

        toemail="amrutha91jun@gmail.com"

        res= send_mail(subject, message, email,[toemail],fail_silently=False)

        if res==1:
            rep=send_mail("REPLY", "Thank you... we will contact you soon", email,[email],fail_silently=False)
            messages.success(request,"Mail send successfully")
            return redirect('/')
        else:
            messages.warning(request,'Mail sending failed')
            return redirect('/')
    else:
        return render(request,'contactus.html')
