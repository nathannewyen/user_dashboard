# Generated by Django 2.2.4 on 2020-05-02 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_dashboard_app', '0003_user_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]