""" Objective:
Tally the discount totals for each team.
The output format should match the input format: List[Dict]

For this we'll use a generator expression inside a dictionary comprehension
inside a list comprehension. """

teams = [
    {"TeamId": 1, "Name": "Awakened"},
    {"TeamId": 2, "Name": "Symphony of Blades"},
    {"TeamId": 3, "Name": "Team Cupcake"},
]
discounts = [
    {'TeamId': 2, 'Discount': 1.00},
    {'TeamId': 3, 'Discount': 2.50},
    {'TeamId': 1, 'Discount': 0.25},
    {'TeamId': 3, 'Discount': 8.00},
    {'TeamId': 1, 'Discount': 5.00},
]

print("Team Discount Totals")
team_discounts = [{
    "TeamId": team["TeamId"],
    "Name": team["Name"],
    "Discount": sum(
        discount["Discount"] for discount in discounts
        if discount["TeamId"] == team["TeamId"]
    )
} for team in teams]
print(team_discounts)
