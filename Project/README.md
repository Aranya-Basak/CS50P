# 🚀Space Mission Tracker🚀
#### Video Demo:  <URL HERE>
##
### Description:

A command-line application that tracks upcoming space launches using data from [The Space Devs API](https://thespacedevs.com/). Users can view launch schedules, filter by agency or country, and even track countdowns to the next mission.

#### project.py file:

This file contains the source code for the project. In this file there are 13 custom functions and a main function. The `fetch_launches()` function calls the API to fetch the launch data, the `save_launches_offline()` funtion caches the acquired data in a save file named `launches.json`. These 2 function ensures that when the user has internet it can fetch and save the upcoming launch data which can later be used when the user may not have internet through `load_launches_offline()` function.

`main()` function starts the app and loads the menu by calling `show_menu()` function and checks which option the user selected. All other functions are used for different features.
This app has the ability to save favorite agencies while using it. It can't save in the permanent storage.

Funtion list:
1. Show upcoming launches: `show_upcoming_launches(launches)`
2. Filter launches by agency: `filter_launches_by_agency(launches)`
3. Search launches by date: `search_launches_by_date(launches)`
4. Countdown to next launch: `countdown_to_next_launch(launches)`
5. Sort launches by date: `sort_launches_by_date(launches)`
6. Add favorite agency: `add_favorite_agency()`
7. Show launches from favorites: `show_launches_from_favorites(launches)`
8. Filter launches by country: `filter_launches_by_country(launches)`
9. Random launch of the day: `random_launch_of_the_day(launches)`

> #### Requirements:

>> For executing this file there are some third party libraries required:

>>> + requests
>>> + colorama
>>> + tabulate


#### test_project.py file:

This file contains all the test executable using pytest module. it uses `patch`, `mock_open`, `Mock` from `unittest.mock` to execute majority of the tests. It uses a mock API response `sample_launches` to do nearly every test.

> #### Requirements:

>> + pytest

Furthermore, `project.py` & `test_project.py` was stylized by `black` module.

##
### Licence:

This project is the final project for my CS50P course. It should be used for educational purposes only.

##
### Acknowledgements:

+ [The Space Devs API](https://thespacedevs.com/) for their free and rich space data API.

##
### Planned Features:

+ GUI to bring simplicity
+ Alert system through sending email

##
### About Me:
Name: Aranya Basak

Email: basakaranya05@gmail.com

Dhaka, Bangladesh
