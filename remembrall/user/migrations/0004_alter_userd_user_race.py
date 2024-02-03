# Generated by Django 3.2.23 on 2024-02-03 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_userd_user_race'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userd',
            name='user_race',
            field=models.CharField(choices=[('American Indian', 'American Indian'), ('Asian', 'Asian'), ('African American', 'African American'), ('Native Hawaiian', 'Native Hawaiian'), ('White', 'White')], max_length=32),
        ),
    ]