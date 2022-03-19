# -*- coding: utf-8 -*-
import os
from django.db import models
from datetime import datetime
from users.models import UserProfile
from django.conf import settings


class Category(models.Model):
    title = models.CharField(max_length=32, verbose_name='分类')

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='名称')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


def upload_to(instance, filename):
    today = datetime.today()
    dir_path = f'video/{today.year}/{today.month}/{today.day}/{instance.title}/{filename}'
    return dir_path


class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name='电影标题')
    # download_url = models.CharField(max_length=300, verbose_name='下载地址', default='')
    # movie_file = models.FileField(max_length=200, upload_to='video/videos/%Y/%m', default='videos/default.mp4',
    #                               verbose_name='视频文件')
    movie_file = models.FileField(max_length=200, upload_to=upload_to, default='videos/default.mp4',
                                  verbose_name='视频文件')
    info = models.TextField(verbose_name="电影简介", default='...')
    logo = models.ImageField(upload_to='image/banner/%Y/%m', max_length=100, verbose_name='封面')
    star = models.IntegerField(verbose_name='星级', blank=True,default=3)
    play_nums = models.IntegerField(verbose_name='播放量', blank=True,default=0)
    comment_nums = models.IntegerField(verbose_name='评论数', blank=True,default=0)
    area = models.CharField(max_length=200, verbose_name='上映地区')
    release_time = models.DateField(default=datetime.now, verbose_name='上映时间')
    length = models.CharField(max_length=200, verbose_name='时长')
    tag = models.ManyToManyField(Tag, default='', verbose_name='标签')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def release_year(self):
        return self.release_time.year

    class Meta:
        verbose_name = '电影信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class Preview(models.Model):
    title = models.CharField(max_length=200, verbose_name='电影标题')
    logo = models.ImageField(upload_to='banner/%Y/%m', default='image/default.png', max_length=100, verbose_name='封面')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '上映预告'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField(verbose_name="评论详情", default='')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='电影')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='用户')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户评论'
        verbose_name_plural = verbose_name


class MovieCol(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='电影')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='用户')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name
