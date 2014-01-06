import re

from markdown.postprocessors import Postprocessor
from markdown.extensions import Extension

from pyramid.renderers import render


class ImageSetProcessor(Postprocessor):

    def __init__(self, request, images_list, images_dict):
        self.request = request
        self.images_list = images_list
        self.images_dict = images_dict

    def filter_images(self, refs):
        images = []
        for ref in refs.split(','):
            ref = ref.strip()
            if ref.isdigit():
                # Look up by index
                image = self.images_list[int(ref) - 1]
            else:
                # Look up by key
                image = self.images_dict[ref]
            images.append(image)
        return images

    def handle_match(self, m):
        images = self.filter_images(m.group(1))
        format = (m.group(2) or 'default').strip()
        return render('imageset.html',
                      dict(
                          images=images,
                          format=format,
                      ),
                      self.request)

    def run(self, text):
        return re.sub(r'\<p\>\{([0-9\,]+)(\ [a-z0-9\-]+)?\}\<\/p\>',
                      self.handle_match, text)


class ImageSetExtension(Extension):

    def __init__(self, request, images):
        self.request = request
        self.images_list = images
        self.images_dict = {im.name: im for im in images}

    def extendMarkdown(self, md, md_globals):
        md.postprocessors.add('imagesetprocessor',
                              ImageSetProcessor(self.request,
                                                self.images_list,
                                                self.images_dict),
                              '_begin')
