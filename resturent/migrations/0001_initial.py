# Generated by Django 5.1 on 2024-09-03 19:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=160)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=260)),
                ('description', models.TextField()),
                ('print', models.DecimalField(decimal_places=4, max_digits=5)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='resturent.category')),
            ],
        ),
        migrations.CreateModel(
            name='Modifier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=260)),
                ('aditional_price', models.DecimalField(decimal_places=4, default=0, max_digits=5)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='resturent.menuitem')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quintity', models.PositiveIntegerField(default=1)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('complate', 'complate')], max_length=20)),
                ('payment_method', models.CharField(choices=[('card', 'Card'), ('cash', 'Cash')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resturent.menuitem')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=4, max_digits=5)),
                ('payment_method', models.CharField(choices=[('card', 'Card'), ('cash', 'Cash')], max_length=20)),
                ('payment_date', models.DateField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='resturent.order')),
            ],
        ),
        migrations.CreateModel(
            name='Resturent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=255)),
                ('employees', models.ManyToManyField(related_name='employed_restaurants', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_restaurants', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='resturent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resturent.resturent'),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='resurent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resturent', to='resturent.resturent'),
        ),
        migrations.AddField(
            model_name='category',
            name='resturent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resturent.resturent'),
        ),
    ]
