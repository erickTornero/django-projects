"""
    Context processor makes public to all templates a context
"""

from social.models import Link

def ctx_dict(request):
    ctx     =   {}
    links   =   Link.objects.all()

    for link in links:
        ctx[link.key] = link.url

    return ctx