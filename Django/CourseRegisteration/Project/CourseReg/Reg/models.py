from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

DAYS_OF_WEEK = (
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
)
DEPT_NAME = (
    (0, 'Engineering'),
    (1, 'Architecture'),
    (2, 'Science'),
    (3, 'Economics'),
    (4, 'Social Science'),
)
SLOT_NAME = (
    (0, 'FREE_I'),(1, 'DEPT_I'), (2, 'COMP_I'),(3, 'MATH101'),(4, 'PHYS101'),
(5, 'FREE_II'),(6, 'FREE_III'),(7, 'COMP_II'),(8, 'DEPT_II'),(9, 'FREE_I'),(10, 'FREE_I'),(11, 'EE335'),(12, 'EE225'),
    (13, 'MATH102'),(14, 'PHYS102'),(14, 'MATH200'),
)
COURSE_HOUR = ((0, '9:00'),
               (1, '10:00'),
               (2, '11:00'),
               (3, '12:00'),
               (4, '13:00'),
               (5, '14:00'),
               (6, '15:00'),
               (7, '16:00'),
               )
SEMESTER = (
    (0, 'FALL'), (1, 'SPRING'),

)


class User(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="")
    email = models.EmailField(default='empty@mail.com')
    password = models.CharField(max_length=255, null=True)
    usertype = models.IntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(3)])


class Register(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    email = models.EmailField(default='empty@mail.com')
    password = models.CharField(max_length=255, null=True)
    usertype = models.IntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(3)], )


class Faculty(models.Model):
    facultyName = models.CharField(max_length=100, primary_key=True, default=None)


class Department(models.Model):
    class Meta:
        unique_together = (('depName', 'majority'),)

    depName = models.CharField(primary_key=True, max_length=100, blank=True)
    majority = models.ForeignKey(Faculty, on_delete=models.CASCADE)


class Course(models.Model):
    class Meta:
        unique_together = (('course_name', 'day', 'hour'),)

    course_name = models.CharField(max_length=200, primary_key=True)
    instructor = models.ForeignKey(Register, default='Emine Ekin', on_delete=models.CASCADE)
    syllabus = models.TextField(null=True)
    section = models.IntegerField(default=1)
    place = models.CharField(max_length=10, null=True, blank=True)
    day = models.IntegerField(choices=DAYS_OF_WEEK, default=None)
    hour = models.IntegerField(choices=COURSE_HOUR, default=None)
    to = models.IntegerField(choices=COURSE_HOUR, default=1)
    credit = models.IntegerField(null=True)
    depName = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name


class Student(models.Model):
    studentNo = models.CharField(max_length=100, primary_key=True, default=218)
    depName = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.OneToOneField(Register, on_delete=models.CASCADE)


class Instructor(models.Model):
    FacName = models.ForeignKey(Faculty, default=None, on_delete=models.CASCADE)
    name = models.OneToOneField(Register, primary_key=True, on_delete=models.CASCADE)


class Slot(models.Model):
    slotName = models.IntegerField(choices=SLOT_NAME,default=0,primary_key=True)


class Student_Instructor_Course(models.Model):
    class Meta:
        unique_together = (('StudentNo', 'CourseName', 'Semester','slotName',),)


    StudentNo = models.ForeignKey(Student, on_delete=models.CASCADE)
    CourseName = models.ForeignKey(Course, on_delete=models.CASCADE)
    Semester = models.IntegerField(choices=SEMESTER, default=0)
    slotName = models.IntegerField(choices=SLOT_NAME,default=0,primary_key=True)


class Student_Slot(models.Model):
    class Meta:
        unique_together = (('studentNo', 'slotName'),)

    studentNo = models.ForeignKey(Student, on_delete=models.CASCADE)
    slotName = models.ForeignKey(Slot, on_delete=models.CASCADE)
    canTake = models.IntegerField(default=0)


class Slot_Course(models.Model):
    class Meta:
        unique_together = (('major', 'slotName', 'courseName'),)

    # majority = models.CharField(max_length=100,primary_key=True, blank=True)
    major = models.ForeignKey(Department, on_delete=models.DO_NOTHING, default=None)
    slotName = models.ForeignKey(Slot, on_delete=models.DO_NOTHING)
    courseName = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
