from django.db import models
from django.contrib.auth.models import User


class GeeksModel(models.Model):
    # fields of the model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now_add=True)

    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title


class Producer(models.Model):
    INTEGER_CHOICES = [tuple([x, x]) for x in range(1, 11)]

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    region = models.CharField(verbose_name="Νομός", max_length=50)
    prefecture = models.CharField(verbose_name="Περιφέρεια", max_length=50)

    location = models.CharField(verbose_name="Τοποθεσία", max_length=50)
    first_name = models.CharField("Όνομα", max_length=20)
    last_name = models.CharField("Επώνυμο", max_length=40)
    email = models.EmailField("Ηλεκτ. Ταχυδρομείο")
    greenhouse_number = models.IntegerField("Αριθμός Θερμοκηπίων")
    cultivation = models.CharField(verbose_name="Καλλιέργεια", max_length=50)
    description = models.TextField("Περιγραφή")

    def __str__(self):
        return str(self.pk)


class Sensor(models.Model):
    SENSOR_SELECTIONS = [
        ("Tin", "Inside Temperature"),
        ("Tout", "Outside Temperature"),
        ("Hin", "Inside Humidity"),
        ("Hout", "Outside Humidity"),
        ("T1", "Tank 1"),
        ("T2", "Tank 2"),
        ("SRin", "Solar Radiation in"),
        ("SRmid", "Solar Radiation middle"),
        ("SRot", "Solar Radiation out"),
    ]
    name = models.CharField(max_length=5, choices=SENSOR_SELECTIONS)

    def __str__(self):
        return str(self.name)


class Datas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gh_name = models.ForeignKey("Producer", on_delete=models.CASCADE)
    sensor = models.ForeignKey("Sensor", on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    value = models.FloatField()

    def __str__(self):
        return str(self.pk)
