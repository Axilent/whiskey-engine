from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from whiskeyengine.models import *
import traceback
from django.conf import settings

def _convert_value(raw_value):
    """
    Converts percentage value to 0.0 to 5.0 range.
    """
    return round(float(raw_value) * 0.1) / 2.0

def home(request,whiskey_slug=None):
    """
    Home page.
    """
    featured_whiskey = None
    if whiskey_slug:
        featured_whiskey = Whiskey.objects.get(slug=whiskey_slug)
    elif 'smooth' in request.GET:
        smooth = _convert_value(request.GET['smooth'])
        bite = _convert_value(request.GET['bite'])
        sweet = _convert_value(request.GET['sweet'])
        
        query_string = 'smooth:%d bite:%d sweet:%d' % (smooth,bite,sweet)
        
        search_results = Whiskey.objects.search(query_string)
        if search_results.exists():
            featured_whiskey = search_results[0]
        else:
            featured_whiskey = Whiskey.objects.all().order_by('?')[0]
    else:
        featured_whiskey = Whiskey.objects.all().order_by('?')[0]
    
    return render_to_response('index.html',{'feature':featured_whiskey},context_instance=RequestContext(request))


def related_whiskey(request,whiskey_id):
    """
    Gets whiskies related to the specified whiskey.
    """
    base_whiskey = Whiskey.objects.get(pk=whiskey_id)
    related = Whiskey.objects.channel(channel='Related Whiskey',basekey=base_whiskey.get_axilent_content_key())
    if len(related) > 3:
        related = related[:3]
    c = RequestContext(request)
    return render_to_response('includes/related.html',{'related':related,'base_whiskey':base_whiskey},context_instance=c)

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
    results = Whiskey.objects.search(request.GET['q'])
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

def _get_profile(request):
    """
    Gets or creates profile for the request.  Will return the tuple of the profile and flag indicating
    the profile is new and should be set in the response.
    """
    if request.COOKIES.has_key('axilent_profile'):
        return request.COOKIES['axilent_profile'], False
    else:
        profile = triggers.profile()['profile']
        return profile, True
    

