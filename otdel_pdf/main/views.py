from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'main/index.html')

def admin_panel(request):
    return render(request, 'main/adminPanel.html')

def new_user(request):
    return render(request, 'main/addNewUser.html')

def delete_user(request):
    return render(request, 'main/deleteUser.html')

def change_password(request):
    return render(request, 'main/changePassword.html')