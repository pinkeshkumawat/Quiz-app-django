# Generated by Django 4.0.6 on 2022-07-15 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0002_alter_quesmodel_op1_alter_quesmodel_op2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quesmodel',
            name='op1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='quesmodel',
            name='op2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='quesmodel',
            name='op3',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='quesmodel',
            name='op4',
            field=models.CharField(max_length=200, null=True),
        ),
    ]