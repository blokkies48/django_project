from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def login_page(request):
    """Checks if user is logged in
    
    if user is logged in 

    :returns: redirect to home
    else

    :returns: redirect to login page"""

    page = 'login'
    # If user is logged in
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Invalid username')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password')

    context = {'page': page}
    return render(request, "login/login_register.html", context)


def logout_user(request):
    ''':logs user out

        :returns: redirect to home page
    '''
    logout(request)
    return redirect('/')

def register_user(request):
    '''
    checks if valid username and password is entered

    :returns: redirect to to home

    else

    :returns: redirect to login/reg page
    '''
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Something happened during registration")
        
    return render(request, 'login/login_register.html', {'form': form})