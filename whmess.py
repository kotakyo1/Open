import pywhatkit
def send_messages():
    number = input('кому хочешь отправить(номер введи) ')
    message_text = input('что хочешь оправить ')
    thour = input('во сколько отвправить, введи время через двоеточие ').split(':')
    hour = int(thour[0])
    minute = int(thour[1])
    pywhatkit.sendwhatmsg(phone_no=number, message=message_text, time_hour=hour, time_min=minute)

def send_message_inst():
    number = input('кому хочешь отправить(номер введи) ')
    message_text = input('что хочешь оправить ')
    pywhatkit.sendwhatmsg_instantly(phone_no=number, message=message_text)

def send_group():
    name_group = 'Джентельмены удачи/W'
    message_text = input('что хочешь оправить ')
    thour = input('во сколько отвправить, введи время через двоеточие ').split(':')
    hour = int(thour[0])
    minute = int(thour[1])
    pywhatkit.sendwhatmsg_to_group(group_id=name_group, message=message_text, time_hour=hour, time_min=minute)

def main():
    send_message_inst()


if __name__ == '__main__':
    main()

