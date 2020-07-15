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

Check out `example_*.json` for examples for the various JSON-responses.

#### Responses

##### Currency
```json
{
	"name": "Exalted Orb",
	"image": "exalted-orb.png",
	"drop_level": 35,
	"stack_size": 10,
	"tab_stack_size": 5000,
	"help_text": "Right click this item then left click a rare item to apply it. Rare items can have up to six random modifiers. The item's Catalyst quality increases the chance of applying a modifier which matches the quality type. Removes 20% Quality applied by Catalysts on use.<br>Shift click to unstack."
}
```

#### Divination cards
```json
{
	"name": "A Dab of Ink",
    "stack_size": 9,
    "drop_areas": [
      "The Library",
      "Academy Map",
      "Museum Map",
      "Scriptorium Map"
    ],
	"drop_restrictions": null
}
```


### Current supported scrapers:

[Currency](https://pathofexile.gamepedia.com/Currency)
[Divination cards](https://pathofexile.gamepedia.com/Divination_card)

### License
Licensed under [CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/) as Gamepedia requires.

![[CC BY-NC-SA 3.0]](https://i.creativecommons.org/l/by-nc-sa/3.0/88x31.png)