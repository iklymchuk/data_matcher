*Set up the virtual env*

```
virtualenv env
source env/bin/activate
```

**1. testing sequence matcher**

```
python matcher/sequence_matcher.py
```

*After typing first word and second we'll see how close they are.*

**2. testing get close matches**

```
python matcher/get_close_matches.py
```

*After typing the word we'll try to find the closest one in the data file and proposing explanation of it.*
