from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from forms import MetadataFormForm, DataUploadForm
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
from django.shortcuts import render


def form(request):
    return render(request, 'sfnform/form.html')


def built_form(request):
    # entirely bypass form page
    return render(request, 'sfnform/form_closed.html')
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
            # return HttpResponseRedirect('/thanks')
            return HttpResponseRedirect(reverse('thanks'))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = MetadataFormForm()
    return render(request, 'sfnform/form.html', {'form': form})


def upload_form(request):
    if request.method == 'POST':
        form = DataUploadForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            metadata = form.save()
            message_body = "Dear contributor,\n\nYour data files have been correctly stored in our server. We will get back to you\nto inform you about the progress in dataprocessing.\nThanks for contributing to SAPFLUXNET,\n\nthe SAPFLUXNET Team.\n"
            if settings.BCC_EMAIL and settings.BCC_EMAIL!='':
                send_mail("[SAPFLUXNET] - Thanks for contributing!", message_body, settings.DEFAULT_FROM_EMAIL,[metadata.email,settings.BCC_EMAIL], fail_silently=False)
            else:
                send_mail("[SAPFLUXNET] - Thanks for contributing!", message_body, settings.DEFAULT_FROM_EMAIL,[metadata.email], fail_silently=False)
            return HttpResponseRedirect(reverse('thanks'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DataUploadForm()
    return render(request, 'sfnform/duform.html', {'form': form})
