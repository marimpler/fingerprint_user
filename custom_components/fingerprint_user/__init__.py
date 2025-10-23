from homeassistant.components.panel_custom import async_register_panel

DOMAIN = "fingerprint_user"

async def async_setup(hass, config):
    async_register_panel(
        hass,
        webcomponent_name="fingerprint_user-panel",
        frontend_url_path="fingerprint_user",
        html_url="/local/community/fingerprint_user/panel_custom/fingerprint_user.html",
        sidebar_title="Test",
        sidebar_icon="mdi:fingerprint",
        require_admin=False,
    )
    return True
