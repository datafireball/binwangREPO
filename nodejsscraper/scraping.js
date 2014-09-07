var request = require('request'), 
    cheerio = require('cheerio'),
    fs = require('fs')
    links = [];

request('http://datafireball.com', function(err, resp, body){
    if(!err && resp.statusCode == 200){
        var $ = cheerio.load(body);
        $('h1.entry-title').each(function(){
            var link = $(this).find('a').attr('href')
            links.push(link);
        });
        console.log(links);

        for(var i = 0; i < links.length; i++){
              fs.appendFile('result.txt', JSON.stringify(request(links[i])) + '\n', function(err){});
        }
    }
});
