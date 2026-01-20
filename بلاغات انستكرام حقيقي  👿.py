from requests import post, get
import os
import time
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.style import Style
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn
from rich.layout import Layout
from rich import box
import concurrent.futures

import os
import sys
import base64
from datetime import datetime, time


import requests
import random
import uuid
import SignerPy
import re
import json
import datetime
import time
from concurrent.futures import ThreadPoolExecutor

token = input("\033[1;93mادخل توكن البوت: \033[0m")  # أصفر + Bold
chat_id = input("\033[1;93mادخل ID: \033[0m")  # أصفر + Bold

# ——————————————————————————
# نص الترحيب مع جميع قنواتك
# ——————————————————————————
welcome_caption = """
👑✨ يـــوزري الــرســمي : @NTBgg ✨👑
🚫💬 الــتــواصــل مــحــظــور : @NTBggbbot 🚫

🎁💎 جــــمــــيــــع قــــنــــواتــــي 💎🎁

🔹 القناة الأساسية:      t.me/ali313eme
🔹 قناة الأدوات:         t.me/XFGGFX
🔹 قناة أدوات تيرمكس:    t.me/ali313emee
🔹 قناة الثقة:           t.me/ali313eme8
🔹 قناة الشروحات:        t.me/ali313eme0

🤖⚡ بــــوت خــــدمــــات PS ⚡🤖

⚡ @fsetgc_bot
⚡ @asdfrd_bot
"""

# ——————————————————————————
# رابط الفيديو
# ——————————————————————————
video_url = "https://t.me/ssddffftq/36"

# ——————————————————————————
# إرسال الفيديو
# ——————————————————————————
try:
    response = requests.post(
        f"https://api.telegram.org/bot{token}/sendVideo",
        data={
            "chat_id": chat_id,
            "video": video_url,
            "caption": welcome_caption
        }
    )
    if response.status_code == 200:
        print("\033[1;92m نجح التحقق منك\033[0m")  # أخضر Bold
    else:
        print("\033[1;91m❌ فشل الإرسال، تحقق من التوكن وID\033[0m")  # أحمر Bold
except Exception as e:
    print("\033[1;91m❌ خطاء في التحقق:\033[0m", e)



console = Console()

session_cache = {}

def load_sessions(file_path):
    try:
        with open(file_path, "r") as file:
            sessions = file.read().splitlines()
        if not sessions:
            console.print("[bold red][!] The file is empty.[/bold red]")
            exit()
        return sessions
    except FileNotFoundError:
        console.print("[bold red][!] sessions.txt file not found.[/bold red]")
        exit()

def get_csrf_token(sessionid):
    try:
        if sessionid in session_cache:
            return session_cache[sessionid]
        
        r1 = get(
            "https://www.instagram.com/",
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0",
            },
            cookies={"sessionid": sessionid},
            timeout=10
        )
        if "csrftoken" in r1.cookies:
            session_cache[sessionid] = r1.cookies["csrftoken"]
            return r1.cookies["csrftoken"]
        else:
            return None
    except Exception as e:
        return None

def validate_session(sessionid):
    try:
        csrf = get_csrf_token(sessionid)
        if csrf:
            test_req = get(
                "https://www.instagram.com/accounts/edit/",
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0",
                },
                cookies={"sessionid": sessionid},
                timeout=10,
                allow_redirects=False
            )
            return test_req.status_code == 200, csrf
        return False, None
    except Exception as e:
        return False, None

def filter_sessions(sessions, max_workers=10):
    valid_sessions = []
    invalid_sessions = []
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[bold blue]{task.description}[/bold blue]"),
        BarColumn(),
        TextColumn("[cyan]{task.completed}/{task.total}[/cyan]"),
        console=console
    ) as progress:
        task = progress.add_task("[bold yellow]Checking sessions...", total=len(sessions))
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_session = {executor.submit(validate_session, session): session for session in sessions}
            
            for future in concurrent.futures.as_completed(future_to_session):
                session = future_to_session[future]
                try:
                    is_valid, csrf = future.result()
                    if is_valid:
                        valid_sessions.append(session)
                        session_cache[session] = csrf
                    else:
                        invalid_sessions.append(session)
                except Exception as e:
                    invalid_sessions.append(session)
                
                progress.update(task, advance=1)
    
    console.print(f"[bold green]✓ Found {len(valid_sessions)} valid sessions[/bold green]")
    console.print(f"[bold red]✗ Excluded {len(invalid_sessions)} invalid sessions[/bold red]")
    
    with open("valid_sessions.txt", "w") as f:
        f.write("\n".join(valid_sessions))
    
    with open("invalid_sessions.txt", "w") as f:
        f.write("\n".join(invalid_sessions))
    
    console.print("[bold green]✓ Valid sessions saved to 'valid_sessions.txt'[/bold green]")
    console.print("[bold red]✗ Invalid sessions saved to 'invalid_sessions.txt'[/bold red]")
    
    return valid_sessions

def report_instagram(target_id, sessionid, csrftoken, reportType):
    try:
        r3 = post(
            f"https://i.instagram.com/users/{target_id}/flag/",
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0",
                "Host": "i.instagram.com",
                "cookie": f"sessionid={sessionid}",
                "X-CSRFToken": csrftoken,
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
            },
            data=f'source_name=&reason_id={reportType}&frx_context=',
            allow_redirects=False,
            timeout=15
        )
        return r3.status_code == 200
    except Exception as e:
        console.print(f"[bold red]Error during reporting: {str(e)}[/bold red]")
        return False

def display_header():
    logo = """

▒▒▒▒▒▐▀▀▀█▄▒▒▒▒▒▒▒▒▒
▒▒▒▒█▀─────█▒▒▒▒▒▒▒▒
▒▒▒█────▄─▄─▌▒▒▒▒▒▒▒
▒▒▒▌───██─█▌▌▒▒▒▒▒▒▒
▒▒▒▌───█▌──▌▌▒▒▒▒▒▒▒
▒▒▒▌────────▌▒▒▒▒▒▒▒
▒▒█─────────▐▒▒▒▒▒▒▒
▒▐▌─▐───────▐▄▄▒▒▒▒▒
▒▐▌─▐────────▄▀▀█▒▒▒
▒█──▀▄──▄█▄▀▀▒▒▒▌▀▄▒
▐▌────██▀█░█▄▒▄▄█▀▀▌
▐▌──▌▐───▐░░▐▀░░░░░▌
▐▌──▌────▐░░▐░░░░░░▌
▐───▌────▐░░▐░░░░░░▌
▐───█────▐░░▐░░░░░░▌
▐───█────▐░░▐░░░░░░▌
▐───█─────▀█▐▄▄▄█▀▀▒
▀▄▄─▐───────▄█▒▒▒▒▒▒
▒▒▒▀█───█▄▀▀▀▒▒▒▒▒▒▒
▒▒▒▒▒▀▀▀▒▒▒▒▒▒▒▒▒▒▒▒

@𝑵𝑻𝑩𝒈𝒈 | 𝒕.𝒎𝒆/𝒂𝒍𝒊313𝒆𝒎𝒆

    """
    
    panel = Panel(
        Text(logo, style="bold white"),
        subtitle="[yellow]For ethical use only. Not responsible for misuse![/yellow]",
        border_style="bright_blue",
        box=box.DOUBLE
    )
    
    console.print(panel)

def display_stats(good_count, bad_count, sleep_time, valid_sessions, current_index=1):
    table = Table(show_header=True, header_style="bold magenta", box=box.SIMPLE)
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")
    
    table.add_row("Successful Reports", f"[bold green]{good_count}[/bold green]")
    table.add_row("Failed Reports", f"[bold red]{bad_count}[/bold red]")
    
    if valid_sessions and current_index <= len(valid_sessions):
        current_session = valid_sessions[current_index - 1]
        session_preview = current_session[:8] + "..."
        table.add_row("Active Session", f"[bold white]{session_preview}[/bold white]")
    else:
        table.add_row("Active Session", f"[bold white]None[/bold white]")
    
    table.add_row("Sleep Interval", f"[bold yellow]{sleep_time} seconds[/bold yellow]")
    
    console.print(table)
    
def starter():
    display_header()
    console.print("\n[bold cyan]→ Loading session data...[/bold cyan]")
    all_sessions = load_sessions("sessions.txt")
    console.print(f"[bold green]✓ Successfully loaded {len(all_sessions)} sessions[/bold green]\n")
    
    valid_sessions = filter_sessions(all_sessions)
    
    if not valid_sessions:
        console.print("[bold red]⚠️ No valid sessions! Please check the sessions.txt file[/bold red]")
        console.print("\n[bold yellow]Press Enter to exit...[/bold yellow]")
        input()
        return
    
    target_id = console.input("[bold magenta]ايدي الهدف  ID: [/bold magenta]").strip()

    table = Table(title="Available Report Types", show_header=True, header_style="bold blue", box=box.ROUNDED)
    table.add_column("Option", style="cyan", justify="center")
    table.add_column("Report Type", style="green")
    table.add_column("Description", style="yellow")

    report_options = {
        1: ("Spam", "Report for spam content or behavior"),
        2: ("Self", "Report for self-harm content"),
        3: ("Drugs", "Report for drug-related content"),
        4: ("Nudity", "Report for nudity or sexual content"),
        5: ("Violence", "Report for violent or threatening content"),
        6: ("Hate", "Report for hate speech or symbols"),
    }

    for key, (value, desc) in report_options.items():
        table.add_row(f"{key}", value, desc)
    
    console.print(table)

    while True:
        try:
            report_type = int(console.input("\n[bold yellow]Choose report type [1-6]: [/bold yellow]"))
            if report_type in report_options:
                break
            else:
                console.print("[bold red]Invalid choice. Try again.[/bold red]")
        except ValueError:
            console.print("[bold red]Invalid input. Enter a number.[/bold red]")

    reason_ids = {
        "Spam": 1,
        "Self": 2,
        "Drugs": 3,
        "Nudity": 4,
        "Violence": 5,
        "Hate": 6,
    }

    chosen_report = report_options[report_type][0]
    reason_id = reason_ids[chosen_report]
    console.print(f"[bold green]✓ Selected report type: [/bold green][cyan]{chosen_report}[/cyan]")

    multiple_sessions = len(valid_sessions) > 1
    if multiple_sessions:
        num_reports_per_session = int(console.input("\n[bold yellow]Enter number of reports per session: [/bold yellow]"))
    else:
        num_reports_per_session = 1
        console.print("[bold green]✓ Using single session mode[/bold green]")
    
    sleep_time = float(console.input("\n[bold yellow]Enter sleep time between reports (seconds): [/bold yellow]"))
    console.print(f"[bold green]✓ Reports will be sent every [/bold green][cyan]{sleep_time}[/cyan][bold green] seconds[/bold green]")

    console.print("\n[bold cyan]Starting reporting process...[/bold cyan]")
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[bold blue]{task.description}[/bold blue]"),
        BarColumn(bar_width=40),
        TextColumn("[bold cyan]{task.fields[info]}[/bold cyan]"),
        TimeElapsedColumn(),
        console=console,
        transient=True,
    ) as progress:
        task = progress.add_task("[bold red]Reporting...", total=None, info="Initializing...")
        
        good_count = 0
        bad_count = 0
        invalid_sessions = []
        show_final_stats = True

        try:
            while True:
                for i, sessionid in enumerate(valid_sessions[:]):
                    if sessionid in invalid_sessions:
                        continue
                        
                    progress.update(task, description=f"Processing session {i+1}/{len(valid_sessions)}", info=f"Good: {good_count} | Bad: {bad_count}")
                    
                    csrftoken = get_csrf_token(sessionid)
                    if not csrftoken:
                        bad_count += 1
                        invalid_sessions.append(sessionid)
                        valid_sessions.remove(sessionid)
                        console.print(f"[bold red]⚠️ Session {sessionid[:8]}... is invalid and has been removed[/bold red]")
                        continue

                    session_success = 0
                    for j in range(num_reports_per_session):
                        try:
                            if report_instagram(target_id, sessionid, csrftoken, reason_id):
                                good_count += 1
                                session_success += 1
                            else:
                                bad_count += 1
                                is_valid, _ = validate_session(sessionid)
                                if not is_valid:
                                    invalid_sessions.append(sessionid)
                                    valid_sessions.remove(sessionid)
                                    console.print(f"[bold red]⚠️ Session {sessionid[:8]}... expired during operation and has been removed[/bold red]")
                                    break

                            progress.update(task, info=f"Good 𝑷𝑺: {good_count} | Bad: {bad_count}")
                            
                            if sleep_time > 0:
                                time.sleep(sleep_time)
                        except Exception as e:
                            bad_count += 1
                            console.print(f"[bold red]Error during report: {str(e)}[/bold red]")
                    
                    if multiple_sessions and i < len(valid_sessions) - 1:
                        progress.stop()
                        console.print(f"\n[bold green]✓ Completed {session_success} reports with session {i+1}/{len(valid_sessions)}[/bold green]")
                        display_stats(good_count, bad_count, sleep_time, valid_sessions, i+1)
                        console.print("\n[bold yellow]Press Ctrl+C to stop or wait for next session...[/bold yellow]")
                        time.sleep(3)
                        progress.start()
                
                with open("valid_sessions.txt", "w") as f:
                    f.write("\n".join(valid_sessions))
                
                if not valid_sessions:
                    console.print("\n[bold red]⚠️ No valid sessions remaining! Operation stopped.[/bold red]")
                    console.print("\n[bold yellow]Press Enter to exit...[/bold yellow]")
                    input()
                    break
                
                if multiple_sessions:
                    progress.stop()
                    console.print("\n")
                    current_session = i+1 if 'i' in locals() and valid_sessions else 1
                    display_stats(good_count, bad_count, sleep_time, valid_sessions, current_session)
                    console.print("\n[bold yellow]Press Ctrl+C to stop or wait for next cycle...[/bold yellow]")
                    time.sleep(3)
                    progress.start()
                
        except KeyboardInterrupt:
            console.print("\n\n[bold green]✓ Operation interrupted by user[/bold green]")
            current_session = i+1 if 'i' in locals() and valid_sessions else 1
            display_stats(good_count, bad_count, sleep_time, valid_sessions, current_session)
            console.print("\n[bold cyan]Thank you for using INSTA EK6Q Reporter[/bold cyan]")
            console.print("\n[bold yellow]Press Enter to exit...[/bold yellow]")
            input()

if __name__ == "__main__":
    try:
        starter()
    except Exception as e:
        console.print(f"\n[bold red]An error occurred: {str(e)}[/bold red]")
    finally:
        console.print("\n[bold yellow]Press Enter to exit...[/bold yellow]")
        input()