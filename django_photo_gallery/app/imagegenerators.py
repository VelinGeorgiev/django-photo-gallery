from imagekit import ImageSpec, register
from imagekit.processors import ResizeToFit

# usage in HTML - {% generateimage 'blog:thumbnail' source=post.thumb -- alt=post.title class='post-thumb' %}
class Thumbnail(ImageSpec):
    processors = [ResizeToFit(200)]
    format = 'JPEG'
    options = {'quality': 85}

register.generator('blog:thumbnail', Thumbnail)