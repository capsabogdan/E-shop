from django.http import HttpResponse


def welcome(request):
    return HttpResponse("Welcome to the Meeting Planner!")

def about(request):
    return HttpResponse("Credits to BoCa97")