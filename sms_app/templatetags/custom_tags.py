from django import template
import datetime
register = template.Library()

@register.filter()
def addDays(days):
   newDate = datetime.date.today() + datetime.timedelta(days=days)
   return newDate

@register.filter()
def minusDays(days):
   newDate = datetime.date.today() - datetime.timedelta(days=days)
   return newDate

@register.filter()
def firstname(this_name):
   this_firstname = this_name.split()[0]
   return this_firstname

@register.filter
def remove_email(value):
    return value.replace("@unord.dk", "").upper()