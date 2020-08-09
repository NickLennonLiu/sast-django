from django import template
import string
from django.utils.safestring import mark_safe
from articles.models import Article

register = template.Library()


@register.filter
def find_clips(article, keyword):
    text = article.content
    pos = text.find(keyword)
    cut = text[max(0, pos-20):min(len(text), pos+20)]
    if max(0, pos-20) == 0:
        return cut.strip(string.punctuation).strip("，").strip("。") + "..."
    else:
        return "..." + cut.strip(string.punctuation).strip("，").strip("。") + "..."

