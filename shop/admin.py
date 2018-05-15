
from django.contrib import admin

from .models import ShoppingList
from django.contrib import messages

class ShoppingListAdmin(admin.ModelAdmin):
    fields = ['item', 'bought']
    list_display = ('item', 'got_it')
    actions = ['mark_bought']
    
    def mark_bought(self, request, queryset):

        queryset.update(bought='Y')    

    
    mark_bought.short_description = "Mark bought"
    
    def get_action_choices(self, request):
        choices = super(ShoppingListAdmin, self).get_action_choices(request)
        # choices is a list, just change it.
        # the first is the BLANK_CHOICE_DASH
        choices.pop(0)
        # do something to change the list order
        # the first one in list will be default option
        choices.reverse()
        return choices 

    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': ''}
        return super(ShoppingListAdmin, self).changelist_view(request, extra_context=extra_context)

admin.site.register(ShoppingList,ShoppingListAdmin)
