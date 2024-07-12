from django.db import models
from ckeditor.fields import RichTextField
#from cloudinary.models import CloudinaryField

class Personal(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    role = models.TextField(max_length=500, blank=True, null=True)
    mini_description = models.TextField(max_length=500, blank=True, null=True)
    cv_description = models.TextField(max_length=500, blank=True, null=True)
    cv_link = models.URLField(blank=True, null=True)
    #photo = CloudinaryField('profile_pic/main')
    photo = models.ImageField(upload_to='profile_pics/main', blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    

    def __str__(self):
        return self.name
    
class About(models.Model):
    description = RichTextField(blank=True, null=True)
    #photo = CloudinaryField('profile_pic/about')
    photo = models.ImageField(upload_to='profile_pics/about', blank=True, null=True)
    
class Education(models.Model):
    school_name = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    start_date = models.CharField(max_length=7)  # Store as string in "MMM YYYY" format
    end_date = models.CharField(max_length=7, null=True, blank=True)  # Store as string in "MMM YYYY" format
    
    @property
    def formatted_start_date(self):
        # Check if the start_date is in the format "MONYYYY"
        if len(self.start_date) == 7:
            month = self.start_date[:3].capitalize()
            year = self.start_date[3:]
            return f"{month} {year}"
        return self.start_date

    @property
    def formatted_end_date(self):
        # Check if the end_date is in the format "MONYYYY"
        if len(self.end_date) == 7:
            month = self.end_date[:3].capitalize()
            year = self.end_date[3:]
            return f"{month} {year}"
        return self.end_date
    
    def __str__(self):
        return self.school_name
    
    class Meta:
        ordering = ['start_date']

    def date_range(self):
        return f"{self.formatted_start_date} - {self.formatted_end_date}"

    def formatted_start_date_as_date(self):
        # Convert the formatted start_date to a date object
        from datetime import datetime
        return datetime.strptime(self.formatted_start_date, "%b %Y")

    def formatted_end_date_as_date(self):
        # Convert the formatted end_date to a date object
        from datetime import datetime
        return datetime.strptime(self.formatted_end_date, "%b %Y")
    
class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.CharField(max_length=7)  # Store as string in "MMM YYYY" format
    end_date = models.CharField(max_length=7, null=True, blank=True)  # Store as string in "MMM YYYY" format
    is_current = models.BooleanField(default=False)
    technologies = models.ManyToManyField('Technology')
    
    @property
    def formatted_start_date(self):
        # Check if the start_date is in the format "MONYYYY"
        if len(self.start_date) == 7:
            month = self.start_date[:3].capitalize()
            year = self.start_date[3:]
            return f"{month} {year}"
        return self.start_date

    @property
    def formatted_end_date(self):
        # Check if the end_date is in the format "MONYYYY"
        if len(self.end_date) == 7:
            month = self.end_date[:3].capitalize()
            year = self.end_date[3:]
            return f"{month} {year}"
        return self.end_date
    
    def __str__(self):
        return self.title

class Description(models.Model):
    text = models.TextField()
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='descriptions')
    order_number = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.text
    
    class Meta:
        unique_together = ('experience', 'order_number')
        
        
class Issuing_Organization(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
        
class Portfolio(models.Model):
    FILTER_CHOICES = [
        ('filter-project', 'Project'),
        ('filter-certification', 'Certification'),
        ('filter-badge', 'Badge'),
    ]

    name = models.CharField(max_length=100)
    filter = models.CharField(max_length=50, choices=FILTER_CHOICES)
    issuer = models.ForeignKey(Issuing_Organization, on_delete=models.CASCADE, null=True, blank=True)
    year = models.CharField(max_length=4, null=True, blank=True)
    object_fit = models.CharField(max_length=100, null=True, blank=True)
    
    
    # def get_cloudinary_folder(self):
    #     if self.filter == 'filter-project':
    #         return 'portfolio/project'
    #     elif self.filter == 'filter-certification':
    #         return 'portfolio/certification'
    #     elif self.filter == 'filter-badge':
    #         return 'portfolio/badge'

    #photo = CloudinaryField(folder=get_cloudinary_folder)
    
    def get_upload_to(self, filename):
        if self.filter == 'filter-project':
            return 'portfolio/project/{}'.format(filename)
        elif self.filter == 'filter-certification':
            return 'portfolio/certification/{}'.format(filename)
        elif self.filter == 'filter-badge':
            return 'portfolio/badge/{}'.format(filename)
        
    photo = models.ImageField(upload_to=get_upload_to, blank=True, null=True)

    link1 = models.URLField(blank=True, null=True)
    link2 = models.URLField(blank=True, null=True)
    link3 = models.URLField(blank=True, null=True)  

    def __str__(self):
        return self.name

# Programming languages and tools
class Technology(models.Model):
    name = models.CharField(max_length=100)
    photo = models.URLField(blank=True, null=True)
    def __str__(self):
        return self.name