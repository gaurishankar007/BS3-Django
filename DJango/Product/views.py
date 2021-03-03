from django.shortcuts import render, redirect
from .models import Product, Student, Person, FileUpload
from .forms import ProductForm, PersonForm
from django.http import HttpResponse
# Create your views here.


def index(request):
    items = Product.objects.all()
    context = {
        'products': items, 'active_product': 'active'
    }
    return render(request, 'Product/django_web.html', context)
# ============================================ #


def post_product_data(request):
    form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'Product/postProduct.html', context)
# ============================================ #


def get_form(request):
    if request.method == 'POST':
        data = PersonForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect('/product/personForm')
    context = {'form': PersonForm, 'active_form': 'active'}

    return render(request, 'Product/PersonForm.html', context)


def show_person_mf(request):
    person = Person.objects.all()
    context = {
        'key': person,
        'active_person': 'active'
    }
    return render(request, 'product/ShowPersonForm.html', context)


def delete_person_form(request, person_id):
    person = Person.objects.get(id=person_id)
    person.delete()
    return redirect('/product/showpersonForm')


def update_person_form(request, person_id):
    person = Person.objects.get(id=person_id)
    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('/product/showpersonForm')
    context = {'form': PersonForm(instance=person)}
    return render(request, 'Product/UpdatePersonForm.html', context)
# ============================================ #


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
            return redirect('/product/studentForm')

    context = {'active_stu': 'active'}

    return render(request, 'Product/addStudent.html', context)


def get_student(request):
    students = Student.objects.all()
    context = {'students': students, 'active_student': 'active'}

    return render(request, 'Product/getStudents.html', context)


def delete_student(request, i_id):
    student = Student.objects.get(id=i_id)
    student.delete()

    return redirect('/product/getForm')


def update_student(request, i_id):
    student = Student.objects.get(id=i_id)
    if request.method == "POST":
        data = request.POST
        student.firstname = data['firstname']
        student.lastname = data['lastname']
        student.batch = data['batch']
        student.category = data['category']
        student.image_url = data['image_url']
        student.save()

        return redirect('/product/getForm')

    context = {'student': student}

    return render(request, 'Product/updateStudent.html', context)
# ============================================ #


def post_file(request):
    if request.method == "POST":
        title = request.POST.get('title')
        file = request.FILES.get('file')
        file_obj = FileUpload(title=title, file=file)
        file_obj.save()
        if file_obj:
            return redirect('/product/getFile')
        else:
            return HttpResponse("File Can not be added")
    context = {'active_file': 'active'}
    return render(request, 'Product/AddFile.html', context)


def get_file(request):
    files = FileUpload.objects.all()
    context = {'files': files, 'active_file': 'active'}
    return render(request, 'Product/ShowFile.html', context)


def delete_file(request, file_id):
    file = FileUpload.objects.get(id=file_id)
    file.delete()
    return redirect('/product/getFile')


def update_file(request, file_id):
    file = FileUpload.objects.get(id=file_id)
    if request.method == 'POST':
        if request.FILES.get('file'):
            file.file.delete()
            file.title = request.POST.get('title')
            file.file = request.FILES.get('file')
            file.save()
        else:
            file.title = request.POST.get('title')
            file.save()
        return redirect('/product/getFile')
    context = {'files': file, 'active_file': 'active'}
    return render(request, 'Product/UpdateFile.html', context)
# ============================================ #

