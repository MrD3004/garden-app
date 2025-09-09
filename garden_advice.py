# Hardcoded values for the season and plant type
season = "summer"  # TODO: Replace with input() to allow user interaction.
plant_type = "flower"  # TODO: Replace with input() to allow user interaction.

# Variable to hold gardening advice
advice = ""

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

"""
garden_advice.py

A simple gardening advice tool that provides seasonal and plant-specific tips
based on user input. Designed for modularity and future feature expansion.
"""

def get_season_advice(season):
    """
    Returns gardening advice based on the season.
    Supported seasons: summer, winter, spring, autumn.
    """
    season_advice = {
        "summer": "Water your plants regularly and provide some shade.",
        "winter": "Protect your plants from frost with covers.",
        "spring": "Start planting herbs and early vegetables.",
        "autumn": "Prepare soil for winter crops."
    }
    return season_advice.get(season, "No advice for this season.")

def get_plant_advice(plant_type):
    """
    Returns gardening advice based on the plant type.
    Supported types: flower, vegetable, herb.
    """
    plant_advice = {
        "flower": "Use fertiliser to encourage blooms.",
        "vegetable": "Keep an eye out for pests!",
        "herb": "Harvest regularly to promote growth."
    }
    return plant_advice.get(plant_type, "No advice for this type of plant.")

def main():
    """
    Main function to collect user input and display gardening advice.
    """
    # Collect user input
    season = input("Enter the season (e.g., summer, winter, spring, autumn): ").lower()
    plant_type = input("Enter the plant type (e.g., flower, vegetable, herb): ").lower()

    # Generate advice
    advice = get_season_advice(season) + "\n" + get_plant_advice(plant_type)

    # Display the advice
    print("\n🌱 Gardening Advice 🌱")
    print(advice)

if __name__ == "__main__":
    main()