var request = require("request");
var cheerio = require("cheerio");


request('http://www.afa.com.ar/deposito/html/v3/index.html?channel=deportes.futbol.primeraa.414158&lang=es_LA', function (error, response, html) {
  if (!error && response.statusCode == 200) {
    console.log(html);
  }
});
