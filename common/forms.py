from django import forms
from django.utils.timezone import timezone
from django.utils.translation import ugettext_lazy as _
from .models import Profile


class SignupForm(forms.Form):
    GENDER_CHOICES = (
        ('M', '男性'),
        ('F', '女性')
    )
    DISCLOSURE = (
        ('T', '同意'),
        ('F', '拒否')
    )

    BIRTH_YEAR_CHOICES = [year for year in range(1900, 2022)]
    gender = forms.BooleanField(
        label=_('性別'),
        widget=forms.RadioSelect(attrs={'placeholder': _('性別')}, choices=GENDER_CHOICES),
    )
    birth_date = forms.DateField(
        label=_("生年月日"),
        widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES),
    )
    school = forms.CharField(
        label=_("学歴"),
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': _('学歴')}),
    )
    first_name = forms.CharField(
        label=_('名'),
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': _('名')})
    )
    last_name = forms.CharField(
        label=_('名字'),
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': _('名字')})
    )

    address1 = forms.CharField(
        label=_("住所1"),
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': _('住所1')})
    )
    address2 = forms.CharField(
        label=_("住所2"),
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': _('住所2')})
    )
    photo = forms.ImageField(
        label=_("プロフィール"),
    )
    self_disclosure = forms.BooleanField(
        label=_("プライバシー"),
        widget=forms.RadioSelect(attrs={'placeholder': _('プライバシー')}, choices=DISCLOSURE),
    )
    introduction1 = forms.CharField(
        label=_("自己紹介1"),
        max_length=4000,
        required=False,
        widget=forms.Textarea(attrs={'placeholder': _('自己紹介1')}),
    )
    introduction2 = forms.CharField(
        label=_("自己紹介2"),
        max_length=4000,
        required=False,
        widget=forms.Textarea(attrs={'placeholder': _('自己紹介2')}, ),
    )
    introduction3 = forms.CharField(
        label=_("自己紹介3"),
        max_length=4000,
        required=False,
        widget=forms.Textarea(attrs={'placeholder': _('自己紹介3')}, ),
    )
    introduction4 = forms.CharField(
        label=_("自己紹介4"),
        max_length=4000,
        required=False,
        widget=forms.Textarea(attrs={'placeholder': _('自己紹介4')}, ),
    )
    introduction5 = forms.CharField(
        label=_("自己紹介5"),
        max_length=4000,
        required=False,
        widget=forms.Textarea(attrs={'placeholder': _('自己紹介5')}, ),
    )
    career1 = forms.CharField(
        label=_("キャリア1"),
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': _('キャリア1')}, ),
    )
    career2 = forms.CharField(
        label=_("キャリア2"),
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': _('キャリア2')}, ),
    )
    career3 = forms.CharField(
        label=_("キャリア3"),
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': _('キャリア3')}, ),
    )
    career4 = forms.CharField(
        label=_("キャリア4"),
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': _('キャリア4')}, ),
    )
    career5 = forms.CharField(
        label=_("キャリア5"),
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': _('キャリア5')}, ),
    )
    interest1 = forms.CharField(
        label=_("気に入り1"),
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': _('気に入り1')}),
    )
    interest2 = forms.CharField(
        label=_("気に入り2"),
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': _('気に入り2')}, ),
    )
    interest3 = forms.CharField(
        label=_("気に入り2"),
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': _('気に入り3')}, ),
    )
    interest4 = forms.CharField(
        label=_("気に入り2"),
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': _('気に入り4')}, ),
    )
    interest5 = forms.CharField(
        label=_("気に入り2"),
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': _('気に入り5')}, ),
    )

    latitude = forms.DecimalField(
        label=_("緯度"),
    )
    longitude = forms.DecimalField(
        label=_("経度"),
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
        profile.introduction1 = self.cleaned_data['introduction1']
        profile.introduction2 = self.cleaned_data['introduction2']
        profile.introduction3 = self.cleaned_data['introduction3']
        profile.introduction4 = self.cleaned_data['introduction4']
        profile.introduction5 = self.cleaned_data['introduction5']

        profile.career1 = self.cleaned_data['career1']
        profile.career2 = self.cleaned_data['career2']
        profile.career3 = self.cleaned_data['career3']
        profile.career4 = self.cleaned_data['career4']
        profile.career5 = self.cleaned_data['career5']

        profile.interest1 = self.cleaned_data['interest1']
        profile.interest2 = self.cleaned_data['interest2']
        profile.interest3 = self.cleaned_data['interest3']
        profile.interest4 = self.cleaned_data['interest4']
        profile.interest5 = self.cleaned_data['interest5']

        profile.latitude = self.cleaned_data['latitude']
        profile.longitude = self.cleaned_data['longitude']
        profile.save()