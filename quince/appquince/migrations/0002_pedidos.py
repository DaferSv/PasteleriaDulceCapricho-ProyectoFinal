# Generated by Django 4.1.3 on 2022-11-10 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appquince', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=200)),
                ('pedido_recibido', models.CharField(max_length=200)),
                ('fecha', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('hora', models.CharField(max_length=200)),
                ('sabor', models.CharField(max_length=200)),
                ('porciones', models.CharField(max_length=200)),
                ('abono', models.CharField(max_length=200)),
                ('precio', models.CharField(max_length=200)),
                ('imagen', models.ImageField(blank=True, upload_to='media')),
            ],
        ),
    ]
