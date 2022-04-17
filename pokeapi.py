import requests

def get_pokemon_info(pokemon_name):
    """
    Gets All information about a specified Pokemon
    :param name: Pokemon name
    :returns: Dictionary of Pokemon Info, if succesful. None, if not.      
    """

    print("Getting Pokemon information...", end=" ")
    
    URL = 'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(URL + str(pokemon_name))

    if response.status_code == 200:
        print('success')
        return response.json() # Convert response body to a dictionary

    else:
        print('failed. Response code:', response.status_code)
        return