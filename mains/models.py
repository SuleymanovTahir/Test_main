from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.urls import reverse
from django.utils.text import slugify
from transliterate import translit
from random import *

#Создаю модельку OneToMany
class Product(models.Model):
    name=models.CharField(max_length=255)
    created=models.DateTimeField(auto_now_add=True)
    # publish=models.DateTimeField(default=(timezone.now()+timedelta(hours=6)))
    # updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering='-name',
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
    
class Icecream(models.Model):
    name=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    slug=models.SlugField(max_length=255,default='')
    price=models.IntegerField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Мороженное'
        verbose_name_plural='Мороженное'

    def get_absolute_url(self):
        return reverse('icecream_detail',args=[self.slug])


from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def seed_data(sender,**kwargs):
    
    icecream_db = [
            {
                'name': 'Золотое мороженое',
                'description': ('Шарики таитянского ванильного мороженого, шоколад '
                                '"Amedei Porcelana" и груда экзотических фруктов.'
                                'Всё это покрыто золотой фольгой, '
                                'её тоже полагается съесть.'),
        },
        {
        'name': 'Готическое мороженое',
        'description': ('Чёрное мороженое в чёрном вафельном рожке для '
                        'true black goths. Состав: сливочное мороженое, '
                        'миндаль, активированный уголь, чернота, мрак, отрицание.'),
        },
        {
        'name': 'Мороженое паста карбонара',
        'description': ('Порция макарон под тёмным соусом. '
                        'Паста — из ванильного мороженого, '
                        'продавленного через пресс с дырочками, '
                        'соус — ликёр с орехами. Buon appetito!'),
        },
        {
        'name': 'Фруктово-ягодное мороженое ГОСТ 119-52',
        'description': ('Сырьё: сливки, пахта, фрукты и ягоды в свежем виде, '
                        'яичный порошок из куриных яиц, патока карамельная. '
                        'Общее количество микробов в 1 мл мороженого: '
                        'не более 250 тыс.'),
        },
        {
        'name': 'Люминесцентное мороженое',
        'description': ('Сливочное мороженое с белками, активированными кальцием. '
                        'Светится, если облизнуть. '
                        'Можно подавать в тыкве на Хэллоуин '
                        'или кормить собаку Баскервилей.'),
        },
        {
        'name': 'Жареное мороженое',
        'description': ('Шарики мороженого обваливают яйце и в панировке, '
                        'сильно замораживают и быстро обжаривают '
                        'в растительном масле. Едят быстро.'),
        },
        {
        'name': 'Томатное мороженое',
        'description': ('Сливки, помидоры, чеснок, лавровый лист, '
                        'молотый перец. Если растает — '
                        'можно подавать к обеду как первое блюдо.'),
        },
    ]
    # for icecream_data in icecream_db:
    #     icecream,created=Icecream.objects.update_or_create(name=icecream_data['name'],defaults={'description':icecream_data['description']})
    #     # print(icecream,created)
    
    # for i in icecream_db: Tovar.objects.create(name=i['name'],description=i['description'],price=random.randint(700,1000))

icecream_db = [
    {
                'name': 'Золотое мороженое',
                'description': ('Шарики таитянского ванильного мороженого, шоколад '
                                '"Amedei Porcelana" и груда экзотических фруктов.'
                                'Всё это покрыто золотой фольгой, '
                                'её тоже полагается съесть.'),
    },
    {
        'name': 'Готическое мороженое',
        'description': ('Чёрное мороженое в чёрном вафельном рожке для '
                        'true black goths. Состав: сливочное мороженое, '
                        'миндаль, активированный уголь, чернота, мрак, отрицание.'),
    },
    {
        'name': 'Мороженое паста карбонара',
        'description': ('Порция макарон под тёмным соусом. '
                        'Паста — из ванильного мороженого, '
                        'продавленного через пресс с дырочками, '
                        'соус — ликёр с орехами. Buon appetito!'),
        },
        {
        'name': 'Фруктово-ягодное мороженое ГОСТ 119-52',
        'description': ('Сырьё: сливки, пахта, фрукты и ягоды в свежем виде, '
                        'яичный порошок из куриных яиц, патока карамельная. '
                        'Общее количество микробов в 1 мл мороженого: '
                        'не более 250 тыс.'),
        },
        {
        'name': 'Люминесцентное мороженое',
        'description': ('Сливочное мороженое с белками, активированными кальцием. '
                        'Светится, если облизнуть. '
                        'Можно подавать в тыкве на Хэллоуин '
                        'или кормить собаку Баскервилей.'),
        },
        {
        'name': 'Жареное мороженое',
        'description': ('Шарики мороженого обваливают яйце и в панировке, '
                        'сильно замораживают и быстро обжаривают '
                        'в растительном масле. Едят быстро.'),
        },
        {
        'name': 'Томатное мороженое',
        'description': ('Сливки, помидоры, чеснок, лавровый лист, '
                        'молотый перец. Если растает — '
                        'можно подавать к обеду как первое блюдо.'),
        },
    ]
