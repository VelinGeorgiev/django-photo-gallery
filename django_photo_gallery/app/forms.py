#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from django import forms
from app.models import Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = []

    zip = forms.FileField(required=False)