#!/usr/bin/python

import VisualDoc
import sys,os

def list_files(path):
    files = []
    for name in os.listdir(path):
	if os.path.isfile(os.path.join(path, name)):
	   files.append(name)
    return files




for docpath in sys.argv[1:]:
    
    doc=VisualDoc.VisualDoc(docpath)
    
    
    #doc = new VisualDoc(docpath)
    #bookdirpath=os.listdir(doc.filepath)
    files = []
    files=list_files(doc.filepath)
    #print str(bookdirpath)
    #for i in range(len(files)):
    for i in range(len(files)):
	doc.docfile.append(files[i])
    for i in range(len(doc.docfile)):
	fileextsplit = doc.docfile[i].split(".jpg")

	cleaned_doc = fileextsplit[0] + "_cleaned.jpg"
	print cleaned_doc
	 
    #doc.bgclean(VisualDoc::BGTYPE_WOOD, cleaned_doc)

    #results_doc = new VisualDoc(docpath + "_flan_results_orig.png");
    #doc.search(VisualDoc::SEARCHALGO_FLAN, tmpl_imagefile, threshold_parms, results_doc)
    #results_doc.saveJSON(outfile);

    #cleaned_results_doc = new VisualDoc(docpath + "_flan_results_cleaned.png");
    #cleaned_doc.search(VisualDoc::SEARCHALGO_FLAN, tmpl_imagefile, threshold_parms, cleaned_results_doc)
    #cleaned_results_doc.saveJSON();


