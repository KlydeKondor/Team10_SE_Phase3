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

def displayEvents(request):
    return render(request, "templates/timeslots.html", {
        "date_1": "11/24/2022",
        "date_2": "11/24/2022",
        "date_3": "11/24/2022",
        "date_4": "11/24/2022",
        "date_5": "11/24/2022",
        "comment": "Choose this slot"
    })


def communityService(request):
    return render(request, "templates/timeslotinformation.html", {
        "date_1": "11/24/2022",
        "date_2": "11/25/2022",
        "date_3": "11/26/2022",
        "date_4": "11/27/2022",
        "date_5": "11/28/2022",
        "start_1": "11:00 AM",
        "end_1": "2:00 PM",
        "start_2": "11:00 AM",
        "end_2": "2:00 PM",
        "start_3": "11:00 AM",
        "end_3": "2:00 PM",
        "start_4": "11:00 AM",
        "end_4": "2:00 PM",
        "start_5": "11:00 AM",
        "end_5": "2:00 PM",
        "comment": "Choose this slot"
    })


def diywednesday(request):
    return render(request, "templates/timeslotinformation.html", {
        "date_1": "08/31/2022",
        "date_2": "09/28/2022",
        "date_3": "10/26/2022",
        "date_4": "11/30/2022",
        "date_5": "12/28/2022",
        "start_1": "11:00 AM",
        "end_1": "2:00 PM",
        "start_2": "11:00 AM",
        "end_2": "2:00 PM",
        "start_3": "11:00 AM",
        "end_3": "2:00 PM",
        "start_4": "11:00 AM",
        "end_4": "2:00 PM",
        "start_5": "11:00 AM",
        "end_5": "2:00 PM",
        "comment": "Choose this slot"
    })


def fivekrun(request):
    return render(request, "templates/timeslotinformation.html", {
        "date_1": "11/24/2022",
        "date_2": "11/25/2022",
        "date_3": "11/26/2022",
        "date_4": "11/27/2022",
        "date_5": "11/28/2022",
        "start_1": "11:00 AM",
        "end_1": "2:00 PM",
        "start_2": "11:00 AM",
        "end_2": "2:00 PM",
        "start_3": "11:00 AM",
        "end_3": "2:00 PM",
        "start_4": "11:00 AM",
        "end_4": "2:00 PM",
        "start_5": "11:00 AM",
        "end_5": "2:00 PM",
        "comment": "Choose this slot"
    })


def potluck(request):
    return render(request, "templates/timeslotinformation.html", {
        "date_1": "11/24/2022",
        "date_2": "11/25/2022",
        "start_1": "11:00 AM",
        "end_1": "2:00 PM",
        "start_2": "11:00 AM",
        "end_2": "2:00 PM",
        "comment": "Choose this slot"
    })


def footballGame(request):
    return render(request, "templates/timeslotinformation.html", {
        "date_1": "08/13/2022",
        "date_2": "09/10/2022",
        "date_3": "10/15/2022",
        "date_4": "11/26/2022",
        "date_5": "12/10/2022",
        "start_1": "6:00 PM",
        "end_1": "9:00 PM",
        "start_2": "6:00 PM",
        "end_2": "9:00 PM",
        "start_3": "2:00 PM",
        "end_3": "5:00 PM",
        "start_4": "2:00 PM",
        "end_4": "5:00 PM",
        "start_5": "6:00 PM",
        "end_5": "9:00 PM",
        "comment": "Choose this slot"
    })

def createEvent(request):
    return render(request, "templates/CreateEvent.html")

def validateEvent(request):
    return render(request, "templates/ValidateEvent.html")