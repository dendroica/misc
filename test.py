import pandas as pd    
df = pd.read_csv('~/Downloads/CTT-4642BFF2FDD4-node-health.2021-06-07_040629.csv.gz',
	error_bad_lines=False, warn_bad_lines=True)


if 'recorded_at' not in df.columns:
	try:
		df2 = pd.read_csv('~/Downloads/CTT-792C1C06A0AF-gps.2021-05-12_162526.csv.gz',
			header = None
		)
	except:
                df2 = pd.read_csv('~/Downloads/CTT-792C1C06A0AF-gps.2021-05-12_162526.csv.gz',
                    error_bad_lines=False,
                    warn_bad_lines=True,
                    header = None,
                    skiprows = 1
                )
	columns = header
	df2.columns = columns
else:
	df2 = df
print(df2)
