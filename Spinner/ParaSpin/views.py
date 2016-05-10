from django.shortcuts import render
from .forms import ParaForm, ParaForm4, ParaForm5
from django.http import HttpResponse
from .ParaSpinner import Hello, ThreePara, FourPara
from .wikiedit import Wiki
from .wikichecker import WikiCheck

# Create your views here.
def main(request):
	# On initiating the page, render the main template with the unfilled form from forms.py #
	if request.method == 'GET':
		return render(request, 'ParaSpin/main.html', {'ParaForm': ParaForm})
	if request.method == 'POST': 
		# Put the results of the form into a variable named form and validate the data #
		form = ParaForm(request.POST)
		form.is_valid()
		# clean the data in order to turn it into a string and put this into a dictionary 
		# that can then be passed to the para template. #
		p1 = form.cleaned_data['para1']
		p2 = form.cleaned_data['para2']
		p3 = form.cleaned_data['para3']
		form = {
			'para1' : p1,
			'para2' : p2,
			'para3' : p3,
		}
		spun = ThreePara(p1,p2,p3)
		return render(request, 'ParaSpin/results.html', {'spun': spun})
		
def para4(request):
	# On initiating the page, render the main template with the unfilled form from forms.py #
	if request.method == 'GET':
		return render(request, 'ParaSpin/Para4.html', {'ParaForm4': ParaForm4})
	if request.method == 'POST': 
		# Put the results of the form into a variable named form and validate the data #
		form = ParaForm4(request.POST)
		form.is_valid()
		# clean the data in order to turn it into a string and put this into a dictionary 
		# that can then be passed to the para template. #
		p1 = form.cleaned_data['para1']
		p2 = form.cleaned_data['para2']
		p3 = form.cleaned_data['para3']
		p4 = form.cleaned_data['para4']
		form = {
			'para1' : p1,
			'para2' : p2,
			'para3' : p3,
			'para4' : p4,
		}
		spun = FourPara(p1,p2,p3,p4)
		return render(request, 'ParaSpin/results.html', {'spun': spun})

def Wikipedia(request):
	if request.method == 'GET':
		edits = Wiki()
		return render(request, 'ParaSpin/wikipedia.html', {'edits': edits})

def WikiChecker(request):
	if request.method == 'GET':
		clients = WikiCheck()
		return render(request, 'ParaSpin/wikichecker.html', {'clients': clients})
