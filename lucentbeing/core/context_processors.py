from django.conf import settings

def static_url(request) :
    '''Make STATIC_URL available to templates.'''

    return dict(
        'STATIC_URL': settings.STATIC_URL
    )
