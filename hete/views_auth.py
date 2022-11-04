from base64 import urlsafe_b64decode
from email.message import EmailMessage
from faulthandler import cancel_dump_traceback_later
import imp
from lib2to3.pgen2.tokenize import generate_tokens
from pdb import post_mortem
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect,render
from django.contrib.auth import authenticate,login,logout
from hetelei import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from . tokens import *
# Create your views here.
def home(request):
    return render(request,"index.html")

def signup(request):
    
    if request.method == "POST":
        # username = request.POST.get(username) # esta manera es valida NO ME FUNCIONO
        username = request.POST['username']
        nombre = request.POST['nombre'] # esta manera tambien es valida
        email = request.POST['correo']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username = username):
            messages.error(request,"El usuario ya existe")
            return redirect('signin')
        # if User.objects.filter(email = email):
        #     messages.error(request,"Este email ya existe")
        #     return redirect('singup')
        if pass1 != pass2:
            messages.error(request,"Las contraseñas no coinciden")
        
        # Properties of the user
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = nombre
        myuser.is_active = False # no se activa hasta que aprienta el link de activacion

        # Insertion of the user
        myuser.save()

        # Welcome mail
        subject = "Bienvenido a HETELEI!!"
        message = "Hola "+myuser.first_name+"!! /nGracias por usar Hetelei, ante cualquier consulta, duda o sugerencia no dudes en escribir al (+595) 985 777 745"
        from_mail = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_mail, to_list,fail_silently=True)
        messages.success(request,"Tu cuenta ha sido creada correctamente, te hemos enviado un correo de saludo")

        #Email address confirmation
        current_site = get_current_site(request)
        conf_subject = "Confirme su email Hetelei login"
        message2 = render_to_string('authentication/email_confirmation.html',{
            'name':myuser.first_name,
            'domain':current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser),
        })
        send_mail(conf_subject,message2,from_mail, to_list,fail_silently=True)
        # email_mesagge = EmailMessage(conf_subject,message2,settings.EMAIL_HOST_USER,[myuser.email],)
        # email.fail_silently = True
        # email_mesagge.send()

        messages.success(request,"Te hemos enviado un correo para confirmar tu cuenta")
        return redirect('signin')
        
    return render(request,"authentication/signup.html")

def signin(request):

    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = authenticate(username = username, password = pass1)

        if user is not None:
            login(request, user)
            fname = user.get_short_name()
            return render(request,'web/inicio.html',{'nombre':fname})
        else:
            messages.error(request,"No se pudo ingresar")
            return redirect('signin')

    return render(request,"authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request,"Ha salido correctamente")
    return redirect('home')

def activate(request,uidb64,token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk = uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None
    
    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
         
        # Insertion of the user
        myuser.save()

        login(request, myuser)
        return redirect('home')
    
    else:
        return render(request,'authentication/activation_failed.html')