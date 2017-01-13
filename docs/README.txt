Need the following modules (written in Python):

SktDoc.py:
    This class denotes a canonical annotated representation (in JSON format) of a Samskrit
    Document including links to its original flat files (audio/video/image/text)
    and their partial annotations or transcripts and any semantic analysis
    results.

    This class supports the following methods:

    load(infile.json) -> True/False
        Initialize the SktDoc object from the input JSON file.

    save(outfile.json) -> True/False
        Save the SktDoc in a JSON format file.

    browse()
        Open a graphical viewer to browse the SktDoc.

    exportAsImage(SktDoc selection) -> output.png
    exportAsAudio(SktDoc selection) -> output.mp3
    exportAsText(SktDoc selection) -> output.html
        Export the selected portion of SktDoc into files in various
        formats.

    search(SktDoc pattern, SktDoc markup) -> SktDoc
        Search for given text supplied as an SktDoc
        (itself an image, text or audio clip) and return an annotated version
        of the original doc with all occurences marked out as described in the
        markup doc.
        The markup itself can be specified in JSON format to include how to
        highlight the matched segments.

    diff(SktDoc doc2, SktDoc markup) -> SktDoc
        Highlight areas where SktDoc differs from doc2 according to the markup
        specified in markup doc. Return the marked up doc.

ScannedSktDoc (derived class of SktDoc):
    import(image files ...)
        Import a set of image files and encapsulate them into a single SktDoc 
        object.

    segment(SktDoc imglayout) -> segmented_sktdoc
        Given an image layout description in SktDoc format,
        produce a segmented image version of the original document.
        For instance, it returns an annotated version of the SktDoc with
        coordinates of all the paragraphs, lines and/or words found in the
        original document.
        The imglayout describes the document's layout such as
        whether it is a palm leaf manuscript or scanned version, # of columns,
        shloka or gadya or dictionary etc.

AudioSktDoc (derived class of SktDoc):
    importAudio(audio.(mp3|wav))
        Import an audio file into a SktDoc object.

    segment(SktDoc audiolayout) -> segmented_sktdoc
        Given an audio file layout description in SktDoc format,
        produce a segmented audio version of the original document.
        For instance, it returns an annotated version of the SktDoc with
        time points of all the paragraphs, phrases nd/or words found in the
        original document.

TextSktDoc (derived class of SktDoc):
    importText(input.html)
        Import a Unicode-encoded text file into a SktDoc object.

    segment(SktDoc textlayout) -> segmented_sktdoc
        Given a unicode file layout description in SktDoc format,
        produce a segmented text version of the original document.
        For instance, it returns an annotated version of the SktDoc with
        byte offsets of all the paragraphs, phrases nd/or words found in the
        original document.
