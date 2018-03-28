from autocomplete.candidate import Candidate
from autocomplete.autocomplete_provider import AutocompleteProvider


### EXAMPLE 1

print('\nExample 1 \n')

# Example passage.
passage = 'The third thing that I need to tell you is that this thing does not \
think thoroughly.'

print('Passage: ' + passage + '\n')

# Inialize AutocompleteProvider.
alg = AutocompleteProvider()

# Train on passage. 
print('Training AutocompleteProvider...')
alg.train(passage)
print('Done.')

# Finding candidate words 
print ('\nAutocomplete candidate of fragment: \'thi\'')
print(alg.getWords('thi'))  
# [thing (2), this (1), third (1), think (1)]

print ('\nAutocomplete candidate of fragment: \'nee\'')
print(alg.getWords('nee'))  
# [need (1)]

print ('\nAutocomplete candidate of fragment: \'th\'')
print(alg.getWords('th'))  
# [thing (2), that (2), this (1), third (1), think (1), the (1), thoroughly (1)]


### EXAMPLE 2

print('\n\nExample 2 \n')

# Passages
passage1 = 'This is passage used as in an example of the AutocompleteProvider \
class.'
passage2 = 'The AutocompleteProvider is used to autocomplete word fragments.'
passage3 = 'This example demonstrates the ability to train online and learn \
from more passages over time.'

print('Passage1: ' + passage1)
print('Passage2: ' + passage2)
print('Passage3: ' + passage3 + '\n')

# Inialize AutocompleteProvider.
alg = AutocompleteProvider()

# Train on passage. 
print('Training AutocompleteProvider...')
alg.train(passage1)
alg.train(passage2)
alg.train(passage3)
print('Done.')

# Finding candidate words 
print ('\nAutocomplete candidate of fragment: \'autocomplete\'')
print(alg.getWords('autocomplete'))  
# [autocompleteprovider (2), autocomplete (1)]

print ('\nAutocomplete candidate of fragment: \'aUtOcOmPlEtEp\'')
print(alg.getWords('aUtOcOmPlEtEp'))  
# [autocompleteprovider (2)]

print ('\nAutocomplete candidate of fragment: \'o\'')
print(alg.getWords('o'))  
# [online (1), over (1), of (1)]


print('\nEnd of examples.')

