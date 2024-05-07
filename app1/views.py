from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Contact
from django.contrib import messages
from .models import RegisterNgo
from django.core import validators
from .models import RegisterNgo
# from .models import UserProfile
# from .forms import UserProfileForm 




# from django.contrib. import messages
# Create your views here.
# @login_required(login_url='login')

def Ngoreg(request):
    servicesData=RegisterNgo.objects.all()
    data={
        'servicesData':servicesData
    }
    return render(request,'ngoprofile.html',data)


def HomePage(request):
     if request.method == 'POST':
        
        contact=Contact()
        name=request.POST.get('name')
        
        mobile=request.POST.get('mobile')
        donation=request.POST.get('donation')
        address=request.POST.get('address')
        message=request.POST.get('message')
        contact.name=name
        contact.mobile=mobile
        contact.donation=donation
        contact.address=address
        contact.message=message
        contact.save()
        if contact.name == "" and contact.mobile == "" :
         messages.error(request, 'Please correct the errors below.')
        else :
            return redirect('home')

    

        
        
        # Process the form data here (save to database, send email, etc.)
        # You can access form data using request.POST.get('name_of_input_field')
        # Redirect or render a thank you page after processing the form
        

     return render(request,'home.html')

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not the same!!")
        # elif User.objects.filter(username=uname).exists():
        #     messages.error(request, "This username is already taken")
        #     return redirect('signup')
        elif User.objects.filter(username=uname).exists():
            return render(request, 'signup.html', {'error_message': 'Username already exists. Please choose a unique username.'})
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')
    else:
        return render(request, 'signup.html')

def Achievement(request):
    return render(request,'achivements.html')
       

# @login_required
# def update_profile(request):
#     if request.method == 'POST':
#         profile_form = UserProfileForm(request.POST, instance=request.user.profile)
#         if profile_form.is_valid():
#             profile_form.save()
#             return redirect('profile')  # Redirect to profile page after update
#     else:
#         profile_form = UserProfileForm(instance=request.user.profile)  # Pre-populate form

#     context = {'profile_form': profile_form}
#     return render(request, 'profile.html', context)       



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def logout(request):
    logout(request)
    
    return redirect ('home')

def Ngo(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        user=authenticate(request,username=username,email=email)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or email is incorrect!!!")


    return render (request,'ngo.html')

def register_ngo(request):
    if request.method == 'POST':
        registration = RegisterNgo()  # Rename the variable
        username = request.POST.get('username')
        name = request.POST.get('name') 
        contact = request.POST.get('contact')
        register_number = request.POST.get('register')  # Renamed to avoid conflict
        address = request.POST.get('address')
    
        email = request.POST.get('email')
        weburl = request.POST.get('weburl')
        
        # Assign values to the model instance
        registration.username = username
        registration.name = name
        registration.contact = contact
        registration.register = register_number  # Assign the register number to the register field
        registration.address = address
        registration.email = email
        registration.webUrl = weburl
        
        registration.save()  # Save the instance to the database
    
    return render(request, 'registers.html')


# views.py



# def contact_view(request):
#     if request.method == 'POST':
#         # Process the form data here (save to database, send email, etc.)
#         # You can access form data using request.POST.get('name_of_input_field')
#         # Redirect or render a thank you page after processing the form
#         al("form submited")
#         return render(request, 'home.html')
#     else:
#         return render(request, 'home.html')

# def Payment(request):
#     return HttpResponse("hello")


def profile(request):
    return render(request,'profile.html')
    
        
