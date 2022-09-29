import os
os.system("clear")

# Task 1
# dictionary = {"key": "value"}
settings = {"title": "My original title"}


def change_site_title(new_title):
    """Change the title of the site."""

    # dictionary["key"] = Value/new_Value
    # 1) can overwrite the former Value with a new Value
    # 2) or can create a new {"key": "value"} pair
    settings["title"] = new_title


# Test cases
# ---------------------------------
print("\n\n------- Task 1 -------")

print("\n# settings before change:")
print(settings)

# change original settings (dict)
change_site_title("A new fancy title")

# print the changed settings (dict)
print("\n# settings after change:")
print(settings)


# Task 2
# ---------------------------------
print("\n\n------- Task 2 -------")

default_settings = {
    "title": "My original title"
}


def get_title(settings=default_settings):
    #            ^            ^
    #      keyword argument   |
    #                    default value
    # default value: here it is the default_settings variable declared above
    # can also be a fixed value e.g. (settings="A boring titel")
    """Get the title of the site."""
    # return settings["title"] -> e.g. "My origanal title"
    return settings['title']


# Test cases

print("\n# get_title(settings): -> settings was changed in task 1")

# by passing a dictionary to this function, nothing is changed,
# just read the "title" of this dict
print(get_title(settings))

# no argument passed, default value is used in function
print("\n# get_title(): -> 'My original title'")
print(get_title())

# now the "title" settings (dict) is changed to the passed string
print("\n# change_site_title('A new fancy title'): -> update settings (dict)")
change_site_title("A new fancy title")


print("\n# get_title(settings): -> udated title in settings (dict)")
print(get_title(settings))

print("\n# get_title(): -> default value from default_settings (dict)")
print(get_title())


# Task 3

print("\n\n------- Task 3 -------")
# a new key-value pair is added
# to settings (dict) and to default_settings (dict)
# the value of key "pages" is an empty list
settings['pages'] = []
default_settings['pages'] = []


def get_pages(settings=default_settings):
    """Return the pages stored in the settings."""
    # return value of key "pages" of every dictonary passed to the function
    # if no dictionary is passed, default value is default_settings (dict)
    return settings['pages']


def add_page(page, settings=default_settings):
    """Add a page to the settings."""
    # by default settings["pages"] is [] -> empty
    # but it could also be already filled with a value
    # by doing something like this: settings["pages"] = page
    # the old value would be overwritten

    # .append() ensures, that the new value doesn't overwrite
    # an already existing value
    settings['pages'].append(page)


# Test cases
# a new value -> new dictionary for key "pages"
home = {"title": "Home", "path": "/"}


print("\n# add_page(home): -> home (dict) as argument to add to default value default_settings (dict)")
add_page(home)

print("\n# get_pages(): -> get updated key 'pages' of settings (dict)")
print(get_pages())

print("\n# get_pages(settings): -> get key 'pages' of settings (dict)")
print(get_pages(settings))

# new value -> new dictionary for key "pages"
about = {"title": "About", "path": "/about/"}
print("\n# add_page(about, settings): -> home as new value for settings (dict)")
add_page(about, settings)


print("\n# get_pages(): -> get 'pages' of default_settings (dict)")
print(get_pages())

print("\n# get_pages(settings): -> get 'pages' of settings (dict)")
print(get_pages(settings))


# Task 4
print("\n\n------- Task 4 -------")


def print_user_profile(gender="female", first=None, last="Doe", pictures=None):
    """Print a summary of a user profile."""
    # its not a good idea to give a keyword argument a mutable value, look at the link below
    # https://florimond.dev/en/posts/2018/08/python-mutable-defaults-are-the-source-of-all-evil/

    # because lists are mutable, the argument, e.g pictures=[] gets remembered,
    # if the function gets called for the second, or more, time.
    # the values, passed befor are still there.

    # for a small introduction of the difference between mutable and unmutable, look into the
    # extra file in this folder: mutable-unmutable-id.py

    # if function is called without pictures argument, the default is None
    # if-statment needs a True condition
    # if pictures=None we cant to assign an empty list
    # but picture=None equals to False
    # so we use "not" to return the complementary of None -> False
    if not pictures:
        pictures = []
    if not first:
        if gender == "female":
            first = "Jane"
        else:
            first = "John"

    # add first element to pictures (list)
    # if list would be pictures=None
    # the following line would throw an error
    pictures.insert(0, "common_header.png")

    print(f"\nThe user {first} {last} has the following pictures:")
    for picture in pictures:
        print(picture)


# Test cases
test_data1 = {
    "gender": "male",
    "last": "Brown",
    "pictures": ["holidays1.png", "easter_grandma.png"]
}
test_data2 = {
    "first": "Alicia",
    "last": "Schmidt"
}
test_data3 = {
    "last": "Korkov",
    "pictures": ["sunset.png"]
}


print_user_profile(**test_data1)
print_user_profile(**test_data2)
print_user_profile(**test_data2)
print_user_profile(**test_data3)
