from django.shortcuts import render
from django.http import HttpResponse
# from reservation.models import
from django.db import connection
from django.db.models import F, Avg, Max, Min, Sum, FloatField
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from reservation import templates
from reservation.models import StudentDetails, BookDetails, ReservationData
import json

# Create your views here.
# Static files (files that do not change over time) - best practice to store each of these files in their own location
# Common Static files: css, js, images, audio, videos


@login_required
def aboutus(request):
    return render(request, 'reservation/about.html')

# Django query set


@login_required
def studentinfo(request):
    studentdata = StudentDetails.objects.all()  # SELECT * FROM RESERVATION_STUDENTDETAILS
    # the 10 represents the number of items(rows) shown on each page
    paginator = Paginator(studentdata, 10)
    page = request.GET.get('page')
    pagedata = paginator.get_page(page)
    context = {'data': pagedata}
    return render(request, 'reservation/studentinfo.html', context)


@login_required
def bookinfo(request):
    bookdata = BookDetails.objects.all().order_by(
        '-timescheckedout')  # SELECT * FROM RESERVATION_BOOKDETAILS
    # the 10 represents the number of items(rows) shown on each page
    paginator = Paginator(bookdata, 10)
    page = request.GET.get('page')
    pagedata = paginator.get_page(page)
    context = {'data': pagedata}
    return render(request, 'reservation/bookinfo.html', context)


@login_required
def bookreservation(request):
    studentdata = StudentDetails.objects.all()
    bookdata = BookDetails.objects.filter(currentlycheckedout="No")
    reservationdata = ReservationData.objects.all()
    context = {'student': studentdata, 'book': bookdata, 'reservation': reservationdata}
    return render(request, 'reservation/reservation.html', context)


def savereservation(request):
    if 'studentname' in request.GET and 'booktitle' in request.GET:
        full_name = request.GET.get('studentname')
        book = request.GET.get('booktitle')
        firstname, lastname = full_name.split(' ', 1) if ' ' in full_name else (full_name, '')

        reservationcount = ReservationData.objects.filter(
            studentfirstname=firstname, studentlastname=lastname).count()
        if reservationcount < 4:
            data = ReservationData(studentfirstname=firstname,
                                   studentlastname=lastname, booktitle=book)
            BookDetails.objects.filter(booktitle=book).update(
                timescheckedout=F('timescheckedout') + 1)
            BookDetails.objects.filter(booktitle=book).update(
                currentlycheckedout='Yes')
            data.save()
            return HttpResponse('Success')
        else:
            return HttpResponse('Error')
    return HttpResponse('Error')



@login_required
def chartdata(request):
    freshmandata = StudentDetails.objects.filter(studentyear='Freshman').count()
    sophomoredata = StudentDetails.objects.filter(studentyear='Sophomore').count()
    juniordata = StudentDetails.objects.filter(studentyear='Junior').count()
    seniordata = StudentDetails.objects.filter(studentyear='Senior').count()
    studentgpadata = StudentDetails.objects.aggregate(Avg('studentgpa'))
    studentgpadata = studentgpadata.get('studentgpa__avg')
    enrolleddata = freshmandata + sophomoredata + juniordata + seniordata

    #  StudentDetails.objects.values_list('studentgpa', flat=True)
    #  StudentDetails.objects.filter(aggregate(Avg('studentgpa')))
    # Entry.objects.filter(myfilter).values(columname).distinct()
    #  Book.objects.aggregate(Avg('price'))

    context = {'freshman': freshmandata, 'sophomore': sophomoredata,
               'junior': juniordata, 'senior': seniordata, 'studentgpa': studentgpadata, 'enrolled': enrolleddata}
    return render(request, 'reservation/dashboard.html', context)


# @login_required
# def chartdata2(request):
    #average_gpa = StudentDetails.objects.values_list(studentgpa, flat=True).order_by('studentgpa')
#studentgpadata = StudentDetails.objects.filter(studentyear='Senior').count()
    # StudentDetails.objects.all().aggregate(Avg('studentgpa'))
    # print(average_gpa)
    #context = {'studentgpa': studentgpadata}
    # return render(request, 'reservation/dashboard.html', context)


# studentenrollmentdata = StudentDetails.objects.filter(studentgpa=x).average()
    # studentgpa = StudentDetails.objects.filter(F(studentgpa)).Avg()
    # studentgpa = StudentDetails.objects.aggregate(Avg(F('studentgpa')))
    # gpadata = StudentDetails.objects.filter(studentgpa=3).count()
# Create a bar chart that displays student information
