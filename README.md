# fl4gotv

Amendment 4 restored the right to vote for an estimated 1.4 to 1.7 million ex-felons who completed all terms of sentence in Florida. `fl4gotv` is a data scraper to help grassroots voter registration organizers parse empirical data to strategically coordinate outreach and engage with unregistered eligible A4 voters by county. Information extracted include A4 eligible voter count, FL county name, and party vote share per county. 

## Requirements

```
Python 3.5.1+
Works on Linux, Windows, macOS
```

## Build

Use `virtualenv` for development via `sudo`:

```
$ sudo easy_install pip
$ sudo pip install virtualenv
$ sudo pip install virtualenvwrapper
```

Create one for this project:

```
$ mkvirtualenv fl4gotv
```

Install dependencies once `virtualenv` is activated:

```
$ pip install -r requirements.txt
```

### Collecting Data

Run script:

```
$ python scrape.py
```

## Credits

2020 FL Primary data provided by [MEDSL](https://electionlab.mit.edu/), [OpenElections Project](https://github.com/openelections), and [Amendment 4](https://dos.elections.myflorida.com/initiatives/initdetail.asp?account=64388&seqnum=1)