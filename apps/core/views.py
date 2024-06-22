from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request, 'home_admin.html')
        return render(request, 'home_user.html')
