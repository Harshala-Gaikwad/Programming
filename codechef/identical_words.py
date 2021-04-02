for _ in range(int(input())):
    s1,s2,s3 = map(str, input().split())
    s1 = "".join(sorted(s1))
    s2="".join(sorted(s2))
    s3="".join(sorted(s3))
    #print(s2)
    if s1==s2 and s1==s3:
        print("Possible")
    else:
        print("Not Possible")
