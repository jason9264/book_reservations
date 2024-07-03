from django.db import models

class StudentDetails(models.Model):
    studentid = models.IntegerField(primary_key=True)
    studentfirstname = models.CharField(max_length=500)
    studentlastname = models.CharField(max_length=500)
    studentmajor = models.CharField(max_length=500)
    studentyear = models.CharField(max_length=500)
    studentgpa = models.FloatField()


class BookDetails(models.Model):
    bookid = models.IntegerField(primary_key=True) 
    booktitle = models.CharField(max_length=500)
    authorname = models.CharField(max_length=500)
    currentlycheckedout = models.CharField(max_length=500)
    timescheckedout = models.IntegerField()

class ReservationData(models.Model):
    studentfirstname = models.CharField(max_length=100)
    studentlastname = models.CharField(max_length=100)
    booktitle = models.CharField(max_length=500)
