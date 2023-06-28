odoo.define("g2p_theme.g2p_logo", function (require) {
    var Widget = require("web.Widget");

    var CustomLogoWidget = Widget.extend({
        start: function () {
            this._super.apply(this, arguments);

            var $logoImage = $("<img>", {
                class: "g2p-logo",
                src: "/g2p_theme/static/src/img/openg2p-black.png",
                alt: "G2P Logo",
            });

            var $customDiv = $("<div>", {
                class: "custom-logo-element",
            });

            $customDiv.prepend($logoImage);
            $(document.body).prepend($customDiv);
        },
    });

    $(document).ready(function () {
        var widget = new CustomLogoWidget();
        widget.appendTo(document.body);
    });

    return CustomLogoWidget;
});
