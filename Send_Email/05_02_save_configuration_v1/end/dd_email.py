import dd_content
import datetime
import smtplib
from email.message import EmailMessage

class DailyDigestEmail:

    def __init__(self):
        self.content = {'quote': {'include': True, 'content': dd_content.get_random_quote()},
                        'weather': {'include': False, 'content': dd_content.get_weather_forecast()},
                        'twitter': {'include': False, 'content': dd_content.get_twitter_trends()},
                        'wikipedia': {'include': False, 'content': dd_content.get_wikipedia_article()}}

        self.recipients_list = ['test@test.com']

        self.cc_list = ['']

        self.bcc_list = ['']

        self.sender_credentials = {'email': '(Ronghui Zhou)rzhou11@its.jnj.com', # your sender email address
                                   'password': 'password'} # your sender password

    """
    Send digest email to all recipients on the recipient list.
    """
    def send_email(self):
        # build email message
        msg = EmailMessage()
        msg['Subject'] = f'Daily Digest - {datetime.date.today().strftime("%d %b %Y")}'
        msg['From'] = self.sender_credentials['email']
        msg['To'] = ', '.join(self.recipients_list)
        msg['Cc'] = ', '.join(self.cc_list)
        msg['Bcc'] = ', '.join(self.bcc_list)

        # add Plaintext and HTML content
        msg_body = self.format_message()
        msg.set_content(msg_body['text'])
        msg.add_alternative(msg_body['html'], subtype='html')

        # secure connection with STMP server and send email
        smtp_server = 'smtp.na.jnj.com'
        smtp_port = 25
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.ehlo()
            server.starttls()

            # no need to login from jnj
            if 'jnj.com' not in smtp_server:
                server.login(self.sender_credentials['email'],
                             self.sender_credentials['password'])
            server.send_message(msg)

    """
    Generate email message body as Plaintext and HTML.
    """
    def format_message(self):
        ##############################
        ##### Generate Plaintext #####
        ##############################
        text = f'*~*~*~*~* Daily Digest - {datetime.date.today().strftime("%d %b %Y")} *~*~*~*~*\n\n'

        # format random quote
        if self.content['quote']['include'] and self.content['quote']['content']:
            text += '*~*~* Quote of the Day *~*~*\n\n'
            text += f'"{self.content["quote"]["content"]["quote"]}" - {self.content["quote"]["content"]["author"]}\n\n'

        # format weather forecast
        if self.content['weather']['include'] and self.content['weather']['content']:
            text += f'*~*~* Forecast for {self.content["weather"]["content"]["city"]}, {self.content["weather"]["content"]["country"]} *~*~*\n\n'
            for forecast in self.content['weather']['content']['periods']:
                text += f'{forecast["timestamp"].strftime("%d %b %H%M")} - {forecast["temp"]}\u00B0C | {forecast["description"]}\n'
            text += '\n'

        # format Twitter trends
        if self.content['twitter']['include'] and self.content['twitter']['content']:
            text += '*~*~* Top Ten Twitter Trends *~*~*\n\n'
            for trend in self.content['twitter']['content'][0:10]: # top ten
                text += f'{trend["name"]}\n'
            text += '\n'

        # format Wikipedia article
        if self.content['wikipedia']['include'] and self.content['wikipedia']['content']:
            text += '*~*~* Daily Random Learning *~*~*\n\n'
            text += f'{self.content["wikipedia"]["content"]["title"]}\n{self.content["wikipedia"]["content"]["extract"]}'
        
        #########################
        ##### Generate HTML #####
        #########################
        html = f"""<html>
    <body>
    <center>
        <h1>Daily Digest - {datetime.date.today().strftime('%d %b %Y')}</h1>
        """

        # format random quote
        if self.content['quote']['include'] and self.content['quote']['content']:
            html += f"""
        <h2>Quote of the Day</h2>
        <i>"{self.content['quote']['content']['quote']}"</i> - {self.content['quote']['content']['author']}
        """

        # format weather forecast
        if self.content['weather']['include'] and self.content['weather']['content']:
            html += f"""
        <h2>Forecast for {self.content['weather']['content']['city']}, {self.content['weather']['content']['country']}</h2> 
        <table>
                    """

            for forecast in self.content['weather']['content']['periods']:
                html += f"""
            <tr>
                <td>
                    {forecast['timestamp'].strftime('%d %b %H%M')}
                </td>
                <td>
                    <img src="{forecast['icon']}">
                </td>
                <td>
                    {forecast['temp']}\u00B0C | {forecast['description']}
                </td>
            </tr>
                        """               

            html += """
            </table>
                    """

        # format Twitter trends
        if self.content['twitter']['include'] and self.content['twitter']['content']:
            html += """
        <h2>Top Ten Twitter Trends</h2>
                    """

            for trend in self.content['twitter']['content'][0:10]: # top ten
                html += f"""
        <b><a href="{trend['url']}">{trend['name']}</a></b><p>
                        """

        # format Wikipedia article
        if self.content['wikipedia']['include'] and self.content['wikipedia']['content']:
            html += f"""
        <h2>Daily Random Learning</h2>
        <h3><a href="{self.content['wikipedia']['content']['url']}">{self.content['wikipedia']['content']['title']}</a></h3>
        <table width="800">
            <tr>
                <td>{self.content['wikipedia']['content']['extract']}</td>
            </tr>
        </table>
                    """

        # footer
        html += """
    </center>
    </body>
</html>
                """

        return {'text': text, 'html': html}

if __name__ == '__main__':
    email = DailyDigestEmail()

    ##### test format_message() #####
    print('\nTesting email body generation...')
    message = email.format_message()

    # print Plaintext and HTML messages
    print('\nPlaintext email body is...')
    print(message['text'])
    print('\n------------------------------------------------------------')
    print('\nHTML email body is...')
    print(message['html'])

    # save Plaintext and HTML messages to file
    with open('message_text.txt', 'w', encoding='utf-8') as f:
        f.write(message['text'])
    with open('message_html.html', 'w', encoding='utf-8') as f:
        f.write(message['html'])

    ##### test send_email() #####
    print('\nSending test email...')
    email.send_email()