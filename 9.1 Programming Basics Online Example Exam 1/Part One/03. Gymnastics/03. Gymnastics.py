dict_grades = {
    'ribbon': {'Russia': [9.1, 9.4], 'Bulgaria': [9.6, 9.4], 'Italy': [9.2, 9.5]},
    'hoop': {'Russia': [9.3, 9.8], 'Bulgaria': [9.55, 9.75], 'Italy': [9.45, 9.35]},
    'rope': {'Russia': [9.6, 9.0], 'Bulgaria': [9.5, 9.4], 'Italy': [9.7, 9.15]},
}

country, device = input(), input()
grade = sum(dict_grades[device][country])
print(f'The team of {country} get {grade:.3f} on {device}.\n{100 - (grade / 20 * 100):.2f}%')

'''
Bulgaria
ribbon
'''
