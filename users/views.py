from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            auth_login(request, form.save())
            return redirect('users:login')
    else: 
        form = UserCreationForm()
    return render(request, 'users/register.html', { 'form': form })


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('posts:list')    
    else: 
        form = AuthenticationForm()
    return render(request, 'users/login.html', { 'form': form })        
             
             
def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('home')
             
             
# redirect(request.POST.get('next') next is the name of the hidden input field in login.html
# with that, we catch the url name we initially want to go before logged in and
# redirected to that url instead of redirect('posts:list')           