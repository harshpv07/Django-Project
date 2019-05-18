from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.views import View
from django.views.generic import TemplateView 
# Dont Repeat Yourself = DRY

from .forms import ContactForm
from blog.models import BlogPost


def home_page(request):
    my_title = "Hello there...."
    qs = BlogPost.objects.all()[:5]
    lis = [1,2,4,5,6]
    context = {"title": "Welcome to Try Django", 'blog_list': qs , 'lis':lis}
    return render(request, "home.html", context)


def about_page(request):
    return render(request, "about.html", {"title": "About"})



def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        "title": "Contact us", 
        "form": form
    }
    return render(request, "form.html", context)



def example_page(request):
    context         =  {"title": "Example"}
    template_name   = "hello_world.html" 
    template_obj    = get_template(template_name)
    rendered_item   = template_obj.render(context)
    return HttpResponse(rendered_item)

class ContactView(TemplateView):
    template_name = "about.html"
    def get_context_data(self, **kwargs):
        context = super(ContactView,self).get_context_data(**kwargs)
        print(context)
        return context
    
