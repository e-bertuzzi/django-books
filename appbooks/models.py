from django.db import models

# Create your models here.
class Author(models.Model):
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    nazionalita = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nome + " " + self.cognome

class Book(models.Model):
    titolo = models.CharField(max_length=100)
    genere = models.CharField(max_length=100)
    autore = models.ManyToManyField(Author)
    pagine = models.IntegerField()

    def __str__(self) -> str:
        return self.titolo

class Reading(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    data_inizio = models.DateField()
    data_fine = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return self.book.__str__() + ", " + self.data_inizio.__str__()