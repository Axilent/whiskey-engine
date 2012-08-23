from sharrock.client import HttpClient, ResourceClient
from django.shortcuts import render_to_response
from django.template import RequestContext
from sharrock.client import HttpClient, ResourceClient
from django.conf import settings
from django.http import HttpResponseRedirect

axl = HttpClient('%s/api' % settings.AXILENT_ENDPOINT,'axilent.content','beta3',auth_user=settings.AXILENT_API_KEY)
content_resource = ResourceClient('%s/api/resource' % settings.AXILENT_ENDPOINT,'axilent.content','beta3','content',auth_user=settings.AXILENT_API_KEY)
triggers = HttpClient('%s/api' % settings.AXILENT_ENDPOINT,'axilent.triggers','beta3',auth_user=settings.AXILENT_API_KEY)

def home(request,whiskey_slug=None):
    """
    Mobile home page.
    """
    featured_whiskey = None
    if whiskey_slug:
        featured_whiskey = axl.getcontentbyuniquefield(content_type='Whiskey',field_name='slug',field_value=whiskey_slug)
    else:
        featured_whiskey = axl.contentchannel(channel='random-whiskey')['default'][0]['content']
    
    related = [item['content'] for item in axl.contentchannel(channel='related-whiskey',basekey=featured_whiskey['key'])['default'][:3]]
    
    return render_to_response('index.html',{'feature':featured_whiskey,'related':related},context_instance=RequestContext(request))

def _convert_value(raw_value):
    """
    Converts percentage value to 0.0 to 5.0 range.
    """
    return round(float(raw_value) * 0.1) / 2.0

def blend(request):
    """
    Blend your whiskey page.
    """
    if request.POST:
        smooth = _convert_value(request.POST['smooth'])
        bite = _convert_value(request.POST['bite'])
        sweet = _convert_value(request.POST['sweet'])
        
        search_results = axl.search(content_types='Whiskey',query='smoothness:%s bite:%s sweet:%s' % (str(smooth),str(bite),str(sweet)))
        if len(search_results):
            feature = search_results[0]
            return HttpResponseRedirect('/whiskey/%s/' % feature['data']['slug'])
            
    return render_to_response('blend.html',{},context_instance=RequestContext(request))

def search(request):
    """
    Search page.
    """
    results = None
    if 'q' in request.GET:
        results = axl.search(content_types='Whiskey',query=request.GET['q'])
    return render_to_response('search.html',{'results':results},context_instance=RequestContext(request))

    