from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse
from django.shortcuts import render
from .models import Emp, Role, Dept
from datetime import datetime
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request, 'index.html')



def all_emp(request):
    emps = Emp.objects.all()
    context = {
        'emps':emps
    }
    # print(context)
    return render(request, 'all_emp.html', context)



# def add_emp(request):

#     if request.method == 'POST':
#         fname = request.POST['fname']
#         lname = request.POST['lname']
#         phoneNo = int(request.POST['phoneNo'])
#         salary = int(request.POST['salary'])
#         department = request.POST['fname']
#         bonus = int(request.POST['fname'])


#     # Assuming you have some logic to fetch departments and roles from the database
#     departments = Dept.objects.all()
#     roles = Role.objects.all()

#     context = {
#         'departments': departments,
#         'roles': roles,
#     }

#     return render(request, 'add_emp.html', context)


@csrf_exempt
def add_emp(request):
    if request.method == 'POST':
        # Retrieve data from the form
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        phoneNo = int(request.POST.get('phoneNo', 0))
        salary = int(request.POST.get('salary', 0))
        department_id = int(request.POST.get('dept', 0))
        role_id = int(request.POST.get('role', 0))
        bonus = int(request.POST.get('bonus', 0))
        email = request.POST.get('email', '')
        joinDate_str = request.POST.get('joinDate', '')  # Retrieve as string

        # Parse the joinDate string to a datetime object
        joinDate = datetime.strptime(joinDate_str, "%Y-%m-%d").date() if joinDate_str else None

        department = Dept.objects.get(pk=department_id)
        role = Role.objects.get(pk=role_id)

        new_emp = Emp(
            fname=fname,
            lname=lname,
            phoneNo=phoneNo,
            salary=salary,
            dept=department,
            role=role,
            bonus=bonus,
            email=email,
            joinDate=joinDate
        )

        new_emp.save()

        return HttpResponse("Employee added successfully")

    departments = Dept.objects.all()
    roles = Role.objects.all()

    context = {
        'departments': departments,
        'roles': roles,
    }

    return render(request, 'add_emp.html', context)
    if request.method == 'POST':
        # Retrieve data from the form
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        phoneNo = int(request.POST.get('phoneNo', 0))
        salary = int(request.POST.get('salary', 0))
        department_id = int(request.POST.get('dept', 0))
        role_id = int(request.POST.get('role', 0))
        bonus = int(request.POST.get('bonus', 0))
        
        joinDate_str = request.POST.get('joinDate', '')  # Retrieve as string

        # Parse the joinDate string to a datetime object
        joinDate = datetime.strptime(joinDate_str, "%Y-%m-%d").date() if joinDate_str else None

        department = Dept.objects.get(pk=department_id)
        role = Role.objects.get(pk=role_id)

        new_emp = Emp(
            fname=fname,
            lname=lname,
            phoneNo=phoneNo,
            salary=salary,
            dept=department,
            role=role,
            bonus=bonus,
            joinDate = datetime.strptime(joinDate_str, "%Y-%m-%d").date() if joinDate_str else None
        )

        new_emp.save()

        return HttpResponse("Employee added successfully")  # Import HttpResponse

    departments = Dept.objects.all()
    roles = Role.objects.all()

    context = {
        'departments': departments,
        'roles': roles,
    }

    return render(request, 'add_emp.html', context)


@csrf_exempt
def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            removed = Emp.objects.get(id=emp_id)
            removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("Select a valid Employee")
    emps = Emp.objects.all()
    context = {
        'emps':emps
    }
    return render(request, 'remove_emp.html', context)



@csrf_exempt
def filter_emp(request):
    if request.method == 'POST':
        # Retrieve data from the form
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        role_id_str = request.POST.get('role', '')

        # Check if role_id_str is not empty before converting to int
        role_id = int(role_id_str) if role_id_str else None

        # Build a Q object for filtering
        filter_conditions = Q()

        if fname:
            filter_conditions &= Q(fname__icontains=fname)

        if lname:
            filter_conditions &= Q(lname__icontains=lname)

        if role_id is not None:
            filter_conditions &= Q(role_id=role_id)

        # Apply filtering
        emps = Emp.objects.filter(filter_conditions)

        context = {
            'emps': emps,
            'fname': fname,
            'lname': lname,
            'selected_role_id': role_id,
            'roles': Role.objects.all(),  # Include all roles for the dropdown
        }

        return render(request, 'all_emp.html', context)

    # If not a POST request, render the form
    return render(request, 'filter_emp.html', {'roles': Role.objects.all()})