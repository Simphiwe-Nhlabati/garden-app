# Hardcoded values for the season and plant type
# TODO: Replace with input() to allow user interaction.

# Variable to hold gardening advice
advice = {}


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

# Determine advice based on the season
if season == "summer":
    advice += "Water your plants regularly and provide some shade.\n"
elif season == "winter":
    advice += "Protect your plants from frost with covers.\n"
else:
    advice += "No advice for this season.\n"

# Determine advice based on the plant type
if plant_type == "flower":
    advice += "Use fertiliser to encourage blooms."
elif plant_type == "vegetable":
    advice += "Keep an eye out for pests!"
else:
    advice += "No advice for this type of plant."

# Print the generated advice
print(advice)

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
