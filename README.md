# random_genre_at_once

![random_genre_at_once](res/random_genre_at_once.svg)
Random genre chooser, made to explore new music at your own pace.

## Dependencies

Python 3.x, tested on 3.11.

```bash
pip install requests
pip install bs4
```

If `pip install` doesn't work, try `python -m pip install` or even `python3 -m pip install`.

## Execution

Run `main.py`. It should print a random genre like this: `Your randomly chosen genre is: neoperreo` (yes that's a genre (not a bug (i hope))).

## Project

- [x] basic utility for printing
- [ ] update genre list without interfering with own progress
- [ ] refactor code
- [ ] user settings
- [ ] tracking genre progress

## Aknowledgements

Of course this random genre chooser uses Glenn McDonald's '[Every Noise At Once](https://everynoise.com/)' to get its list of genres.
To get to this list I copied code of [coco-zxc](https://github.com/coco-zxc)'s [charting-sounds](https://github.com/coco-zxc/charting-sounds) for my ./bin/get_genres get_genre_list_base() function.