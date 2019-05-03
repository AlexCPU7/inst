# Generated by Django 2.1.4 on 2019-05-03 13:14

import core.models.user
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Электронная почта')),
                ('date_birth', models.DateField(verbose_name='Дата рождения')),
                ('phone', models.CharField(blank=True, max_length=12, null=True, verbose_name='Номер телефона')),
                ('gender', models.CharField(blank=True, choices=[('man', 'Мужчина'), ('women', 'Женщина')], max_length=5, null=True, verbose_name='Пол')),
                ('is_staff', models.BooleanField(default=False, help_text='Указывает, может ли пользователь войти на этот сайт администратора.', verbose_name='Доступ к админке')),
                ('is_active', models.BooleanField(default=True, help_text='Активный пользователь', verbose_name='Активность')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата присоединения')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            managers=[
                ('objects', core.models.user.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, verbose_name='Вопрос')),
                ('answer', models.TextField(max_length=3000, verbose_name='Ответ')),
                ('active', models.BooleanField(default=1, verbose_name='Активность')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'Вопрос-ответ',
                'verbose_name_plural': 'Вопрос-ответ',
            },
        ),
        migrations.CreateModel(
            name='QuestionGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('active', models.BooleanField(default=1, verbose_name='Активность')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'Группа вопросов',
                'verbose_name_plural': 'Группы вопросов',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.QuestionGroup', verbose_name='Группа'),
        ),
    ]