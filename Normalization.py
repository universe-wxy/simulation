import pandas as pd
import numpy as np
import datetime

class Normalization:
	def __init__(self)->None:
		self._gold=pd.read_csv('./LBMA-GOLD.csv')
		self._mkpru=pd.read_csv('./BCHAIN-MKPRU.csv')
		self.final=pd.DataFrame()
		self.combine()
		self.final.to_csv('../Final.csv')

	def combine(self)->None:
		self.final['Date']=self._mkpru['Date']
		self.final=self.final.merge(self._mkpru,on=['Date'],how='outer')
		self.final=self.final.merge(self._gold,on=['Date'],how='outer')
		self.final['Date']=pd.to_datetime(self.final['Date'])


if __name__ == '__main__':
	normalization=Normalization()
