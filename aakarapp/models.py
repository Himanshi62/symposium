from django.db import models

# Create your models here.


class Submission(models.Model):
    author = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    colgName = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    mobileNo = models.IntegerField(max_length=10)
    co1 = models.CharField(max_length=200)
    mail1 = models.CharField(max_length=100)
    co2 = models.CharField(max_length=200)
    mail2 = models.CharField(max_length=100)
    co3 = models.CharField(max_length=200)
    mail3 = models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    others = models.CharField(max_length=100)
    abstract = models.CharField(max_length=100)
    authentication = models.CharField(max_length=200)

    def _str_(self):
        return (
            f"{self.author} | "
            f"{self.email} "
        )
