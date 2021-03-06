# -*- coding: utf-8 -*-

# Generated by Django 1.10.1 on 2018-05-11 02:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('body', models.TextField(verbose_name='正文')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('status', models.CharField(choices=[('d', 'part'), ('p', 'Published')], max_length=1, verbose_name='文章状态')),
                ('abstract', models.CharField(blank=True, help_text='可选项，若为空格则摘取正文钱54个字符', max_length=54, null=True, verbose_name='摘要')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='浏览量')),
                ('likes', models.PositiveIntegerField(default=0, verbose_name='点赞数')),
                ('topped', models.BooleanField(default=False, verbose_name='置顶')),
            ],
            options={
                'ordering': ['-last_modified_time'],
            },
        ),
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100, verbose_name='评论者名字')),
                ('body', models.TextField(verbose_name='评论内容')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='评论发表时间')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.Article', verbose_name='评论所属文章')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='类名')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='组名')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='姓名')),
                ('studentID', models.CharField(max_length=30, verbose_name='学号')),
                ('gender', models.CharField(max_length=10, verbose_name='性别')),
                ('birthday', models.DateField(auto_now_add=True, verbose_name='出生年月')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('password', models.CharField(max_length=10, verbose_name='密码')),
                ('profession', models.CharField(max_length=30, verbose_name='专业')),
                ('academy', models.CharField(max_length=30, verbose_name='学院')),
                ('permission', models.CharField(max_length=10, verbose_name='权限')),
                ('articles', models.ManyToManyField(to='lab.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Suggest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suggest', models.TextField(max_length=200, verbose_name='意见')),
                ('suggest_time', models.DateTimeField(auto_now_add=True, verbose_name='提出时间')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='标签名')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.Member'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lab.Category', verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, to='lab.Tag', verbose_name='标签集合'),
        ),
    ]
