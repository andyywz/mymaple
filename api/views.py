from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Daily

def index(req):
    dailies = Daily.objects.all()

    # reset the daily if it is past reset
    for daily in dailies:
        if daily.is_stale():
            daily.reset()

    return render(req, 'dailies/index.html', { 'dailies': dailies })

# Temporary route to be deleted in the future
def show(req, daily_id):
    daily = get_object_or_404(Daily, pk=daily_id)

    if daily.is_stale():
        daily.reset()

    return render(req, 'dailies/show.html', { 'daily': daily })
