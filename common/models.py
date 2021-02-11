from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import User

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

'''
class MemInfo(models.Model):
    mem_id = models.AutoField(primary_key=True),
    mem_google = models.CharField(max_length=100, null=False, unique=True),
    mem_nickname = models.CharField(max_length=20, null=False, unique=True),
    mem_gender = models.BooleanField(null=False),
    mem_birthday = models.DateTimeField(null=False),
    mem_school = models.CharField(max_length=50),
    mem_address1 = models.CharField(max_length=100, null=False),
    mem_address2 = models.CharField(max_length=100, null=False),
    mem_email = models.EmailField(null=False),
    mem_register_datetime = models.DateTimeField(null=False, auto_now_add=True),
    mem_lastlogin_datetime = models.DateTimeField(null=False, auto_now=True),
    mem_photo = models.ImageField(),
    mem_email_cert = models.BooleanField(null=False),
    mem_receive_email = models.BooleanField(null=False),
    mem_open_profile = models.BooleanField(null=False),
    mem_is_admin = models.BooleanField(null=False),
    mem_introduction_1 = models.CharField(max_length=250),
    mem_introduction_2 = models.CharField(max_length=250),
    mem_introduction_3 = models.CharField(max_length=250),
    mem_introduction_4 = models.CharField(max_length=250),
    mem_introduction_5 = models.CharField(max_length=250),
    mem_career_1 = models.CharField(max_length=250),
    mem_career_2 = models.CharField(max_length=250),
    mem_career_3 = models.CharField(max_length=250),
    mem_career_4 = models.CharField(max_length=250),
    mem_career_5 = models.CharField(max_length=250),
    mem_attend_apply_count = models.IntegerField(null=False, default=0),
    mem_attend_actual_count = models.IntegerField(null=False, default=0),
    mem_google_first_name = models.CharField(max_length=250),
    mem_google_last_name = models.CharField(max_length=250),
    mem_google_email = models.EmailField(),
    mem_google_photo = models.ImageField(),
    mem_current_latitude = models.IntegerField(),
    mem_current_longitude = models.IntegerField()

class Category(models.Model):
    category_id = models.AutoField(primary_key=True),
    category_largy = models.CharField(max_length=50, null=False),
    category_small = models.CharField(max_length=50, null=False)

class MemberCategory(models.Model):
    member_category_id = models.AutoField(primary_key=True),
    mem_id = models.ForeignKey(MemInfo, on_delete=models.CASCADE),
    category_id = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

class GroupInfo(models.Model):
    group_id = models.AutoField(primary_key=True),
    mem_id = models.ForeignKey(MemInfo, on_delete=models.CASCADE),
    category_id = models.ForeignKey(Category, on_delete=models.DO_NOTHING),
    group_title = models.CharField(max_length=50, null=False),
    group_generate = models.DateTimeField(null=False, auto_created=True),
    group_is_class = models.BooleanField(null=False),
    group_photo = models.ImageField(),
    group_is_secret = models.BooleanField(default=False, null=False),
    group_score = models.IntegerField(default=0, null=False),
    group_count = models.IntegerField(default=1, null=False),
    group_introduction_1 = models.CharField(max_length=250, null=False, default=""),
    group_introduction_2 = models.CharField(max_length=250, null=False, default=""),
    group_introduction_3 = models.CharField(max_length=250, null=False, default=""),
    group_introduction_4 = models.CharField(max_length=250, null=False, default=""),
    group_introduction_5 = models.CharField(max_length=250, null=False, default="")

class Feed(models.Model):
    feed_id = models.AutoField(primary_key=True),
    group_id = models.ForeignKey(GroupInfo, on_delete=models.CASCADE),
    mem_id = models.ForeignKey(MemInfo, on_delete=models.DO_NOTHING),
    category_id = models.ForeignKey(Category, on_delete=models.DO_NOTHING),
    feed_title = models.CharField(max_length=250, null=False),
    feed_is_meeting = models.BooleanField(null=False),
    feed_write = models.DateTimeField(auto_created=True),
    feed_meeting_address = models.CharField(max_length=250),
    feed_meeting_address_detail = models.CharField(max_length=250),
    feed_meeting_start_date = models.DateField(),
    feed_meeting_end_date = models.DateField(),
    feed_meeting_start_hour = models.IntegerField(),
    feed_meeting_end_hour = models.IntegerField(),
    feed_meeting_fee = models.IntegerField(),
    feed_meeting_status = models.CharField(max_length=1),
    feed_score = models.IntegerField(),
    feed_latitude = models.IntegerField(),
    feed_longitude = models.IntegerField()

class FeedFile(models.Model):
    feed_file_id = models.AutoField(primary_key=True),
    feed_id = models.ForeignKey(Feed, on_delete=models.CASCADE),
    feed_file_originname = models.CharField(max_length=250, null=False),
    feed_file_filename = models.CharField(max_length=250, null=False),
    feed_file_type = models.CharField(max_length=10, null=False),
    feed_file_order = models.IntegerField(null=False),
    feed_file_path = models.FilePathField(path='', match=None, recursive=False,
                                          allow_files=True, allow_folders=False, max_length=100) #수정요망

class Config(models.Model):
    mem_id = models.ForeignKey(MemInfo, on_delete=models.CASCADE),
    config_option_a = models.BooleanField(),
    config_option_z = models.BooleanField()

class Letter(models.Model):
    letter_id = models.AutoField(primary_key=True),
    mem_id = models.ForeignKey(MemInfo, on_delete=models.CASCADE),
    letter_sender = models.ForeignKey(MemInfo, on_delete=models.DO_NOTHING),
    letter_recipient = models.ForeignKey(MemInfo, on_delete=models.DO_NOTHING),
    letter_content = models.CharField(max_length=250, null=False),
    letter_date = models.DateTimeField(auto_created=True, null=False),
    letter_read_date = models.DateTimeField(auto_now_add=True)

class MemManage(models.Model):
    mem_id = models.ForeignKey(MemInfo, on_delete=models.DO_NOTHING),
    mem_google = MemInfo.objects.get(mem_id=mem_id).mem_google,
    mem_status = models.CharField(max_length=1, null=False),

class Credential(models.Model):
    credential_id = models.AutoField(primary_key=True),
    credential_key = models.CharField(max_length=250),
    mem_id = models.ForeignKey(MemInfo, on_delete=models.CASCADE),
    credential_type = models.CharField(max_length=1),
    credential_generate_datetime = models.DateTimeField(auto_created=True),
    credential_expire = models.DateTimeField(null=False)

class AutoLogin(models.Model):
    auto_login_id = models.AutoField(primary_key=True),
    mem_id = models.ForeignKey(MemInfo, on_delete=models.CASCADE),
    credential_id = models.ForeignKey(Credential, on_delete=models.CASCADE),
    auto_login_date = models.DateTimeField(auto_now=True)

class Notification(models.Model):
    not_id = models.AutoField(primary_key=True),
    mem_id = models.ForeignKey(MemInfo, on_delete=models.CASCADE),
    target_mem_id = models.IntegerField(null=False)

class ReportCategory(models.Model):
    report_category_id = models.AutoField(primary_key=True),
    report_category_text = models.CharField(max_length=20)

class Report(models.Model):
    report_id = models.AutoField(primary_key=True),
    report_reporter = models.ForeignKey(MemInfo, on_delete=models.DO_NOTHING),
    report_target = models.ForeignKey(MemInfo, on_delete=models.DO_NOTHING),
    group_id = models.ForeignKey(GroupInfo, on_delete=models.DO_NOTHING),
    report_category_id = models.ForeignKey(ReportCategory, on_delete=models.DO_NOTHING),
    report_date = models.DateTimeField(auto_created=True, null=False),
    report_content = models.CharField(max_length=500, null=False)

class Block(models.Model):
    block_id = models.AutoField(primary_key=True),
    report_id = models.ForeignKey(Report, on_delete=models.DO_NOTHING),
    #block_requester_id = models.ForeignKey(MemInfo, on_delete=models.DO_NOTHING),
    #block_requester_google = MemInfo.objects.get(mem_id=reporter_id).mem_google,
    block_requester_google = MemInfo.objects.get(
        mem_id=models.ForeignKey(MemInfo, on_delete=models.DO_NOTHING)) \
                                 .mem_google,

    #block_target_id = models.ForeignKey(MemInfo, on_delete=models.DO_NOTHING),
    #block_target_google = MemInfo.objects.get(mem_id=block_target_id).mem_google,
    block_target_google = MemInfo.objects.get(
        mem_id=models.ForeignKey(MemInfo, on_delete=models.DO_NOTHING)) \
                              .mem_google,

    group_id = models.ForeignKey(GroupInfo, on_delete=models.DO_NOTHING),
    block_date = models.DateTimeField(auto_created=True)

class TextFavorite(models.Model):
    text_id = models.AutoField(primary_key=True),
    text_title = models.CharField(max_length=50, null=False),
    text_content = models.CharField(max_length=250, null=False)

class GroupMember(models.Model):
    group_member_id = models.AutoField(primary_key=True),
    group_id = models.ForeignKey(GroupInfo, on_delete=models.CASCADE),
    mem_id = models.ForeignKey(MemInfo, on_delete=models.CASCADE),
    group_join = models.DateTimeField(auto_created=True)

class JoinInvitation(models.Model):
    join_invitation_id = models.AutoField(primary_key=True),
    join_invitation_target = models.ForeignKey(MemInfo, on_delete=models.CASCADE),
    join_invitation_sender = models.ForeignKey(GroupMember, on_delete=models.CASCADE),
    join_invitation_date = models.DateTimeField(auto_created=True)

class JoinRequest(models.Model):
    join_request_id = models.AutoField(primary_key=True),
    join_request_target = models.ForeignKey(MemInfo, on_delete=models.CASCADE),
    join_request_sender = models.ForeignKey(MemInfo, on_delete=models.CASCADE),
    join_request_date = models.DateTimeField(auto_created=True)

class PromotionCode(models.Model):
    promotion_code_id = models.AutoField(primary_key=True),
    promotion_code = models.CharField(max_length=12),
    promotion_discount_rate = models.FloatField(null=False),
    promotion_is_used = models.BooleanField(default=False),
    promotion_expire = models.DateTimeField(null=False)

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True),
    payment_imp_uid = models.CharField(max_length=50, unique=True, null=False),
    mem_id = models.ForeignKey(MemInfo, on_delete=models.DO_NOTHING),
    mem_google = MemInfo.objects.get(mem_id=mem_id).mem_google,
    feed_id = models.ForeignKey(Feed, on_delete=models.DO_NOTHING),
    mem_name = MemInfo.objects.get(mem_id=mem_id).mem_nickname,
    payment_total_money = models.IntegerField(null=False),
    promotion_code_id = models.ForeignKey(PromotionCode, on_delete=models.DO_NOTHING),
    payment_paid_money = models.IntegerField(null=False),
    payment_date = models.DateTimeField(auto_created=True),
    payment_approval_number = models.CharField(max_length=50)

class Cmt(models.Model):
    cmt_id = models.AutoField(primary_key=True),
    feed_id = models.ForeignKey(Feed, on_delete=models.CASCADE),
    group_member_id = models.ForeignKey(GroupMember, on_delete=models.DO_NOTHING),
    cmt_content = models.CharField(max_length=4000, null=True),
    cmt_datetime = models.DateTimeField(auto_created=True),
    cmt_star = models.IntegerField()

class Attendance(models.Model):
    feed_id = models.AutoField(primary_key=True),
    group_member_id = models.ForeignKey(GroupMember, on_delete=models.CASCADE),
    att_date = models.DateTimeField(auto_created=True)

class Vote(models.Model):
    vote_id = models.AutoField(primary_key=True),
    feed_id = models.ForeignKey(Feed, on_delete=models.CASCADE),
    vote_generate = models.DateTimeField(auto_created=True),
    vote_start_date = models.DateTimeField(null=False),
    vote_end_date = models.DateTimeField(null=False),
    vote_title = models.CharField(max_length=250, null=False),
    vote_count = models.IntegerField(null=False, default=0),
    vote_multiple_selection = models.BooleanField(default=False, null=False)

class VoteItem(models.Model):
    vote_item_id = models.AutoField(primary_key=True),
    vote_id = models.ForeignKey(Vote, on_delete=models.CASCADE),
    vote_item = models.CharField(max_length=250, null=False),

class VoteRecord(models.Model):
    vote_record_id = models.AutoField(primary_key=True),
    vote_id = models.ForeignKey(Vote, on_delete=models.CASCADE),
    vote_item_id = models.ForeignKey(VoteItem, on_delete=models.CASCADE),
    group_member_id = models.ForeignKey(GroupMember, on_delete=models.DO_NOTHING),
    vote_date = models.DateTimeField(auto_created=True)


#https://github.com/narrowfail/django-channels-chat
# <editor-fold desc="Chat">
class MessageModel(models.Model):
    """
    This class represents a chat message. It has a owner (user), timestamp and
    the message body.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user',
                             related_name='from_user', db_index=True)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='recipient',
                                  related_name='to_user', db_index=True)
    timestamp = models.DateTimeField('timestamp', auto_now_add=True, editable=False,
                                     db_index=True)
    body = models.TextField('body')

    def __str__(self):
        return str(self.id)

    def characters(self):
        """
        Toy function to count body characters.
        :return: body's char number
        """
        return len(self.body)

    def notify_ws_clients(self):
        """
        Inform client there is a new message.
        """
        notification = {
            'type': 'recieve_group_message',
            'message': '{}'.format(self.id)
        }

        channel_layer = get_channel_layer()
        print("user.id {}".format(self.user.id))
        print("user.id {}".format(self.recipient.id))

        async_to_sync(channel_layer.group_send)("{}".format(self.user.id), notification)
        async_to_sync(channel_layer.group_send)("{}".format(self.recipient.id), notification)

    def save(self, *args, **kwargs):
        """
        Trims white spaces, saves the message and notifies the recipient via WS
        if the message is new.
        """
        new = self.id
        self.body = self.body.strip()  # Trimming whitespaces from the body
        super(MessageModel, self).save(*args, **kwargs)
        if new is None:
            self.notify_ws_clients()

    # Meta
    class Meta:
        app_label = 'core'
        verbose_name = 'message'
        verbose_name_plural = 'messages'
        ordering = ('-timestamp',)
# </editor-fold>

#https://github.com/django-notifications/django-notifications

'''