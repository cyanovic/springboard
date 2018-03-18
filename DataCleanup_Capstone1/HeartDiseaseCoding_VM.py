import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from scipy.stats.mstats import mode

'''
age: age in years; 
sex: sex (1 = male; 0 = female); 
cp: chest pain type -- Value 1: typical angina -- Value 2: atypical angina -- Value 3: non-anginal pain -- Value 4: asymptomatic;
trestbps: resting blood pressure (in mm Hg on admission to the hospital); 
chol: serum cholestoral in mg/dl; 
fbs: (fasting blood sugar > 120 mg/dl)  (1 = true; 0 = false),
restecg: resting electrocardiographic results -- Value 0: normal -- Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression
of > 0.05 mV) -- Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria; 
thalach: maximum heart rate achieved; 
exang: exercise induced angina (1 = yes; 0 = no); 
oldpeak = ST depression induced by exercise relative to rest; 
slope: the slope of the peak exercise ST segment -- Value 1: upsloping -- Value 2: flat -- Value 3: downsloping; 
ca: number of major vessels (0-3) colored by flourosopy; 
thal: 3 = normal; 6 = fixed defect; 7 = reversable defect;
num: diagnosis of heart disease (angiographic disease status) -- Value 0: < 50% diameter narrowing -- Value 1: > 50% diameter narrowing 
(in any major vessel: attributes 59 through 68 are vessels)

I was planning to use the unprocessed data files until I saw the warning file about corrupted information in the unprocessed cleveland file. 

Missing in cleveland and long beach and first processed hungarian is ? and missing in reprocessed hungarian is -9.0 and for newdata file.
First 304 of "newdata" file are cleveland data, so likely the newdata file is a combo of all, and maybe plus some, but it doesn't distinguish easily and has nearly all missing values outside of cleveland (for ca esp.)

When done can write files as like: out_csv = 'filename.csv' then filename.to_csv(out_csv) or out_tsv = 'filename.tsv' then filename.to_csv(out_tsv. sep='\t')

IMPORTANT NOTES FOR ANYONE READING THIS AS OF 3/12/18 UPLOAD:
***Data cleanup at this point involves reading the files in that I'll attempt to use, replacing missing values with NaN's and adding column names as appropriate.
***Right now I have changed datatypes mostly to floats, but that will change after I decide how to manage NaN's, since integer type doesn't accept those.
***Cleveland has essentially no NaN's, so I'm not too concerned there and identify that file as being a good source for developing the model, which I can test on others.
***The 'newdata' file seems to include cleveland and perhaps others, but will look at that later.
***NaN's in cleveland I'll switch out with likely the median or mode values. For other datasets it's unclear yet because some have several missing in a column, etc.
***I can either keep each file separate for analyses based on location, or combine them into a dataframe after I have developed the model and am testing it.
'''
#___________________________________________cleveland import_______________________________________________________________________________________________________
cleveland_df = pd.read_csv('.../Processed/processed_cleveland_data.csv', header=None, na_values = '?')
cleveland_df.columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'num']
cleveland_df['sex'] = cleveland_df['sex'].astype(float)
cleveland_df['cp'] = cleveland_df['cp'].astype(float)
cleveland_df['fbs'] = cleveland_df['fbs'].astype(float)
cleveland_df['restecg'] = cleveland_df['restecg'].astype(float)
cleveland_df['exang'] = cleveland_df['exang'].astype(float)
cleveland_df['slope'] = cleveland_df['slope'].astype(float)
cleveland_df['ca'] = cleveland_df['ca'].astype(float) #throws errors over the NaN for int, just changing these to floats for now
cleveland_df['thal'] = cleveland_df['thal'].astype(float)
cleveland_df.insert(0, 'location', 'Cleveland')
print('cleveland')
print(cleveland_df.head()) 
print(cleveland_df.columns) 
print(cleveland_df.info()) 

#___________________________________________hungarian import_______________________________________________________________________________________________________
hungarian_df = pd.read_csv('.../Processed/reprocessed_hungarian_data.txt', sep=" ", header=None, na_values = '-9.0')
hungarian_df.columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'num']
hungarian_df['sex'] = hungarian_df['sex'].astype(float)
hungarian_df['cp'] = hungarian_df['cp'].astype(float)
hungarian_df['fbs'] = hungarian_df['fbs'].astype(float)
hungarian_df['restecg'] = hungarian_df['restecg'].astype(float)
hungarian_df['exang'] = hungarian_df['exang'].astype(float)
hungarian_df['slope'] = hungarian_df['slope'].astype(float)
hungarian_df['ca'] = hungarian_df['ca'].astype(float)
hungarian_df['thal'] = hungarian_df['thal'].astype(float)
hungarian_df['num'] = hungarian_df['num'].astype(float)
hungarian_df.insert(0, 'location', 'Hungary')
print('hungarian')
print(hungarian_df.head()) 
print(hungarian_df.columns) 
print(hungarian_df.info()) 

#___________________________________________long beach import_______________________________________________________________________________________________________
long_beach_df = pd.read_csv('.../Processed/processed_va_data.csv', header=None, na_values = '?')
long_beach_df.columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'num']
long_beach_df['age'] = long_beach_df['age'].astype(float)
long_beach_df['fbs'] = long_beach_df['fbs'].astype(float)
long_beach_df['exang'] = long_beach_df['exang'].astype(float)
long_beach_df['slope'] = long_beach_df['slope'].astype(float)
long_beach_df['ca'] = long_beach_df['ca'].astype(float)
long_beach_df['thal'] = long_beach_df['thal'].astype(float)
long_beach_df.insert(0, 'location', 'Long_Beach')
print('long beach')
print(long_beach_df.head()) 
print(long_beach_df.columns) 
print(long_beach_df.info()) 

#___________________________________________new-data import_______________________________________________________________________________________________________
'''
new_data_df = pd.read_csv('.../Processed/new_data.txt', sep=" ", header=None)
#new_data_df.columns = ['ccf', 'age', 'sex', 'painloc', 'painexer', 'relrest', 'pncaden', 'cp', 'trestbps', 'htn', 'chol', 'smoke', 'cigs', 'years', 'fbs', 
#                       'dm', 'famhist', 'restecg', 'ekgmo', 'ekgday', 'ekgyr', 'dig', 'prop', 'nitr', 'pro', 'diuretic', 'proto', 'thaldur', 'thaltime', 'met',
#                       'thalach', 'thalrest', 'tpeakbps', 'tpeakbpd', 'dummy', 'trestbpd', 'exang', 'xhypo', 'oldpeak', 'slope', 'rldv5', 'rldv5e', 'ca', 'restckm', 'exerckm',
#                       'restef', 'restwm', 'exeref', 'exerwm', 'thal', 'thalsev', 'thalpul', 'earlobe', 'cmo', 'cday', 'cyr', 'num', 'lmt', 'ladprox', 'laddist',
#                       'diag', 'cxmain', 'ramus', 'om1', 'om2', 'rcaprox', 'rcadist', 'lvx1', 'lvx2', 'lvx3', 'lvx4', 'lvf', 'cathef', 'junk', 'name']
#A	B	age	sex	C	D	E	F	cp	trestbps		chol	G	H	I	fbs	J	K	restecg	L	M	N	O	P	Q	R	S	T	U	V	W	thalach	X	Y	Z	AA	BB	
#exang	CC	oldpeak	slope	DD	EE	ca	FF	GG	HH	II	JJ	KK	thal	LL	MM	NN	OO	PP	QQ	num	RR	SS	TT	UU	VV	WW	XX	YY	ZZ	AAA	BBB	CCC	DDD	EEE	FFF	GGG	
#HHH	III	JJJ	KLL	LLL	MMM	NNN	OOO	PPP	QQQ	RRR	SSS	TTT	UUU	VVV	WWW - a guide to placement of column names if needed
new_data_df.columns = ['A','B','age','sex','C','D','E','F','cp','trestbps',	'chol','G','H','I','fbs','J','K','restecg','L','M','N','O','P','Q','R','S',	'T','U',	'V','W','thalach','X','Y',	'Z',	'AA','BB','exang','CC','oldpeak','slope','DD','EE','ca','FF','GG','HH','II','JJ','KK','thal',	'LL','MM','NN','OO','PP','QQ','num','RR','SS','TT','UU','VV','WW',	'XX','YY','ZZ','AAA','BBB','CCC','DDD',	'EEE','FFF','GGG',	
'HHH','III','JJJ','KLL','LLL',	'MMM','NNN','OOO','PPP','QQQ',	'RRR','SSS','TTT','UUU','VVV','WWW']
print(new_data_df.head()) 
print(new_data_df.columns) 
print(new_data_df.info()) 
#The new_data file has 90 columns instead of 76 or 14, so I have no idea what is in it. Leaving in here though in case there's something to work with later.
'''
#___________________________________________ca distribution and fix na in hungarian, switch out NaN's_______________________________________________________________________________________________________
cleveland_df['ca'].plot(kind='hist', color='blue')
plt.show()
hungarian_df['ca'].plot(kind='hist', color='red')
plt.show()
long_beach_df['ca'].plot(kind='hist', color='purple')
plt.show()
print(hungarian_df['ca'][30:50])
hungarian_df['ca'][39] = np.nan
print(hungarian_df['ca'][30:50])
cleveland_df['ca'].plot(kind='hist', color='blue')
plt.show()
hungarian_df['ca'].plot(kind='hist', color='red')
plt.show()
long_beach_df['ca'].plot(kind='hist', color='purple')
plt.show()
#ca is not normally distributed. In the case where dataset mostly complete, it's skewed toward 0, and the only values present in the other datasets show up as 0.
#Since it is not normally distributed, continuous variable, mode is more appropriate for allocation of missing values.
print('ca')
cleveland_df['ca'].plot(kind='hist', color='blue')
hungarian_df['ca'].plot(kind='hist', color='red')
long_beach_df['ca'].plot(kind='hist', color='purple')
plt.show()
#discrete and non-normal. use mode.
ca_mode_cleveland = cleveland_df.ca.mode()
cleveland_df['ca'] = cleveland_df.ca.fillna(ca_mode_cleveland[0])
print(cleveland_df.info())
ca_mode_hungarian = hungarian_df.ca.mode()
hungarian_df['ca'] = hungarian_df.ca.fillna(ca_mode_hungarian[0])
print(hungarian_df.info())
ca_mode_long_beach = long_beach_df.ca.mode()
long_beach_df['ca'] = long_beach_df.ca.fillna(ca_mode_long_beach[0])
print(long_beach_df.info())

#___________________________________________age distribution, switch out NaN's_______________________________________________________________________________________________________
print('age')
cleveland_df['age'].plot(kind='hist', color='blue')
hungarian_df['age'].plot(kind='hist', color='red')
long_beach_df['age'].plot(kind='hist', color='purple')
plt.show()
#dist varies by pop but overall mostly normal, slight skew to right. continuous var. will use median for missing.
age_median_cleveland = cleveland_df.age.median()
cleveland_df['age'] = cleveland_df.age.fillna(age_median_cleveland)
age_median_hungarian = hungarian_df.age.median()
hungarian_df['age'] = hungarian_df.age.fillna(age_median_hungarian)
age_median_long_beach = long_beach_df.age.median()
long_beach_df['age'] = long_beach_df.age.fillna(age_median_long_beach)

#___________________________________________sex distribution, switch out NaN's_______________________________________________________________________________________________________
print('sex')
cleveland_df['sex'].plot(kind='hist', color='blue')
hungarian_df['sex'].plot(kind='hist', color='red')
long_beach_df['sex'].plot(kind='hist', color='purple')
plt.show()
#discrete and non-normal. mostly male. use mode for right now, subject to change.
sex_mode_cleveland = cleveland_df.sex.mode()
cleveland_df['sex'] = cleveland_df.sex.fillna(sex_mode_cleveland[0])
sex_mode_hungarian = hungarian_df.sex.mode()
hungarian_df['sex'] = hungarian_df.sex.fillna(sex_mode_hungarian[0])
sex_mode_long_beach = long_beach_df.sex.mode()
long_beach_df['sex'] = long_beach_df.sex.fillna(sex_mode_long_beach[0])

#___________________________________________cp distribution, switch out NaN's_______________________________________________________________________________________________________
print('cp')
cleveland_df['cp'].plot(kind='hist', color='blue')
hungarian_df['cp'].plot(kind='hist', color='red')
long_beach_df['cp'].plot(kind='hist', color='purple')
plt.show()
#discrete and non-normal, but hungarian looks different from others. either median or mode, not sure yet. just go with median right now.
cp_median_cleveland = cleveland_df.cp.median()
cleveland_df['cp'] = cleveland_df.cp.fillna(cp_median_cleveland)
cp_median_hungarian = hungarian_df.cp.median()
hungarian_df['cp'] = hungarian_df.cp.fillna(cp_median_hungarian)
cp_median_long_beach = long_beach_df.cp.median()
long_beach_df['cp'] = long_beach_df.cp.fillna(cp_median_long_beach)

#___________________________________________trestbps distribution, switch out NaN's_______________________________________________________________________________________________________
print('trestbps')
cleveland_df['trestbps'].plot(kind='hist', color='blue')
hungarian_df['trestbps'].plot(kind='hist', color='red')
long_beach_df['trestbps'].plot(kind='hist', color='purple')
plt.show()
#continuous and close enough to normal. use median.
trestbps_median_cleveland = cleveland_df.trestbps.median()
cleveland_df['trestbps'] = cleveland_df.trestbps.fillna(trestbps_median_cleveland)
trestbps_median_hungarian = hungarian_df.trestbps.median()
hungarian_df['trestbps'] = hungarian_df.trestbps.fillna(trestbps_median_hungarian)
trestbps_median_long_beach = long_beach_df.trestbps.median()
long_beach_df['trestbps'] = long_beach_df.trestbps.fillna(trestbps_median_long_beach)

#___________________________________________chol distribution, switch out NaN's_______________________________________________________________________________________________________
print('chol')
cleveland_df['chol'].plot(kind='hist', color='blue')
hungarian_df['chol'].plot(kind='hist', color='red')
long_beach_df['chol'].plot(kind='hist', color='purple')
plt.show()
#continuous and close enough to normal. use median.
chol_median_cleveland = cleveland_df.chol.median()
cleveland_df['chol'] = cleveland_df.chol.fillna(chol_median_cleveland)
chol_median_hungarian = hungarian_df.chol.median()
hungarian_df['chol'] = hungarian_df.chol.fillna(chol_median_hungarian)
chol_median_long_beach = long_beach_df.chol.median()
long_beach_df['chol'] = long_beach_df.chol.fillna(chol_median_long_beach)

#___________________________________________fbs distribution, switch out NaN's_______________________________________________________________________________________________________
print('fbs')
cleveland_df['fbs'].plot(kind='hist', color='blue')
hungarian_df['fbs'].plot(kind='hist', color='red')
long_beach_df['fbs'].plot(kind='hist', color='purple')
plt.show()
#discrete and non-normal. vast majority one value. use mode.
fbs_mode_cleveland = cleveland_df.fbs.mode()
cleveland_df['fbs'] = cleveland_df.fbs.fillna(fbs_mode_cleveland[0])
fbs_mode_hungarian = hungarian_df.fbs.mode()
hungarian_df['fbs'] = hungarian_df.fbs.fillna(fbs_mode_hungarian[0])
fbs_mode_long_beach = long_beach_df.fbs.mode()
long_beach_df['fbs'] = long_beach_df.fbs.fillna(fbs_mode_long_beach[0])

#___________________________________________restecg distribution, switch out NaN's_______________________________________________________________________________________________________
print('restecg')
cleveland_df['restecg'].plot(kind='hist', color='blue')
hungarian_df['restecg'].plot(kind='hist', color='red')
long_beach_df['restecg'].plot(kind='hist', color='purple')
plt.show()
#looks discrete and non-normal. varies by population. unclear whether median or mode best yet. just go with median right now.
restecg_median_cleveland = cleveland_df.restecg.median()
cleveland_df['restecg'] = cleveland_df.restecg.fillna(restecg_median_cleveland)
restecg_median_hungarian = hungarian_df.restecg.median()
hungarian_df['restecg'] = hungarian_df.restecg.fillna(restecg_median_hungarian)
restecg_median_long_beach = long_beach_df.restecg.median()
long_beach_df['restecg'] = long_beach_df.restecg.fillna(restecg_median_long_beach)

#___________________________________________thalach distribution, switch out NaN's_______________________________________________________________________________________________________
print('thalach')
cleveland_df['thalach'].plot(kind='hist', color='blue')
hungarian_df['thalach'].plot(kind='hist', color='red')
long_beach_df['thalach'].plot(kind='hist', color='purple')
plt.show()
#continuous but dist depends on population. use median for now.
thalach_median_cleveland = cleveland_df.thalach.median()
cleveland_df['thalach'] = cleveland_df.thalach.fillna(thalach_median_cleveland)
thalach_median_hungarian = hungarian_df.thalach.median()
hungarian_df['thalach'] = hungarian_df.thalach.fillna(thalach_median_hungarian)
thalach_median_long_beach = long_beach_df.thalach.median()
long_beach_df['thalach'] = long_beach_df.thalach.fillna(thalach_median_long_beach)

#___________________________________________exang distribution, switch out NaN's_______________________________________________________________________________________________________
print('exang')
cleveland_df['exang'].plot(kind='hist', color='blue')
hungarian_df['exang'].plot(kind='hist', color='red')
long_beach_df['exang'].plot(kind='hist', color='purple')
plt.show()
#exang discrete and non-normal, but depends on pop. probably use mode for each pop.
exang_mode_cleveland = cleveland_df.exang.mode()
cleveland_df['exang'] = cleveland_df.exang.fillna(exang_mode_cleveland[0])
exang_mode_hungarian = hungarian_df.exang.mode()
hungarian_df['exang'] = hungarian_df.exang.fillna(exang_mode_hungarian[0])
exang_mode_long_beach = long_beach_df.exang.mode()
long_beach_df['exang'] = long_beach_df.exang.fillna(exang_mode_long_beach[0])

#___________________________________________old peak distribution, switch out NaN's_______________________________________________________________________________________________________
print('oldpeak')
cleveland_df['oldpeak'].plot(kind='hist', color='blue')
hungarian_df['oldpeak'].plot(kind='hist', color='red')
long_beach_df['oldpeak'].plot(kind='hist', color='purple')
plt.show()
#continuous but non-normal, skewed to 0. use mode or median, use median for now.
oldpeak_median_cleveland = cleveland_df.oldpeak.median()
cleveland_df['oldpeak'] = cleveland_df.oldpeak.fillna(oldpeak_median_cleveland)
oldpeak_median_hungarian = hungarian_df.oldpeak.median()
hungarian_df['oldpeak'] = hungarian_df.oldpeak.fillna(oldpeak_median_hungarian)
oldpeak_median_long_beach = long_beach_df.oldpeak.median()
long_beach_df['oldpeak'] = long_beach_df.oldpeak.fillna(oldpeak_median_long_beach)

#___________________________________________slope distribution, switch out NaN's_______________________________________________________________________________________________________
print('slope')
cleveland_df['slope'].plot(kind='hist', color='blue')
hungarian_df['slope'].plot(kind='hist', color='red')
long_beach_df['slope'].plot(kind='hist', color='purple')
plt.show()
#discrete and non-normal but not really skewed. use median.
slope_median_cleveland = cleveland_df.slope.median()
cleveland_df['slope'] = cleveland_df.slope.fillna(slope_median_cleveland)
slope_median_hungarian = hungarian_df.slope.median()
hungarian_df['slope'] = hungarian_df.slope.fillna(slope_median_hungarian)
slope_median_long_beach = long_beach_df.slope.median()
long_beach_df['slope'] = long_beach_df.slope.fillna(slope_median_long_beach)

#___________________________________________thal distribution, switch out NaN's_______________________________________________________________________________________________________
print('thal')
cleveland_df['thal'].plot(kind='hist', color='blue')
hungarian_df['thal'].plot(kind='hist', color='red')
long_beach_df['thal'].plot(kind='hist', color='purple')
plt.show()
#discrete and non-normal. but evenly split. maybe median? just to keep with current convention of erring on side of median, use median right now.
thal_median_cleveland = cleveland_df.thal.median()
cleveland_df['thal'] = cleveland_df.thal.fillna(thal_median_cleveland)
thal_median_hungarian = hungarian_df.thal.median()
hungarian_df['thal'] = hungarian_df.thal.fillna(thal_median_hungarian)
thal_median_long_beach = long_beach_df.thal.median()
long_beach_df['thal'] = long_beach_df.thal.fillna(thal_median_long_beach)

#___________________________________________num distribution for curiosity (is target value, not a variable)_______________________________________________________________________________________________________
#TARGET variable is num
print('num')
cleveland_df['num'].plot(kind='hist', color='blue')
hungarian_df['num'].plot(kind='hist', color='red')
long_beach_df['num'].plot(kind='hist', color='purple')
plt.show()
cleveland_df['num'].plot(kind='hist', color='blue')
plt.show()
hungarian_df['num'].plot(kind='hist', color='red')
plt.show()
long_beach_df['num'].plot(kind='hist', color='purple')
plt.show()
#switch NaN's with modes or medians from each population.

#___________________________________________check each df had missing values converted_______________________________________________________________________________________________
print(cleveland_df.info())
print(hungarian_df.info())
print(long_beach_df.info())

#___________________________________________concat df's into one df_______________________________________________________________________________________________________
#add location columns to each up above so as to combine.
all_three_df = pd.concat([cleveland_df, hungarian_df, long_beach_df], ignore_index=True)
print(all_three_df)
#___________________________________________set dtypes_____________________________________________________________________________________________________________
all_three_df['location'] = all_three_df['location'].astype(str)
all_three_df['age'] = all_three_df['age'].astype(float)
all_three_df['sex'] = all_three_df['sex'].astype(int)
all_three_df['cp'] = all_three_df['cp'].astype(int)
all_three_df['trestbps'] = all_three_df['trestbps'].astype(float)
all_three_df['chol'] = all_three_df['chol'].astype(float)
all_three_df['fbs'] = all_three_df['fbs'].astype(int)
all_three_df['restecg'] = all_three_df['restecg'].astype(int)
all_three_df['thalach'] = all_three_df['thalach'].astype(float)
all_three_df['exang'] = all_three_df['exang'].astype(int)
all_three_df['oldpeak'] = all_three_df['oldpeak'].astype(float)
all_three_df['slope'] = all_three_df['slope'].astype(int)
all_three_df['ca'] = all_three_df['ca'].astype(int)
all_three_df['thal'] = all_three_df['thal'].astype(int)
all_three_df['num'] = all_three_df['num'].astype(float) #because missing values that I think I shouldn't change for target
print(all_three_df.info())

#________________________________________plot hist of each combined now for fun and to check out colors____________________________________________________________________________________
#all_three_df['location'].plot(kind='hist', color='grey')
#plt.title('location')
#plt.show()
all_three_df['age'].plot(kind='hist', color='pink')
plt.title('age')
plt.show()
all_three_df['sex'].plot(kind='hist', color='purple')
plt.title('sex')
plt.show()
all_three_df['cp'].plot(kind='hist', color='blue')
plt.title('cp')
plt.show()
all_three_df['trestbps'].plot(kind='hist', color='red')
plt.title('trestbps')
plt.show()
all_three_df['chol'].plot(kind='hist', color='yellow')
plt.title('chol')
plt.show()
all_three_df['fbs'].plot(kind='hist', color='violet')
plt.title('fbs')
plt.show()
all_three_df['restecg'].plot(kind='hist', color='turquoise')
plt.title('restecg')
plt.show()
all_three_df['thalach'].plot(kind='hist', color='magenta')
plt.title('thalach')
plt.show()
all_three_df['exang'].plot(kind='hist', color='orange')
plt.title('exang')
plt.show()
all_three_df['oldpeak'].plot(kind='hist', color='green')
plt.title('oldpeak')
plt.show()
all_three_df['slope'].plot(kind='hist', color='indigo')
plt.title('slope')
plt.show()
all_three_df['ca'].plot(kind='hist', color='black')
plt.title('ca')
plt.show()
all_three_df['thal'].plot(kind='hist', color='brown')
plt.title('thal')
plt.show()
all_three_df['num'].plot(kind='hist', color='aqua')
plt.title('num')
plt.show()









