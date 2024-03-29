# Generated by Django 4.2.3 on 2023-09-07 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('images', '0004_alter_image_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=1)),
                ('desc', models.TextField(blank=True)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='images.image')),
            ],
        ),
    ]
