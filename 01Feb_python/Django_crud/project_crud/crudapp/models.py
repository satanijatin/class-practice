from django.db import models
import os

# Create your models here.

class Student(models.Model):
    uname=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    lang=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    img=models.ImageField(upload_to='images')
    
    
    # def delete(self, *args, **kwargs):
    #         # Delete the image file from the file system
    #     if self.img:
    #         if os.path.isfile(self.img.path):
    #             os.remove(self.img.path)
    #     super().delete(*args, **kwargs)

    # def delete_old_image(self):
    #     if self.pk:
    #         old_instance = Student.objects.get(pk=self.pk)
    #         if old_instance.img:
    #             if os.path.isfile(old_instance.img.path):
    #                 os.remove(old_instance.img.path)

    # def save(self, *args, **kwargs):
    #     self.delete_old_image()  # Delete old image before saving new one
    #     super().save(*args, **kwargs)

    # def save1(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
