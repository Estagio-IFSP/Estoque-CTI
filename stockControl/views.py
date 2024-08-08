from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from stockControl.models import ConsumableGood
from .forms import ConsumableGoodForm

def login(request):
    return render(request, "login.html")

def dashboard(request):
    return render(request, "dashboard.html")

def post_consumable_good(request):
    if request.method == "POST":
        form = ConsumableGoodForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/success")
    else:
        form = ConsumableGoodForm()

    return render(request, "consumable_good.html", { "form": form })

class ConsumableGoodListView(ListView):
    model = ConsumableGood
    template_name = "consumable_list.html"
    context_object_name = "consumables"
