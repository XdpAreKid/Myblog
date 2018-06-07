#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from django.forms import ModelForm
from django.forms import CharField
from django.forms import Textarea


class BlogForm(ModelForm):
    snippet = CharField(label='摘要',
                        widget=Textarea(attrs={'cols': 85, 'rows': 7}),
                        required=False)


    def save(self, commit=True):
        instance = super(BlogForm, self).save(commit=False)
        if instance.status == 'p' and instance.publish_time is None:
            instance.publish_time = datetime.datetime.now()
        if commit:
            instance.save()
        return instance
