'''Lucentbeing.com specific views.'''

from django.shortcuts import render_to_response
from django.template import RequestContext

from djournal.models import Entry

def index(request, template='core/index.html'):
    '''Set up a general context for the front-page.'''

    entry = Entry.public.latest()

    context = {
        'entry': entry,
    }

    return render_to_response(
        template,
        context,
        context_instance=RequestContext(request),
    )
