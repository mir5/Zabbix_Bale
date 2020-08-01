# ارسال هشدار های زبیکس توسط پیام رسان بله

با توجه به فیلتر شدن تلگرام در ایران و عدم امکان ارسال پیام از طریق تلگرام، در این پروژه با استفاده از پیام رسان بله پیام های زبیکس را دریافت خواهید کرد

## روش نصب
در پیام رسان بله به جای نام بات از بازو استفاده می شود ولی از نظر قابلیت و امکانات دقیقا معادل بات های تلگرام می باشد.

ابتدا با استفاده از [این لینک](https://devbale.ir/quick-start) ویدیو آموزش ساخت بازو در پیام رسان بله را مشاهده کنید

```bash
https://devbale.ir/quick-start
```
کلید تولید شده توسط BotFather که مانند فرمت زیر است را دریافت کنید


```bash
968611111:36678045d11111112215559c761d4e65b0300def
```
فایل های پروژه را به سرور زبیکس کپی کنید

اطمینان حاصل کنید که python 3.6 و Pip3 بر روی سرور نصب باشد

وارد فولدر Bale شوید و دستور زیر را اجرا کنید


```bash
pip3 install -r req.txt
```
فایل sendbaleBot.py را ویرایش کنید


```bash
vi sendbaleBot.py
```
 
و توکن دریافت شده را در فایل ویرایش کنید

```python
  bot = telegram.Bot(token='968611111:36678045d11111112215559c761d4e65b0300def',
                       base_url="https://tapi.bale.ai/")
```

فایل Bale.sh را به مسیر زیر کپی کنید

```bash
 /usr/lib/zabbix/alertscripts/Bale.sh
```
فایل فوق را مانند فایل sendbaleBot.py ویرایش و توکن خودتان را جایگزین کنید.

با استفاده از دستور زیر فایل sendBaleBot.py را اجرا کنید این فایل مسئول تحویل chatid به شماست


```python
python3.6 sendbaleBot.py
```

با استفاده از پیام رسان بله در گوشی همراه خود به بات پیام Code را ارسال کنید به این ترتیب بات کد chatid را در پاسخ برای شما ارسال می کند.

وارد پنل زبیکس شده در بخش administrator بخش Media type  یک media type جدید به اسم Bale بسازید و نوع آن را script انتخاب کنید.

پارامتر های اسکریپت شامل موارد زیر است:
```python
{ALERT.SENDTO}
{ALERT.MESSAGE}
```
درصورت نیاز متن پیام های ارسالی را نیز ویرایش کنید.

سپس وارد بخش administrator بخش user شوید برای کاربر مورد نظر خود در بخش media type گزینه Bale را انتخاب کنید و سپس کدی که توسط گوشی موبایل دریافت کرده این را وارد و ذخیره کنید.

در بخش action می توانید media type بله را انتخاب کنید

تبریک هشدار های این اکشن را می توانید در پیام رسان بله دریافت کنید
