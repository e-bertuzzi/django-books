from django.db import models

# Create your models here.
class Book(models.Model):
    titolo = models.CharField(max_length=100)
    genere = models.CharField(max_length=100)
    autore = models.CharField(max_length=100)
    pagine = models.IntegerField()

    def __str__(self) -> str:
        return self.titolo

class Reading(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    data_inizio = models.DateField()
    data_fine = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return self.book.__str__() + ", " + self.data_inizio.__str__()