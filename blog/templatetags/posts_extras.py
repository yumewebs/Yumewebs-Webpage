from django import template
from blog.models import Post

register = template.Library()

@register.simple_tag
def get_post_list():
    posts = Post.objects.all()
    return posts