import secrets
s = secrets.token_hex(3)
purpose = input(" do you want to decode or encode a message?")

if purpose == "encode":
  
  message = input("enter your message without space in between words")
  if len(message) % 2 == 0:
    k = len(message) // 2
    p = message[0:k]
    w = p[::-1]

    q = message[k:]
    e = q[::-1]
    j = w + e
    print(f'{s}{w}{s}{e}')
  else :
    a=(len(message)-1)
    b=a//2
    c=message[0:b]
    d=c[::-1]
    f=message[b:]
    g=f[::-1]
    print(f'{s}{d}{s}{g}')


if purpose == "decode":
  message2= input("enter your coded message") 
  if len(message2)!= 0: 
    n=len(message2)-12
    y=n//2
    r=message2[6:6+y]
    l=r[::-1]
    z=12+y
    t=message2[z:]
    v=t[::-1]
    print(f'{l}{v}')