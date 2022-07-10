import imaplib
import email
import traceback

MY_EMAIL = "litvakpatricia@gmail.com"
# appPassword - only when 2-step verification turned on in gmail account
# required because google disabled "less secure apps" option
MY_PWD = "qplryqbofyzmbfbm"
SERVER = "imap.gmail.com"
PORT = 993


def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SERVER)
        mail.login(MY_EMAIL, MY_PWD)
        mail.select('inbox')

        data = mail.search(None, 'X-GM-RAW "Category:Primary"')
        mail_id = data[1]
        id_list = mail_id[0].split()
        print('The total number of emails in the Primary tab(task 8): ' + str(len(id_list)) + '\n')
        Nth = 9
        Nth_mail_data = mail.fetch(str(int(id_list[Nth - 1])), '(RFC822)')
        print('Get the Nth Email(task 9):\n')
        print_mail(Nth_mail_data, Nth - 1)
        print_all_senders_and_subjects_in_inbox(id_list, mail)

    except Exception as e:
        traceback.print_exc()
        print(str(e))


def print_all_senders_and_subjects_in_inbox(id_list, mail):
    print('All E-mails from Primary tab(task10):\n')
    for n in range(0, len(id_list), +1):
        data = mail.fetch(str(int(id_list[n])), '(RFC822)')
        print_mail(data, n)


def print_mail(data, n):
    for response_part in data:
        arr = response_part[0]
        if isinstance(arr, tuple):
            message = email.message_from_string(str(arr[1], 'utf-8'))
            email_subject = message['subject']
            email_from = message['from']
            print('Email number ' + str(n + 1) + ':' + '\n')
            print('Sender : ' + email_from)
            print('Mail Subject : ' + email_subject + '\n')


if __name__ == '__main__':
    read_email_from_gmail()
