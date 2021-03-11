from django.shortcuts import render

def home(request):
    return render(request, 'eduwebapp/index.html')

def about(request):
    return render(request, 'eduwebapp/about.html')

def blog(request):
    return render(request, 'eduwebapp/blog.html')

def contact(request):
    return render(request, 'eduwebapp/contact.html')

def blogsingle(request):
    return render(request, 'eduwebapp/blog-single.html')

def pricing(request):
    return render(request, 'eduwebapp/pricing.html')

def coursegrid2(request):
    return render(request, 'eduwebapp/course-grid-2.html')

def coursegrid3(request):
    return render(request, 'eduwebapp/course-grid-3.html')

def coursegrid4(request):
    return render(request, 'eduwebapp/course-grid-4.html')

def teachers(request):
    return render(request, 'eduwebapp/teachers.html')