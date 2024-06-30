from django.shortcuts import render, get_object_or_404
from .models import Student, SubjectMarks

def student_list_view(request):
    students = Student.objects.all()
    return render(request, 'student_app/student_list.html', {'students': students})

def student_detail_view(request, id):
    print(f"Student ID: {id}")  
    student = get_object_or_404(Student, pk=id)
    print(f"Student: {student}")  
    subject_marks = SubjectMarks.objects.filter(student=student)
    return render(request, 'student_app/student_detail.html', {'student': student, 'subject_marks': subject_marks})
