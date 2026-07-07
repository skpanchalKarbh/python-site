from django.shortcuts import render, redirect
from django.contrib import messages
from .models import VisionMission, AboutUs, Event, Testimonial, Gallery, ContactMessage, ImpactCounter, Volunteer, TeamMember, Certificate

def home(request):
    vision_mission = VisionMission.objects.first()
    events = Event.objects.filter(is_active=True)[:3]
    
    # Chunk testimonials into groups of 3 for the carousel
    testimonials_qs = list(Testimonial.objects.filter(is_active=True))
    testimonial_chunks = [testimonials_qs[i:i + 3] for i in range(0, len(testimonials_qs), 3)]
    
    counters = ImpactCounter.objects.filter(is_active=True)
    team_members = TeamMember.objects.filter(is_active=True)
    certificates = Certificate.objects.filter(is_active=True)
    context = {
        'vision_mission': vision_mission,
        'events': events,
        'testimonial_chunks': testimonial_chunks,
        'counters': counters,
        'team_members': team_members,
        'certificates': certificates,
    }
    return render(request, 'main/home.html', context)

def about(request):
    about_info = AboutUs.objects.first()
    team_members = TeamMember.objects.filter(is_active=True)
    certificates = Certificate.objects.filter(is_active=True)
    context = {
        'about': about_info,
        'team_members': team_members,
        'certificates': certificates,
    }
    return render(request, 'main/about.html', context)

def events(request):
    events = Event.objects.filter(is_active=True)
    context = {'events': events}
    return render(request, 'main/events.html', context)

def gallery(request):
    images = Gallery.objects.filter(is_active=True)
    context = {'images': images}
    return render(request, 'main/gallery.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        ContactMessage.objects.create(
            name=name, email=email, phone=phone, message=message
        )
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('main:contact')
        
    return render(request, 'main/contact.html')

def join_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        profession = request.POST.get('profession')
        message = request.POST.get('message')
        
        Volunteer.objects.create(
            name=name, email=email, phone=phone, 
            profession=profession, message=message
        )
        messages.success(request, 'Thank you! Your application has been submitted successfully. Our team will contact you soon.')
        return redirect('main:join_us')
        
    return render(request, 'main/join_us.html')
