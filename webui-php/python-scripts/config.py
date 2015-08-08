import sys,os

class Config(object):
      def __init__ ( self ):
	  self.userupload_dir="/example-images/user_uploads/"
          self.segbook_dir = "/tmp/segmented-books/"
          self.segresultimg_dir = "/tmp/segmented-images/"
          self.idxbooks = "/books/"
          self.tempmatchresult_imgdir = r"/tmp/searched-images/Template-Match/"
          self.fuzzybooks = "/tmp/fuzzysegmented-books/"
