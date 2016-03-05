from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib import messages
from .forms import PhotoForm


def index(request):

    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            #handle_uploaded_file(request.FILES['file'])
            messages.success(request, "Photo upload successful")
            return HttpResponseRedirect(reverse('photos:index'))
        else:
            messages.warning(request, "Photo upload failed")
    else:
        form = PhotoForm()
    return render(request, 'photos/index.html', {'form': form})
