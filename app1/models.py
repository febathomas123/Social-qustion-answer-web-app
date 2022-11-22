from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class user(models.Model):
    #id=models.AutoField(primary_key=True,)

    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    mobile = models.IntegerField()
    email = models.EmailField(max_length=30,unique=True)
    password = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)

    def __str__(self):
       return (self.f_name)
class expert_tbl(models.Model):
     # id=models.AutoField(primary_key=True,)

    f_name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=30)
    cat = models.CharField(max_length=30)
    interest = models.CharField(max_length=20)
    email = models.EmailField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    status = models.IntegerField(default=0)
    fileToUpload = models.FileField(upload_to='e_proof/%m',null=False)


    def __str__(self):
      return (self.f_name)


class question(models.Model):
    # id=models.AutoField(primary_key=True,)

    person = models.ForeignKey("user", on_delete=models.CASCADE)
    categry = models.ForeignKey("categry", on_delete=models.CASCADE)
    question = models.CharField(max_length=1000)
    rating=models.IntegerField(default=1)
    e_date= models.DateField(blank=True, null=True, verbose_name="ed")
    # amount=models.IntegerField()
    question_status=models.IntegerField(default=0)
    # pending_status=models.IntegerField(default=1)
    expert=models.CharField(max_length=50,null=True)

    def __str__(self):
        return (self.question)

class Pending(models.Model):
    expert = models.ForeignKey("expert_tbl",on_delete=models.CASCADE )
    question=models.ForeignKey("question", on_delete=models.CASCADE)
    status=models.IntegerField(default=1)

    def __str__(self):
        return (self.question.question)


class categry(models.Model):
    cat=models.CharField(max_length=30, unique=True,validators=[RegexValidator('^[A-Z ]*$',
                               'Only uppercase letters  allowed.')])

    def __str__(self):
        return (self.cat)


class subcategory(models.Model):
    categry=models.ForeignKey("categry",on_delete=models.CASCADE)
    subcat=models.CharField(max_length=30, unique=True)

    def __str__(self):
        return (self.subcat)

class tbl_answer(models.Model):
    pending=models.ForeignKey("Pending",on_delete=models.CASCADE)
    answer=models.CharField(max_length=1500, null=True)
    review = models.CharField(max_length=100, null=True)
    status=models.IntegerField(default=0)









