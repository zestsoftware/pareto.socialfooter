from zope.formlib import form
from zope.interface import implements
from zope.component import adapts
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.controlpanel.form import ControlPanelForm
from plone.app.controlpanel.events import ConfigurationChangedEvent
from Products.CMFPlone.interfaces import IPloneSiteRoot
from plone.protect import CheckAuthenticator
from zope.event import notify
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from pareto.socialfooter.browser.interfaces import ISocialFooterPanelSchema

from pareto.socialfooter import _

INTERFACE = 'pareto.socialfooter.browser.interfaces.ISocialFooterPanelSchema'


class SocialFooterPanelAdapter(object):

    adapts(IPloneSiteRoot)
    implements(ISocialFooterPanelSchema)

    def __init__(self, context):
        registry = getUtility(IRegistry)
        self.context = context
        self.type = registry.records.get('%s.%s' % (INTERFACE, 'type')).value
        self.color = registry.records.get('%s.%s' % (INTERFACE, 'color')).value
        self.size = registry.records.get('%s.%s' % (INTERFACE, 'size')).value
        self.provider = ''
        self.link = ''
        self.icons = registry.records.get('%s.%s' % (INTERFACE, 'icons')).value


class SocialFooterPanel(ControlPanelForm):

    template = ViewPageTemplateFile('socialfooter-panel.pt')

    form_fields = form.FormFields(ISocialFooterPanelSchema)
    form_name = _(u'Social Footer Setup')
    label = _(u'Social Footer Setup')
    description = _(u'Create links to social platforms with icon from Mono.')

    def values(self):
        registry = getUtility(IRegistry)
        return dict(
            color=registry.records.get('%s.%s' % (INTERFACE, 'color')).value,
            type=registry.records.get('%s.%s' % (INTERFACE, 'type')).value,
            icons=registry.records.get('%s.%s' % (INTERFACE, 'icons')).value,
        )

    def extra_script(self):
        return """
var iColor = $('[id="form.color"] option:selected').val(),
    iType =  $('[id="form.type"] option:selected').val(),
    iSize =  $('[id="form.size"]').val().;

$('input[name=form.icons.add]').remove();
$('.sequencewidget td:first-child').width('30px');
$('.sequencewidget .textType').hide().each(function(){
    var $me = $(this).hide(),
        tokens = $me.val().split('|'),
        iProvider = tokens[0],
        iTitle = iProvider.split('_')[0],
        iUrl = tokens[1];
    $me.after('<a style="background-color: #ccc; ' +
                        'border: 1px solid #999; ' +
                        'border-radius: .5em; ' +
                        'padding: .5em; ' +
                        'display: block; ' +
                        'margin-bottom: .5em; ' +
                        'float: left; " ' +
                  'href="' + iUrl + '">' +
                  '<img src="++resource++pareto.socialfooter.mono/' +
                             iType + '/' +
                             iColor + '/' +
                             iProvider + '.png"' +
                        'alt="' + iTitle + '" ' +
                        'title="' + iTitle + '" ' +
                        'width="' + iSize + '" ' +
                        'height="' + iSize + '" ' +
                  '/></a>');
});
        """

    @form.action(_(u'label_save_icon_properties',
                   default=u'Save icon properties'), name=u'save_properties')
    def handle_properties_action(self, action, data):
        CheckAuthenticator(self.request)
        if form.applyChanges(self.context, self.form_fields, data,
                             self.adapters):
            self.status = _("Changes saved.")
            notify(ConfigurationChangedEvent(self, data))
            self._on_save(data)
        else:
            self.status = _("No changes made.")

    @form.action(_(u'label_add_icon',
                   default=u'Add icon'), name=u'add_icon')
    def handle_add_icon_action(self, action, data):
        CheckAuthenticator(self.request)
        if form.applyChanges(self.context, self.form_fields, data,
                             self.adapters):
            self.status = _("Changes saved.")
            notify(ConfigurationChangedEvent(self, data))
            self._on_save(data)
        else:
            self.status = _("No changes made.")

    @form.action(_(u'label_remove',
                   default=u'Save'), name=u'remove')
    def handle_save_action(self, action, data):
        CheckAuthenticator(self.request)
        if form.applyChanges(self.context, self.form_fields, data,
                             self.adapters):
            self.status = _("Changes saved.")
            notify(ConfigurationChangedEvent(self, data))
            self._on_save(data)
        else:
            self.status = _("No changes made.")

    def _on_save(self, data=None):
        registry = getUtility(IRegistry)
        if 'form.actions.save_properties' in self.request.form:
            record_type = registry.records.get('%s.%s' % (INTERFACE, 'type'))
            record_type.value = data['type']
            record_color = registry.records.get('%s.%s' % (INTERFACE, 'color'))
            record_color.value = data['color']
            record_size = registry.records.get('%s.%s' % (INTERFACE, 'size'))
            record_size.value = data['size']
            return

        if 'form.actions.add_icon' in self.request.form:
            record = registry.records.get('%s.%s' % (INTERFACE, 'icons'))
            value = record.value
            value.append(u'%s|%s' % (data['provider'], data['link']))
            # This is not a PersistentList, but a standard Python list, so
            # appending is not enough to persistently save it: we need to set
            # the value explicitly.
            record.value = value

        if 'form.actions.remove' in self.request.form:
            record = registry.records.get('%s.%s' % (INTERFACE, 'icons'))
            record.value = data['icons']
