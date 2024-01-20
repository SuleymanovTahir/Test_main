from django.db import models

#Создаю модельку OneToMany
class Product(models.Model):
    name=models.CharField(max_length=255)

    class Meta:
        verbose_name='Продукт'
        verbose_name_plural='Продукты'

    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=255)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'
    
    def __str__(self):
        return self.name

#создаю модельку OneToOne
class User(models.Model):
    name=models.CharField(max_length=255)

    class Meta:
        verbose_name='Пользователь'
        verbose_name_plural='Пользователи'

    def __str__(self):
        return self.name

class Profile(models.Model):
    name=models.CharField(max_length=255)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name='Профиль'
        verbose_name_plural='Профили'

    def __str__(self):
        return self.name


#ManyToMany
class Students(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()

    class Meta:
        verbose_name='Студент'
        verbose_name_plural='Студенты'

    def __str__(self):
        return self.name

class Courses(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    students=models.ManyToManyField(Students,related_name='courses')

    class Meta:
        verbose_name='Курс'
        verbose_name_plural='Курсы'

    def __str__(self):
        return self.title

