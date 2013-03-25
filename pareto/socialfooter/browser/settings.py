from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.z3cform import layout

from zeelandia.edit.browser.interfaces import IZeelandiaSettings
from zeelandia.edit import _

class SettingsEditForm(RegistryEditForm):
    """Zeelandia Settings edit form for plone.app.registry.
    """
    schema = IZeelandiaSettings
    label = _(u"Zeelandia Settings")
    # redirect to ourselves after edit
    control_panel_view = "zeelandia-settings"


SettingsView = layout.wrap_form(SettingsEditForm, ControlPanelFormWrapper)
