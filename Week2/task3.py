sampleDictionary = [
    {'make': ' Google ', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

sortedDictionary = sorted(sampleDictionary, key=lambda x: int(x['model']))

print(sortedDictionary)
