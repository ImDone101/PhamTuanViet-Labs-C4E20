from gmail import GMail, Message
from random import choice
from datetime import datetime
html_content = """
<p style="text-align: center;"><strong>CỘNG H&Ograve;A X&Atilde; HỘI CHỦ NGHĨA VIỆT NAM</strong></p>
<p style="text-align: center;"><strong>Độc lập - Tự do - Hạnh ph&uacute;c</strong></p>
<p style="text-align: center;"><strong>ĐƠN XIN NGHỈ HỌC</strong></p>
<p style="text-align: justify;">K&iacute;nh gửi: Gi&aacute;o vi&ecirc;n chủ nhiệm lớp</p>
<p style="text-align: justify;">T&ecirc;n em l&agrave; Phạm Tuấn Việt.</p>
<p style="text-align: justify;">H&ocirc;m nay em viết đơn n&agrave;y l&agrave; để xin thầy cho em nghỉ buổi học v&agrave;o tối nay {{sickness}} Em xin hứa sẽ học b&agrave;i v&agrave; l&agrave;m b&agrave;i đầy đủ Em xin cảm ơn !</p>
<p style="text-align: justify;">Tuấn Việt</p> """

reason =['để đi chơi','do em bị tai nạn','do em bị bệnh']

#time
now = str(datetime.now())[11:]
limit = now[:5]

condi = True
while limit > '07:00' and condi:
    reason_random = choice(reason)
    html_new = html_content.replace("{{sickness}}", reason_random )

    gmail = GMail('vietc4e20@gmail.com', 'Viet5564833')
    msg = Message('Text Message',to='20130075@student.hust.edu.vn',html=html_new)
    gmail.send(msg)
    condi = False