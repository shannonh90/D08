#!/usr/bin/env python3
# HW08_ch11_ex02c.py
# (1) Modify reverse_lookup_old so that it builds and returns a list of all
# keys that map to v, or an empty list if there are none.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Do not edit what is in main(). It should print what is returned, a list
# of the keys that map to the values passed.
###############################################################################
# Imports


#Body
def reverse_lookup_old(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise ValueError


def reverse_lookup_new(d, v):
	key_list = []

	for key in d:
		if d[key] == v:
			key_list.append(key)

	return key_list


###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
pledge_histogram = {}

def histogram_old(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def histogram_new(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1 #the value = the existing value + 1
    return d


def get_pledge_list():
    """ Opens pledge.txt and converts to a list, each item is a word in
    the order it appears in the original file. returns the list.
    """
    pass
    with open("pledge.txt", "r") as pledge:
        pledge_string = pledge.read()   #reads pledge, returns as string
        pledge_list = pledge_string.split()  #returns a list of words in a string
    return pledge_list

###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a ABOVE: ###########################
###############################################################################
def main():   # DO NOT CHANGE BELOW

	pledge_histogram = histogram_new(get_pledge_list())
	print(reverse_lookup_new(pledge_histogram, 1))
	print(reverse_lookup_new(pledge_histogram, 9))
	print(reverse_lookup_new(pledge_histogram, "Python"))

if __name__ == '__main__':
    main()
