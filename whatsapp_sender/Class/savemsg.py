class message:
    def save(msg):
        savemsg_file = open(r"msg/msg.txt",'w',encoding='utf8')
        savemsg_file.write(msg)
    
    def readfile():
        msg_file = open(r"msg/msg.txt",'r', encoding='utf8')
        return msg_file.read()