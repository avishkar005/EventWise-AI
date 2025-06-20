# event_planner.py

mock_vendors = [
    {"name": "Royal Banquet", "type": "Venue", "location": "Pune", "price": 40000, "rating": 4.5},
    {"name": "Elite Catering", "type": "Catering", "location": "Pune", "price": 30000, "rating": 4.7},
    {"name": "Flora Decor", "type": "Decoration", "location": "Pune", "price": 20000, "rating": 4.4},
    {"name": "SnapIt Studio", "type": "Photography", "location": "Pune", "price": 15000, "rating": 4.8},

    {"name": "Sunshine Banquet", "type": "Venue", "location": "Mumbai", "price": 50000, "rating": 4.3},
    {"name": "Tasty Bites", "type": "Catering", "location": "Mumbai", "price": 35000, "rating": 4.6},
    {"name": "EventLights", "type": "Decoration", "location": "Mumbai", "price": 25000, "rating": 4.1},
    {"name": "PixelSnap", "type": "Photography", "location": "Mumbai", "price": 18000, "rating": 4.7}
]

def recommend_vendors(event_type, location, budget):
    services = ["Venue", "Catering", "Decoration", "Photography"]
    recommendations = {}
    budget_split = budget / len(services)  # Equal split among services

    for service in services:
        options = [v for v in mock_vendors if v['type'] == service and v['location'].lower() == location.lower()]
        filtered = [v for v in options if v['price'] <= budget_split]

        if filtered:
            best = sorted(filtered, key=lambda x: x['rating'], reverse=True)[0]
        elif options:
            best = sorted(options, key=lambda x: x['price'])[0]  # Pick cheapest if over budget
        else:
            best = {"name": "No vendor available", "type": service}

        recommendations[service] = best
    return recommendations

def get_planning_steps():
    return [
        "Step 1: Finalize the date and location",
        "Step 2: Book the venue",
        "Step 3: Confirm catering and decoration",
        "Step 4: Hire a photographer",
        "Step 5: Send invitations",
        "Step 6: Setup and rehearse event day flow"
    ]

def main():
    event_type = "Wedding"
    location = "Pune"
    budget = 100000

    print("\n📌 Recommended Vendors:")
    recs = recommend_vendors(event_type, location, budget)
    for service, vendor in recs.items():
        print(f"{service}: {vendor['name']} - ₹{vendor.get('price', 'N/A')} | Rating: {vendor.get('rating', 'N/A')}")

    print("\n📋 Planning Steps:")
    steps = get_planning_steps()
    for step in steps:
        print(step)

if __name__ == "__main__":
    main()
