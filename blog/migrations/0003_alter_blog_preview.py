# Generated by Django 5.0.6 on 2024-06-22 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_blog_delete_blogarticle"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="preview",
            field=models.ImageField(
                blank=True,
                help_text="Добавьте изображение товара",
                null=True,
                upload_to="blog/preview",
                verbose_name="Изображение",
            ),
        ),
    ]
