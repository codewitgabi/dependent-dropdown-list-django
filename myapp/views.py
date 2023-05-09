from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Person, City, Country


def index(request):
    if request.method == "POST":
        # get form data
        name = request.POST.get("name")
        country = Country.objects.get(name=request.POST.get("country"))
        city = request.POST.get("city")

        # create person instance
        person = Person.objects.create(
                name= name,
                city_id=city,
                country=country)
        person.save()

        # redirect
        messages.info(request, f"{person.name}'s profile created successfully.")
        return redirect("index")

    return render(request, "index.html")

