def reverse(str):
    result = ''
    for symbol in str:
        result = symbol + result
    return result

print(reverse('Hello'))