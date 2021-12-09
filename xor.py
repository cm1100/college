print("Raghav Soni A2305218217 7CSE-4X")
con="y"
while(con=="y"):
    ch=int(input("\nEnter number of inputs (2/3): "))
    if ch==2:
        A=[0,1]
        B=[0,1]
        print("\nA","B","A.(~B)","(~A).B","A^B",sep="    ")
        for i in range(2):
            for j in range(2):
                print(str(A[i]),"   "+str(B[j]),"     "+str(A[i]&(~B[j])),"         "+str((~A[i])&B[j]),"      "+str(A[i]^B[j]))
    elif ch==3:
        A=[0,1]
        B=[0,1]
        C=[0,1]
        print("\nA","B","C","ABC","A'B'C","A'BC'","AB'C'","A^B^C",sep="    ")
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    print(str(A[i]),"   "+str(B[j]),"   "+str(C[k]),"    "+str(A[i]&B[j]&C[k]),"      "+str((~A[i])&(~B[j])&C[k]),"       "+str((~A[i])&B[j]&(~C[k])),"       "
                    +str(A[i]&(~B[j])&(~C[k])),"       "+str(A[i]^B[j]^C[k]))

    con=input("\nContinue (y/n): ")
