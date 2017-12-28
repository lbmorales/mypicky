from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView

from django.db.models import Q
from .models import RestaurantLocation

class RestaurantListView(ListView):
    def get_queryset(self):
        slug = self.kwargs.get("slug")

        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()
        
        return queryset

class RestaurantDetailView(DetailView):

    queryset = RestaurantLocation.objects.all()

    #capture custom id name from url
    def get_object(self, *args, **kwargs):
        rest_id = self.kwargs.get('rest_id')
        obj = get_object_or_404(RestaurantLocation, id=rest_id)
        return obj