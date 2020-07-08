# Generated by Django 3.0.8 on 2020-07-07 08:03

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
            name='UserSpecies',
            fields=[
                ('id', models.SmallIntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('species', models.CharField(blank=True, max_length=5, null=True, verbose_name='種族')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=20, verbose_name='お名前')),
                ('age', models.SmallIntegerField(null=True, verbose_name='年齢')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('species', models.ForeignKey(on_delete=models.SET(0), related_name='p_species', to='login_test_app.UserSpecies', verbose_name='種族')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='p_names', to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
        ),
    ]
