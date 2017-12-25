from django.shortcuts import render
from django.views.generic.base import TemplateView

class ContactView(TemplateView):
    template_name = "contact.html"

class HomeView(TemplateView):
    template_name = "home.html"

class AboutView(TemplateView):
    template_name = "about.html"


'''
class ContactView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, "contact.html", context)
'''