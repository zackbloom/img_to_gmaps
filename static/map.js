var mine_type_options = {
    getTileUrl: function(coord, zoom){
        var normal_coord = getNormalizedCoord(coord, zoom);
        if (!normal_coord)
            return null;

        var bound = Math.pow(2, zoom);
        return '/static/cart_imgs/' + zoom + 
            '/' + normal_coord.y +
            '/' + normal_coord.x + '.png';
    },
    tileSize: new google.maps.Size(640, 480),
    isPng: true,
    maxZoom: 5,
    minZoom: 0,
    name: "MineWorld"
};

var dayMapType = new google.maps.ImageMapType(mine_type_options);

function initialize(){
    var lat_lng = new google.maps.LatLng(-85, 0);
    var opts = {
        center: lat_lng,
        zoom: 0,
        mapTypeControlOptions: {
            mapTypeIds: ["mine_world_day"]
        }
    };

    map = new google.maps.Map(document.getElementById("map_canvas"), opts);
    map.mapTypes.set('mine_world_day', dayMapType);
    map.setMapTypeId('mine_world_day');
}
// Borrowed from Google Example
// Normalizes the coords that tiles repeat across the x axis (horizontally)
// like the standard Google map tiles.
function getNormalizedCoord(coord, zoom) {
  var y = coord.y;
  var x = coord.x;
    // tile range in one direction range is dependent on zoom level
  // 0 = 1 tile, 1 = 2 tiles, 2 = 4 tiles, 3 = 8 tiles, etc
  var tileRange = 1 << zoom;
    // don't repeat across y-axis (vertically)
  if (y < 0 || y >= tileRange) {
    return null;
  }
    // repeat across x-axis
  if (x < 0 || x >= tileRange) {
    x = (x % tileRange + tileRange) % tileRange;
  }
    return {
    x: x,
    y: y
  };
}
