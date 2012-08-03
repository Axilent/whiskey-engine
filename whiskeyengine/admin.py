from django.contrib import admin
from whiskeyengine.models import Whiskey, Feature, Drinker, Review, Category, Distillery

class WhiskeyAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'distillery', 'category', 'description', 'bottle')
            }),
        ('Flavor Ratings', {
            'classes': ('collapse',),
            'fields': ('herbs_spice', 'flowers', 'fruit', 'candy', 'wood', 'length_of_finish', 'complexity', 'smoothness')
            }),
        )

    #list_display = ('name', 'slug', 'distillery', 'category', 'herbs_spice', 'flowers', 'fruit', 'candy', 'wood', 'length_of_finish', 'complexity', 'smoothness')
    list_display = ('name', 'bottle', 'distillery', 'category')
    #list_editable = ('slug', 'distillery', 'category', 'herbs_spice', 'flowers', 'fruit', 'candy', 'wood', 'length_of_finish', 'complexity', 'smoothness')
    list_editable = ('bottle', )
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Distillery)
admin.site.register(Whiskey, WhiskeyAdmin)
admin.site.register(Feature)
admin.site.register(Drinker)
admin.site.register(Review)
admin.site.register(Category)
