# Generated by Django 4.1.1 on 2023-01-18 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductMainModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=20)),
                ('Description', models.TextField(max_length=150)),
                ('price', models.IntegerField(unique=True)),
                ('Size', models.IntegerField(choices=[('10', '10'), ('20', '20'), ('30', '30')], default='10')),
                ('Quality', models.CharField(choices=[('high', 'high'), ('Low', 'Low'), ('medium', 'medium')], default='Low', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='productImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='FirstApp.productmainmodel')),
            ],
        ),
        migrations.CreateModel(
            name='ProductcolorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Colour', models.CharField(choices=[('red', 'red'), ('blue', 'blue'), ('green', 'green'), ('black', 'black')], default='red', max_length=50)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='FirstApp.productmainmodel')),
            ],
        ),
    ]
