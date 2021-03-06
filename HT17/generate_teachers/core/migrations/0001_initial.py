# Generated by Django 3.1.2 on 2020-10-17 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID'
                                        )),
                ('title', models.CharField(max_length=255,
                                           verbose_name='Название'
                                           )),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID'
                                        )),
                ('firstname', models.CharField(default='',
                                               max_length=255,
                                               verbose_name='Имя'
                                               )),
                ('lastname', models.CharField(default='',
                                              max_length=255,
                                              verbose_name='Фамилия'
                                              )),
                ('age', models.IntegerField(default=1,
                                            verbose_name='Возраст'
                                            )),
            ],
            options={
                'verbose_name': 'Учитель',
                'verbose_name_plural': 'Учителя',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID'
                                        )),
                ('firstname', models.CharField(default='',
                                               max_length=255,
                                               verbose_name='Имя'
                                               )),
                ('lastname', models.CharField(default='',
                                              max_length=255,
                                              verbose_name='Фамилия'
                                              )),
                ('age', models.IntegerField(default=1,
                                            verbose_name='Возраст'
                                            )),
                ('group', models.ForeignKey(
                    on_delete=models.SET('Without Group'),
                    to='core.group',
                    verbose_name='Группа'
                )),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='teacher',
            field=models.ForeignKey(on_delete=models.SET('No Teacher'),
                                    to='core.teacher',
                                    verbose_name='Учитель'
                                    ),
        ),
    ]
