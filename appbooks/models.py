from django.db import models
from django_countries.fields import CountryField

# Create your models here.
class Author(models.Model):
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    nazionalita = CountryField()

    def __str__(self) -> str:
        return self.nome + " " + self.cognome

class Quote(models.Model):
    frase = models.TextField()
    autore_frase = models.CharField(max_length=100)
    pagina = models.IntegerField()

    def __str__(self) -> str:
        new_string = self.autore_frase.replace(" ","_")
        return new_string + self.pagina.__str__()

class Book(models.Model):
    titolo = models.CharField(max_length=100)
    genere = models.CharField(max_length=100)
    autore = models.ManyToManyField(Author)
    quotes = models.ManyToManyField(Quote, blank=True)
    pagine = models.IntegerField()

    def __str__(self) -> str:
        return self.titolo

class Reading(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    data_inizio = models.DateField()
    data_fine = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return self.book.__str__() + ", " + self.data_inizio.__str__()