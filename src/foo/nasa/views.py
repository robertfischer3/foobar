from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .forms import PhotoOfDayForm
from bootstrap_datepicker_plus import DateTimePickerInput
from . api import API
from datetime import datetime
from foo import settings
from . import models

def homepage(request):
    """Render the homepage.
    """
    template = 'homepage.html'
    ctx = {}

    return render(request, template, ctx)


# TODO: Write a view that renders an APOD template, displaying the image in the HTML page.

def picture_of_day(request):
    template = 'pod.html'
    api =  API(settings.NASA_API_SECRET)
    data_json = api.get_apod(date=datetime.today().strftime('%Y-%m-%d'))

    url = determine_url(data_json)
    title = data_json['title']
    explanation = data_json['explanation']
    ctx = {'url':url, 'title': title, 'explanation': explanation}

    return render(request, template, ctx)

def photo_form(request):
    if request.method == 'POST':
        form = PhotoOfDayForm(request.POST)
        # It is possible to pull the information into the
        # the form using the date and JavaScript to capture
        # the date change. However time did not allow for this
        if request.POST.get('getdate01'):
            # By grabbing the button getdate01 submit we can pull forward
            # another record from the service
            photodate = request.POST['photodate']
            return render(request, 'form.html', {'form': form})

        if request.POST.get('savedate01'):
            title = request.POST['title']
            # A ModelForm should have been used if more time was available
            if form.is_valid():

                photo = models.PhotoOfDay(photodate = request.POST['photodate'],
                                          title=request.POST['title'],
                                          url=request.POST['url'],
                                          hdurl=request.POST['hdurl'],
                                          copyright=request.POST['copyright'],
                                          explanation=request.POST['explanation'],
                                          media_type=request.POST['media_type'],
                                          service_version=request.POST['service_version'])

                photo.save()

    api = API(settings.NASA_API_SECRET)
    data_json = api.get_apod(date=datetime.today().strftime('%Y-%m-%d'))

    form = PhotoOfDayForm(initial={
            'photodate': data_json['date'],
            'title': data_json['title'],
            'url':data_json['url'],
            'hdurl': data_json['hdurl'],
            'copyright': data_json['copyright'],
            'explanation': data_json['explanation'],
            'media_type': data_json['media_type'],
            'service_version': data_json['service_version'],
            })
    # form = PhotoOfDayForm(initial={'title': 'my happy value'})
    return render(request, 'form.html', {'form':form})

def photo_list(request):
    # pods = models.PhotoOfDay.objects.all()
    return render(request, 'pod_list.html', {"pods":pods})

class PhotoOfDayListView(ListView):
    template_name = 'pod_list.html'
    model = models.PhotoOfDay
    context_object_name = 'pods'



def determine_url(data_json):
    # Not every day is the picture made available in HD
    # Need to test what is avaible
    if 'hdurl' in data_json:
        url = data_json['hdurl']
    elif 'url' in data_json:
        url = data_json['url']
    else:
        url = settings.FILE_NOT_FOUND
    if 'video' in data_json['media_type']:
        url = settings.FILE_NOT_FOUND
    return url
