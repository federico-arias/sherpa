from lxml import etree
from django.conf import settings
from slugify import slugify
import shutil, os, sys


def slug(context, s):
    return slugify(s.encode('utf-8', 'ignore').decode('utf-8', 'ignore'))

class Unidad:
    def __init__(self, filename, stylesheet, folder):
        self.stylesheet = os.path.join(settings.MEDIA_ROOT, stylesheet)
        self.filename = os.path.join(settings.MEDIA_ROOT, filename)
        self.folder = os.path.join(settings.MEDIA_ROOT, os.path.dirname(filename), folder)
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)

        self.xml = etree.parse(self.filename)
        self.parse_xml()

    def parse_xml(self):
        temas = self.xml.xpath('/temas/tema')
        ns = etree.FunctionNamespace("urn:federico")
        ns.prefix = 'f'
        ns['slugify'] = slug
        stylesheet = etree.parse(self.stylesheet)
        transform = etree.XSLT(stylesheet)
        for tema in temas:
            self.create_files(tema, transform)

    def create_files(self, node, xslt):
        node = etree.ElementTree(node)
        webpage = xslt(node, inicio="'1'", biblio="'2'")
        name = self.slug(node.find('filename').text)
        webpage.write(os.path.join(self.folder, name + '.html'))

    def getZipFileName(self):
        fname = shutil.make_archive(os.path.join(os.path.dirname(self.folder), self.filename), 'zip', os.path.dirname(self.folder), base_dir=self.folder)
        shutil.rmtree(self.folder)
        return fname

    def slug(self, s):
        return slugify(s.encode('utf-8', 'ignore').decode('utf-8', 'ignore'))

