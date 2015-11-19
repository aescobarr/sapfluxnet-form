from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from models import MetadataFormForm
from datetime import datetime

# Create your views here.
from django.shortcuts import render

def form(request):
	return render(request, 'sfnform/form.html')

def built_form(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
  	# create a form instance and populate it with data from the request:
		form = MetadataFormForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			metadata = form.save(commit=False)
			metadata.date_posted = datetime.now()
			metadata.save()
			# ...
			# redirect to a new URL:
			#return HttpResponseRedirect('/thanks')
			return HttpResponseRedirect(reverse('thanks'))
	# if a GET (or any other method) we'll create a blank form
	else:
		form = MetadataFormForm()
	return render(request, 'sfnform/form.html', {'form': form})