// Common RequireJS config
// Used only in development and for optimization
var require = {
  baseUrl: '/_light/js/vendor',

  paths: {
  },

  shim: {
    underscore: {
      exports: '_',
      init: function () {
         this._.templateSettings = {
          evaluate    : /\{\{(.+?)\}\}/g,
          interpolate : /\{\{=(.+?)\}\}/g,
          escape      : /\{\{-(.+?)\}\}/g,
        };
      }
    },

    'affix': ['jquery'],
    'alert': ['jquery'],
    'button': ['jquery'],
    'carousel': ['jquery'],
    'collapse': ['jquery', 'transition'],
    'dropdown': ['jquery'],
    'modal': ['jquery'],
    'popover': ['jquery', 'tooltip'],
    'scrollspy': ['jquery'],
    'tab': ['jquery'],
    'tooltip': ['jquery'],
    'transition': ['jquery'],
  }
};
