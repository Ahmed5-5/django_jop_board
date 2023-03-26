from django.db import models

# Create your models here.
def image_upload(instacne,filename):
    image_name, extention = filename.split(".")
    return "jops/ %s.%s"%(instacne.title,extention)
    
class jop(models.Model):
    '''
    Django_models_feilds:
        -Html_wedjet
        -validation
        -db size
    '''
    JOP_TITLE = (
        ("Full_time","Full_time"),("Part_time","Part_time")
    )

    title = models.CharField(max_length=50)
   # location = models.CharField(max_length=20)
    jop_title = models.CharField(max_length=20,choices=JOP_TITLE)
    description = models.TextField(max_length=500)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    image = models.ImageField(upload_to=image_upload)
    category = models.ForeignKey('Category' , on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length= 20)

    def __str__(self):
        return self.name