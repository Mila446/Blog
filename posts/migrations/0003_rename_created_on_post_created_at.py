# Generated by Django 5.0.6 on 2024-06-14 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_delete_posts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_on',
            new_name='created_at',
        ),
    ]
