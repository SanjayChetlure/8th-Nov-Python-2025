#Example2: Multi_Level Inheritance

#super class
class WhatsAppV1:
    def textMsg(self):
        print("text msg")

#sub/super class
class WhatsAppV2(WhatsAppV1):
    def ac(self):
        print("Audio Calling")

    # def textMsg(self):
    #     print("text msg")

#sub/super class
class WhatsAppV3(WhatsAppV2):
    def vc(self):
        print("Video Calling")

    # def ac(self):
    #     print("Audio Calling")

    # def textMsg(self):
    #     print("text msg")

#sub class
class WhatsAppV4(WhatsAppV3):
    def status(self):
        print("Status")

    # def vc(self):
    #     print("Video Calling")

    # def ac(self):
    #     print("Audio Calling")

    # def textMsg(self):
    #     print("text msg")

v4=WhatsAppV4()
v4.textMsg()
v4.ac()
v4.vc()
v4.status()