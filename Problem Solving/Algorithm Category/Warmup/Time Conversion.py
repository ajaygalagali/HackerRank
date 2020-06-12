
s = input()

spm = s.replace("PM", "")
only = spm.replace("AM","")
elements = only.split(":")
hour = int(elements[0])
twenty_hour = int(elements[0])+12
if "AM" in s:

    if hour == 12:
        print("00:"+elements[1]+":"+elements[2])
    else:
        print(only)

else:

    if hour == 12:
        print("12:"+elements[1]+":"+elements[2])
    else:
        print(str(twenty_hour)+":"+elements[1]+":"+elements[2])



