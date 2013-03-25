from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase

from plone.registry.interfaces import IRegistry
from zope.component import getUtility

INTERFACE = 'pareto.customimages.browser.interfaces.IZeelandiaSettings'

def vocabulary(name):
    registry = getUtility(IRegistry)
    return registry.records.get('%s.%s' % (INTERFACE, name)).value

class SocialFooterViewlet(ViewletBase):
    index = ViewPageTemplateFile('socialfooter.pt')

    def update(self):
        self.computed_value = 'any output'


class ISocialFooterPanelSchema(Interface):

    color = Choice(         
        title=_(u'Choose icon color'),
        values=vocabulary('colors'))
    type = Choice(         
        title=_(u'Choose icon type'),
        values=vocabulary('types'))
    provider = Choice(         
        title=_(u'Choose social provider'),
        values=vocabulary('providers'))
    link = URI(title=u"Link to social page")
    

class SocialFooterPanel(ControlPanelForm):

    template = ViewPageTemplateFile('socialfooter-panel.pt')

    form_fields = form.FormFields(ISocialFooterPanelSchema)
    form_name = _(u'Social Footer Setup')
    label = _(u'Social Footer Setup')
    description = _(u'Create links to social platforms with icon from Mono.')

    def images(self):
        registry = getUtility(IRegistry)
        value = registry.records.get('%s.images' % INTERFACE).value
        images = dict([tuple([str(w) if i == 0 else w 
                              for i, w in enumerate(v.split('|'))]) 
                       for v in value])
        return images

    def _on_save(self, data=None):
        import pdb; pdb.set_trace()
#        if data is None:
#            # no form data, return without doing anything
#            return
#
#        new_image = data.get('image', None)
#        if not new_image:
#            # image not uploaded, return without doing anything
#            return
#
#        image_id = self.request.form.get('image_id', None)
#        if image_id:
#            image_id = str(image_id)
#        else:
#            image_id = LOGO_ID
#
#        image_title = self.request.form.get('image_title', None)
#        if not image_title:
#            image_title = u'Custom Logo'
#
#        skins = getToolByName(self.context, 'portal_skins')
#        target = self.context
#        if 'custom' in skins:
#            target = skins['custom']
#
#        if image_id in target:
#            img = target[image_id]
#            if isinstance(img, Image):
#                # this is an OFS image, or subclass, we should have the
#                # update_data method
#                try:
#                    img.update_data(new_image)
#                    return
#                except TypeError, e:
#                    # there is a problem with the image data, it's unicode
#                    raise e
#                except AttributeError, e:
#                    # no update_data method.  make a new one and replace this
#                    # one
#                    pass
#            else:
#                # let's override it, it isn't an expected type.
#                pass
#
#        img = Image(image_id, 'Custom %s' % image_title, new_image)
#        target._setObject(image_id, img)
#        return

#
#    @form.action(_(u'label_save', default=u'Save'), name=u'save')
#    def handle_edit_action(self, action, data):
#        CheckAuthenticator(self.request)
#        if form.applyChanges(self.context, self.form_fields, data,
#                             self.adapters):
#            self.status = _("Changes saved.")
#            notify(ConfigurationChangedEvent(self, data))
#            self._on_save(data)
#        else:
#            self.status = _("No changes made.")
#
#    @form.action(_(u'label_cancel', default=u'Cancel'),
#                 validator=null_validator,
#                 name=u'cancel')
#    def handle_cancel_action(self, action, data):
#        IStatusMessage(self.request).addStatusMessage(_("Changes canceled."),
#                                                      type="info")
#        url = getMultiAdapter((self.context, self.request),
#                              name='absolute_url')()
#        self.request.response.redirect(url + '/plone_control_panel')
#        return ''
#
#    @form.action(_(u'label_clear', default=u'Clear'), 
#                 validator=null_validator,
#                 name=u'clear')
#    def handle_clear_action(self, action, data):
#        skins = getToolByName(self.context, 'portal_skins')
#        target = skins.get('custom', self.context)
#        image_id = self.request.form.get('image_id', None)
#        if not image_id:
#            self.status = _("No image id.")
#        elif image_id in target:
#            target._delObject(image_id)
#            self.status = _("Changes saved.")
#        else:
#            self.status = _("No changes made.")