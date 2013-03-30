from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from plone.registry.interfaces import IRegistry
from zope.component import getUtility

from pareto.socialfooter import _

INTERFACE = 'pareto.socialfooter.browser.interfaces.ISocialFooterPanelSchema'
TEMPLATE = '''<a href="%(url)s" id="socialfooter_%(id)s">
    <img src="%(src)s" alt="%(title)s" title="%(title)s" 
         width="%(size)s" height="%(size)s"/>
</a>''' 
RESOURCE = '++resource++pareto.socialfooter.mono'
EXT='.png'

class SocialFooterViewlet(ViewletBase):
    index = ViewPageTemplateFile('socialfooter.pt')

    def update(self):
        registry = getUtility(IRegistry)
        try:
            color = registry.records.get('%s.%s' % (INTERFACE, 'color')).value
            type = registry.records.get('%s.%s' % (INTERFACE, 'type')).value
            size = registry.records.get('%s.%s' % (INTERFACE, 'size')).value
            icons = [i.split('|') for i in 
                registry.records.get('%s.%s' % (INTERFACE, 'icons')).value]
            self.icons = ' '.join([TEMPLATE % dict(
                     url=i[1], id=i[0], size=size,
                     title=i[0].split('_')[0].capitalize(),
                     src='/'.join([RESOURCE, type, color, (i[0] + EXT)])) 
                for i in icons])
        except AttributeError:
            self.icons = ''
