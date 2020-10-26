from django.db import models


class EcsServer(models.Model):
    instance_id = models.CharField(db_column='Instance_ID', primary_key=True, max_length=30)  # Field name made lowercase.
    instance_name = models.CharField(db_column='Instance_Name', max_length=30)  # Field name made lowercase.
    os_type = models.CharField(db_column='OS_Type', max_length=15)  # Field name made lowercase.
    os_name = models.CharField(db_column='OS_Name', max_length=30)  # Field name made lowercase.
    cpu = models.IntegerField(db_column='CPU')  # Field name made lowercase.
    memory = models.IntegerField(db_column='Memory')  # Field name made lowercase.
    primary_ip_address = models.CharField(db_column='Primary_IP_Address', max_length=20, blank=True, null=True)  # Field name made lowercase.
    public_ip_address = models.CharField(db_column='Public_IP_Address', max_length=20, blank=True, null=True)  # Field name made lowercase.
    expired_time = models.DateTimeField(db_column='Expired_Time')  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='Update_Time')  # Field name made lowercase.
    belong_account = models.CharField(db_column='Belong_Account', max_length=30)  # Field name made lowercase.
    is_delete = models.IntegerField()
    region = models.CharField(db_column='Region', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ecs_server'


class Waf(models.Model):
    domain_name = models.CharField(db_column='Domain_Name', primary_key=True, max_length=40)  # Field name made lowercase.
    instance_id = models.CharField(db_column='Instance_ID', max_length=30)  # Field name made lowercase.
    source_ip_addr = models.CharField(db_column='Source_IP_Addr', max_length=255, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=255, blank=True, null=True)  # Field name made lowercase.
    belong_account = models.CharField(db_column='Belong_Account', max_length=30)  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='Update_Time')  # Field name made lowercase.
    is_delete = models.IntegerField()
    is_update = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'waf'

class WafWhitelist(models.Model):
    domain_name = models.CharField(db_column='Domain_Name', primary_key=True, max_length=50)  # Field name made lowercase.
    ip_address = models.CharField(db_column='IP_Address', max_length=15)  # Field name made lowercase.
    is_delete = models.IntegerField()
    update_time = models.DateTimeField(db_column='Update_Time')  # Field name made lowercase.
    acl_id = models.CharField(db_column='Acl_ID', max_length=15)  # Field name made lowercase.
    acl_name = models.CharField(db_column='Acl_Name', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'waf_whitelist'
        unique_together = (('domain_name', 'ip_address'),)



class Cdn(models.Model):
    product_id = models.CharField(db_column='Product_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    domain_name = models.CharField(db_column='Domain_Name', max_length=50)  # Field name made lowercase.
    ssl_protocol = models.CharField(db_column='SSL_Protocol', max_length=5)  # Field name made lowercase.
    cdn_type = models.CharField(db_column='CDN_Type', max_length=14)  # Field name made lowercase.
    cname = models.CharField(db_column='Cname', max_length=255)  # Field name made lowercase.
    source_type = models.CharField(db_column='Source_Type', max_length=255)  # Field name made lowercase.
    source_content = models.CharField(db_column='Source_Content', max_length=255)  # Field name made lowercase.
    domain_status = models.CharField(db_column='Domain_Status', max_length=10)  # Field name made lowercase.
    belong_account = models.CharField(db_column='Belong_Account', max_length=30)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=40, blank=True, null=True)  # Field name made lowercase.
    service_name = models.CharField(db_column='Service_Name', max_length=40)  # Field name made lowercase.
    purpose = models.CharField(db_column='Purpose', max_length=100, blank=True, null=True)  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='Update_Time')  # Field name made lowercase.
    is_delete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cdn'
        unique_together = (('id', 'domain_name'),)
