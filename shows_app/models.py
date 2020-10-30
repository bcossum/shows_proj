from django.db import models

class network(models.Model):
  name = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class show(models.Model):
  title = models.CharField(max_length=255)
  release_date = models.DateField()
  desc = models.TextField(null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  networks = models.ForeignKey(network, related_name=("shows"), on_delete=models.CASCADE)