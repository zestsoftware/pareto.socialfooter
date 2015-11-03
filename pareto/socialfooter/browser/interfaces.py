from zope.interface import Interface
from zope import schema

from pareto.socialfooter import _

COLORS = [_(u'black'), _(u'white')]
TYPES = [_(u'transparent'), _(u'circle'), _(u'rounded')]

PROVIDERS = [
    '500px',
    'about_me',
    'add_this',
    'amazon',
    'aol',
    'app_store',
    'app_store_alt',
    'apple',
    'bebo',
    'behance',
    'bing',
    'blip',
    'blogger',
    'coroflot',
    'daytum',
    'delicious',
    'design_bump',
    'designfloat',
    'deviant_art',
    'digg',
    'digg_alt',
    'dribbble',
    'drupal',
    'ebay',
    'email',
    'ember_app',
    'etsy',
    'facebook',
    'feed_burner',
    'flickr',
    'foodspotting',
    'forrst',
    'foursquare',
    'friendsfeed',
    'friendstar',
    'gdgt',
    'github',
    'google_buzz',
    'google_talk',
    'gowalla',
    'gowalla_pin',
    'grooveshark',
    'heart',
    'hyves',
    'icondock',
    'icq',
    'identica',
    'imessage',
    'itune',
    'last.fm',
    'linkedin',
    'meetup',
    'metacafe',
    'mixx',
    'mobileme',
    'mr_wong',
    'msn',
    'myspace',
    'newsvine',
    'paypal',
    'photobucket',
    'picasa',
    'pinterest',
    'podcast',
    'posterous',
    'qik',
    'quora',
    'reddit',
    'retweet',
    'rss',
    'scribd',
    'share_this',
    'skype',
    'slashdot',
    'slideshare',
    'smugmug',
    'sound_cloud',
    'spotify',
    'squidoo',
    'stackoverflow',
    'star',
    'stumbleupon',
    'technorati',
    'tumblr',
    'twitter',
    'twitter_bird',
    'viddler',
    'vimeo',
    'virb',
    'w3',
    'wikipedia',
    'windows',
    'wordpress',
    'xing',
    'yahoo',
    'yahoo_buzz',
    'yelp',
    'youtube',
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
    size = schema.Int(
        title=_(u'Size'),
        description=_(u'Pixel size of the icon (square), the icons are 32px '
                      u'by default, bigger sizes will start to look blocky. '
                      u'Smaller should be fine.'),
        default=32)
    provider = schema.Choice(
        title=_(u'Choose social provider'),
        values=sorted(PROVIDERS),
        default=sorted(PROVIDERS)[0])
    link = schema.URI(
        title=_(u"Link to social page"),
        required=False)
    icons = schema.List(
        title=_(u"Icons"),
        description=_(u'After removing one or more icons you have to save for '
                      u'the change to be permanent.'),
        required=False,
        default=[],
        value_type=(schema.TextLine(title=_(u"Icon"))))
