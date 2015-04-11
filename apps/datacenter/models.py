import os
from django.db import models
from django.db.models import permalink
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
# from dciim.settings import LANGUAGES


ROLE_CHOICES={
    'controller': _('Openstack controller node'),
    'network': _('Openstack network node'),
    'compute': _('Openstack compute node'),
    'infrastructure': _('Infrastructure'),
    'development': _('Development server')
}
TYPE_CHOICES={
    'HP DL380 G8': _('Openstack controller node'),
    'supermicro SC825TQ-R740': _('Openstack network node'),
    'blade BL20P G3': _('Openstack compute node'),
    'blade BL45P G3': _('Infrastructure'),
}
RAID_CHOICES={
    'RAID 0': _('RAID 0'),
    'RAID 1': _('RAID 1'),
    'RAID 5': _('RAID 5'),
    'RAID 1 + 0': _('RAID 1 + 0'),
}

class Project(models.Model):
    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

    name = models.CharField(_('Project Name'),max_length=300, blank=False, help_text=_('Project / Tenant name'))
    start_date = models.DateTimeField(default=datetime.now())
    stop_date = models.DateTimeField(blank=True, null=True)
    owner = models.ForeignKey(Customer)

    def __unicode__(self):
        return self.name

class Customer(models.Model):
    class Meta:
       verbose_name = _('Project')
       verbose_name_plural = _('Projects')
    name = models.CharField(_('Customer name'),max_length=300, blank=False)
    phone = models.CharField(max_length=300, blank=False)
    email = models.CharField(max_length=300, blank=False)
    secondary_email = models.CharField(max_length=300, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return self.name

class Infrastructure(models.Model):
    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')
    data_center_code = models.CharField(max_length=300, blank=False)
    hostname = models.CharField(max_length=300, blank=False)
    role = models.CharField(max_length=300, blank=False)
    server_type = models.CharField(max_length=300, blank=False)
    ram = models.CharField(max_length=300, blank=False, choices=TYPE_CHOICES)
    cpu = models.CharField(max_length=300, blank=False)
    hdd = models.CharField(max_length=300, blank=False)
    hdd_raid = models.CharField(max_length=300, blank=False, choices=RAID_CHOICES)
    operating_system = models.CharField(max_length=300, blank=False)
    nic_count = models.CharField(max_length=300, blank=False)
    nic_mac = models.CharField(max_length=300, blank=False)
    nic_vlan = models.CharField(max_length=300, blank=False)
    nic_switch_port = models.CharField(max_length=300, blank=False)
    nic_internal_ip = models.CharField(max_length=300, blank=False)
    nic_external_ip = models.CharField(max_length=300, blank=False)
    firewall_access_rules = models.CharField(max_length=300, blank=False)
    guarantee = models.CharField(max_length=300, blank=False)

    def __unicode__(self):
        return self.hostname