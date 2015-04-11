#!/usr/bin/python
import sys,os
#import bgfilter
#import search
#import segment
#bgfilterobj=bgfilter.bgfilter()

#infile=sys.argv[1]
#outfile=sys.argv[2]

class VisualDoc(object):
	#bgfilters = [];
      filepath="" # original file path
      json="" # json produced after processing the file
      imgfile="" # image after applying transformations to original file
      
      


      def __init__(self,docpath):
          self.bgtypes = ["BGTYPE_PAPER", "BGTYPE_PRINTEDTEXT", "BGTYPE_WOOD", "BGTYPE_DARKWOOD" ]
	  self.filepath=docpath
	  #addFilterAlgo(bgtypes)
          print "Hello",";",self.filepath
          self.docfile=[]

	  
	  #bgfilter = new BgFilter();
	#for i in range(len(self.bgtypes)):
		#self.bgfilters[i] = bgfilter;

      #def getJSON()
      	  #return json;

      #def produceImage(outimgfile)
      	 # ...

      #def clean(bgtype,outdoc)
           #bgfilters[bgtype].doClean(filename,outdoc.filename)
      
      #def search(algotype = SEARCHALGO_FLAN, template_img, threshold_parms, out_doc)
           #out_doc.json = searchalgos[algotype].search(template_img, filename, threshold_parms)

      #def segment(parms)
           #json = segmentalgo.doSegment(parms, filename);
