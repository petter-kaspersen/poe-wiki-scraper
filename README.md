# Path of Exile wiki scraper

Simple to use Path of Exile wiki scraper utilizing Scrapy

## Usage
1) `pip install -r requirements.txt`
2) `python3 run.py`

Data (json and images) are then saved under the `data` folder in the root directory.

The folder structure is: 

```
{scraper_name}.json
{scraper_name}/
	{item_name}.png
	{item_name}.png
```

You can find an example in the `example_response.json` file for how the .json file looks.

### Current supported scrapers:

[Currency](https://pathofexile.gamepedia.com/Currency)

### License
Licensed under [CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/) as Gamepedia requires.

![[CC BY-NC-SA 3.0]](https://i.creativecommons.org/l/by-nc-sa/3.0/88x31.png)