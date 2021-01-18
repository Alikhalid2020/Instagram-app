# Generated by Django 3.1 on 2021-01-17 13:46

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(default='default.png', upload_to='images/')),
                ('bio', models.TextField(blank=True, default='My Bio', max_length=350)),
                ('name', models.CharField(blank=True, max_length=150)),
                ('location', models.CharField(blank=True, max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250)),
                ('caption', models.CharField(blank=True, max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('likes', models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='instaClone.profile')),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='instaClone.profile')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='instaClone.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='instaClone.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='instaClone.profile')),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
    ]
