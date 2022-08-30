from django.shortcuts import render
from django.views.generic import ListView
from .forms import GeeksForm
from .models import HomeSlider, Banner, CarModel, Social, HomeOnecolumn, Callus, HomeTwocolumns, HomeThreecolumns, Category, Product
# Create your views here.

class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        context = GeeksForm()
        banner = Banner.objects.all()
        onecolumn = HomeOnecolumn.objects.all()
        twocolumns = HomeTwocolumns.objects.all()
        threecolumns = HomeThreecolumns.objects.all()
        social = Social.objects.all()
        slider = HomeSlider.objects.all()
        return render(request, self.template_name, {'slider':slider, "banner":banner, "context":context, "social":social, "onecolumn":onecolumn, "twocolumns":twocolumns, "threecolumns":threecolumns})

class AboutListView(ListView):
    template_name = 'about.html'

    def get(self, request):
        banner = Banner.objects.all()
        slider = HomeSlider.objects.all()
        return render(request, self.template_name, {'slider':slider, "banner":banner})

class ContactListView(ListView):
    template_name = 'contact.html'

    def get(self, request):
        banner = Banner.objects.all()
        slider = HomeSlider.objects.all()
        return render(request, self.template_name, {'slider':slider, "banner":banner})


class GalleryListView(ListView):
    template_name = 'gallery.html'

    def get(self, request):
        banner = Banner.objects.all()
        slider = HomeSlider.objects.all()
        return render(request, self.template_name, {'slider':slider, "banner":banner})


class ProductsListView(ListView):
    template_name = 'products.html'

    def get(self, request):
        banner = Banner.objects.all()
        callus = Callus.objects.all()
        slider = HomeSlider.objects.all()
        products = Category.objects.all()
        carmodel = CarModel.objects.all()
        return render(request, self.template_name, {"carmodel":carmodel, 'slider':slider, "banner":banner, "products":products, "callus":callus })


class ServicesListView(ListView):
    template_name = 'services.html'

    def get(self, request):
        banner = Banner.objects.all()
        slider = HomeSlider.objects.all()
        return render(request, self.template_name, {'slider':slider, "banner":banner})