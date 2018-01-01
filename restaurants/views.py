from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from django.db.models import Q
from .models import RestaurantLocation
from .forms import RestaurantLocationCreateForm

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

class RestaurantCreateView(CreateView):
    form_class = RestaurantLocationCreateForm
    template_name = 'restaurants/form.html'
    success_url = '/restaurants/'
    
    '''
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        print(self.request.POST.get('name'))
        print(form.cleaned_data)
        return super(RestaurantCreateView, self).form_valid(form)
    '''