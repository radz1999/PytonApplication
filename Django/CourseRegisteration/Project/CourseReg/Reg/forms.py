from django import forms
from .models import Course, User, Register, Student_Instructor_Course,Slot_Course
from django.contrib.auth import get_user_model

widgets = {'days': forms.CheckboxSelectMultiple}


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('course_name', 'instructor', 'syllabus',
                  'section', 'hour', 'to',
                  'place', 'day', 'credit', 'depName',)


class CourseSelectForm(forms.ModelForm):
    class Meta:
        model = Student_Instructor_Course
        fields = ('StudentNo','CourseName', 'Semester','slotName',)


class CourseSelectFormAddition(forms.ModelForm):
    class Meta:
        model= Slot_Course
        exclude=('studentNo','slotName','canTake',)


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ('name', 'email', 'password',)


class CourseTakenForm(forms.ModelForm):
    class Meta:
        model = Student_Instructor_Course
        fields = ('CourseName', 'Semester',)


class LoginForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ('email', 'password',)

    UserModel = get_user_model()

    @property
    def emailgetter(self):
        return self.email
