#!/usr/bin/python3
# -*- coding: utf-8 -*-


from django.db import models


# Create your models here.

class User(models.Model):

    gender = (
        ('male', '男'),
        ('female', '女'),
    )


    user_name = models.CharField(max_length=128, unique=True)  # 名字不能重复
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)                     # 邮箱不能重复
    sex = models.CharField(max_length=32, choices=gender, default='男')
    create_time = models.DateTimeField(auto_now_add=True)
    # 默认False表示未注册
    has_confirmed = models.BooleanField(default=False)

    # 显示对象信息
    def __str__(self):
        return self.user_name

    class Meta:
        ordering = ["-create_time"]   # 按创建时间反序排列，最近创建的先显示
        verbose_name = '用户'          # b别名
        verbose_name_plural = '用户'    # 模型的复数形式
        db_table = 'user'

# ConfirmString模型保存了用户和注册码之间的一对一关系
class ConfirmString(models.Model):
    # code 是哈希后的注册码
    code = models.CharField(max_length=256)
    user = models.OneToOneField('User')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.user_name + ": " + self.code

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "确认码"
        verbose_name_plural = "确认码"
        db_table = "confirm_string"