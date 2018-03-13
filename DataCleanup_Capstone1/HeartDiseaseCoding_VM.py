import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

cleveland_df = pd.read_csv('/Users/vickimoore/Desktop/Springboard/UCIheartdiseasedata/UCI_heart_newDL/Processed/processed_cleveland_data.csv', header=None, na_values = '?')
cleveland_df.columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'num']
cleveland_df['sex'] = cleveland_df['sex'].astype(float)
cleveland_df['cp'] = cleveland_df['cp'].astype(float)
cleveland_df['fbs'] = cleveland_df['fbs'].astype(float)
cleveland_df['restecg'] = cleveland_df['restecg'].astype(float)
cleveland_df['exang'] = cleveland_df['exang'].astype(float)
cleveland_df['slope'] = cleveland_df['slope'].astype(float)
cleveland_df['ca'] = cleveland_df['ca'].astype(float) #throws errors over the NaN for int, just changing these to floats for now
cleveland_df['thal'] = cleveland_df['thal'].astype(float)
print('cleveland')
print(cleveland_df.head()) 
print(cleveland_df.columns) 
print(cleveland_df.info()) 

hungarian_df = pd.read_csv('/Users/vickimoore/Desktop/Springboard/UCIheartdiseasedata/UCI_heart_newDL/Processed/reprocessed_hungarian_data.txt', sep=" ", header=None, na_values = '-9.0')
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
print('hungarian')
print(hungarian_df.head()) 
print(hungarian_df.columns) 
print(hungarian_df.info()) 

long_beach_df = pd.read_csv('/Users/vickimoore/Desktop/Springboard/UCIheartdiseasedata/UCI_heart_newDL/Processed/processed_va_data.csv', header=None, na_values = '?')
long_beach_df.columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'num']
long_beach_df['age'] = long_beach_df['age'].astype(float)
long_beach_df['fbs'] = long_beach_df['fbs'].astype(float)
long_beach_df['exang'] = long_beach_df['exang'].astype(float)
long_beach_df['slope'] = long_beach_df['slope'].astype(float)
long_beach_df['ca'] = long_beach_df['ca'].astype(float)
long_beach_df['thal'] = long_beach_df['thal'].astype(float)
print('long beach')
print(long_beach_df.head()) 
print(long_beach_df.columns) 
print(long_beach_df.info()) 

'''
new_data_df = pd.read_csv('/Users/vickimoore/Desktop/Springboard/UCIheartdiseasedata/UCI_heart_newDL/Processed/new_data.txt', sep=" ", header=None)
new_data_df.columns = ['ccf', 'age', 'sex', 'painloc', 'painexer', 'relrest', 'pncaden', 'cp', 'trestbps', 'htn', 'chol', 'smoke', 'cigs', 'years', 'fbs', 
                       'dm', 'famhist', 'restecg', 'ekgmo', 'ekgday', 'ekgyr', 'dig', 'prop', 'nitr', 'pro', 'diuretic', 'proto', 'thaldur', 'thaltime', 'met',
                       'thalach', 'thalrest', 'tpeakbps', 'tpeakbpd', 'dummy', 'trestbpd', 'exang', 'xhypo', 'oldpeak', 'slope', 'rldv5', 'rldv5e', 'ca', 'restckm', 'exerckm',
                       'restef', 'restwm', 'exeref', 'exerwm', 'thal', 'thalsev', 'thalpul', 'earlobe', 'cmo', 'cday', 'cyr', 'num', 'lmt', 'ladprox', 'laddist',
                       'diag', 'cxmain', 'ramus', 'om1', 'om2', 'rcaprox', 'rcadist', 'lvx1', 'lvx2', 'lvx3', 'lvx4', 'lvf', 'cathef', 'junk', 'name']
#A	B	age	sex	C	D	E	F	cp	trestbps		chol	G	H	I	fbs	J	K	restecg	L	M	N	O	P	Q	R	S	T	U	V	W	thalach	X	Y	Z	AA	BB	
#exang	CC	oldpeak	slope	DD	EE	ca	FF	GG	HH	II	JJ	KK	thal	LL	MM	NN	OO	PP	QQ	num	RR	SS	TT	UU	VV	WW	XX	YY	ZZ	AAA	BBB	CCC	DDD	EEE	FFF	GGG	
#HHH	III	JJJ	KLL	LLL	MMM	NNN	OOO	PPP	QQQ	RRR	SSS	TTT	UUU	VVV	WWW - a guide to placement of column names if needed
print(new_data_df.head()) 
print(new_data_df.columns) 
print(new_data_df.info()) 
The new_data file has 90 columns instead of 76 or 14, so I have no idea what is in it. Leaving in here though in case there's something to work with later.
'''
