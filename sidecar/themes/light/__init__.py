from pyramid_frontend.theme import Theme
from pyramid_frontend.images import FilterChain


class LightTheme(Theme):
    key = 'light'
    require_config_path = '/_light/js/require_config.js'
    require_base_url = '/_light/js/vendor/'

    image_filters = (
        FilterChain(
            'thumb', width=330, height=220, extension='jpg',
            crop=True, quality=80, sharpness=1.5),

        FilterChain(
            'square', width=300, height=300, extension='jpg',
            crop=True, quality=80, sharpness=1.5),

        FilterChain(
            'about', width=400, height=300, extension='jpg',
            quality=80, sharpness=1.5),

        FilterChain(
            'large', width=800, height=600, extension='jpg', resize=True,
            quality=85, sharpness=1.5),

        FilterChain(
            'huge', width=2400, height=500, extension='jpg', quality=90,
            sharpness=1.5),
    )

    assets = {
        'main-less': ('/_light/css/main.less', 'less'),
        'main-js': ('/_light/js/main.js', 'requirejs'),
    }
