import time
import pandas as pd

counter=0
sf = float(input("Enter the drawing scale: "))
standard_pieces = pd.DataFrame(columns=['H1XW1', 'Pieces', 'Joint'])
extra_pieces = pd.DataFrame(columns=['H1XW1', 'Length', 'Joint'])
fittings = pd.DataFrame(columns=["Fitting Name", "C1", "W1", "C2", "W2", "T1", "T2", "OFF-1", "OFF-2", "L", "R", "Joint 1", "Joint 2"])
stan_lis_sec=[]
stan_lis_no=[]
stan_lis_joint=[]

extr_lis_sec=[]
extr_lis_len=[]
extr_lis_joint=[]

fitt_lis_name=[]
while True:
    start_point =input("To Start a Duct line Press any key\nPress Q to Quit\n")
    if start_point == 'q' or start_point == 'Q':
        standard_pieces.to_csv('MainPieces.csv')
        extra_pieces.to_csv('Extra.csv')
        fittings.to_csv('Fittings.csv')
        break
    else:
        print("\n"*100)
        duct_len = float(input("Enter the length of the duct line: "))*1000
        print("\n"*100)
        cross_wid = float(input("Enter the cross sectional width: "))
        print("\n"*100)
        cross_hie = float(input("Enter the cross sectional hieght: "))
        print("\n"*100)
        cross_area = cross_wid*cross_hie
        duct_len = duct_len*sf
        if cross_area <= 12*6:
            print("This is a slip joint!!")
            piece_no = duct_len // 1200
            excess_len = (duct_len % 1200)
            time.sleep(2)
            print("\n"*100)
            print("Standard Slip Duct(1200mm) # = {}pieces, The Extra piece Length = {}mm".format(piece_no, excess_len))
            time.sleep(2)
            a=str(cross_wid)+" X "+str(cross_hie)
            b=str(piece_no)
            c=str(cross_wid)+" X "+str(cross_hie)
            d=str(excess_len)
            joint='Slip'

            stan_lis_sec.append(a)
            stan_lis_joint.append(joint)
            stan_lis_no.append(b)

            extr_lis_sec.append(a)
            extr_lis_joint.append(joint)
            extr_lis_len.append(d)
            for i,j,k,l in zip(stan_lis_sec, stan_lis_no, stan_lis_joint, range(len(stan_lis_sec))):
                standard_pieces.loc[l]=[i,j,k]
            for i,j,k,l in zip(extr_lis_sec, extr_lis_len, extr_lis_joint, range(len(extr_lis_sec))):
                extra_pieces.loc[l]=[i,j,k]

            while True:
                print("\n"*100)
                trig=input("Want to pass a fitting? Y or N: \nEnter Q to quit...\n")
                trig.lower()
                if trig=='q':
                    break
                elif trig == 'n':
                    pass

                elif trig=='y':
                    while True:
                        print("\n"*100)
                        fitt_type=int(input("Choose the fitting: \nELBOW-45 OFFSET TRANSITION ELBOW-A ELBOW-B    Straight Line/Exit\n    1      2        3        4       5              9\n"))

                        if fitt_type == 1:
                            counter = counter + 1
                            C1=float(input("Enter The Width (C1) in inches: "))
                            W1=float(input("Enter The Hieght (W1) in inches: "))
                            C2=float(input("Enter The Width (C2) of the next Duct in inches: "))
                            W2=float(input("Enter The Hieght (W2) of the next Duct in inches: "))
                            if C1*W1 <= 12*6:
                                joint1 = "Slip"
                            else:
                                joint1 = "TDC"

                            if C2*W2 <= 12*6:
                                joint2 = "Slip"
                            else:
                                joint2 = "TDC"
                            T1=float(input("Enter T1 in cm: "))*sf*1000
                            T2=float(input("Enter T2 in cm: "))*sf*1000
                            fittings.loc[counter]=["ELBOW-45",C1,W1,C2,W2,T1,T2,"None","None","None","None", joint1, joint2]


                        elif fitt_type == 2:
                            counter = counter + 1
                            C1=float(input("Enter The Width (C1) in inches: "))
                            W1=float(input("Enter The Hieght (W1) in inches: "))
                            C2=float(input("Enter The Width (C2) of the next Duct: "))
                            W2=float(input("Enter The Hieght (W2) of the next Duct: "))
                            if C1*W1 <= 12*6:
                                joint1 = "Slip"
                            else:
                                joint1 = "TDC"

                            if C2*W2 <= 12*6:
                                joint2 = "Slip"
                            else:
                                joint2 = "TDC"
                            OFF_1=float(input("Enter OFF1 in cm: "))*sf*1000
                            L=float(input("Enter the length in cm: "))*sf*1000
                            fittings.loc[counter]=["OFFSET",C1,W1,C2,W2,"None","None",OFF_1,"None",L,"None", joint1, joint2]

                        elif fitt_type == 3:
                            counter = counter + 1
                            C1=float(input("Enter The Width (C1) in inches: "))
                            W1=float(input("Enter The Hieght (W1) in inches: "))
                            C2=float(input("Enter The Width (C2) of the next Duct in inches: "))
                            W2=float(input("Enter The Hieght (W2) of the next Duct in inches: "))
                            if C1*W1 <= 12*6:
                                joint1 = "Slip"
                            else:
                                joint1 = "TDC"

                            if C2*W2 <= 12*6:
                                joint2 = "Slip"
                            else:
                                joint2 = "TDC"
                            OFF_1=float(input("Enter OFF1 in cm: "))*sf*1000
                            OFF_2=float(input("Enter OFF2 in cm: "))*sf*1000
                            fittings.loc[counter]=["TRANSITION",C1,W1,C2,W2,"None","None",OFF_1,OFF_2,"None","None", joint1, joint2]

                        elif fitt_type == 4:
                            counter = counter + 1
                            C1=float(input("Enter The Width (C1) in inches: "))
                            W1=float(input("Enter The Hieght (W1) in inches: "))
                            C2=float(input("Enter The Width (C2) of the Next Duct in inches: "))
                            W2=float(input("Enter The Hieght (W2) of the Next Duct in inches: "))
                            if C1*W1 <= 12*6:
                                joint1 = "Slip"
                            else:
                                joint1 = "TDC"

                            if C2*W2 <= 12*6:
                                joint2 = "Slip"
                            else:
                                joint2 = "TDC"
                            T1=float(input("Enter T1 in cm: "))*sf*1000
                            T2=float(input("Enter T2 in cm: "))*sf*1000
                            fittings.loc[counter]=["ELBOW-A",C1,W1,C2,W2,T1,T2,"None","None","None","None", joint1, joint2]

                        elif fitt_type == 5:
                            counter = counter + 1
                            C1=float(input("Enter The Width (C1) in inches: "))
                            W1=float(input("Enter The Hieght (W1) in inches: "))
                            C2=float(input("Enter The Width (C2) of the Next Duct in inches: "))
                            W2=float(input("Enter The Hieght (W2) of the Next Duct in inches: "))
                            if C1*W1 <= 12*6:
                                joint1 = "Slip"
                            else:
                                joint1 = "TDC"

                            if C2*W2 <= 12*6:
                                joint2 = "Slip"
                            else:
                                joint2 = "TDC"
                            print(joint1)
                            print(joint2)
                            R=float(input("Enter The Radius (R) of the elbow in cm: "))*sf*1000
                            fittings.loc[counter]=["ELBOW-B", C1, W1, C2, W2, "None", "None", "None", "None", "None", R, joint1, joint2]

                        elif fitt_type == 9:
                            break
            else:
                print("\n"*100)
                print("Input is not accepted")


        else:
            print("This is a TDC duct")
            piece_no = duct_len // 1130
            excess_len = (duct_len % 1130)
            print("Standard TDC Duct(1130) # = {}, The Extra piece Length = {}mm".format(piece_no, excess_len))
            time.sleep(2)
            print("\n"*100)
            a=str(cross_wid)+" X "+str(cross_hie)
            b=piece_no
            c=str(cross_wid)+" X "+str(cross_hie)
            d=excess_len
            joint="TDC"

            stan_lis_sec.append(a)
            stan_lis_joint.append(joint)
            stan_lis_no.append(b)

            extr_lis_sec.append(a)
            extr_lis_joint.append(joint)
            extr_lis_len.append(d)
            for i,j,k,l in zip(stan_lis_sec, stan_lis_no, stan_lis_joint, range(len(stan_lis_sec))):
                standard_pieces.loc[l]=[i,j,k]
            for i,j,k,l in zip(extr_lis_sec, extr_lis_len, extr_lis_joint, range(len(extr_lis_sec))):
                extra_pieces.loc[l]=[i,j,k]

            trig=input("Want to pass a fitting? Y or N: \nEnter Q to quit...\n")
            trig.lower()
            if trig=='q':
                break
            elif trig=='n':
                pass

            elif trig=='y':
                    while True:
                        print("\n"*100)
                        fitt_type=int(input("Choose the fitting: \nELBOW-45 OFFSET TRANSITION ELBOW-A ELBOW-B    Straight Line/Exit\n    1      2        3        4       5              9\n"))
                        if fitt_type == 1:
                            counter = counter + 1
                            C1=float(input("Enter The Width (C1) in inches: "))
                            W1=float(input("Enter The Hieght (W1) in inches: "))
                            C2=float(input("Enter The Width (C2) of the next Duct in inches: "))
                            W2=float(input("Enter The Hieght (W2) of the next Duct in inches: "))
                            if C1*W1 <= 12*6:
                                joint1 = "Slip"
                            else:
                                joint1 = "TDC"

                            if C2*W2 <= 12*6:
                                joint2 = "Slip"
                            else:
                                joint2 = "TDC"
                            T1=float(input("Enter T1 in cm: "))*sf*1000
                            T2=float(input("Enter T2 in cm: "))*sf*1000
                            fittings.loc[counter]=["ELBOW-45",C1,W1,C2,W2,T1,T2,"None","None","None","None", joint1, joint2]


                        elif fitt_type == 2:
                            counter = counter + 1
                            C1=float(input("Enter The Width (C1) in inches: "))
                            W1=float(input("Enter The Hieght (W1) in inches: "))
                            C2=float(input("Enter The Width (C2) of the next Duct: "))
                            W2=float(input("Enter The Hieght (W2) of the next Duct: "))
                            if C1*W1 <= 12*6:
                                joint1 = "Slip"
                            else:
                                joint1 = "TDC"

                            if C2*W2 <= 12*6:
                                joint2 = "Slip"
                            else:
                                joint2 = "TDC"
                            OFF_1=float(input("Enter OFF1 in cm: "))*sf*1000
                            L=float(input("Enter the length in cm: "))*sf*1000
                            fittings.loc[counter]=["OFFSET",C1,W1,C2,W2,"None","None",OFF_1,"None",L,"None", joint1, joint2]

                        elif fitt_type == 3:
                            counter = counter + 1
                            C1=float(input("Enter The Width (C1) in inches: "))
                            W1=float(input("Enter The Hieght (W1) in inches: "))
                            C2=float(input("Enter The Width (C2) of the next Duct in inches: "))
                            W2=float(input("Enter The Hieght (W2) of the next Duct in inches: "))
                            if C1*W1 <= 12*6:
                                joint1 = "Slip"
                            else:
                                joint1 = "TDC"

                            if C2*W2 <= 12*6:
                                joint2 = "Slip"
                            else:
                                joint2 = "TDC"
                            OFF_1=float(input("Enter OFF1 in cm: "))*sf*1000
                            OFF_2=float(input("Enter OFF2 in cm: "))*sf*1000
                            fittings.loc[counter]=["TRANSITION",C1,W1,C2,W2,"None","None",OFF_1,OFF_2,"None","None", joint1, joint2]

                        elif fitt_type == 4:
                            counter = counter + 1
                            C1=float(input("Enter The Width (C1) in inches: "))
                            W1=float(input("Enter The Hieght (W1) in inches: "))
                            C2=float(input("Enter The Width (C2) of the Next Duct in inches: "))
                            W2=float(input("Enter The Hieght (W2) of the Next Duct in inches: "))
                            if C1*W1 <= 12*6:
                                joint1 = "Slip"
                            else:
                                joint1 = "TDC"

                            if C2*W2 <= 12*6:
                                joint2 = "Slip"
                            else:
                                joint2 = "TDC"
                            T1=float(input("Enter T1 in cm: "))*sf*1000
                            T2=float(input("Enter T2 in cm: "))*sf*1000
                            fittings.loc[counter]=["ELBOW-A",C1,W1,C2,W2,T1,T2,"None","None","None","None", joint1, joint2]

                        elif fitt_type == 5:
                            counter = counter + 1
                            C1=float(input("Enter The Width (C1) in inches: "))
                            W1=float(input("Enter The Hieght (W1) in inches: "))
                            C2=float(input("Enter The Width (C2) of the Next Duct in inches: "))
                            W2=float(input("Enter The Hieght (W2) of the Next Duct in inches: "))
                            if C1*W1 <= 12*6:
                                joint1 = "Slip"
                            else:
                                joint1 = "TDC"

                            if C2*W2 <= 12*6:
                                joint2 = "Slip"
                            else:
                                joint2 = "TDC"
                            R=float(input("Enter The Radius (R) of the elbow in cm: "))*sf*1000
                            fittings.loc[counter]=["ELBOW-B", C1, W1, C2, W2, "None", "None", "None", "None", "None", R, joint1, joint2]

                        elif fitt_type == 9:
                            break
            else:
                print("\n"*100)
                print("Input is not accepted")
