from zope.interface import Interface
from zope import schema

from pareto.socialfooter import _

COLORS = ['black', 'white']
TYPES = ['transparent', 'circle', 'rounded']
PROVIDERS = [
    'quora', 'pinterest', 'imessage', 'foodspotting', 'etsy', 'about_me', 
    '500px', 'w3', 'stackoverflow', 'spotify', 'sound_cloud', 'smugmug', 
    'grooveshark', 'gowalla', 'gdgt', 'blip', 'wikipedia', 'scribd', 
    'photobucket', 'itune', 'github', 'forrst', 'dribbble', 'daytum', 
    'app_store_alt', 'star', 'podcast', 'identica', 'icondock', 'hyves', 
    'foursquare', 'ember_app', 'coroflot', 'yelp', 'xing', 'paypal', 
    'metacafe', 'icq', 'heart', 'gowalla_pin', 'drupal', 'add_this', 
    'share_this', 'rss', 'picasa', 'meetup', 'google_buzz', 'feed_burner', 
    'email', 'ebay', 'bing', 'squidoo', 'posterous', 'friendstar', 
    'deviant_art', 'designfloat', 'design_bump', 'behance', 'bebo', 
    'wordpress', 'virb', 'vimeo', 'viddler', 'tumblr', 'qik', 'mr_wong', 
    'blogger', 'windows', 'msn', 'mobileme', 'last.fm', 'apple', 'app_store', 
    'aol', 'amazon', 'youtube', 'yahoo', 'yahoo_buzz', 'technorati', 
    'slideshare', 'reddit', 'newsvine', 'google_talk', 'friendsfeed', 
    'stumbleupon', 'slashdot', 'skype', 'myspace', 'mixx', 'linkedin', 
    'digg', 'digg_alt', 'twitter', 'twitter_bird', 'retweet', 'flickr', 
    'facebook', 'delicious',
]

class ISocialFooterPanelSchema(Interface):

    type = schema.Choice(         
        title=_(u'Choose icon type'),
        values=TYPES,
        default=TYPES[0])
    color = schema.Choice(         
        title=_(u'Choose icon color'),
        values=COLORS,
        default=COLORS[0])
    size =  schema.Int(         
        title=_(u'Size'),
        description=_(u'Pixel size of the icon (square), the icons are 32px '
                u'by default, bigger sizes will start to look blocky. Smaller '
                u'should be fine.'),
        default=32)
    provider = schema.Choice(         
        title=_(u'Choose social provider'),
        values=sorted(PROVIDERS),
        default=sorted(PROVIDERS)[0])
    link = schema.URI(
        title=u"Link to social page",
        required=False)
    icons = schema.List(
        title=u"Icons",
        description=_(u'After removing one or more icons you have to save for '
                      u'the change to be permanent.'),
        required=False,
        default=[],
        value_type=(schema.TextLine(title=u"Icon")))
