from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from events.models import Event

def home(request):
	return render(request, 'events_list.html')


class EventsListView(ListView):
	template_name = "events_list.html"
	model = Event
	queryset = Event.objects.all()


class EventDetailView(DetailView):
    model = Event
    template_name = "event_detail.html"