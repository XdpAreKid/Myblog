# Generated by Django 2.0 on 2018-05-27 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180527_0737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(blank=True, help_text='标签', to='blog.Tag', verbose_name='标签集合'),
        ),
    ]
