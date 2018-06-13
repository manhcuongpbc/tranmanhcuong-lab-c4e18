# Learn how to get the current hour of your computer
from datetime import datetime
time = datetime.now().minute
print(time)
while True:

    if datetime.now().hour == 13 and datetime.now().minute == 42:
        from gmail import GMail, Message
        import random
        gmail = GMail('CuongCaoCa<manhcuongpbc3@gmail.com>','159357456258')
        html_content = """ 
        <p style="text-align: center;"><strong>Cộng h&ograve;a x&atilde; hội chủ nghĩa Việt Nam</strong></p>
        <p style="text-align: center;"><strong>Độc lập - Tự do - Hạnh ph&uacute;c</strong></p>
        <p style="text-align: center;">&nbsp;</p>
        <p style="text-align: center;"><em><strong>ĐƠN XIN BỎ HỌC</strong></em></p>
        <p style="text-align: left;">&nbsp;</p>
        <p style="text-align: left;"><strong><em>K&iacute;nh gửi: Thầy gi&aacute;o chủ nhiệm of mine</em></strong></p>
        <p style="text-align: left;">Hello thầy, dạo gần đ&acirc;y em thấy {{lý do}}, thầy cho em nghỉ nh&eacute;!!!</p>
        <p style="text-align: left;">&nbsp;</p>
        <p><span style="text-decoration: line-through;">Cường super đz</span></p>
        """
        #placeholder

        reasons = ['Bị ốm', 'gia đình có việc', 'bạn gái có bầu', 'em trai thi đh']

        html_content_new = html_content.replace("{{lý do}}", random.choice(reasons))

        msg = Message('Thong bao Tang luong', to='manhcuongpbc2@gmail.com',html = html_content_new)
        # msg = Message('Thong bao Tang luong', to='20130075@student.hust.edu.vn',text='f*ck u', html ="<b>hello from\
        #  other site<b>")
        gmail.send(msg)
        break
    else:
        print('no')
        break