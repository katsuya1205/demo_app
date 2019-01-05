from django.db import models
from datetime import date
# 下の方で、today関数を使っているから、datetimeをインポート

class Customers(models.Model):
    # DBのカラム(列名)の定義 (primary_key = Trueなら重複を許さない)
    # 性別(sex)を1, 2 で選択するからその設定を最初にしておく
    gender_options = (
    (1, "male"),# 左がデータベースに入る値。右のmaleはアプリで表示される文字
    (2, "female")
    )
    education_options = (
    (1,"graduate_school"),
    (2,"university"),
    (3,"high school"),
    (4,"other")
    )
    marital_options = (
    (1, 'married'),
    (2, 'single'),
    (3, 'others')
    )
    payment_history = (
    (-1, 'pay early'),
    (0, 'pay dully'),
    (1, '1month_dalay'),
    (2, '2months_dlay')
    )

    id = models.AutoField(primary_key = True)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    limit_balance = models.IntegerField(default=100000)
    sex = models.IntegerField(choices=gender_options, default=1)
    education = models.IntegerField(choices=education_options, default=1)
    marriage = models.IntegerField(choices=marital_options, default=1)
    age = models.IntegerField()
    pay_0 = models.IntegerField(choices=payment_history, default=0)
    pay_2 = models.IntegerField(choices=payment_history, default=0)
    pay_3 = models.IntegerField(choices=payment_history, default=0)
    pay_4 = models.IntegerField(choices=payment_history, default=0)
    pay_5 = models.IntegerField(choices=payment_history, default=0)
    pay_6 = models.IntegerField(choices=payment_history, default=0)
    bill_amt_1 = models.IntegerField(default=0.0)
    pay_amt_1 = models.IntegerField(default=5000)
    pay_amt_2 = models.IntegerField(default=5000)
    pay_amt_3 = models.IntegerField(default=5000)
    pay_amt_4 = models.IntegerField(default=5000)
    pay_amt_5 = models.IntegerField(default=5000)
    pay_amt_6 = models.IntegerField(default=5000)
    result = models.IntegerField(blank=True, null=True)# blank, null = True だと空欄を許す設定になる
    proba = models.FloatField(default=0.0)
    comment = models.CharField(max_length=200, blank=True, null=True)
    registered_date = models.DateField(default=date.today)

    def register(self):# どんな関数を動かすかここで定義する
        self.registered_date = date.today()
        self.save()

    def __str__(self):
        if self.proba == 0.0:
            return '%s, %d, %s' % (self.registered_date.strftime('%Y-%m-%d'), self.id, self.last_name+self.first_name)
        else:
            return '%s, %d, %s, %d, %s, %s' % (self.registered_date.strftime('%Y-%m-%d'), self.id, self.last_name+self.first_name, self.result, '{}%'.format(round(self.proba*100, 2)), self.comment)
