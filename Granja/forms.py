from django import forms
from Granja.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'

#class AlimentoForm(forms.ModelForm):
 #   class Meta:
  #      model=Alimento
   #     fields='__all__'

#class ContactoForm(forms.ModelForm):
 #   class Meta:
  #      model=Contacto
   #     fields='__all__'