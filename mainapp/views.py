from django.shortcuts import render



def index(reqyest):
    data = {
        'title': 'Главная страница',
        'values': ['some', 'Hello', '1234'],
        'obj': {
           'car': 'BMW',
            'age': 18,
            'hobby': 'football'
        }

        }
    return render(reqyest, 'mainapp/index.html',  data)


def about(reqyest):
    return render(reqyest, 'mainapp/about.html')


