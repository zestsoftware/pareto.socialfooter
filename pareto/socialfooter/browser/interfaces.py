from zope.interface import Interface
from zope import schema

from zeelandia.edit import _

class IParetoSocialSettings(Interface):
    """ Zeelandia settings """

    color = schema.Text(
        title=_(u"address"),
        description=_(u"Content of the addres block."),
        required=False,
        )
