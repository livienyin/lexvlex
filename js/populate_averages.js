$.getJSON('data/city_average.json', function(data) {
  for (var average in data) {
    $('#' + average + '_avg').html(data[average]);
  }
});
