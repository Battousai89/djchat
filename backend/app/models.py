from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    nickname = models.CharField(max_length=255, unique=True, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.username

class Server(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_servers')
    members = models.ManyToManyField(User, related_name='servers', through='ServerMember')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Channel(models.Model):
    TEXT = 'text'
    VOICE = 'voice'
    CHANNEL_TYPES = [
        (TEXT, 'Text'),
        (VOICE, 'Voice'),
    ]

    name = models.CharField(max_length=100)
    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name='channels')
    channel_type = models.CharField(max_length=10, choices=CHANNEL_TYPES, default=TEXT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.server.name} - {self.name}"

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.content[:20]}"

class Role(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name='roles')
    name = models.CharField(max_length=50)
    permissions = models.JSONField(default=dict)  # JSON с разрешениями.

    def __str__(self):
        return f"{self.server.name} - {self.name}"

class ServerMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        unique_together = ('user', 'server')
