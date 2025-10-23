from homeassistant.components.frontend import async_register_built_in_panel
from homeassistant.core import HomeAssistant

async def async_setup(hass: HomeAssistant, config: dict):
    async_register_built_in_panel(
        hass,
        frontend_url_path="doorbell-fingerprint",
        sidebar_title="Fingerprint",
        sidebar_icon="mdi:fingerprint",
        module_url="/frontend/doorbell-fingerprint/doorbell-fingerprint.js",
        require_admin=True,
    )
    return True
