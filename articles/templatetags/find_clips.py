from django import template
from django.utils.safestring import mark_safe
from articles.models import Article

register = template.Library()

@register.filter
def find_clips(article, keyword):
    if len(article.content) <= 20:
        return article.content
    else:
        return article.content[:20] + "..."