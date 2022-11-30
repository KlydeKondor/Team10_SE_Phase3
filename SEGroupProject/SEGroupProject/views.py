from django.shortcuts import render
import pyrebase

config = {
    "apiKey": "AIzaSyAAczCtfS-w4aTtOkcEbbP8Y5QO7DHjWJg",
    "authDomain": "segroupproject-e96f7.firebaseapp.com",
    "databaseURL": "https://segroupproject-e96f7-default-rtdb.firebaseio.com/",
    "projectId": "segroupproject-e96f7",
    "storageBucket": "segroupproject-e96f7.appspot.com",
    "messagingSenderId": "1039057704730",
    "appId": "1:1039057704730:web:c282b99886b18638447ea3"
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()


def home(request):
    day = "1"#database.child('Data').child('Day').get().val()
    id = "d"#database.child('Data').child('Id').get().val()
    projectname = "demo"#database.child('Data').child('Projectname').get().val()
    print("++++++++++++++++++++++++", projectname, "+++++++++++++++++++++++++++++++++")
    return render(request, "templates/Welcome.html", {"day": day, "id": id, "projectname": projectname})

    #return render(request, "SEGroupProject/templates/home.html", {"day": day, "id": id, "projectname": projectname})

def displayevents(request):
    return render(request, "templates/timeslots.html", {
        "date_1": "11/24/2022",
        "date_2": "11/24/2022",
        "date_3": "11/24/2022",
        "date_4": "11/24/2022",
        "date_5": "11/24/2022",
        "comment": "Choose this slot"
    })


def communityService():
    return None


def diywednesday():
    return None


def fivekrun():
    return None


def potluck():
    return None


def footballGame(request):
    return render(request, "templates/timeslotinformation.html", {
        "date_1": "11/24/2022",
        "date_2": "11/25/2022",
        "date_3": "11/26/2022",
        "date_4": "11/27/2022",
        "date_5": "11/28/2022",
        "comment": "Choose this slot"
    })