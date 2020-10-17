# Generated by Django 3.1.1 on 2020-10-16 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fund', '0010_auto_20201014_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='FundHistoricalNetWorth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fund_code', models.CharField(db_index=True, default='', max_length=20, verbose_name='基金代码')),
                ('current_unit_net_worth', models.FloatField(default=0, verbose_name='当前单位净值')),
                ('current_cumulative_net_worth', models.FloatField(default=0, verbose_name='当前累计净值')),
                ('daily', models.FloatField(default=0, verbose_name='日涨跌幅')),
                ('subscription_status', models.CharField(default='', max_length=20, null=True, verbose_name='申购状态')),
                ('redemption_status', models.CharField(default='', max_length=20, null=True, verbose_name='赎回状态')),
                ('dividend_distribution', models.CharField(default='', max_length=200, null=True, verbose_name='分红送配')),
                ('current_date', models.DateField(default='', verbose_name='当前日期')),
                ('insert_time', models.DateTimeField(auto_now_add=True, verbose_name='爬取时间')),
                ('update_time', models.DateTimeField(null=True, verbose_name='更新时间')),
                ('is_deleted', models.IntegerField(default=0, verbose_name='是否删除')),
            ],
            options={
                'unique_together': {('fund_code', 'current_date')},
            },
        ),
        migrations.CreateModel(
            name='FundRanking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fund_code', models.CharField(db_index=True, default='', max_length=20, verbose_name='基金代码')),
                ('start_unit_net_worth', models.FloatField(default=0, verbose_name='起始单位净值')),
                ('start_cumulative_net_worth', models.FloatField(default=0, verbose_name='起始累计净值')),
                ('current_unit_net_worth', models.FloatField(default=0, verbose_name='当前单位净值')),
                ('current_cumulative_net_worth', models.FloatField(default=0, verbose_name='当前累计净值')),
                ('daily', models.FloatField(default=0, verbose_name='日涨跌幅')),
                ('last_week', models.FloatField(default=0, verbose_name='周涨跌')),
                ('last_month', models.FloatField(default=0, verbose_name='最近一个月涨跌')),
                ('last_three_month', models.FloatField(default=0, verbose_name='最近三个月涨跌')),
                ('last_six_month', models.FloatField(default=0, verbose_name='最近六个月涨跌')),
                ('last_year', models.FloatField(default=0, verbose_name='最近一年涨跌')),
                ('last_two_year', models.FloatField(default=0, verbose_name='最近两年涨跌')),
                ('last_three_year', models.FloatField(default=0, verbose_name='最近三年涨跌')),
                ('last_five_year', models.FloatField(default=0, verbose_name='最近五年涨跌')),
                ('ten_thousand_income', models.FloatField(default=0, verbose_name='万份收益')),
                ('annualized_income_7day', models.FloatField(default=0, verbose_name='7天年化收益率')),
                ('annualized_income_14day', models.FloatField(default=0, verbose_name='14天年化收益率')),
                ('annualized_income_28day', models.FloatField(default=0, verbose_name='28天年化收益率')),
                ('this_year', models.FloatField(default=0, verbose_name='今年以来涨跌')),
                ('since_founded', models.FloatField(default=0, verbose_name='成立以来涨跌')),
                ('since_founded_bonus', models.FloatField(default=0, verbose_name='成立以来分红')),
                ('since_founded_bonus_num', models.IntegerField(default=0, verbose_name='成立以来分红次数')),
                ('handling_fee', models.FloatField(default=0, verbose_name='手续费率')),
                ('current_date', models.DateField(default='', verbose_name='当前日期')),
                ('insert_time', models.DateTimeField(auto_now_add=True, verbose_name='爬取时间')),
                ('update_time', models.DateTimeField(null=True, verbose_name='更新时间')),
                ('is_deleted', models.IntegerField(default=0, verbose_name='是否删除')),
            ],
            options={
                'unique_together': {('fund_code', 'current_date')},
            },
        ),
        migrations.DeleteModel(
            name='FundHistoricalNetWorthRanking',
        ),
    ]
