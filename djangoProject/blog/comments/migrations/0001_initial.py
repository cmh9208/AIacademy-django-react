# Generated by Django 4.1.3 on 2022-12-31 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("posts", "0001_initial"),
        ("buser", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogComment",
            fields=[
                ("comment_id", models.AutoField(primary_key=True, serialize=False)),
                ("content", models.CharField(max_length=1000)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("parent_id", models.TextField(null=True)),
                (
                    "blog_post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="posts.blogpost"
                    ),
                ),
                (
                    "blog_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buser.blogbuser",
                    ),
                ),
            ],
            options={
                "db_table": "blog_comments",
            },
        ),
    ]
