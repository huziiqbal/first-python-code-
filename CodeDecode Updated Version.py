code = {"A":"e6*","B":"g4@","C":"z1*","D":"j6*","E":"v7#","F":"o3@","G":"q1@","H":"c6*"," ":"yt$","I":"m7#","J":"s8$","K":"p2*","L":"x2#","M":"h8@","N":"w9*","O":"f3#","P":"b9*","Q":"r3$","R":"d1#","S":"y5*","T":"i4$","U":"a4#","V":"l5@","W":"t1#","X":"k5*","Y":"n7$","Z":"u2*"}
purpose = input(" do you want to decode or encode a message?")
k=[]
if purpose == "encode":
    message = input("enter your message in capital letters ")
    for u in message:
        k.append(u)
    for u in k:
        print(code[u],end = "")
        
if purpose == "decode":
    message2 = input("enter your coded message")
    i=3
    y=0
    r=[]
    while i <=len(message2):
        m=message2[y:i]
        i=i+3
        y=y+3
        r.append(m)
    for y in r:
     e = {v: k for k, v in code.items()}
     print(e[y], end="")
     