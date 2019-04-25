from django.views.generic import TemplateView
import os
import markdown

class single_page(TemplateView):
    template_name = 'single.html'

    def get_context_data(self, **kwargs):
        category = kwargs.get('category')
        slug = kwargs.get('slug')

        content = open(os.path.dirname(__file__) + '/../data/%s/%s.md' % (category, slug)).read()

        md = markdown.Markdown(extensions = ['meta'])
        html = md.convert(content)

        title = md.Meta['title'][0]
        category = md.Meta['category'][0]

        ctx = super(single_page, self).get_context_data(**kwargs)
        ctx['content'] = html
        ctx['title'] = title
        ctx['category'] = category

        return ctx
