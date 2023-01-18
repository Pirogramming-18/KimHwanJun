# Generated by Django 4.1.5 on 2023-01-18 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dev',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
                ('kind', models.CharField(max_length=12)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='IdeaStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=12)),
                ('photo', models.ImageField(blank=True, upload_to='posts/%Y%m%d')),
                ('content', models.TextField()),
                ('interest', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('devtool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.dev')),
                ('star', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.ideastar')),
            ],
        ),
    ]
