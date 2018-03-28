# autocomplete_algorithm

This is my solution to the _Mobile Device Keyboard_ programming challenge.

## Problem Summary

The following is taken directly from the code challenge instructions:

We are developing a keyboard autocomplete algorithm to be used in various mobile devices. This algorithm will analyze the passages typed by the user in order to suggest a set of candidate autocomplete words given a word fragment.

We need you to write the algorithm that will learn the words typed by the user over time and then determine a ranked list of autocomplete candidates given a word fragment (you should ignore capitalization when providing suggestions). The algorithm will be trained in an online manner, meaning that additional training passages can be submitted and incorporated into the algorithm at the same time as the algorithm is being used to provide autocomplete suggestions. Ideally, the accuracy of the algorithm will improve over time as more and more training passages are incorporated. Due to the deployment environment for this algorithm, efficiency is critical. The data structure utilized by your algorithm should be optimized for space and time.


## About the Algorithm

This autocomplete algorithm memorizes a word by storing each letter and the number of occurences in nested dictionaries. Each letter in the word is a dictionary key to both the next letter and occurance count of the key letter. This allows for fast word candidate generation and minimzes the memory space required.


## How To Use

### Programming Language

Code was developed using Python 2.7.10. Thus, it is recommended to run code using Python 2.7. 

### Imports

Import the `Candidate` and `AutocompleteProvider` with:

```
from autocomplete.candidate import Candidate
from autocomplete.autocomplete_provider import AutocompleteProvider
```

### Running .py files

It is recommended to run .py files with the Python module option using the command

`python -m <file>`

to ensure imports function properly.

#### Running `example.py`

Run the example file using the command

`python -m example`

in the top directory. 

## Unit Tests

Run the `AutocompleteProvider` unit tests and the `Candidate` unit test using the commands

`python -m autocomplete.tests.autocomplete_provider_test`

and

`python -m autocomplete.tests.candidate_test`

respecively, at the top directory. 


