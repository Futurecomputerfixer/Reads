from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
from django.db import IntegrityError
from django.http import JsonResponse
from datetime import date, timedelta
from urllib.parse import unquote
# emojis 🥰 😂
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        records = Record.objects.filter(user=user).order_by("book_id").all()
        time = [value["timestamp"] for value in records.values("timestamp")]
        records = records.values_list("book", "checkin")
        print(records)
        books = Book.objects.filter(id__in=[record[0] for record in records])
        print(books)
        checkin = [record[1] for record in records]

        iter = range(len(books))
        data = []
        for i in iter:
            if not checkin[i]:
                time[i] = time[i] + timedelta(days=7)
            time[i] = time[i].strftime("%m/%d/%y")
            data.append([time[i], checkin[i], books[i]])
        print(data)

        return render(request, "checkin/index.html", {"data": data})
    else:
        return HttpResponseRedirect(reverse("login"))


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "checkin/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "checkin/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "checkin/register.html", {
                "message": "Passwords must match."

            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "checkin/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "checkin/register.html")


def library(request):  # return a list of books ordered in checkouts for recommendation
    user = User.objects.get(username=request.user)
    records = Record.objects.filter(user=user).order_by("-timestamp").all()
    records = records.values("book")
    books = Book.objects.exclude(
        id__in=[record['book'] for record in records]).order_by("-checkouts").all()
    return render(request, "checkin/library.html", {
        "books": books
    })


def checkout(request, book):
    user = User.objects.get(username=request.user)
    book = unquote(book)
    book = Book.objects.get(title=book)
    book.checkouts = book.checkouts + 1
    book.save()
    try:
        record = Record.objects.get(user=user, book=book)
        record.checkin = True
        record.save()
        return HttpResponseRedirect(reverse("index"))

    except:
        record = Record(user=user, book=book)
        record.save()
        today = date.today() + timedelta(days=7)

        return JsonResponse({"date": today.strftime("%m/%d/%y")})
