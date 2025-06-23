# Variable to hold gardening advice
# A dictionary for holding the season advice
advice_season = {
    "summer": "Water your plants regularly and provide some shade.\n",
    "winter": "Protect your plants from frost with covers.\n" 
}

# A dictionary for holding the plant advice
advice_plants = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!"
}


def info_from_user():
    """Prompt the user to enter the season and plant type.

    Returns:
        season: _description_
        plant_type: _description_
    """
    season = input("Make a selection between summer or winter: ").strip().lower()
    plant_type = input("Make a selection between flower or vegetable: ").strip().lower()
    return season, plant_type


def recommendations_seasons(season, plant_type):
    """Provides gardening advice based on season and plant type.

    Returns:
        advice: Gets it from the user via input then provides recommended advice
    """
    advice = ""
    advice += advice_season.get(season, "No advice for this season.\n")
    advice += advice_plants.get(plant_type, "No advice for this type of plant.")
    return advice
