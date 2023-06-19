from django.db import models

# Create your models here.
class DEPT(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    def __str__(self):
        return self.dname

class EMP(models.Model):
    empno=models.IntegerField()
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    hiredate=models.DateField()
    mgr=models.IntegerField()
    sal=models.IntegerField()
    comm=models.IntegerField()
    deptno=models.ForeignKey(DEPT,on_delete=models.CASCADE)

    def __str__(self):
        return self.ename


    
