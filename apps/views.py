from django.views.generic import TemplateView, ListView, DetailView

from apps.models import Category, Product


class HomePageView(ListView):
    model = Category
    queryset = Category.objects.all()
    context_object_name = 'categories'
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=object_list, **kwargs)
        data['products'] = Product.objects.all()
        return data


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ShopPageView(ListView):
    template_name = 'shop.html'
    queryset = Product.objects.all()
    context_object_name = 'products'


class ContactPageView(TemplateView):
    template_name = 'contact.html'


class SinglePageView(DetailView):
    model = Product
    context_object_name = 'product_single'
    template_name = 'shop-single.html'

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.object = None

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)
