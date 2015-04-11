#!/usr/bin/python
import sys,os
import bgfilter
#import search
#import segment
bgfilterobj=bgfilter.bgfilter()

infile=sys.argv[1]
outfile=sys.argv[2]

class VisualDoc:
	#bgfilters = [];
	string filepath; # original file path
	string json; # json produced after processing the file
	string imgfile; # image after applying transformations to original file
      
      def __init__(self)
          self.bgtypes = ["BGTYPE_PAPER", "BGTYPE_PRINTEDTEXT", "BGTYPE_WOOD", "BGTYPE_DARKWOOD" ]
	  addFilterAlgo(bgtypes)
          #self.bgtypes = { "BGTYPE_PAPER", "BGTYPE_PRINTEDTEXT", "BGTYPE_WOOD", "BGTYPE_DARKWOOD" };
	  bgfilter = new BgFilter();
	for i in range(len(self.bgtypes)):
		self.bgfilters[i] = bgfilter;

      def getJSON()
      	  return json;

      def produceImage(outimgfile)
      	  ...

      def clean(bgtype,outdoc)
           bgfilters[bgtype].doClean(filename,outdoc.filename)
      
      def search(algotype = SEARCHALGO_FLAN, template_img, threshold_parms, out_doc)
           out_doc.json = searchalgos[algotype].search(template_img, filename, threshold_parms)

      def segment(parms)
           json = segmentalgo.doSegment(parms, filename);
