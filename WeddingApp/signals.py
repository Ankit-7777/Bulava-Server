# from channels.layers import get_channel_layer
# from asgiref.sync import async_to_sync
from django.db.models.signals import post_save
from django.dispatch import receiver
from WeddingApp.models import Event, Group, UserEvent

# @receiver(post_save, sender=Event)
# def send_event_notification(sender, instance, created, **kwargs):
#     if created:
#         user_id = instance.user.id
#         group_name = f"user_{user_id}"
#         notification_message = f"A new event '{instance.event_category}' has been created."

#         print(f"Sending notification to group {group_name}: {notification_message}")

#         channel_layer = get_channel_layer()
#         async_to_sync(channel_layer.group_send)(
#             group_name,
#             {
#                 "type": "notification_message",
#                 "message": notification_message,
#                 "event_id": instance.id
#             }
#         )

@receiver(post_save, sender=Event)
def create_group_for_event(sender, instance, created, **kwargs):
    if created:
        group_name = f"{instance.event_category.category_name} Group_{instance.id}"
        group = Group.objects.create(name=group_name, event=instance, owner=instance.user, is_active=True)
        group.member.add(instance.user)


@receiver(post_save, sender=UserEvent)
def add_guest_to_group(sender, instance, **kwargs):
    if instance.status == 'accepted':
        try:
            group = Group.objects.get(event=instance.event)
            group.member.add(instance.guest)
            group.save()
            instance.event.invited.add(instance.guest)
            instance.event.save()
        except Group.DoesNotExist:
            pass


