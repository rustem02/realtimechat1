# Generated by Django 4.0.4 on 2022-05-08 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public_chat', '0002_alter_publicchatroom_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicchatroom',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='publicroomchatmessage',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]