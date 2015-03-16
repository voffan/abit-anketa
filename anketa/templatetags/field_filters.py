from django import template
from django.forms import ChoiceField
#import pdb

register = template.Library()

@register.filter(is_safe=True)
def renderbootstrap(field, placeholder=None):
    """Converts a field into a control with a Bootstrap CSS class"""

    att = {"class":"form-control"} if type(field.field) != ChoiceField else {"class":"radio-inline"}
    
    if placeholder != None:
        att["placeholder"] = placeholder
    else:
        try:
            att["placeholder"] = field.placeholder
        except:
            pass
    return field.as_widget(widget=None, attrs=att, only_initial=False)
