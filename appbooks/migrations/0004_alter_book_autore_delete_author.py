# Generated by Django 4.2.5 on 2023-09-07 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appbooks', '0003_author_alter_book_autore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='autore',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
