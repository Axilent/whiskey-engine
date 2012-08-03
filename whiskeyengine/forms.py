from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
import uuid
from django.contrib import auth
from whiskeyengine.models import Drinker, Review
from django.conf import settings
from sharrock.client import HttpClient

c = HttpClient(settings.SAASPIRE_API,'saaspire.triggers','0.1dev',auth_user=settings.SAASPIRE_API_KEY)

class UseMobileForm(forms.Form):
    use_mobile = forms.ChoiceField(choices=(('y', 'y'), ('n', 'n')))

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Drinker
        exclude = ('user', 'shelf', 'registered', 'wishlist', 'pic', 'saaspire_profile')

class UserProfileWithPicForm(forms.ModelForm):
    class Meta:
        model = Drinker
        exclude = ('user', 'registered', 'shelf', 'wishlist', 'saaspire_profile')

class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and password.
    """
    username = forms.RegexField(label=_("Username"), max_length=30, regex=r'^\w+$',
        help_text = _("Required. 30 characters or fewer. Alphanumeric characters only (letters, digits and underscores)."),
        error_message = _("This value must contain only letters, numbers and underscores."))
    password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(_("A user with that username already exists."))

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise forms.ValidationError(_("The two password fields didn't match."))
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class ReviewForm(forms.Form):
    """
    A form to register reviews.
    """
    star = forms.IntegerField()
    review = forms.CharField(widget=forms.Textarea,required=False)
    email = forms.EmailField(required=False)
    
    def create_profile(self,request):
        """
        Creates a new profile.
        """
        drinker = None
        if request.user.is_anonymous():
            user, user_created = User.objects.get_or_create(username=self.cleaned_data['email'])
            
            try:
                drinker = user.get_profile()
            except Drinker.DoesNotExist:
                drinker = Drinker.objects.create(user=user,saaspire_profile=uuid.uuid4().hex)
            
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            auth.login(request,user)
        else:
            drinker = request.user.get_profile()
        
        return drinker
    
    def create_review(self,profile,whiskey):
        """
        Creates a new review.
        """
        star_num = self.cleaned_data['star']
        if star_num >= 4:
            c.trigger(data={'profile':profile.saaspire_profile,
                            'category':'whiskey',
                            'action':'endorsement',
                            'variables':{'whiskey':whiskey.saaspire_key}})
        elif star_num <= 2:
            c.trigger(data={'profile':profile.saaspire_profile,
                            'category':'whiskey',
                            'action':'disendorsement',
                            'variables':{'whiskey':whiskey.saaspire_key}})
        
        return Review.objects.create(reviewer=profile,
                                     whiskey=whiskey,
                                     comments=self.cleaned_data['review'],
                                     rating=self.cleaned_data['star'])
