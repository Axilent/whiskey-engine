from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from whiskeyengine.models import *
#from whiskeyengine.forms import *
#from whiskeyengine import graphstack
import traceback
#from haystack.query import SearchQuerySet
from django.conf import settings
from sharrock.client import HttpClient

axl = HttpClient('%s/api' % settings.AXILENT_ENDPOINT,'axilent.content','beta3',auth_user=settings.AXILENT_API_KEY)

def home(request,whiskey_slug=None):
    """
    Home page.
    """
    featured_whiskey = None
    if whiskey_slug:
        featured_whiskey = axl.getcontentbyuniquefield(content_type='Whiskey',field_name='slug',field_value=whiskey_slug)
    elif 'smooth' in request.GET:
        pass # TODO
    else:
        featured_whiskey = axl.contentchannel(channel='random-whiskey')['default'][0]['content']
    
    return render_to_response('index.html',{'feature':featured_whiskey},context_instance=RequestContext(request))
    # featured_whiskey = None
    # if whiskey_slug:
    #     featured_whiskey = Whiskey.objects.get(slug=whiskey_slug)
    # elif 'smooth' in request.GET:
    #     # slider params
    #     try:
    #         featured_whiskey = Whiskey.objects.get_whiskey_by_sliders(request.GET.get('smooth',0),
    #                                                                   request.GET.get('bite',0),
    #                                                                   request.GET.get('sweet',0))
    #     except Whiskey.DoesNotExist:
    #         featured_whiskey = Whiskey.objects.all().order_by('?')[0]
    # else:
    #     featured_whiskey = Whiskey.objects.all().order_by('?')[0]
    # c = RequestContext(request)
    # 
    # smooth_percent = request.GET.get('smooth',featured_whiskey.smooth_percent)
    # bite_percent = request.GET.get('bite',featured_whiskey.bite_percent)
    # sweet_percent = request.GET.get('sweet',featured_whiskey.sweet_percent)
    # 
    # return render_to_response('index.html', {'feature':featured_whiskey,
    #                                          'smooth_percent':smooth_percent,
    #                                          'bite_percent':bite_percent,
    #                                          'sweet_percent':sweet_percent}, context_instance=c)

def recommended_whiskey(request):
    """
    Pulls recommended whiskey for the profiled user.
    """
    recommended = []
    if dummy_mode:
        recommended = Whiskey.objects.all().order_by('?')[:3] # Graphstack bypass
    else:
        if not request.user.is_anonymous():
            profile = request.user.get_profile().saaspire_profile
            recommended = graphstack.get_recommended_whiskies(profile)
    
    c = RequestContext(request)
    return render_to_response('includes/recommended.html',{'recommended':recommended},context_instance=c)

def related_whiskey(request,whiskey_id):
    """
    Gets whiskies related to the specified whiskey.
    """
    whiskey = Whiskey.objects.get(pk=whiskey_id)
    if dummy_mode:
        related = Whiskey.objects.all().order_by('?')[:3] # Graphstack bypass
    else:
        related = graphstack.get_related_whiskies(whiskey.saaspire_key,profile=graphstack.profile(request))
    
    c = RequestContext(request)
    return render_to_response('includes/related.html',{'related':related,'base_whiskey':whiskey},context_instance=c)

def review_whiskey(request,whiskey_id):
    """
    Review the specified whiskey.
    """
    try:
        drinker = None
        form = None
        whiskey = Whiskey.objects.get(pk=whiskey_id)
        if request.POST:
            form = ReviewForm(request.POST)
            if form.is_valid():
                drinker = form.create_profile(request)
                form.create_review(drinker,whiskey)
                return HttpResponse('OK') # flag to close dialog
        else:
            form = ReviewForm()
    
        c = RequestContext(request)
        return render_to_response('review.html',{'whiskey':whiskey,'form':form,'drinker':drinker},context_instance=c)
    except:
        traceback.print_exc()

def search(request):
    """
    Search for whiskey.
    """
    results = axl.search(content_types='Whiskey',query=request.GET['q'])
    c = RequestContext(request)
    return render_to_response('search_results.html',{'results':results},context_instance=c)

def about_whiskey_engine(request):
    """
    About whiskey engine static page.
    """
    return render_to_response('about_whiskey_engine.html',{},context_instance=RequestContext(request))

def about_american_whiskey(request):
    """
    About american whiskey static page.
    """
    return render_to_response('about_american_whiskey.html',{},context_instance=RequestContext(request))


