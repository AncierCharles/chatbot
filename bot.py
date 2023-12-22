import datetime
import psutil  # Install it using 'pip install psutil'

def get_time():
    return datetime.datetime.now().strftime("%H:%M:%S")

def get_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")

def get_storage_space():
    total_space = psutil.disk_usage('/').total
    free_space = psutil.disk_usage('/').free
    used_space = total_space - free_space
    return f"Storage space: {used_space / (1024 ** 3):.2f} GB used out of {total_space / (1024 ** 3):.2f} GB."

def get_battery_capacity():
    try:
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        percent = battery.percent
        return f"Battery: {percent}%{' (Plugged in)' if plugged else ''}."
    except Exception as e:
        return f"Unable to retrieve battery information: {str(e)}"

def chatbot_response(message):
    if "time" in message:
        return f"The current time is {get_time()}."
    elif "date" in message:
        return f"Today's date is {get_date()}."
    elif "storage" in message or "space" in message:
        return get_storage_space()
    elif "battery" in message:
        return get_battery_capacity()
    else:
        return "Sorry, I didn't understand that."

# Example usage
user_input = input("Ask the chatbot: ")
response = chatbot_response(user_input)
print(response)
