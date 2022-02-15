planet = {
    'name': 'Earth',
    'moons': 1
}


print(planet.get('name'))
print(planet['name'])

wibble = planet.get('wibble') # Regresa None
print(wibble)
# wibble = planet['wibble'] # Arroja un KeyError
# print(wibble)

planet.update({'name': 'Makemake'})
print(planet.get('name'))
planet['name'] = 'Makemake2'
print(planet.get('name'))

# Usando update
planet.update({
    'name': 'Earth',
    'moons': 1
})
print(planet)
# Usando corchetes
planet['name'] = 'Jupiter'
planet['moons'] = 79
print(planet)

planet['orbital period'] = 4333
print(planet)
planet.pop('orbital period')
print(planet)

# Añadimos los datos
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}
print(planet)

print(f"{planet['name']} polar diameter: {planet['diameter (km)']['polar']}")

rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')


# Si, 'december' existe en rainfall
if 'december' in rainfall:
    # rainfall [en la posición december] es igual a
    # rainfall [en la posición december] + 1 (2.1+1)
    rainfall['december'] = rainfall['december'] + 1
# Si no:
else:
    # rainfall [en la posición december] es igual a 1
    rainfall['december'] = 1 
print(rainfall)

# Si, 'september' existe en rainfall
if 'september' in rainfall:
    rainfall['september'] = rainfall['september'] + 1

else:
    rainfall['september'] = 1
print(rainfall)
rainfall.pop('september')

#Total de precipitaciones 0
total_rainfall = 0

# Para cada valor en los valores de rainfall
for value in rainfall.values():    
    # El total de las precipitaciones será igual a ese mismo + el valor que se está iterando
    total_rainfall = total_rainfall + value

# Muestra 'Hay un total de precipitaciones (el valor total) en centímetros en el último cuarto (haciendo referencia al cuarto del año)
print(f'There was {total_rainfall}cm in the last quarter')
