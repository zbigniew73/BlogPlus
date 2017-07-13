# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render_to_response
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.views.generic import ListView
from blog.models import Post
from taggit.models import Tag
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django.utils.encoding import force_str
from django.utils.safestring import mark_safe
import markdown2

class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

class TagListView(TagMixin, ListView):
    template_name = 'blog/tag_post_list.html'

    model = Post
    context_object_name = 'post'

    def get_queryset(self, **kwargs):
        return Post.objects.filter(tags__slug=self.kwargs.get('slug'))    

class PostsFeed(Feed):
    title = "RSS BlogPlus 24z.biz"
    description = "Latest Posts of BlogPlus 24z.biz"
    link = '/'

    def items(self):
        return Post.objects.order_by('-pub_date')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        extras = ["fenced-code-blocks"]
        content = mark_safe(markdown2.markdown(force_str(item.text),
                                               extras = extras))
        return content

class AtomPostsFeed(PostsFeed):
    feed_type = Atom1Feed
    subtitle = PostsFeed.description

def getSearchResults(request):
    """
    Search for a post by title or text
    """
    # Get the query data
    query = request.GET.get('q', '')
    page = request.GET.get('page', 1)

    # Query the database
    results = Post.objects.filter(Q(text__icontains=query) | Q(title__icontains=query))

    # Add pagination
    pages = Paginator(results, 5)

    # Get specified page
    try:
        returned_page = pages.page(page)
    except EmptyPage:
        returned_page = pages.page(pages.num_pages)

    # Display the search results
    return render_to_response('blog/search_post_list.html',
                              {'page_obj': returned_page,
                               'object_list': returned_page.object_list,
                               'search': query})


