#import splitintolines_matformat
#import splitintolines_updated
import sys,os

class Parameters(object):
      def __init__ ( self ):
	  self.m_white_row_threshold = 0
	  self.m_white_row_fill_factor = 1.0
	  self.m_white_col_threshold = 0
	  self.m_white_col_fill_factor = 1.0
	  self.m_MIN_INTER_WORD_GAP = 5
          self.m_lineBoundaries1=[]
	  self.m_lineBoundaries2=[]
          self.m_lineBoundaries_y=[]
          self.m_lineBoundaries_w=[]
	  self.m_wordBoundaries1 = []
	  self.m_wordBoundaries2 = []
          self.m_wordBoundaries= []
	  self.currLineTop=0
	  self.currLineBottom=0
          self.segimgname=""
        
          
