#RANDOM USER GENERATER CS PROJECT
LONG='y'
while LONG=='y':
	print()
	print("WELCOME TO RANDOM USER GENERATER PROGRAM");
	print("Select");
	print('''[1] Male
	         [2] Female''');
	MNAME=['Satish','Ramesh','Max','Michel','Ram','Franklin','Triver','Lamar','Frester']
	male=len(MNAME)
	Caddress=['85,xyz,indore','59,dhr,Mumbai','56,jfk,Luciana','953,Rmaroff Gate,London','84,odh,delhi','22,hdm,delhi','224,Marconi Street,Wallington','005,Mochmall,Washington DC']
	address=len(Caddress)
	Cemailid=['satishxyz@gmail.com','Rameshdhr@gmail.com','Maxjfk@gmail.com','Michelbfc@gmail.com','Danealahdm@gmail.com','Saraswatikgt@gmail.com','anjellahbk@gmail.com']
	email=len(Cemailid)
	Cage=[23,62,56,25,32,82,45,58,92]
	age=len(Cage)
	Fname=['Anjali','Roamy','Daneala','Saraswati','Rima','Nirma','Sara','Dilpreet']
	female=len(Fname)
	
	import random
	
	adhaar=random.randrange(100000000000,999999999999)
	pancard=random.randrange(111111111111,888888888888)
	M=random.randrange(0,male)
	MI=MNAME[M];
	C_EMAIL=random.randrange(0,email)
	EMAILI=Cemailid[C_EMAIL];
	C_ADDRESS=random.randrange(0,address)
	ADDRESSI=Caddress[C_ADDRESS];
	C_AGE=random.randrange(0,age)
	AGEI=Cage[C_AGE];
	F=random.randrange(0,female)
	FI=Fname[F];
	choice=int(input("Press '1' for Male & '2' for Female"));
	if choice==1:
	    print("RANDOM MALE USER GENRATOR ARE-","\n","NAME OF MALE IS:-",MI,"\n","ADDRESS OF THE PERSON:-",ADDRESSI,"\n","EMAIL-ID OF THE PERSON:-",EMAILI,"\n","AGE OF THE PERSON:-",AGEI,"\n","ADHARCARD-NUMBER OF THE PERSON:-",adhaar,"\n","PANCARD-NUMBER OF THE PERSON:-",pancard)
	          
	elif choice==2:
	    print("RANDOM FEMALE USER GENRATOR ARE-","\n","NAME OF FEMALE IS:-",FI,"\n","ADDRESS OF THE PERSON:-",ADDRESSI,"\n","EMAIL-ID OF THE PERSON:-",EMAILI,"\n","AGE OF THE PERSON:-",AGEI,"\n","ADHARCARD-NUMBER OF THE PERSON:-",adhaar,"\n","PANCARD-NUMBER OF THE PERSON:-",pancard)
	LONG=str(input("you want to continue press'y'or No press'n'"))

else:
    print("THANK YOU FOR USEING RANDOM USER GENERATOR")


	
   
