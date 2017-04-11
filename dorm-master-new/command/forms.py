"""
Forms that send command to device
"""
from django import forms

class SendCommand(forms.Form):
	"""
	Forms of send command
	"""
	command = models.CharField(label = '下行指令',max_length=26)
