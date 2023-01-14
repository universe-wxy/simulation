import pandas as pd
import numpy as np
import datetime

class Normalization:
	def __init__(self)->None:
		self._gold=pd.read_csv('../LBMA-GOLD.csv')
		self._mkpru=pd.read_csv('../BCHAIN-MKPRU.csv')
		self.final=pd.DataFrame()
		self.combine()


	def combine(self)->None:
		self.final['Date']=pd.to_datetime(self._gold['Date'],format="%m/%d/%y")

	def test(self)->None:
		print(self.final['Date'])

if __name__ == '__main__':
	normalization=Normalization()
	normalization.test()