8# Ex02 Django ORM Web Application
## Date: 24/04/2025

## AIM
To develop a Django application to store and retrieve data from Movies Database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

![web](https://github.com/user-attachments/assets/62153f4c-0903-4cad-846b-f4142b9757c1)



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```python
admin.py
from django.contrib import admin
from .models import Movie,MovieAdmin
admin.site.register(Movie,MovieAdmin)


models.py
from django.db import models
from django.contrib import admin
class Movie(models.Model):
    mid=models.IntegerField()
    mname=models.CharField(max_length=100)
    collection=models.IntegerField()
    year=models.IntegerField()
    rating=models.FloatField()

class MovieAdmin(admin.ModelAdmin):
    list_display=('mid','mname','collection','year','rating')

```




## OUTPUT


![alt text](nikshi.png)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
