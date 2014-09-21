<map version="freeplane 1.2.0">
<!--To view this file, download free mind mapping software Freeplane from http://freeplane.sourceforge.net -->
<node TEXT="IndicTools" ID="ID_1723255651" CREATED="1283093380553" MODIFIED="1404555619238" BACKGROUND_COLOR="#ffcccc"><hook NAME="MapStyle">

<map_styles>
<stylenode LOCALIZED_TEXT="styles.root_node">
<stylenode LOCALIZED_TEXT="styles.predefined" POSITION="right">
<stylenode LOCALIZED_TEXT="default" MAX_WIDTH="600" COLOR="#000000" STYLE="as_parent">
<font NAME="SansSerif" SIZE="10" BOLD="false" ITALIC="false"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.details"/>
<stylenode LOCALIZED_TEXT="defaultstyle.note"/>
<stylenode LOCALIZED_TEXT="defaultstyle.floating">
<edge STYLE="hide_edge"/>
<cloud COLOR="#f0f0f0" SHAPE="ROUND_RECT"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.user-defined" POSITION="right">
<stylenode LOCALIZED_TEXT="styles.topic" COLOR="#18898b" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subtopic" COLOR="#cc3300" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subsubtopic" COLOR="#669900">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.important">
<icon BUILTIN="yes"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.AutomaticLayout" POSITION="right">
<stylenode LOCALIZED_TEXT="AutomaticLayout.level.root" COLOR="#000000">
<font SIZE="18"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,1" COLOR="#0033ff">
<font SIZE="16"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,2" COLOR="#00b439">
<font SIZE="14"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,3" COLOR="#990000">
<font SIZE="12"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,4" COLOR="#111111">
<font SIZE="10"/>
</stylenode>
</stylenode>
</stylenode>
</map_styles>
</hook>
<hook NAME="AutomaticEdgeColor" COUNTER="6"/>
<hook NAME="accessories/plugins/AutomaticLayout.properties" VALUE="ALL"/>
<node TEXT="External formats" POSITION="right" ID="ID_1228644207" CREATED="1404554772586" MODIFIED="1404555877556">
<edge COLOR="#ff0000"/>
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_173668154" MIDDLE_LABEL="Parser" STARTINCLINATION="-114;-67;" ENDINCLINATION="-80;-37;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<node TEXT="Audio" ID="ID_1061344418" CREATED="1404554778909" MODIFIED="1404554781832"/>
<node TEXT="Video" ID="ID_321018228" CREATED="1404554782160" MODIFIED="1404554783973"/>
<node TEXT="Images" ID="ID_1939235198" CREATED="1404554784669" MODIFIED="1404554796120">
<node TEXT="Manuscripts" ID="ID_1364808844" CREATED="1404554798856" MODIFIED="1404554807560"/>
<node TEXT="Photographed Text" ID="ID_1249420904" CREATED="1404554807904" MODIFIED="1404554815735"/>
<node TEXT="Printed Text" ID="ID_1220390950" CREATED="1404554815990" MODIFIED="1404554818571"/>
</node>
<node TEXT="Unicode Text" ID="ID_703354423" CREATED="1404554823500" MODIFIED="1404554830059">
<node TEXT="Fully annotated" ID="ID_1559718580" CREATED="1404554836143" MODIFIED="1404554845110"/>
<node TEXT="not proof-read" ID="ID_622076290" CREATED="1404554845382" MODIFIED="1404554854223"/>
</node>
</node>
<node TEXT="IndicDoc (JSON)" POSITION="left" ID="ID_173668154" CREATED="1404554867129" MODIFIED="1404664134783">
<edge COLOR="#0000ff"/>
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#ff0000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1228644207" MIDDLE_LABEL="Synthesizer" STARTINCLINATION="5;-51;" ENDINCLINATION="-40;-112;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<richcontent TYPE="DETAILS">

<html>
  <head>
    
  </head>
  <body>
    <p>
      Canonical
    </p>
    <p>
      annotated representation
    </p>
    <p>
      of an Indic document;
    </p>
    <p>
      Machine-processable,
    </p>
    <p>
      indexable, extensible
    </p>
  </body>
</html>

</richcontent>
<node TEXT="Content Graph" ID="ID_1799361334" CREATED="1404554876589" MODIFIED="1404560254277"><richcontent TYPE="DETAILS">

<html>
  <head>
    
  </head>
  <body>
    <p>
      Auto-generated, user-editable
    </p>
  </body>
</html>

</richcontent>
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_71238134" MIDDLE_LABEL="Concept Analyzer" STARTINCLINATION="-61;-12;" ENDINCLINATION="-96;-14;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<node TEXT="CVAD tags" ID="ID_168285999" CREATED="1404560426684" MODIFIED="1404560544034"><richcontent TYPE="DETAILS">

<html>
  <head>
    
  </head>
  <body>
    <p>
      Consonant, Vowel, Accent, Delimiter
    </p>
  </body>
</html>

</richcontent>
</node>
</node>
<node TEXT="Concept Graph" ID="ID_71238134" CREATED="1404554887685" MODIFIED="1404556230141"><richcontent TYPE="DETAILS">

<html>
  <head>
    
  </head>
  <body>
    <p>
      Auto-generated, user-editable
    </p>
  </body>
</html>

</richcontent>
<node TEXT="Simple Words" ID="ID_670734707" CREATED="1404560566469" MODIFIED="1404560765756">
<node TEXT="base" ID="ID_1101441392" CREATED="1404560611856" MODIFIED="1404560664973"/>
<node TEXT="suffix" ID="ID_1292712366" CREATED="1404560651437" MODIFIED="1404560672217"/>
<node TEXT="vibhakti" ID="ID_1762171118" CREATED="1404560673177" MODIFIED="1404560718288"/>
<node TEXT="linga, vachana" ID="ID_1829169673" CREATED="1404663899285" MODIFIED="1404663907333"/>
</node>
<node TEXT="Compound words" ID="ID_1131564814" CREATED="1404560772991" MODIFIED="1404560777391">
<node TEXT="sandhi" ID="ID_1816498003" CREATED="1404560719071" MODIFIED="1404560728614"/>
<node TEXT="vigraha" ID="ID_1289616925" CREATED="1404560729006" MODIFIED="1404560740990"/>
</node>
</node>
<node TEXT="Template&#xa;library" ID="ID_113343432" CREATED="1404555004852" MODIFIED="1404557583478"><richcontent TYPE="DETAILS">

<html>
  <head>
    
  </head>
  <body>
    <p>
      User-supplied
    </p>
  </body>
</html>

</richcontent>
<node TEXT="Scanned Doc Layout" ID="ID_895489601" CREATED="1404555017232" MODIFIED="1404559808982"><richcontent TYPE="DETAILS">

<html>
  <head>
    
  </head>
  <body>
    <p>
      imglayout.json
    </p>
  </body>
</html>

</richcontent>
<hook NAME="FirstGroupNode"/>
</node>
<node TEXT="Unicode Text Layout" ID="ID_944913990" CREATED="1404556478190" MODIFIED="1404559741014"><richcontent TYPE="DETAILS">

<html>
  <head>
    
  </head>
  <body>
    <p>
      txtlayout.json
    </p>
  </body>
</html>

</richcontent>
</node>
<node TEXT="Audio Layout" ID="ID_1683463534" CREATED="1404556770882" MODIFIED="1404559750963"><richcontent TYPE="DETAILS">

<html>
  <head>
    
  </head>
  <body>
    <p>
      audiolayout.json
    </p>
  </body>
</html>

</richcontent>
</node>
<node TEXT="Rich media layout" ID="ID_580781087" CREATED="1404557845834" MODIFIED="1404559767587"><richcontent TYPE="DETAILS">

<html>
  <head>
    
  </head>
  <body>
    <p>
      multimedialayout.json
    </p>
  </body>
</html>

</richcontent>
</node>
<node TEXT="Document types" ID="ID_604849409" CREATED="1404556920249" MODIFIED="1404556933726">
<hook NAME="SummaryNode"/>
<node TEXT="Dictionary" ID="ID_1633921798" CREATED="1404555039538" MODIFIED="1404555043019"/>
<node TEXT="padya grantha" ID="ID_1130607575" CREATED="1404555043412" MODIFIED="1404555065534"/>
<node TEXT="gadya-grantha" ID="ID_1119346198" CREATED="1404555065886" MODIFIED="1404555070658"/>
<node TEXT="sUtra-grantha" ID="ID_543230988" CREATED="1404555070922" MODIFIED="1404555642131"/>
<node TEXT="Bhaashya" ID="ID_1391163236" CREATED="1404555643282" MODIFIED="1404555646008"/>
</node>
<node TEXT="Markup Layout" ID="ID_369996009" CREATED="1404555238209" MODIFIED="1404559789333"><richcontent TYPE="DETAILS">

<html>
  <head>
    
  </head>
  <body>
    <p>
      display.json
    </p>
  </body>
</html>

</richcontent>
</node>
</node>
</node>
<node TEXT="Basic Tools" POSITION="right" ID="ID_1752458282" CREATED="1404554966779" MODIFIED="1404558076042">
<edge COLOR="#00ff00"/>
<node TEXT="Parsers" ID="ID_751155599" CREATED="1404554971064" MODIFIED="1404554973687"/>
<node TEXT="Viewers" ID="ID_1061445271" CREATED="1404557634908" MODIFIED="1404557640100"/>
<node TEXT="Annotators" ID="ID_1112942384" CREATED="1404557614373" MODIFIED="1404663987422"/>
<node TEXT="Indexers" ID="ID_712535353" CREATED="1404664018619" MODIFIED="1404664047164"/>
<node TEXT="Synthesizers" ID="ID_384404161" CREATED="1404554978418" MODIFIED="1404554982388"/>
<node TEXT="Analyzers" ID="ID_404224318" CREATED="1404554974295" MODIFIED="1404554978154"/>
</node>
<node TEXT="End-user applications" POSITION="left" ID="ID_1457966708" CREATED="1404557893561" MODIFIED="1404557900870">
<edge COLOR="#ffff00"/>
<node TEXT="Visual search for scanned books" ID="ID_705566789" CREATED="1404560946415" MODIFIED="1404664606642"/>
<node TEXT="Community-based Palm-leaf Text Study" ID="ID_567670465" CREATED="1404561691782" MODIFIED="1404664375628"/>
<node TEXT="Cross-referencer for Multi-script Text" ID="ID_1272611644" CREATED="1404663775052" MODIFIED="1404664342301"/>
</node>
</node>
</map>
