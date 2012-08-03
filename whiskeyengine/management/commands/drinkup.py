"""
Management command to tag whiskies.
"""
from django.core.management.base import BaseCommand
from django.conf import settings
from whiskeyengine.models import Whiskey
from sharrock.client import ResourceClient

class Command(BaseCommand):
    """
    Command class.
    """
    def handle(self,*args,**options):
        """
        Handler method.
        """
        # create content type
        content_type = ResourceClient(settings.SAASPIRE_RESOURCE_API,'saaspire.content','0.1dev','contenttyperesource',auth_user=settings.SAASPIRE_API_KEY)
        content_type.post(data={'name':'Whiskey',
                                'slug':'whiskey',
                                'content_fields':[{'name':'name','salience':99},
                                                  {'name':'herbs_spice','salience':40},
                                                  {'name':'flowers','salience':40},
                                                  {'name':'fruit','salience':40},
                                                  {'name':'candy','salience':70},
                                                  {'name':'wood','salience':50},
                                                  {'name':'length_of_finish','salience':60},
                                                  {'name':'complexity','salience':80},
                                                  {'name':'smoothness','salience':90}]})
        
        
        # Add whiskey
        content = ResourceClient(settings.SAASPIRE_RESOURCE_API,'saaspire.content','0.1dev','contentresource',auth_user=settings.SAASPIRE_API_KEY)

        for whiskey in Whiskey.objects.all():
            whiskey.saaspire_key = content.post(data={'content_type_slug':'whiskey',
                                                      'content':{'name':whiskey.name,
                                                                 'herbs_spice':unicode(whiskey.herbs_spice),
                                                                 'flowers':unicode(whiskey.flowers),
                                                                 'fruit':unicode(whiskey.fruit),
                                                                 'candy':unicode(whiskey.candy),
                                                                 'wood':unicode(whiskey.wood),
                                                                 'length_of_finish':unicode(whiskey.length_of_finish),
                                                                 'complexity':unicode(whiskey.complexity),
                                                                 'smoothness':unicode(whiskey.smoothness)}})

            whiskey.save()
        
        
        # create related whiskey policy
        policy = ResourceClient(settings.SAASPIRE_RESOURCE_API,'saaspire.content','0.1dev','contentpolicyresource',auth_user=settings.SAASPIRE_API_KEY)

        policy.post(data={'name':'Related Whiskey',
                          'slug':'related-whiskey',
                          'total_return':3,
                          'params':{'content_type_slug':'whiskey'},
                          'generators':[{'generator_type':'Related Via Metadata','weight':1}]})
        
        # create personalized whiskey policy
        policy.post(data={'name':'Personalized Whiskey',
                          'slug':'personalized-whiskey',
                          'total_return':3,
                          'params':{'content_type_slug':'whiskey'},
                          'generators':[{'generator_type':'Personalized','weight':1}]})
        
        # Add reactor and inferences to graphstack
        reactor = ResourceClient(settings.SAASPIRE_RESOURCE_API,'saaspire.reactor','0.1dev','reactorresource',auth_user=settings.SAASPIRE_API_KEY)
        reactor.post(params={'reactor_type_name':'editorial'})

        inference = ResourceClient(settings.SAASPIRE_RESOURCE_API,'saaspire.reactor','0.1dev','inferenceresource',auth_user=settings.SAASPIRE_API_KEY)
        
        # Add affinity inference for endorsement triggers
        inference.post(data={'reactor_type_name':'editorial',
                             'name':'Endorsement Inference',
                             'inference_type':'Affinity',
                             'listeners':[{'category':'whiskey','action':'endorsement'}],
                             'params':{'content_key_param':'whiskey','content_type':'whiskey','correlation':80}})
        
        # Add negative inference for disendorsement triggers
        inference.post(data={'reactor_type_name':'editorial',
                             'name':'Disendorsement Inference',
                             'inference_type':'Ban',
                             'listeners':[{'category':'whiskey','action':'disendorsement'}],
                             'params':{'content_key_param':'whiskey','content_type':'whiskey'}})

