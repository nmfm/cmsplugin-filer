from django import forms
from cmsplugin_filer_html5video.models import Html5Video

class Html5VideoForm(forms.ModelForm):

    class Meta:
        model = Html5Video
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')
        