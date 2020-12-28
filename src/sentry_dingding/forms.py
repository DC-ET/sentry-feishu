# coding: utf-8

from django import forms

class FeiShuOptionsForm(forms.Form):
    url = forms.CharField(
        max_length=255,
        help_text='FeiShu robot Webhook'
    )
