from django import template
from .templates_tags import show_header, show_footer

register = template.Library()
register.inclusion_tag("includes/header.html")(show_header)
register.inclusion_tag("includes/footer.html")(show_footer)
