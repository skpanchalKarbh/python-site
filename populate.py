import os
import django
from datetime import date, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from main.models import Event, AboutUs, Testimonial

def populate():
    print("Populating database with realistic data for Patrakaar Ekta Foundation...")

    # 1. About Us
    if not AboutUs.objects.exists():
        AboutUs.objects.create(
            title="About Patrakaar Ekta Foundation",
            description="""Patrakaar Ekta Foundation is a leading non-profit organization dedicated to the welfare, unity, and empowerment of journalists and media professionals across India. 

Our mission is to safeguard the rights of the press, provide financial and legal aid to journalists in need, and promote ethical and unbiased journalism. We believe that a free and fair press is the pillar of a healthy democracy.

Through various workshops, national seminars, and cultural programs, we strive to bridge the gap between media houses and independent reporters, ensuring that every voice is heard and protected. Join us in our journey to uphold the integrity of journalism!""",
            image=""
        )
        print("Created AboutUs data.")

    # 2. Events
    events_data = [
        {
            "title": "National Media Ethics Conclave 2026",
            "description": "A massive gathering of senior editors and ground reporters to discuss the future of digital journalism and media ethics in the era of AI. Guest speakers include prominent news anchors and social activists.",
            "event_type": "NATIONAL",
            "days_offset": -5
        },
        {
            "title": "Journalists Welfare Fundraiser",
            "description": "A charity event organized to raise funds for the medical and legal assistance of independent journalists facing hardships in rural areas. Featuring live cultural performances and award distributions.",
            "event_type": "OTHER",
            "days_offset": -15
        },
        {
            "title": "International Press Freedom Summit",
            "description": "In collaboration with global media watchdogs, this summit addressed the rising challenges to press freedom in South Asia. Over 500 delegates from 12 countries participated.",
            "event_type": "INTERNATIONAL",
            "days_offset": -30
        },
        {
            "title": "UNESCO Heritage & Media Workshop",
            "description": "A special workshop conducted in association with UNESCO to train local journalists on how to report and document endangered cultural heritage sites effectively.",
            "event_type": "UNESCO",
            "days_offset": -45
        },
        {
            "title": "Digital Security Training for Reporters",
            "description": "A hands-on workshop teaching investigative journalists how to secure their digital footprint, protect their sources, and safely use encrypted communication tools.",
            "event_type": "NATIONAL",
            "days_offset": -60
        },
        {
            "title": "Annual Excellence in Journalism Awards",
            "description": "Honoring the brave and fearless journalists who have brought the truth to light against all odds. Awards were distributed across 15 different categories including investigative, sports, and rural reporting.",
            "event_type": "NATIONAL",
            "days_offset": -90
        }
    ]

    for ed in events_data:
        event, created = Event.objects.get_or_create(
            title=ed['title'],
            defaults={
                'description': ed['description'],
                'event_type': ed['event_type'],
                'date': date.today() + timedelta(days=ed['days_offset']),
                'image': ''
            }
        )
        if created:
            print(f"Created Event: {event.title}")

    # 3. Testimonials
    testimonials = [
        {"author": "Rajat Sharma", "role": "Senior Editor", "quote": "Patrakaar Ekta Foundation has been a beacon of hope for independent reporters across the state."},
        {"author": "Arundhati Roy", "role": "Author & Activist", "quote": "Their work in protecting press freedom and supporting rural journalists is truly commendable and necessary for our democracy."},
        {"author": "UNESCO Rep", "role": "Cultural Partner", "quote": "We are proud to partner with this foundation to bring global reporting standards to local journalism."}
    ]

    for t in testimonials:
        Testimonial.objects.get_or_create(
            author=t['author'],
            defaults={'role': t['role'], 'quote': t['quote']}
        )
    
    print("Data population complete!")

if __name__ == '__main__':
    populate()
