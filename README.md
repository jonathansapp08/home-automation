# Home Automation

As someone who has leaned into the world of smart devices, I have found it frustrating to have an app for every appliance. Limiting control to just my phone means others can't exercise control and if I lose my phone it's all over. My goal is to create a solution that solves these issues (while providing some extra fetures along the way).

This is largely meant to be a learning opportunity for me. The solution will be specific for my use cases, but feel free to take what works for you.

## Features

### Todo List
The todo list is made using shelve. For shelve documentation see:
[Shelve Documentation](https://docs.python.org/3/library/shelve.html)

### Roku
For a full list of actions see:
[Roku API Documentation](https://developer.roku.com/docs/developer-program/debugging/external-control-api.md)

### Hue Lights
For a full list of actions see:
[Hue API Documentation](https://developers.meethue.com/develop/hue-api/)

## Instructions

1. Install Flask
```
pip install Flask
```

2. Export the necessary info for the app 

```
export roku_ip='<ROKU IP>'
export hue_ip='<HUE IP>'
export hue_username='<HUE USERNAME>'
```

3. Run the Flask app
```
python main.py
```
