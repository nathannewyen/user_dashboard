# Generated by Django 2.2.4 on 2020-05-02 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_dashboard_app', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
