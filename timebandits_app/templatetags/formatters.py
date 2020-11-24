from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()

# code inspired by
# https://stackoverflow.com/questions/346467/format-numbers-in-django-templates

# /***************************************************************************************
# *  REFERENCES
# *  Title: Filtering program
# *  Author: Dave Aaron Smith
# *  Date: 2/1/2020
# *  Code version: 1
# *  URL: https://stackoverflow.com/questions/346467/format-numbers-in-django-templates
# *  Software License: MIT
# ***************************************************************************************/


def currency(dollars):
    dollars = round(float(dollars), 2)
    return "$%s%s" % (intcomma(int(dollars)), ("%0.2f" % dollars)[-3:])


def volunteer_level(hours):
    return int(hours / 10) + 1

# def remove_midnight(datestr):
#     datestr.replace(', midnight')


register.filter('currency', currency)
register.filter('level', volunteer_level)
# register.filter('midnight', remove_midnight)
