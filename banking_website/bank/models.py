from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE


# Create your models here.
class District(models.Model):
    district=models.CharField(max_length=250,unique=True)

    def __str__(self):
        return self.district

class Branch(models.Model):
    district_id = models.ForeignKey(District, on_delete=models.CASCADE)
    branch=models.CharField(max_length=250)

    def __str__(self):
        return self.branch




    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['branch'].queryset = branch.objects.none()

# class bankform(models.Model):
#     name = models.CharField(max_length=250)
#     dob = models.DateField(max_length=8)
#     gender = models.IntegerField(choices=GENDER_CHOICES)
#     phone_number = models.CharField(max_length=12)
#     email = models.CharField(max_length=250)
#     address = models.TextField()
#     district = models.ForeignKey(district, on_delete=models.CASCADE)
#     branch = models.ForeignKey(branch, on_delete=models.CASCADE)





