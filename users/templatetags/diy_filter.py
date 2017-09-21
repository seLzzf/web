from django import template

register=template.Library()
@register.filter
def x_in_list(list,x):
	try:
		return list[x]
	except:
		return "it's not a list"