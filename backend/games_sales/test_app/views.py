from django.shortcuts import render

from accounts.models import Account
from django.views import View


def get_users(request):
    users = Account.objects.all()
    return render(request, 'test_app/users.html', {'users': users})


class TestAppView(View):
    def get(self, request):
        users = Account.objects.all().select_related('profile')

        return render(request, 'test_app/users.html', {'users': users})
