#!/usr/bin/python3.2
i = 1
while 1:
    iSet = set(str(i))
    iiSet = set(str(2*i))
    if iSet == iiSet:
        iiSet = set(str(3*i))
        if iSet == iiSet:
            iiSet = set(str(4*i))
            if iSet == iiSet:
                iiSet = set(str(5*i))
                if iSet == iiSet:
                    iiSet = set(str(6*i))
                    if iSet == iiSet:
                        print(i)
                        break
    i += 1
