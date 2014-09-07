This is a script inspired by Smitha Milli in her video ["Web Scraping in Node.js"](http://youtu.be/LJHpm0J688Y) from Youtube. 
In the code, it fetches the home page of site "datafireball" and then crawl the all the articles links, go to their article detail page and then store the raw http response to a file in the format of json

you can install nodejs on a Ubuntu box by run command 

```
sudo apt-get update
sudo apt-get install nodejs
sudo apt-get install npm

npm install cheerio
npn install request

nodejs scraping.js
```
You will see a list of URLs got printed to the standout and there will be a file `result.txt` contain the scraping result.
And you should be good to go.
