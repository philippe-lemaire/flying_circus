# Generated by Django 4.0.4 on 2022-05-31 09:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('level', models.CharField(choices=[('1', 'Débutant'), ('2', 'Intermédiaire'), ('3', 'Avancé')], default='1', max_length=1)),
                ('order', models.IntegerField(default=1)),
                ('content', tinymce.models.HTMLField()),
                ('manager', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('order', models.IntegerField(default=1)),
                ('content', tinymce.models.HTMLField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.course')),
                ('manager', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]