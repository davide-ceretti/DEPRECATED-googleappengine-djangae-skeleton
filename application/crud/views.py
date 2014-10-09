from django.views import generic
from django.core.urlresolvers import reverse

from application.crud.models import Item


class ItemCreateView(generic.CreateView):
    model = Item
    template_name = 'form.html'

    def get_success_url(self):
        return reverse('index')

    def get_context_data(self, *args, **kwargs):
        data = super(ItemCreateView, self).get_context_data(*args, **kwargs)
        data['item_list'] = Item.objects.all()
        return data
