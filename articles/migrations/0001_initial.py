# Generated by Django 4.2.4 on 2023-08-29 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('uid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=120)),
                ('type', models.CharField(choices=[('BOOK', 'BOOK'), ('ARTICLE', 'ARTICLE')], default='BOOK', max_length=10)),
                ('category', models.CharField(choices=[('UNKNOWN', 'UNKNOWN'), ('MATH', 'MATH'), ('PHYSICS', 'PHYSICS'), ('CALCULUS', 'CALCULUS'), ('PROGRAMMING', 'PROGRAMMING'), ('LITERATURE', 'LITERATURE'), ('ECONOMY', 'ECONOMY'), ('GEOMETRY', 'GEOMETRY'), ('CHEMISTRY', 'CHEMISTRY')], default='UNKNOWN', max_length=20)),
                ('author', models.CharField(max_length=60)),
            ],
        ),
    ]
