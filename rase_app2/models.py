from django.db import models



class TimeTable(models.Model):
    origin_station= models.CharField(max_length=100, verbose_name='ایستگاه مبدا')
    destination_station = models.CharField(max_length=100, verbose_name='ایستگاه مقصد')
    time_of_the_next_bus = models.CharField(max_length=100, verbose_name='زمان رسیدن اتوبوس بعدی')
    start_time = models.CharField(max_length=100, verbose_name='ساعت شروع حرکت')
    time_at_the_terminal = models.CharField(max_length=100, verbose_name='ساعت رسیدن به پایانه')
    is_admin = models.BooleanField(verbose_name='admin', default=False)



    class Meta:
        verbose_name = "time table"
        verbose_name_plural = 'list time table'



