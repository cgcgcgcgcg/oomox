import os

from oomox_gui.export.theme import GtkThemeExportDialog, OPTION_GTK2_HIDPI
from oomox_gui.plugin_api import OomoxThemePlugin


plugin_dir = os.path.dirname(os.path.realpath(__file__))


class MateriaThemeExportDialog(GtkThemeExportDialog):
    timeout = 1000
    theme_dir = os.path.join(plugin_dir, "materia-theme/")

    def do_export(self):
        export_args = [
            "bash",
            os.path.join(self.theme_dir, "change_color.sh"),
            "--hidpi", str(self.export_config[OPTION_GTK2_HIDPI]),
            "--output", self.theme_name,
            self.temp_theme_path,
        ]
        super().do_export(export_args)


class Plugin(OomoxThemePlugin):

    name = 'materia'
    display_name = 'Materia'
    description = '(GTK+2, GTK+3, Gnome Shell, Metacity, Unity, Xfwm)'
    export_dialog = MateriaThemeExportDialog
    gtk_preview_css_dir = os.path.join(plugin_dir, "gtk_preview_css/")

    theme_model_gtk = [
        {
            'key': 'BG',
            'type': 'color',
            'display_name': _('Background')
        },
        {
            'key': 'FG',
            'type': 'color',
            'display_name': _('Foreground/text')
        },
        {
            'key': 'MENU_BG',
            'type': 'color',
            'display_name': _('Menu/toolbar background')
        },
        {
            'key': 'MENU_FG',
            'type': 'color',
            'display_name': _('Menu/toolbar text'),
        },
        {
            'key': 'SEL_BG',
            'type': 'color',
            'display_name': _('Selection highlight')
        },
        {
            'key': 'SEL_FG',
            'type': 'color',
            'display_name': _('Selection text'),
        },
        {
            'key': 'ACCENT_BG',
            'fallback_key': 'SEL_BG',
            'type': 'color',
            'display_name': _('Accent color (checkboxes, radios)'),
        },
        {
            'key': 'TXT_BG',
            'type': 'color',
            'display_name': _('Textbox background')
        },
        {
            'key': 'BTN_BG',
            'type': 'color',
            'display_name': _('Button background')
        },
        {
            'key': 'BTN_FG',
            'type': 'color',
            'display_name': _('Button text'),
        },
    ]

    theme_model_options = [
        {
            'key': 'GTK3_GENERATE_DARK',
            'type': 'bool',
            'fallback_value': True,
            'display_name': _('(GTK3) Add dark variant'),
        },
        {
            'key': 'MATERIA_STYLE_COMPACT',
            'type': 'bool',
            'fallback_value': True,
            'display_name': _('Compact style'),
        },
    ]

    theme_model_other = [
        {
            'key': 'GNOME_SHELL_PANEL_OPACITY',
            'type': 'float',
            'fallback_value': 0.6,
            'max_value': 1.0,
            'display_name': _('Gnome Shell panel opacity'),
            'value_filter': {
                'THEME_STYLE': 'materia'
            },
        },
    ]

    def preview_before_load_callback(self, preview_object, colorscheme):
        colorscheme["TXT_FG"] = colorscheme["FG"]
        colorscheme["WM_BORDER_FOCUS"] = colorscheme["MENU_BG"]
        colorscheme["WM_BORDER_UNFOCUS"] = colorscheme["BTN_BG"]
        colorscheme["HDR_BTN_FG"] = colorscheme["MENU_FG"]
        colorscheme["HDR_BTN_BG"] = colorscheme["MENU_BG"]
        colorscheme["ROUNDNESS"] = 0
        colorscheme["GRADIENT"] = 0
        preview_object.WM_BORDER_WIDTH = 0