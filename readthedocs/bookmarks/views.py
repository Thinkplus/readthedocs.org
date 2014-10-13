import simplejson

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import ListView

from bookmarks.models import Bookmark


class BookmarkListView(ListView):
    model = Bookmark

    def get(self, request):
        return HttpResponse()
