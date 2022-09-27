from django.shortcuts import render



def index(reqyest):
    return render(reqyest, 'mainapp/index.html')


def about(reqyest):
    return render(reqyest, 'mainapp/about.html')


