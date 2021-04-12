# Generated by Django 3.2 on 2021-04-08 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='url')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True, verbose_name='url')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='url')),
                ('author', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ImageField(blank='true', upload_to='photos/%Y/%m/%d/')),
                ('views', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='blog.category')),
                ('tag', models.ManyToManyField(blank=True, related_name='posts', to='blog.Tag')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
