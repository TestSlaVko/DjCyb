# Generated by Django 4.0.4 on 2022-05-15 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='coursevi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('duration', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='podatoci',
            name='userCourses',
            field=models.TextField(default=''),
        ),
    ]
