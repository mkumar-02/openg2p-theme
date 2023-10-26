{
    "name": "OpenG2P Theme",
    "category": "G2P",
    "version": "15.0.1.2.0",
    "sequence": 1,
    "author": "OpenG2P",
    "website": "https://openg2p.org",
    "license": "Other OSI approved licence",
    "depends": ["base", "web", "auth_signup"],
    "development_status": "Alpha",
    "data": [
        "data/res_company_data.xml",
        "templates/g2p_login_page.xml",
        "templates/g2p_reset_password.xml",
    ],
    "assets": {
        "web.assets_backend": [
            # "g2p_theme/static/src/scss/assets_menu.scss",
            "g2p_theme/static/src/js/g2p_window_title.js",
            "g2p_theme/static/src/css/style.css",
            "g2p_theme/static/src/js/g2p_logo.js",
        ],
        "web.assets_frontend": [
            "g2p_theme/static/src/scss/new_login_page.scss",
        ],
        "web.assets_qweb": [],
    },
    "demo": [],
    "images": [],
    "application": True,
    "installable": True,
    "auto_install": False,
}
