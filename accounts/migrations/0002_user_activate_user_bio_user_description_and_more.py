# Generated by Django 5.0.6 on 2024-07-11 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="activate",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="user",
            name="bio",
            field=models.CharField(default="", max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="description",
            field=models.CharField(default="", max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="followers_count",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="user",
            name="followings_count",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="user",
            name="is_private",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="is_reported",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="posts_count",
            field=models.IntegerField(default=0),
        ),
    ]
