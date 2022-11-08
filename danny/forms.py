from django import forms


# Create your models here.
class registration(forms.Form):
    name = forms.CharField(label="Enter Your Name", max_length=11)
    roll_no = forms.CharField(label="Enter Roll No", max_length=10)
    contact_no = forms.IntegerField(label="Contact No")
    # text_field = forms.Textarea()
    url_field = forms.URLField(label="URL field")
