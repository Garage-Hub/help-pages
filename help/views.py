from django.views.generic import TemplateView
import os


class single_page(TemplateView):
    template_name = 'single.html'

    def get_context_data(self, **kwargs):
        category = kwargs.get('category')
        slug = kwargs.get('slug')

        content = open(os.path.dirname(__file__) + '/../data/%s/%s.md' % (category, slug)).read()

        ctx = super(single_page, self).get_context_data(**kwargs)
        ctx['content'] = content

        return ctx
