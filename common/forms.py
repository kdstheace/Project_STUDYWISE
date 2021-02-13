from django import forms
from django.utils.timezone import timezone
from django.utils.translation import ugettext_lazy as _
from .models import Profile


class SignupForm(forms.Form):
    GENDER_CHOICES = (
        ('M', 'male'),
        ('F', 'female')
    )
    DISCLOSURE = (
        ('T', 'agree'),
        ('F', 'disagree')
    )

    BIRTH_YEAR_CHOICES = [year for year in range(1900, 2022)]
    gender = forms.BooleanField(
        label=_('gender'),
        widget=forms.RadioSelect(attrs={'placeholder': _('gender')}, choices=GENDER_CHOICES),
    )

    birth_date = forms.DateField(
        label=_("birth_date"),
        widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES),
    )
    school = forms.CharField(
        label=_("education"),
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': _('birth_date')}),
    )
    first_name = forms.CharField(
        label=_('first_name'),
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': _('first_name')})
    )
    last_name = forms.CharField(
        label=_('last_name'),
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': _('last_name')})
    )

    address1 = forms.CharField(
        label=_("address1"),
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': _('address1')})
    )
    address2 = forms.CharField(
        label=_("address2"),
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': _('address2')})
    )
    photo = forms.ImageField(
        label=_("photo"),
    )
    self_disclosure = forms.BooleanField(
        label=_("agreement"),
        widget=forms.RadioSelect(attrs={'placeholder': _('agreement')}, choices=DISCLOSURE),
    )

    introduction = forms.CharField(
        label=_("career_info1"),
        max_length=4000,
        required=False,
        widget=forms.Textarea(attrs={'placeholder': _('introduction')}),
    )

    career1 = forms.CharField(
        label=_("career1"),
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': _('career1')}, ),
    )
    career2 = forms.CharField(
        label=_("career2"),
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': _('career2')}, ),
    )
    career3 = forms.CharField(
        label=_("career3"),
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': _('career3')}, ),
    )
    career4 = forms.CharField(
        label=_("career4"),
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': _('career4')}, ),
    )
    career5 = forms.CharField(
        label=_("career5"),
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': _('career5')}, ),
    )

    interest = forms.CharField(
        label=_("interest"),
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': _('interest')}),
    )

    latitude = forms.DecimalField(
        label=_("latitude"),
    )
    longitude = forms.DecimalField(
        label=_("longitude"),
    )

    # 이메일은 기본적으로 되어 있음
    # 이름 기본적으로 있음
    # 성 기본적으로 있음
    # 구글 이메일 기본적으로 있음
    # 구글 제공 사진 기본적으로 있음

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        profile = Profile()
        profile.user = user
        profile.birth_date = self.cleaned_data['birth_date']
        profile.school = self.cleaned_data['school']
        profile.address1 = self.cleaned_data['address1']
        profile.address2 = self.cleaned_data['address2']
        profile.photo = self.cleaned_data['photo']

        profile.self_disclosure = self.cleaned_data['self_disclosure']
        profile.introduction1 = self.cleaned_data['introduction']

        profile.career1 = self.cleaned_data['career1']
        profile.career2 = self.cleaned_data['career2']
        profile.career3 = self.cleaned_data['career3']
        profile.career4 = self.cleaned_data['career4']
        profile.career5 = self.cleaned_data['career5']

        profile.interest1 = self.cleaned_data['interest']

        profile.latitude = self.cleaned_data['latitude']
        profile.longitude = self.cleaned_data['longitude']
        profile.save()