from django.db import models


# Create your models here.

class TempHum(models.Model):
    """
    温湿度
    """
    temperature = models.FloatField(verbose_name='温度')
    humidity = models.FloatField(verbose_name='湿度')
    date_time = models.DateTimeField(verbose_name='更新时间', auto_now_add=True, )


class ToDo(models.Model):
    """
    待办事项
    """
    title = models.CharField(verbose_name='待办事项', max_length=16, help_text='最多16个字符')
    date = models.DateField(verbose_name='事项日期')
    period = models.SmallIntegerField(verbose_name='事项周期', default=0, help_text='每n天执行的事项')
    fix_day = models.BooleanField(verbose_name='固定日期', default=False, help_text='例如：事项是16日执行，此后每月固定16日执行此事项.优先级大于事项周期。')

    # date_time = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)
    def __str__(self):
        msg = ''
        if self.fix_day:
            msg = '%s办理%s事项,每月这个日期执行一下' % (self.date, self.title)
        elif self.period:
            msg = '%s办理%s事项，每%s天执行一下' % (self.date, self.title, self.period)
        else:
            msg = '%s办理%s事项' % (self.date, self.title)

        return msg
