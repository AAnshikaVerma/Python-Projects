print("                                         🚕-WELCOME TO TRAVEL_SHAUKEENS-🚕")

current_location=input("PLEASE ENTER YOUR CURRENT LOCATION : ")
destination=input("PLEASE ENTER THE DESTINATION LOCATION : ")
nearby_riders_available=[["Ronak","CAB"] , ["Preet","CAB"] , ["Shwet","AUTO"] , ["Lavyansh","CAB"] , ["Aman","AUTO"]]
details_of_riders=[["9872724980" ,"4280 XYZ" , "White" , "SUV"],["8289247890" , "2982 ABC" , "Grey" , "Wagonar"],["7428827892" , "6789 MNO" , "Green and Yellow" , "AUTO"],["6289637480" , "42902 LMN" , "Black" , "Verna"],["7249093734" , "23451 PQR" , "Pink" , "AUTO"]]
for i in range(len(nearby_riders_available)):
    print(nearby_riders_available[i])

# choose between rider1 to rider5 only

rider1="Ronak"
rider2="Preet"
rider3="Shwet"
rider4="Lavyansh"
rider5="Aman"
riders=input("ENTER THE DRIVER YOU WOULD LIKE TO CHOOSE : ")     

if riders==rider1:
 print((details_of_riders[0][::]) , "CAB will be coming in 10 mins")
elif riders==rider2:
 print( (details_of_riders[1][::]) , "CAB will be coming in 20 mins")
elif riders==rider3:
 print( (details_of_riders[2][::]) , "AUTO will be coming in 12 mins")
elif riders==rider4:
 print( (details_of_riders[3][::]) , "CAB will be coming in 10 mins")
elif riders==rider5:
 print( (details_of_riders[4][::]) , "AUTO will be coming in 15 mins")
else:
    print("NO SERVICES AVAILABLE TO YOUR LOCATION")

# when the cab or auto is reached

print("CAB IS REACHED")

print("PLEASE ENTER THE OTP")

# after entering the OTP journey will start

print("YOUR JOURNEY HAS BEEN STARTED")

# when you reach the destination

print("YOUR JOURNEY HAS BEEN ENDED")

print("please select mode of payment")

payment_mode=input("enter the payment mode : ")

if payment_mode=="cash":
    print("you can give cash")
else:
    print("pay online")

# after payemnt next step is you have to give ratings and feedback to the driver

rating=input("enter the rating points :")
if rating=="***":
    print("The ride was excellent.")
elif rating=="**":
    print("The ride was good.")
elif rating=="*":
    print("The ride was okay.")
elif rating=="**":
    print("It was a bad ride.")
else:
    print(" I didnt like the ride at all.")

# after rating we need feedback

feedback=input("enter the feedback you would like to give to the driver : ")
print("                -🙏🏻THANK YOU FOR USING TRAVEL SHAUKEENS🙏🏻-")
print("                   -WE WOULD LOVE TO SEEE YOU AGAIN :)")