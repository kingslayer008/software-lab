# Generated by Django 3.1.7 on 2021-05-02 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('e_app', '0003_coursetype_cousename'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CouseName',
            new_name='CourseName',
        ),
        migrations.CreateModel(
            name='CourseDes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.IntegerField(null=True)),
                ('course_des', models.CharField(max_length=200)),
                ('course_year', models.DateField(null=True)),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='e_app.coursename')),
                ('course_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='e_app.coursetype')),
            ],
        ),
    ]