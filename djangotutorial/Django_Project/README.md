

## How to Connect html and css file in Django 

1. Make a folder in your App and name it "static"
2. Make another folder in your App and named it "templates"
3. In templates create all the HTML files and in static creat all the CSS file
4. Include
    {% load static %} -> This should be in very Top of the HTML file 
    <link rel = "stylesheet" href = "{% static 'css_file_name'%}"> -> in the head of header file

## Render of templates
 def name(request):
    return render(request, name.html) -> This should be in views.py file