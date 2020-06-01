# -*- coding: utf-8 -*-
"""
@author: jw
@contact: jiangwen.zhang@xfxb.net
@time: 2020/5/29 17:58
@file: forms.py
"""
from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Username", 'autofocus': ''}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': "Password"}))
