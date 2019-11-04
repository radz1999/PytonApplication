from django.contrib import admin
from .models import Course,Faculty,Instructor,Student_Instructor_Course, Register, Student, Student_Slot, Slot_Course, Slot, Department

# Register your models here.

admin.site.register(Register)

admin.site.register(Faculty)

admin.site.register(Instructor)

admin.site.register(Student_Instructor_Course)

admin.site.register(Course)

admin.site.register(Student)

admin.site.register(Slot)

admin.site.register(Student_Slot)

admin.site.register(Slot_Course)

admin.site.register(Department)
