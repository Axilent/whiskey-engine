"""
Saspire integration.
"""

from django.conf import settings
from whiskeyengine.models import Whiskey
from sharrock.client import HttpClient
  
c = HttpClient(settings.SAASPIRE_API,'saaspire.content','0.1dev',auth_user=settings.SAASPIRE_API_KEY)

def profile(request):
    """
    Attempts to retrieve the profile from the request.
    """
    return request.COOKIES.get('saaspire.profile',None)

def load_whiskies(policy):
    """
    Loads the whiskies from the policy result.
    """
    loaded_whiskey = []
    results = policy['default'] # only using default group
    for result in results:
        content_key = result['content']['key']
        loaded_whiskey.append(Whiskey.objects.get(saaspire_key=content_key))
    return loaded_whiskey

def get_related_whiskies(basekey,profile=None):
    """
    Gets whiskies related to the basekey whiskey.
    """
    results = c.policycontent(content_policy_slug='related-whiskey',basekey=basekey,profile=profile)
    return load_whiskies(results)

def get_recommended_whiskies(profile):
    """
    Gets whiskies recommended for the specified profile.
    """
    results = c.policycontent(content_policy_slug='personalized-whiskey',basekey=None,profile=profile)
    return load_whiskies(results)
