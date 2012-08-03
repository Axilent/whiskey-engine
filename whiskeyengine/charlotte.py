"""
RQuery Access to SaaSpire Charlotte.
"""
from saaspire.client.rquery import RQuery
from saaspire.client.triggers import Triggers
from django.conf import settings
from whiskeyengine.models import Whiskey


def _rq():
    """
    Gets the rquery client.
    """
    if hasattr(settings,'CHARLOTTE_DOMAIN'):
        return RQuery(settings.CHARLOTTE_ACCOUNT,settings.CHARLOTTE_API_TOKEN,settings.CHARLOTTE_DOMAIN)
    else:
        return RQuery(settings.CHARLOTTE_ACCOUNT,settings.CHARLOTTE_API_TOKEN)

def _triggers():
    """
    Gets the triggers client.
    """
    if hasattr(settings,'CHARLOTTE_DOMAIN'):
        return Triggers(settings.CHARLOTTE_ACCOUNT,settings.CHARLOTTE_API_TOKEN,settings.CHARLOTTE_DOMAIN)
    else:
        return Triggers(settings.CHARLOTTE_ACCOUNT,settings.CHARLOTTE_API_TOKEN)

def profile(request):
    """
    Gets the saaspire profile for the request.
    """
    if not request.user.is_anonymous():
        drinker = request.user.get_profile()
        if not drinker.saaspire_profile:
            t = _triggers()
            drinker.saaspire_profile = t.profile()
            drinker.save()
        return drinker.saaspire_profile
    else:
        return None

def new_profile():
    """
    Gets a new profile.
    """
    t = _triggers()
    return t.profile()

def recommended_whiskey(profile, base_whiskey, limit=3):
    """
    Gets a recommendation of 3 whiskeys based on the current user.
    """
    rq = _rq()
    results = rq.content().basekey({'id':base_whiskey.pk,'name':base_whiskey.name,'content_type':'whiskey'}).filters({'herbs_spice':'$this',
                                                                                                                      'flowers':'$this',
                                                                                                                      'fruit':'$this',
                                                                                                                      'candy':'$this',
                                                                                                                      'wood':'$this',
                                                                                                                      'length_of_finish':'$this',
                                                                                                                      'complexity':'$this',
                                                                                                                      'smoothness':'$this'}).content_types('whiskey').profile(profile).limit(limit+1).fields('id').execute()
    whiskey_ids = [result['id'] for result in results['all'][1:]]
    return Whiskey.objects.filter(id__in=whiskey_ids)

def related_whiskey(whiskey_id,profile=None,limit=3):
    """
    Gets whiskies related to this whiskey.
    """
    rq = _rq()
    rq.content().content_types('whiskey').limit(limit).fields('id').basekey(whiskey_id).filters({'$rtag':'$this'})

    if profile:
        rq.profile(profile)

    whiskey_ids = rq.execute()['all']
    return Whiskey.objects.filter(id__in=whiskey_ids)

def preferred_whiskey(profile):
    """
    Gets a single preferred whiskey.
    """
    rq = _rq()
    results = rq.content().profile(profile).content_types('whiskey').limit(1).fields('id').execute()
    if results['all']:
        whiskey_id = results['all'][0]['id']
        return Whiskey.object.get(pk=whiskey_id)
    else:
        return Whiskey.objects.all().order_by('?')[0]

def record_rating(whiskey_id,profile,rating):
    """
    Records a rating for a whiskey.  Sends trigger to charlotte.
    """
    t = _triggers()
    t.async(profile,'rating',str(rating),whiskey=whiskey_id)

def shelve(whiskey_id,profile):
    """
    Add whiskey to shelf - sends trigger to charlotte.
    """
    t = _triggers()
    t.async(profile,'shelf','add',whiskey=whiskey_id)

def unshelve(whiskey_id,profile):
    """
    Removes a whiskey from the shelf.  Sends trigger.
    """
    t = _triggers()
    t.async(profile,'shelf','remove',whiskey=whiskey_id)

def wishlist(whiskey_id,profile):
    """
    Adds whiskey to wishlist.
    """
    t = _triggers()
    t.async(profile,'wishlist','add',whiskey=whiskey_id)

def unwishlist(whiskey_id,profile):
    t = _triggers()
    t.async(profile,'wishlist','remove',whiskey=whiskey_id)

