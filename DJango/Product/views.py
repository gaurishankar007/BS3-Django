from django.shortcuts import render, HttpResponse
from .models import Product, Student
from .forms import ProductForm, PersonForm
# Create your views here.


def index(request):
    items = Product.objects.all()
    context = {
        'products': items
    }
    return render(request, 'Product/django_web.html', context)


def post_product_data(request):
    form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'Product/postProduct.html', context)


def ger_form(request):
    form = PersonForm()
    context = {'form': form}
    return render(request, 'Product/PersonForm.html', context)


def post_student(request):
    if request.method == 'POST':
        data = request.POST
        firstname = data['firstname']
        lastname = data['lastname']
        batch = data['batch']
        image_url = data['image_url']
        category = data['category']
        student = Student.objects.create(firstname=firstname, lastname=lastname, batch=batch,
                                         image_url=image_url, category=category)

        if student:
            return HttpResponse("Student added successfully")
        else:
            return HttpResponse("Failed to add Student")

    return render(request, 'Product/addStudent.html')


def get_student(request):
    students = Student.objects.all()
    context = {'students': students}

    return render(request, 'Product/getStudents.html', context)