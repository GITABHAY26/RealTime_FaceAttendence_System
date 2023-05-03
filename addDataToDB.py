
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred ,{
    "databaseURL" :"https://face-attendence-real-tim-a2d78-default-rtdb.firebaseio.com/"

})

ref = db.reference('students')

data={
    "456771" :
        {

            "id": 456771,
            "name": "Abhay sonakiya",
            "major" :"designing",
            "starting_year" : 2022,
            "total_attendance" : 5,
            "standing": "Good",
            "year":5,
            "last_attendance_time":"2023-24-04 00:54:34"
        },

    "852741" :
        {   "id":852741,
            "name": "palak dixit",
            "major" :"designing",
            "starting_year" : 2022,
            "total_attendance" : 3,
            "standing": "Good",
            "year":5,
            "last_attendance_time":"2023-24-04 00:54:34"
        },

    "963852" :
        {
            "name": "teji parsh",
            "major" :"designing",
            "starting_year" : 2022,
            "total_attendance" : 3,
            "standing": "Good",
            "year":5,
            "last_attendance_time":"2023-24-04 00:54:34"
        },

    "321654" :
        {
            "name": "mukul Jangid",
            "major" :"IT",
            "starting_year" : 2022,
            "total_attendance" : 3,
            "standing": "Good",
            "year":5,
            "last_attendance_time":"2023-24-04 00:54:34"
        }
}

for key,value in data.items():
    ref.child(key).set(value)