# Generated by Django 4.2.6 on 2023-11-08 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(blank='false', to='articles.category'),
        ),
    ]