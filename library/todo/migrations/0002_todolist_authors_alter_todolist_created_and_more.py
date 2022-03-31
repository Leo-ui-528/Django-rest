# Generated by Django 4.0.2 on 2022-03-28 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0003_book_biography_article'),
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='authors',
            field=models.ManyToManyField(to='authors.Author'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateField(default='2022-03-28'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='due_date',
            field=models.DateField(default='2022-03-28'),
        ),
    ]