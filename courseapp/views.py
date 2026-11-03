from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads

# Create your views here.

class Course_View(View):

    def get(self, request):

        data = [
            {
                "ID": 101,
                "Course_Name": "Python Programming",
                "Category": "Programming",
                "Description": "Learn Python from basics",
                "Duration": "3 Months",
                "Course_Fee": 5000,
                "Instructor_Name": "Rahul",
                "Availability": True
            },
            {
                "ID": 102,
                "Course_Name": "Django Development",
                "Category": "Web Development",
                "Description": "Learn Django and REST APIs",
                "Duration": "4 Months",
                "Course_Fee": 7000,
                "Instructor_Name": "Arun",
                "Availability": True
            },
            {
                "ID": 103,
                "Course_Name": "Data Science",
                "Category": "Data Science",
                "Description": "Learn data analysis and visualization",
                "Duration": "6 Months",
                "Course_Fee": 10000,
                "Instructor_Name": "Anjali",
                "Availability": False
            }
        ]

        return JsonResponse(data, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class Add_Course_View(View):

    def post(self, request):
        data = request.body
        form_data = loads(data)

        Course_Name = form_data.get('Course_Name')
        Category = form_data.get('Category')
        Description = form_data.get('Description')
        Duration = form_data.get('Duration')
        Course_Fee = form_data.get('Course_Fee')
        Instructor_Name = form_data.get('Instructor_Name')
        Availability = form_data.get('Availability')

        Course = {
            "Course_Name": Course_Name,
            "Category": Category,
            "Description": Description,
            "Duration": Duration,
            "Course_Fee": Course_Fee,
            "Instructor_Name": Instructor_Name,
            "Availability": Availability
        }

        return JsonResponse(Course)

@method_decorator(csrf_exempt, name='dispatch')
class Update_Course_View(View):

    def put(self, request, id):

        data = request.body
        form_data = loads(data)
        Course_id= form_data.ger('id')
        Course_Name = form_data.get('Course_Name')
        Category = form_data.get('Category')
        Description = form_data.get('Description')
        Duration = form_data.get('Duration')
        Course_Fee = form_data.get('Course_Fee')
        Instructor_Name = form_data.get('Instructor_Name')
        Availability = form_data.get('Availability')

        Course = {
            "ID": Course_id,
            "Course_Name": Course_Name,
            "Category": Category,
            "Description": Description,
            "Duration": Duration,
            "Course_Fee": Course_Fee,
            "Instructor_Name": Instructor_Name,
            "Availability": Availability
        }

        return JsonResponse(Course)