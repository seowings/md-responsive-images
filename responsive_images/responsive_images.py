from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension
from PIL import Image


class InlineImageProcessor(Treeprocessor):
    def run(self, root):
        for element in root.iter('img'):
            attrib = element.attrib

            # if attrib
            fl, ext = attrib['src'].split('.webp')
            element.set('title', attrib['alt'])
            element.set('srcset', f"{fl}-480w.webp 480w, {fl}-800w.webp 800w")
            element.set('sizes', "(max-width: 600px) 480px, 800px")
            im = Image.open(attrib['src'])
            element.set('width', str(im.width))
            element.set('height', str(im.height))
            element.set('loading', "lazy")


class ImageExtension(Extension):
    def extendMarkdown(self, md):
        md.treeprocessors.register(
            InlineImageProcessor(md), 'responsive_images', 15)

def makeExtension(**kwargs):
    return ImageExtension(**kwargs)