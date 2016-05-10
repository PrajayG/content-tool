from django import forms

class ParaForm(forms.Form):
	para1 = forms.CharField(widget=forms.Textarea)
	para2 = forms.CharField(widget=forms.Textarea)
	para3 = forms.CharField(widget=forms.Textarea)

class ParaForm4(forms.Form):
	para1 = forms.CharField(widget=forms.Textarea)
	para2 = forms.CharField(widget=forms.Textarea)
	para3 = forms.CharField(widget=forms.Textarea)
	para4 = forms.CharField(widget=forms.Textarea)

class ParaForm5(forms.Form):
	para1 = forms.CharField(widget=forms.Textarea)
	para2 = forms.CharField(widget=forms.Textarea)
	para3 = forms.CharField(widget=forms.Textarea)
	para4 = forms.CharField(widget=forms.Textarea)
	para5 = forms.CharField(widget=forms.Textarea)