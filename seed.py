#!/usr/bin/env python3

import csv
from models import db, Occupation, Group, Guest
from app import create_app  # Import the app instance

# Create the app instance and initialize the database
app = create_app()
db.init_app(app)

def seed_database(file_path):
    with app.app_context():
        # Open the CSV file for reading
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                # Create or get Occupation
                occupation_name = row['GoogleKnowledge_Occupation'].strip()
                occupation = Occupation.query.filter_by(name=occupation_name).first()
                if not occupation:
                    occupation = Occupation(name=occupation_name)
                    db.session.add(occupation)
                
                # Create or get Group
                group_name = row['Group'].strip()
                group = Group.query.filter_by(name=group_name).first()
                if not group:
                    group = Group(name=group_name)
                    db.session.add(group)
                
                # Add Guest
                guest = Guest(
                    name=row['Raw_Guest_List'].strip(),
                    show_date=row['Show'].strip(),
                    year=int(row['YEAR'].strip()),
                    occupation=occupation,
                    group=group
                )
                
                db.session.add(guest)

            # Commit all changes to the database
            db.session.commit()
            print("Database seeded successfully.")

# Run the script
if __name__ == "__main__":
    seed_database("path/to/seed.csv")  # Update with your actual CSV file path
