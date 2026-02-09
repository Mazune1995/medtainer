from django.shortcuts import render  # ✅ This is required

def home(request):
    return render(request, 'medtainer_app/home.html')
