#creo una dictionary con key: city e la value: tutte
# le città connesse con la città chiave
# in questo modo ho modellato l'environment
streets = {
    'Andria': ['Corato', 'Trani'],
    'Corato': ['Ruvo', 'Trani', 'Andria'],
    'Altamura': ['Corato', 'Ruvo', 'Modugno'],
    'Ruvo': ['Corato', 'Ruvo', 'Modugno'],
    'Terlizzi': ['Ruvo', 'Molfetta', 'Bitonto'],
    'Bisceglie': ['Trani', 'Ruvo', 'Molfetta'],
    'Trani': ['Andria', 'Corato', 'Bisceglie'],
    'Molfetta': ['Bisceglie', 'Giovinazzo', 'Terlizzi'],
    'Giovinazzo': ['Molfetta', 'Modugno', 'Bari', 'Bitonto'],
    'Bitonto': ['Modugno', 'Giovinazzo', 'Terlizzi'],
    'Modugno': ['Bitonto', 'Giovinazzo', 'Bari', 'Altamura'],
    'Bari': ['Modugno', 'Giovinazzo'],
}