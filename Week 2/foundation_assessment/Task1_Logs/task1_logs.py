from datetime import datetime, timedelta, date

data = [ 
    "  2026-05-04 |  user_jdoe  |  LOGIN_SUCCESS  | IP:192.168.1.1 ",
    "  2026-07-06 |  user_goody  |  LOGIN_SUCCESS  | IP:192.168.1.81 ",
    "  2026-02-04 |  user_bluechief  |  LOGIN_SUCCESS  | IP:192.168.1.21 ",
    "  2026-12-25 |  user_miebi  |  LOGIN_SUCCESS  | IP:192.168.1.18 ",
    "  2026-05-25 |  user_godswill  |  LOGIN_SUCCESS  | IP:192.168.1.10 ",
    "  2026-05-27 |  user_willz  |  LOGIN_SUCCESS  | IP:192.168.1.12 ",
    "  2026-11-18 |  user_jane  |  LOGIN_SUCCESS  | IP:192.168.1.61 ",
    "  2026-05-09 |  user_jjoe  |  LOGIN_SUCCESS  | IP:192.168.1.51 ",
    "  2026-07-10 |  user_jite  |  LOGIN_SUCCESS  | IP:192.168.1.91 ",
    "  2026-09-24 |  user_piko  |  LOGIN_SUCCESS  | IP:192.168.1.25 "
]

for raw_log in data:

    trimmed_raw_log = raw_log.strip()
    split_raw_log = trimmed_raw_log.split("|")

    username = split_raw_log[1].strip()
    ip_address = split_raw_log[3].strip()
    date_obj = split_raw_log[0].strip()

    final_username = username.split("_")[1].upper()
    final_ip_address = ip_address.split(":")[1]
    final_date = datetime.strptime(date_obj, "%Y-%m-%d").date()
    days = (date(final_date.year, 12, 31) - final_date).days

    fin_date = final_date.strftime("%d/%m/%Y")
#print(final_username)
#print(final_ip_address)
    print(f"[SECURITY ALERT]: User {final_username} accessed from {final_ip_address} on {fin_date}. Days remaining in year: {days}.")