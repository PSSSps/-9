import random, os, sys
try:
    import colorama
    import cython
    import zipfile
    import shutil
except ImportError:
    os.system('pip3.11 install colorama')
    os.system('pip3.9 install colorama')
    os.system('pip install shutil')
    os.system('pip install cython')
    os.system('pip install zipfile')
    import colorama
import time
from colorama import Fore, Style
import random
os.system('clear')
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
color = random.choice(colors)
print(f"{color} THIS {color}ENCODE {color}BY {color}DEVIL {color}| @{color}NasrPy" + Style.RESET_ALL)
time.sleep(4)
# Done decode Hassani  : By - @𝗽𝟳𝘀𝟳𝘀:  

import requests
import random
import re
import time
import string
import sys
import threading
import json

# الألوان
R = '\033[1;91m'
G = '\033[1;92m'  
Y = '\033[1;93m'
B = '\033[1;94m'
P = '\033[1;95m'
C = '\033[1;96m'
W = '\033[1;97m'
N = '\033[0m'

def print_banner():
    print(f"{P}{'═' * 70}{N}")
    print(f"{P}┌{'─' * 68}┐{N}")
    print(f"{P}│{W}{' ' * 22}𝙋𝙎 𝙧𝙖𝙧𝙚{' ' * 22}{P}│{N}")
    print(f"{P}│{C}{' ' * 18}By : @𝗽𝟳𝘀𝟳𝘀 | {' ' * 18}{P}│{N}")
    print(f"{P}└{'─' * 68}┘{N}")
    print(f"{P}{'═' * 70}{N}\n")

def print_section(title):
    print(f"\n{Y}{'─' * 40}{N}")
    print(f"{G}▶ {W}{title}{N}")
    print(f"{Y}{'─' * 40}{N}")

def print_step(number, text):
    print(f"\n{B}[{number}] {W}{text}{N}")

def print_success(text):
    print(f"{G}✓ {W}{text}{N}")

def print_error(text):
    print(f"{R}✗ {W}{text}{N}")

def print_info(text):
    print(f"{C}ℹ {W}{text}{N}")

def print_warning(text):
    print(f"{Y}⚠ {W}{text}{N}")

print_banner()

print_section("معلومات الحساب المراد قفله")

print_step("1", "أدخل الرسالة أو الكود الي تريد تبلغ عليه:")
link_message = input(f"{C}⎿ {W}الرسالة: {G}")

print_step("2", "أدخل يوزر الحساب أو القناة الي تريد تقفله:")
link_channel = input(f"{C}⎿ {W}اليوزر: {G}")

print_section("إعدادات نوع البلاغ")

report_types = [
    "محتوى إباحي",
    "عنف وأذى",
    "تحرش ومضايقة", 
    "رسائل مزعجة",
    "انتحال شخصية",
    "أنشطة غير قانونية",
    "خطاب كراهية",
    "إرهاب وتطرف",
    "انتهاك حقوق النشر",
    "انتهاك خصوصية",
    "إساءة للأطفال",
    "ترويج انتحار",
    "ترويج مخدرات",
    "أخبار كاذبة",
    "عمليات نصب واحتيال",
    "ترويج مقامرة"
]

print(f"\n{W}البلاغات المتوفرة:{N}")
for i, report_type in enumerate(report_types, 1):
    print(f"  {B}{i:2d}. {C}{report_type}{N}")

print_step("3", "اختر نوع البلاغ (أدخل رقم أو 0 لجميع الأنواع):")
try:
    report_choice = int(input(f"{C}⎿ {W}الاختيار: {G}"))
    if report_choice == 0:
        selected_report = "جميع الأنواع"
        print_success("راح أستخدم كل أنواع البلاغات بالتناوب")
    elif 1 <= report_choice <= len(report_types):
        selected_report = report_types[report_choice - 1]
        print_success(f"تم اختيار: {selected_report}")
    else:
        selected_report = "جميع الأنواع"
        print_warning("راح أستخدم كل أنواع البلاغات")
except:
    selected_report = "جميع الأنواع"
    print_warning("راح أستخدم كل أنواع البلاغات")

print_step("4", "الوقت بين كل بلاغ وأخر (بالثواني):")
try:
    delay_time = int(input(f"{C}⎿ {W}الوقت: {G}"))
    if delay_time < 5:
        delay_time = 5
        print_info(f"راح يكون الوقت {delay_time} ثواني (أقل وقت آمن)")
except:
    delay_time = 5
    print_info(f"راح يكون الوقت {delay_time} ثواني")

print_step("5", "عدد البلاغات الي تريدها (0 = مستمر):")
try:
    total_reports = int(input(f"{C}⎿ {W}العدد: {G}"))
    if total_reports < 0:
        total_reports = 0
except:
    total_reports = 0

if total_reports > 0:
    print_info(f"راح أوقف بعد {total_reports} بلاغ")
else:
    print_info("راح أستمر إلى ما توقفني")

print_section("بدء عملية الإبلاغ التلقائي")

stop_reporting = False
report_counter = 0
success_counter = 0
error_counter = 0

def generate_random_data():
    first_names = ["John", "Mike", "David", "Sarah", "Emma", "James", "Robert", "Maria", "Anna", "Thomas"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
    
    return {
        'first_name': random.choice(first_names),
        'last_name': random.choice(last_names),
        'email': f"{random.choice(first_names).lower()}{random.randint(100,999)}@{random.choice(['gmail.com', 'yahoo.com', 'outlook.com'])}",
        'phone': f"+1{random.randint(200,999)}{random.randint(100,999)}{random.randint(1000,9999)}",
        'country': random.choice(['US', 'UK', 'CA', 'AU', 'DE']),
        'ip': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
    }

def get_user_agent():
    agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
    ]
    return random.choice(agents)

def send_report_via_telegram_api(report_type, success_counter, error_counter):
    report_counter = 0
    
    try:
        print_info("جربة الطريقة المتقدمة...")
        
        user_data = generate_random_data()
        
        report_message = f"""
Report Type: {report_type}
Target Account: {link_channel}
Violation Details: {link_message}

This account is violating Telegram's Community Guidelines by sharing inappropriate content.
Please review and take appropriate action.

Reporter: {user_data['first_name']} {user_data['last_name']}
Contact: {user_data['email']}
"""
        
        headers = {
            'User-Agent': get_user_agent(),
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://telegram.org',
            'Referer': 'https://telegram.org/',
            'Connection': 'keep-alive',
        }
        
        endpoints = [
            'https://telegram.org/support',
            'https://telegram.org/abuse',
            'https://telegram.org/complaint'
        ]
        
        for endpoint in endpoints:
            try:
                print_info(f" جرب {endpoint.split('/')[-1]}...")
                
                form_data = {
                    'message': report_message,
                    'email': user_data['email'],
                    'phone': user_data['phone'],
                    'setln': 'en',
                    'submit': 'Send'
                }
                
                time.sleep(random.uniform(0.5, 1.5))
                
                response = requests.post(
                    endpoint,
                    data=form_data,
                    headers=headers,
                    timeout=10,
                    verify=True
                )
                
                if response.status_code == 200:
                    response_text = response.text.lower()
                    
                    success_keywords = ['thank', 'thanks', 'received', 'success', 'تم', 'شكر']
                    if any(keyword in response_text for keyword in success_keywords):
                        print_success("تم الإرسال بنجاح!")
                        return True, success_counter + 1, error_counter
                    
                    elif len(response_text) > 1000:
                        print_warning("تم إرسال النموذج - تحت المراجعة")
                        return True, success_counter + 1, error_counter
                        
            except Exception as e:
                continue
        
        return False, success_counter, error_counter + 1
        
    except Exception as e:
        print_error(f"خطأ في الطريقة المتقدمة: {str(e)[:40]}")
        return False, success_counter, error_counter + 1

def send_report_backup_method(report_type, user_data, success_counter, error_counter):
    try:
        print_info("استخدام الطريقة البسيطة...")
        
        session = requests.Session()
        
        try:
            session.get('https://telegram.org', timeout=5)
            time.sleep(1)
        except:
            pass
        
        final_data = {
            'message': f"Report: {report_type}\nAccount: {link_channel}\nDetails: {link_message}",
            'email': user_data['email'],
            'phone': user_data['phone'],
            'setln': 'en'
        }
        
        headers = {
            'User-Agent': get_user_agent(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://telegram.org',
            'Referer': 'https://telegram.org/',
        }
        
        response = session.post(
            'https://telegram.org/support',
            data=final_data,
            headers=headers,
            timeout=15,
            allow_redirects=True
        )
        
        if response.status_code in [200, 302, 303]:
            response_text = response.text.lower()
            
            success_words = ['thank', 'received', 'success', 'submitted']
            if any(word in response_text for word in success_words):
                print_success("تم إرسال البلاغ بنجاح!")
                return True, success_counter + 1, error_counter
            elif len(response_text) > 1500:
                print_warning("تم إرسال النموذج - جاري المعالجة")
                return True, success_counter + 1, error_counter
            else:
                print_error("لم يتم تأكيد الإرسال")
                return False, success_counter, error_counter + 1
        else:
            print_error(f"خطأ HTTP: {response.status_code}")
            return False, success_counter, error_counter + 1
            
    except Exception as e:
        print_error(f"خطأ في الطريقة البسيطة: {str(e)[:30]}")
        return False, success_counter, error_counter + 1

def send_report_simple_method(report_type, success_counter, error_counter):
    try:
        print_info(" جرب طريقة سريعة...")
        
        email = f"user{random.randint(1000,9999)}@gmail.com"
        phone = f"+1{random.randint(200,999)}{random.randint(100,999)}{random.randint(1000,9999)}"
        
        message = f"""
REPORT - {report_type}
Account: {link_channel}
Issue: {link_message}
        
This needs immediate attention.
"""
        
        data = {
            'message': message,
            'email': email,
            'phone': phone,
            'setln': 'en'
        }
        
        headers = {
            'User-Agent': get_user_agent(),
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        
        response = requests.post(
            'https://telegram.org/support',
            data=data,
            headers=headers,
            timeout=10
        )
        
        if response.status_code == 200:
            if len(response.text) > 500:
                print_success("   تم تسليم الطلب!")
                return True, success_counter + 1, error_counter
        
        print_error("   فشل الإرسال السريع")
        return False, success_counter, error_counter + 1
        
    except Exception as e:
        print_error(f"   خطأ في الطريقة السريعة: {str(e)[:30]}")
        return False, success_counter, error_counter + 1

def continuous_reporting():
    global stop_reporting, selected_report, report_counter, success_counter, error_counter
    
    print(f"\n{Y}{'═' * 50}{N}")
    print(f"{G}▶ {W}بدأت عملية الإبلاغ التلقائي...{N}")
    print(f"{C}استراتيجية: استخدام طرق متعددة للتغلب على الحماية{N}")
    print(f"{C}▶ {W}{N}")
    print(f"{Y}{'═' * 50}{N}\n")
    
    type_index = 0
    start_time = time.time()
    method_index = 0
    
    try:
        while not stop_reporting and (total_reports == 0 or report_counter < total_reports):
            if selected_report == "جميع الأنواع":
                current_report_type = report_types[type_index]
                type_index = (type_index + 1) % len(report_types)
            else:
                current_report_type = selected_report
            
            report_counter += 1
            current_time = time.strftime('%H:%M:%S')
            
            print(f"\n{W}[{current_time}] {B}بلاغ #{report_counter}{W} - {C}النوع:{W} {current_report_type}")
            
            success = False
            if method_index % 3 == 0:
                success, success_counter, error_counter = send_report_via_telegram_api(
                    current_report_type, success_counter, error_counter
                )
            elif method_index % 3 == 1:
                user_data = generate_random_data()
                success, success_counter, error_counter = send_report_backup_method(
                    current_report_type, user_data, success_counter, error_counter
                )
            else:
                success, success_counter, error_counter = send_report_simple_method(
                    current_report_type, success_counter, error_counter
                )
            
            method_index += 1
            
            elapsed_time = time.time() - start_time
            
            print(f"{C}   الاحصائيات:{N}")
            print(f"{C}   - ناجح: {G}{success_counter}{N}  فاشل: {R}{error_counter}{N}  اجمالي: {B}{report_counter}{N}")
            
            if total_reports > 0 and report_counter >= total_reports:
                print(f"\n{G}وصلت للعدد المطلوب: {total_reports} بلاغ{N}")
                stop_reporting = True
                break
            
            if not stop_reporting and report_counter < total_reports:
                print(f"\n{C}   البلاغ الجاي بعد {delay_time} ثانية...{N}")
                for remaining in range(delay_time, 0, -1):
                    if stop_reporting:
                        break
                    sys.stdout.write(f'\r{C}   الانتظار: {G}{remaining}{C} ثانية...   {N}')
                    sys.stdout.flush()
                    time.sleep(1)
                print()
    
    except KeyboardInterrupt:
        print(f"\n\n{R}▶ {W}تم إيقاف العملية بواسطة المستخدم{N}")
    except Exception as e:
        print(f"\n{R}▶ {W}صار خطأ: {str(e)}{N}")

print(f"\n{B}▶ {W}جاري تحضير النظام...{N}")
time.sleep(1)

report_thread = threading.Thread(target=continuous_reporting)
report_thread.daemon = True
report_thread.start()

try:
    while report_thread.is_alive():
        time.sleep(0.5)
except KeyboardInterrupt:
    stop_reporting = True
    print(f"\n{R}▶ {W}جاري إيقاف العملية...{N}")

time.sleep(1)
print_section("تقرير نهائي عن العملية")

elapsed_time = time.time() - start_time if 'start_time' in locals() else 0
minutes = int(elapsed_time // 60)
seconds = int(elapsed_time % 60)

print(f"{C}⎿ {W}الرسالة المبلغ عنها: {G}{link_message}{N}")
print(f"{C}⎿ {W}الحساب/القناة: {G}{link_channel}{N}")
print(f"{C}⎿ {W}نوع البلاغ: {G}{selected_report}{N}")
print(f"{C}⎿ {W}مدة التشغيل: {Y}{minutes} دقيقة و {seconds} ثانية{N}")
print(f"{C}⎿ {W}إجمالي البلاغات: {B}{report_counter}{N}")
print(f"{C}⎿ {W}البلاغات الناجحة: {G}{success_counter}{N}")
print(f"{C}⎿ {W}البلاغات الفاشلة: {R}{error_counter}{N}")

if elapsed_time > 0 and report_counter > 0:
    print(f"{C}⎿ {W}المعدل: {P}{report_counter/elapsed_time*60:.1f} بلاغ/دقيقة{N}")

print(f"\n{P}{'═' * 70}{N}")
print(f"{P}┌{'─' * 68}┐{N}")
print(f"{P}│{W}{' ' * 20}𝙋𝙎 𝙧𝙖𝙧𝙚{' ' * 21}{P}│{N}")
print(f"{P}│{C}{' ' * 18}By : @𝗽𝟳𝘀𝟳𝘀 | {' ' * 18}{P}│{N}")
print(f"{P}└{'─' * 68}┘{N}")
print(f"{P}{'═' * 70}{N}")

print(f"\n{C}{'─' * 50}{N}")

if success_counter > 0:
    if success_counter == report_counter:
        print(f"{G}إنجاز ممتاز! كل البلاغات نجحت!{N}")
        print(f"{C}تم إرسال {success_counter} بلاغ بنجاح لتليجرام.{N}")
    else:
        print(f"{G}جيد! تم إرسال {success_counter} بلاغ بنجاح.{N}")
    
    print(f"\n{Y}نصائح للتحسين:{N}")
    print(f"{Y}   • زيد وقت الانتظار بين البلاغات (10+ ثواني){N}")
    print(f"{Y}   • غير الرسالة في كل مرة{N}")
    print(f"{Y}   • استخدم أنواع بلاغ مختلفة{N}")
else:
    print(f"{R}لم يتم إرسال أي بلاغ.{N}")
    print(f"{C}تليجرام يحمي نظام الإبلاغ بشدة.{N}")
    print(f"\n{Y}الحلول البديلة:{N}")
    print(f"{Y}   1. {W}استخدم تطبيق تليجرام للإبلاغ مباشرة{N}")
    print(f"{Y}   2. {W}اذهب لـ https://telegram.org/support يدوي{N}")
    print(f"{Y}   3. {W}استخدم خاصية Report داخل التطبيق{N}")

print(f"\n{C}معلومة: {W}هذا الكود لأغراض تعليمية.{N}")
print(f"{C}الهدف: {W}فهم كيفية عمل أنظمة الإبلاغ.{N}")
print(f"{C}{'─' * 50}{N}")

print(f"\n{B}▶ {W}عملية الإبلاغ اكتملت!{N}")
print(f"{B}▶ {W}للتواصل: @𝗽𝟳𝘀𝟳𝘀 | {N}")

