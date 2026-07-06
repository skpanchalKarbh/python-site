from django.db import models

class VisionMission(models.Model):
    vision = models.TextField(help_text="Enter the Vision statement for the home page.", default="To build a fearless and empowered community of journalists where truth prevails, and every voice is heard and protected across the nation.")
    mission = models.TextField(help_text="Enter the Mission statement for the home page.", default="We are dedicated to safeguarding the rights of the press, providing essential support to media professionals, and promoting ethical, unbiased journalism for a stronger democracy.")

    class Meta:
        verbose_name = "Vision & Mission"
        verbose_name_plural = "Vision & Mission"

    def __str__(self):
        return "Website Vision and Mission"

class AboutUs(models.Model):
    title = models.CharField(max_length=200, default="About Us")
    description = models.TextField()
    image = models.ImageField(upload_to='about/')

    def __str__(self):
        return self.title

class Event(models.Model):
    EVENT_TYPES = (
        ('NATIONAL', 'National'),
        ('INTERNATIONAL', 'International'),
        ('UNESCO', 'UNESCO'),
        ('OTHER', 'Other'),
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='events/')
    date = models.DateField(blank=True, null=True)
    event_type = models.CharField(max_length=50, choices=EVENT_TYPES, default='OTHER')
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date', '-id']

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    author = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True, help_text="e.g. Member, Partner, UNESCO Representative")
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True, help_text="Optional: Photo of the person")
    quote = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.author} - {self.role}"

class Gallery(models.Model):
    caption = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='gallery/')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Galleries"

    def __str__(self):
        return self.caption if self.caption else f"Gallery Image {self.id}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name} - {self.email}"

class ImpactCounter(models.Model):
    title = models.CharField(max_length=100, help_text="e.g. Active Members, Events Organized")
    count = models.IntegerField(default=0, help_text="Target number to count up to")
    icon_class = models.CharField(max_length=100, default="bi-people-fill", help_text="Bootstrap Icon class, e.g. bi-people-fill, bi-calendar-check-fill")
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.title} ({self.count})"

class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    profession = models.CharField(max_length=100, blank=True)
    message = models.TextField(help_text="Why do you want to join?")
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Volunteer: {self.name} - {self.email}"
