from Link import SingleLink

def mergelink(alink:SingleLink,blink:SingleLink)->SingleLink:
    a = alink._head
    b = blink._head
    clink = SingleLink()
    while a!=None and b!=None:
        if a.value <= b.value:
            clink.append(a.value)
            a = a.next
        else:
            clink.append(b.value)
            b = b.next
    while a != None:
        clink.append(a.value)
        a = a.next
    while b != None:
        clink.append(b.value)
        b = b.next
    return clink

if __name__ == "__main__":
    alink = SingleLink()
    blink = SingleLink()
    for i in range(1,10,2):
        alink.append(i)
    for i in range(0,10,2):
        blink.append(i)
    clink = mergelink(alink,blink)
    clink.travel()
    