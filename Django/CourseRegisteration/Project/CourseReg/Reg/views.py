from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Student_Instructor_Course, Student, Student_Slot, Slot, Register
from .forms import CourseForm, RegisterForm, CourseSelectForm, CourseTakenForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
import array


# Create your views here.


def home(request):
    return render(request, 'users/login.html')


def course_list(request):
    courses = Course.objects.all()
    print(courses)
    return render(request, 'users/course_list.html', {'courses': courses})


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'users/course_detail.html', {'course': course})


def course_taken(request, userNo):
    course = Student_Instructor_Course.objects.filter(StudentNo=userNo)
    print(course)
    print(userNo)
    return render(request, 'users/courseTaken.html', {'course': course})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)  #I USED OWN LOGIN FORM THAN AuthenticationForm , because I Do Have another field that the USER TABLE DOES NOT HAVE.
        if form.is_valid():  # IF VALID , LETS LOG IN THE USER
            isStudent = Register.objects.filter(email=form['email'].value())#SELECT QUERY

            for a in isStudent:#GET ITEM FROM QUERY SET
                print(a.name)
                if (a.usertype == 1) and (a.password == form['password'].value()):
                    print(a.email)
                    studentInfo = Student.objects.filter(name=a.name)  # STUDENT TABLE ENTERED FIELDS ROW!
                    print(studentInfo)
                    for student in studentInfo:#THIS IS ALSO QUERYSET TO GET ITEM
                        print(student.studentNo)
                        # login(request, user)
                        if 'next' in request.POST:
                            return redirect(request.POST.get('next'),{'stuNo':student.studentNo})
                        else:
                            print(student.studentNo)
                            return redirect('course_list' )#..direct('course',{'userNo':student.studentNo}) SENDING USERNO
                else:
                    return render(request, 'users/login1.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login_view')


def register(request):#REGISTER FORM
    if request.method == "POST":
        form2 = RegisterForm(data=request.POST)
        if form2.is_valid():
            user2 = form2.save(commit=False)
            user2.author = request.user
            user2.save()
            return redirect('login_view')
    else:
        form2 = RegisterForm()
    return render(request, 'users/register.html', {'form': form2})


def course_new(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            courses = form.save(commit=False)
            courses.author = request.user
            courses.save()
            return redirect('course_detail', pk=courses.pk)
    else:
        form = CourseForm()
    return render(request, 'users/course_edit.html', {'form': form})


def curriculum(request, userNo): # ACTUALLY THIS GETS THE COURSES ONE BY ONE AND ADDS IT ON ARRAY.
    course = Student_Instructor_Course.objects.filter(StudentNo=userNo)
    print(course)
    finCourse = []
    for currCourse in course: #GETTING DATA FROM QUERY SET
        finCourse.append(Course.objects.filter(course_name=currCourse.CourseName))# THIS IS INSERTS COURSE object to array THAT THE TAKEN FROM STUDENT
        a = Course.objects.filter(course_name=currCourse.CourseName)

    return render(request, 'users/curriculum.html', {'finCourse': finCourse})


def courseSelect(request, userNo):
    if request.method == "POST":
        form = CourseSelectForm(request.POST)  # initial={"StudentNo": userNo}
        if form.is_valid():
            courses = form.save(commit=False)
            courses.author = request.user
            courses.save()
            return redirect('courseTaken', userNo=userNo)
    else:
        form = CourseSelectForm()
    return render(request, 'users/courseSelect.html', {'form': form})



def course_edit(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save(commit=False)
            course.author = request.user
            course.save()
            return redirect('course_edit', pk=course.pk)
    else:
        form = CourseForm(instance=course)
    return render(request, 'users/course_edit.html', {'form': form})
