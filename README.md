# Transit Lens

Created as a Multimedia Scholarship honors thesis for the USC School of Cinematic Arts. Lives at http://transitlens.org

## transitlens.org

In here you'll find the HTML, CSS, and Javascript (conveniently all in one HTML file!) and the geodata & resources used to build the site. Except I didn't include my Mapbox keys so you'll need to add that in for yourself if you want to use this stuff for anything.

## Data scraping and prep

These are the (messy) Python scripts I used to gather the data from Trimet and organize it for use in transitlens.org

I had stuff saved in multiple locations since I was using a mixture of Dropbox, local files, and some stuff on the IML server all together. I haven't done anything to fix the file paths so if you were to use this for anything you'd probably have to change all those things.

### Using these things to get data

You'll need a Trimet API key, from http://developer.trimet.org/. It goes on line 26 of `mainAPIscraper.py`.

1. Set up all the file paths and time/date settings across all the scripts. Some of them cleverly implement constants at the top, some of them lazily implement in-line times. Things will break if they don't match.
2. Run `mainAPIscraper` with `MAIN LOGIC FOR MOST OF THE TIME` active and `TRY TO FILL IN MISSING` commented out. Just let 'er roll for as long as it takes.
3. There will inevitably be some failures, so run `missingChecker` to generate a list of those.
4. Swap which halves of `mainAPIscraper` are commented, and run it again.
5. Repeat 3 & 4 as necessary.
6. Run CSV Compiler over it.

### Then you need other tools

So at this point I used geojson.io and QGIS to burn that CSV usably to geodata. Here's how I did it, in my own words (my at-the-time note to myself so I wouldn't forget):

1. csv durations-3 to geojson with geojson.io
1. export shapefile
1. qgis spatial join to trimmed polygons
1. convert to geojson with mygeodata.eu
1. add var and save a .js
1. use jsonTitleChanger to clean & rename with "-i"
