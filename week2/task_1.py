# input: apple candy grapes banana
# output: I have apple, candy, grapes, banana in my shopping cart.

words = input().split()  # sequence - container & flat
formatted_sentence = 'I have {objects} in my shopping cart.'
results = ', '.join(words)
print(
    # 'I have' + results + 'in my shopping cart.'
    # f'I have {results} in my shopping cart.'
    formatted_sentence.format(objects=results)
)
