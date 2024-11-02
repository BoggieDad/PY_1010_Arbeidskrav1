"""
Created on Sat Nov 02 17:12:00 2024

@author: Borgar Stenseth
e-post: borgar.stenseth@gmail.com
Revision: Rev01
"""
K = 15000  #[km] kjørelengde
D = 365  #[dager] 
F_El = 5000  #[kr] per år
F_Bensin = 7500  #[kr] per år
TF = 8.38  #[kr] avgift per dag
DF_El = 0.2  #[kWh/km] forbruk
SP = 2.0  #[kr/kWh] strømpris
DF_Bensin = 1.0  #[kr/km] drivstoff forbruk bensinbil
Bom_el = 0.1  #[kr/km]bomavgift el
Bom_ben = 0.3  #[kr/km]bomavgift bensin
#%% Delformler
TFY = TF*D  #[kr] Traffikforsikringsavgift per år
DFY_El = DF_El*SP*K
DFY_Ben = DF_Bensin*K
Bom_El_Y = Bom_el*K
Bom_ben_Y = Bom_ben*K
#%% Utregning for El bil, Bensin Bil og prosent
El_Bil = F_El + TFY + DFY_El + Bom_El_Y
Ben_Bil = F_Bensin + TFY + DFY_Ben + Bom_ben_Y
Bil_prosent = (El_Bil/Ben_Bil)*100
Bil_diff = Ben_Bil - El_Bil
#%% Utskrift
print("Årlig driftskostnad for elektrisk bil er", round(El_Bil,0),"kroner mens for en bensinbil er den", round(Ben_Bil,0), "kroner. Det betyr at en el bil vil ha ", round(Bil_prosent,2), "prosent lavere driftskostnad enn en bensin bil per år med en kjørelengde på:", K, "kilometer i året")
print ("Differansen mellom elektrisk bil og bensin bil i kroner er da at bensinbilen er", Bil_diff, "kroner dyrere i drift enn en elektrisk bil per år med en kjørelengde på", K, "kilometer i året.")