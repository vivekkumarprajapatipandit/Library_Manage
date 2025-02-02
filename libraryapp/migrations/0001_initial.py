# Generated by Django 5.0.3 on 2024-04-12 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookdata',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('BookName', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=500)),
                ('Author', models.CharField(max_length=50)),
                ('Price', models.IntegerField()),
                ('Category', models.CharField(max_length=50)),
                ('Pages', models.IntegerField()),
                ('Date_Of_Publish', models.DateField()),
                ('Photo', models.ImageField(blank=True, upload_to='profile_pics')),
            ],
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Username', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Password', models.CharField(max_length=20)),
                ('Password2', models.CharField(max_length=20)),
                ('DOB', models.DateField()),
                ('Gender', models.CharField(max_length=10)),
                ('Language', models.CharField(max_length=50)),
                ('Aadhar', models.IntegerField()),
                ('Profilepic', models.ImageField(blank=True, upload_to='profile_pics')),
            ],
        ),
    ]
