/*globals define, google*/
define(['jquery', 'underscore'], function ($, _) {
  "use strict";

  var
    _mapsLoaded = $.Deferred(),
    $container = $('#google-map');

  function GoogleMaps() {
    _mapsLoaded.done(_.bind(function () {
      this.init();
    }, this));
  }

  GoogleMaps.prototype.init = function () {
    console.log("maps: GoogleMaps.init");
  };

  GoogleMaps.prototype.createMap = function ($container) {
    console.log("maps: GoogleMaps.createMap");

    var address = $container.data('address');

    _mapsLoaded.done(_.bind(function () {
      // Create the maps object
      var geocoder = new google.maps.Geocoder();

      console.log("maps: geocoding", address);

      geocoder.geocode({'address': address}, function (results, status) {
        if (status === google.maps.GeocoderStatus.OK) {

          var map = new google.maps.Map($container[0], {
              center: new google.maps.LatLng(37.4419, -122.1419),
              zoom: 11,
              mapTypeId: google.maps.MapTypeId.ROADMAP,
              scrollwheel: false
            }),
            marker = new google.maps.Marker({
              map: map,
              position: results[0].geometry.location
            });

          map.setCenter(results[0].geometry.location);
        }
      });
    }, this));

  };

  window.gmapsLoaded = function () {
    console.log("maps: gmapsLoaded");
    delete window.gmapsLoaded;
    _mapsLoaded.resolve();
  };

  function loadMapsAPI() {
    console.log("maps: inserting gmaps script tag");

    var
      js = document.createElement('script'),
      first = document.getElementsByTagName('script')[0];

    js.src = '//maps.googleapis.com/maps/api/js?sensor=false&callback=gmapsLoaded';
    first.parentNode.insertBefore(js, first);
    console.log("maps: inserted gmaps script tag");
  }

  if ($container.length > 0) {
    loadMapsAPI();
    window.gmaps = new GoogleMaps();
    window.gmaps.createMap($container);
  }

});
