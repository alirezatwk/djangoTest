# Generated by Django 2.0.5 on 2019-01-29 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190129_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='photo',
            field=models.ImageField(default='', upload_to='media/photo'),
        ),
    ]