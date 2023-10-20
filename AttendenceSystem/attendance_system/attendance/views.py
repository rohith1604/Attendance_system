from django.shortcuts import render
from .models import Attendance

def attendance_list(request):
    attendance_records = Attendance.objects.all()
    return render(request, 'attendance/attendance_list.html', {'attendance_records': attendance_records})
