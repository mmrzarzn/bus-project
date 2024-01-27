from django import forms
from .models import TimeTable


class TimeTableModelForm(forms.ModelForm):
    class Meta:
        model = TimeTable
        fields = ['origin_station', 'destination_station', 'time_of_the_next_bus','start_time', 'time_at_the_terminal']
        widgets = {
            'origin_station': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            ' destination_station': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'time_of_the_next_bus': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'start_time': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'time_at_the_terminal': forms.TextInput(attrs={
                'class': 'form-control'
            })


        }

        # labels = {
        #     'full_name': 'full_name ',
        #     'email': 'email'
        # }
        #
        # error_messages = {
        #     'full_name': {
        #         'required': ' you should inter a name or last name'
        #     }
        # }