from django.db import models


class Tourist(models.Model):
    email = models.CharField(max_length=100)
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.email


class Pereval(models.Model):
    NEW = 'NW'
    PENDING = 'PN'
    ACCEPTED = 'AC'
    REJECTED = 'RJ'
    STATUS_CHOICES = (
        ('NW', 'new'),
        ('PN', 'pending'),
        ('AC', 'accepted'),
        ('RJ', 'rejected'),
    )

    beauty_title = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    other_titles = models.CharField(max_length=128)
    connect = models.CharField(max_length=128)
    add_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Tourist, on_delete=models.CASCADE)
    coords = models.OneToOneField('Coordinates', on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=NEW)
    level = models.ForeignKey('Level', on_delete=models.CASCADE)


class Coordinates(models.Model):
    latitude = models.DecimalField(decimal_places=8, max_digits=10)
    longitude = models.DecimalField(decimal_places=8, max_digits=10)
    elevation = models.IntegerField(default=0)


class Level(models.Model):
    LVLA_1 = '1A'
    LVLA_2 = '2A'
    LVLA_3 = '3A'
    LVLB_1 = '1Б'
    LVLB_2 = '2Б'
    LVLB_3 = '3Б'
    LEVEL_CHOICES = (
        ('1A', '1A'),
        ('2A', '2A'),
        ('3A', '3A'),
        ('1Б', '1Б'),
        ('2Б', '2Б'),
        ('3Б', '3Б'),
    )

    winter = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=LVLA_1)
    spring = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=LVLA_1)
    summer = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=LVLA_1)
    autumn = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=LVLA_1)


class PerevalImage(models.Model):
    images = models.ImageField(upload_to='static/images')
    title = models.CharField(max_length=128)
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE, related_name='images') # id перевала

    def __str__(self):
        return self.title


# Create your models here.
