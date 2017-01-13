/**
 * 
 */

var MstrMngr = function () {};
$(MstrMngr.registerMstrListEvents);


var comments = $( "#comments" ),
remarks = $( "#remarks" ),
allFields = $( [] ).add( comments ).add( remarks ),
tips = $( ".validateTips" );
BOOK_CONTAINER_ID = "#book-cntr";
var jcrop_api = null;


MstrMngr.registerMstrListEvents = function() {

	$(".add-new-book").on("click", MstrMngr.addNewBook);
	$(".tn3-in-image").on("click", MstrMngr.onClickInlineZoom);
	$("#zoomImage").on('click', alert);

	$("#inlineZoom").on("click", MstrMngr.onClickInlineZoom);
	$("#topPositionMap,#leftPositionMap,#rightPositionMap,#bottomPositionMap").on("click", MstrMngr.moveButtonClickHandler);
	$("#zoomInButton,#zoomOutButton").on("click", MstrMngr.zoomButtonClickHandler);
	
};

MstrMngr.showBooks = function () {
	$(".demo-wrapper").css('display', 'block');
};

MstrMngr.loadBooks = function () {
//	var lstBookOBJ = $.parseJSON(bookLstJSON);
	var divBooks = '<ol>', BOOKLIST_CONTAINER_ID = "#bookList-cntr";

//	var lstBookOBJ = MstrMngr.getJsonFrom("/getbooks");

	var lstBookOBJ = '';
	var jqxhr = $.getJSON( "/getbooks", function(data) {
		console.log(data);
	})
	.done(function(response) {
		lstBookOBJ = $.parseJSON(jqxhr.responseText);
		$.each(lstBookOBJ, function(index, book) {
			divBooks += '<li><a>'+ book + '</a></li>';
		});
		divBooks += '</ol>';

		$(BOOKLIST_CONTAINER_ID).html(divBooks);
		
		$("#bookList-cntr ol li").on('click', MstrMngr.handleBookSelection);
	})
	.fail(function(error) {
		data = error;
	});
};

MstrMngr.addNewBook = function() {
	alert();
};

MstrMngr.handleBookSelection = function() {

//	var bookOBJ = $.parseJSON(MstrMngr.getJsonFrom("/getBook/halayudha1"));
//	
//	var jqxhr = $.getJSON( "/getBook/halayudha1", function(data) {
//		console.log(data);
//	})
//	.done(function() {
//		console.log("done");
//	})
//	.fail(function(error) {
//		data = error;
//	});
	var $carousel = $(BOOK_CONTAINER_ID);

	$carousel.trigger('destroy.owl.carousel');
	$carousel.empty();

	var bookOBJ = $.parseJSON(getBookJSON);

	var pages = bookOBJ.images;
	var divPages = '';
	$.each(pages, function(index, pagePath) {
		divPages += '<a class="item link" pageid="' + pagePath + '"> <img src="/media/' + pagePath + '" pageid="' + pagePath + '"/> </a>';
	});

	$carousel.html(divPages);
	$carousel.css("display", "block");
	$carousel.owlCarousel({
		items : 3,
		responsive: false
	});

	$(".link").on("click", MstrMngr.handlePageSelection);
};


MstrMngr.onSelectPage = function() {
	$('#gallery-container').sGallery({
		fullScreenEnabled: true
	});
};

MstrMngr.onClickInlineZoom = function() {
	
};

MstrMngr.zoomImage = function (event) {
	$("#o1").zoomTarget();
};

MstrMngr.zoomButtonClickHandler = function(e){
	var scaleToAdd = 0.8;
	if(e.target.id == 'zoomOutButton')
		scaleToAdd = -scaleToAdd;
	$('#imageFullScreen').smartZoom('zoom', scaleToAdd);
}

MstrMngr.moveButtonClickHandler = function(e) {
	var pixelsToMoveOnX = 0;
	var pixelsToMoveOnY = 0;

	switch(e.target.id){
		case "leftPositionMap":
			pixelsToMoveOnX = 50;	
		break;
		case "rightPositionMap":
			pixelsToMoveOnX = -50;
		break;
		case "topPositionMap":
			pixelsToMoveOnY = 50;	
		break;
		case "bottomPositionMap":
			pixelsToMoveOnY = -50;	
		break;
	}
	$('#imageFullScreen').smartZoom('pan', pixelsToMoveOnX, pixelsToMoveOnY);
};

MstrMngr.handlePageSelection = function(event) {
	var $this = $(this);
//	if($this.hasClass('clicked')) {
//		$this.removeAttr('style').removeClass('clicked');
//	} else{
//		$this.css('background','#7fc242').addClass('clicked');
//	}
	
	
	var SLCTD_PG_INFO = $this.attr('pageid');
	$("#slctdPageInfo").text();
	$("#slctdPage").html($this.html());

	var $slctdPage = new Image();
	$slctdPage.src = $("#slctdPage img").attr("src");
//	alert('width: ' + image.naturalWidth + ' and height: ' + image.naturalHeight);
	
	var pgNaturlalWidth = $slctdPage.naturalWidth,
		pgNaturalHeight = $slctdPage.naturalHeight,
		pgWidth = $("#slctdPage img").width(),
		pgHeight = $("#slctdPage img").height();
	
var scaleX =  pgNaturlalWidth / pgWidth,
	scaleY =  pgNaturalHeight / pgHeight,
	vwPortWidth = pgWidth * scaleX,
	vwPortHeight = pgHeight * scaleY;


	var svg = d3.select("#slctdPage")
				.append("svg")
				.attr("width", $("#slctdPage img").width())
				.attr("height", $("#slctdPage img").height())
				.attr("class","sgmntnOverlay")
				.attr("viewBox","0 0 " + " " + vwPortWidth + " " + vwPortHeight);
//				.attr("preserveAspectRatio","xMinYMin meet")
//				.append('svg:g');
//				.call(d3.behavior.zoom().on("zoom", redraw))
//				.append('svg:g');
//				preserveAspectRatio="xMinYMin meet"      style="border: 1px solid #cccccc;"
		

	var tip = d3.tip()
		.attr('class', 'd3-tip')
		.offset([-10, 0])
		.html(function(d) {
			return "<strong>name:</strong> <span style='color:red'>" + d.text + "</span>";
		});

	svg.call(tip);


	d3.json("/media/" + MstrMngr.getSgmntdJSON(SLCTD_PG_INFO), function(error, sgmntdJSON) {

		if(sgmntdJSON === 'undefined' || sgmntdJSON === undefined) {
			return false;
		}
		
		var imgs = svg.selectAll("image").data([0])
						.enter()
						.append("svg:image")
						.attr('image-rendering','optimizeQuality')
						.attr("x", "0")
						.attr("y", "0");

		var img = new Image();

		img.src = sgmntdJSON.imagepath;

		img.onload=function(){
//			alert(this.width + "  &  " + this.height);
			var width=this.width;
			var height=this.height;
			imgs.attr("width", width)
				.attr("height",height);
		}
		
	//Draw the Rectangle

		var rectangle = svg.selectAll("rect").data(sgmntdJSON.segments)
							.enter()
							.append("svg:rect")
							.attr("class","overlay")
							.attr("pointer-events", "all")
							.attr("x", function (d) { return d.geometry.x; } )
							.attr("y", function (d) { return d.geometry.y; } )
							.attr("width", function (d) { return d.geometry.height; } )
							.attr("height", function (d) { return d.geometry.width; } )
							.style("fill-opacity",0.2)
							.attr('fill',function (d) { return "blue"; } );
//							.on('mouseover',tip.show)
//							.on('mouseout',tip.hide)
//							.on("click", MstrMngr.showAnnotaionDailog($(this)));
	});
	
/*	$("#slctdPage").Jcrop({
		bgColor: 'red'
	},function(){
		jcrop_api = this;
	});
	jcrop_api.disable();*/
	$(".img-selector").on("click", MstrMngr.onClickImgSelector);
};


function redraw() {
	svg.attr("transform", "translate(" + d3.event.translate + ")scale(" + d3.event.scale + ")");
}


/*MstrMngr.showAnnotaionDailog = function (compref) {
		
	var dialogHtml = '<div id="slctdAnnotation"><img alt="Selected Annotaton" src="{{ MEDIA_URL }}book1/k1.jpg" id="slctdImg"></div>'
	+ '<div>'
	+ '		Comments:	<input type="text" id="comments" />'
	+ ' 	Remarks: 	<input type="text" id="remarks" />'
	+ '</div>';

	$("#annotaion_dialog_form").html(dialogHtml);

	var rx = 100 / $(compref).attr('width');
	var ry = 100 / $(compref).attr('height');
	$('#slctdAnnotation').css({
		overflow: 'hidden',
		width: $(compref).attr('width') + 'px',
		height: $(compref).attr('height') + 'px'
	});
	
	$('#slctdImg').css({
		position: 'relative',
		overlow: 'hidden',
//		width: Math.round(rx * 1391) + 'px',
//		height: Math.round(ry * 1851) + 'px',
		width: '1391px',
		height: '1851px',
		marginLeft: '-' + $(compref).attr('x') + 'px',
		marginTop: '-' + $(compref).attr('y') + 'px'
	});

	var dialogOBJ = $( "#annotaion_dialog_form" ).dialog({
//		autoOpen: false,
		height: 200,
		width: 350,
		modal: true,
		buttons: {
			"Add an annotation": MstrMngr.addAnnotation,
			Cancel: function() {
				dialogOBJ.dialog( "close" );
			}
		},
		close: function() {
			allFields.removeClass( "ui-state-error" );
		}
	});

	
};
*/
MstrMngr.addAnnotation = function() {
	var valid = true;
	allFields.removeClass( "ui-state-error" );

	
	valid = valid && checkLength( comments, "comments", 3, 100 );
	valid = valid && checkLength( remarks, "remarks", 6, 100 );

	if ( valid ) {

		
		
		dialog.dialog( "close" );
	}
      return valid;
};


MstrMngr.onClickImgSelector = function() {
//	if(jcrop_api === null) {	
//		$("#slctdPage").Jcrop({
//			bgColor: 'red'
//		},function(){
//			jcrop_api = this;
//		});
//	} else {
//		jcrop_api.destroy();
//	}

/*	if($(".img-selector").hasClass("clicked")) {
		$(".img-selector").removeClass("clicked");
		jcrop_api.disable();
	} else {
		$(".img-selector").addClass("clicked");
		jcrop_api.enable();
	}*/
};

MstrMngr.getJsonFrom = function(srvcURL) {
	
	return jqxhr.responseText;
};

function checkLength( o, n, min, max ) {
	if ( o.val().length > max || o.val().length < min ) {
		o.addClass( "ui-state-error" );
		updateTips( "Length of " + n + " must be between " +
				min + " and " + max + "." );
		return false;
	} else {
		return true;
	}
 };

MstrMngr.getSgmntdJSON = function(pgPath) {
	return pgPath.replace(/images/g, '/segments').replace(/\.jpg/g, '_segments.json');
};

var getBookJSON =  '{"images":["public/images/halayudha1/aksharunicodetext.jpg","public/images/halayudha1/vishnu-chalisa.jpg",'
	+'"public/images/halayudha1/P1000395.jpg","public/images/halayudha1/upanishad1.jpg","public/images/halayudha1/hindi-sample.jpg",'
	+'"public/images/halayudha1/P1000395.jpg","public/images/halayudha1/upanishad1.jpg","public/images/halayudha1/hindi-sample.jpg",'
	+'"public/images/halayudha1/P1000395.jpg","public/images/halayudha1/upanishad1.jpg","public/images/halayudha1/hindi-sample.jpg",'
	+'"public/images/halayudha1/P1000395.jpg","public/images/halayudha1/P1000395.jpg"]}';

var bookJSON = '{"annotation": {"author": "", "comment": "", "date": "", "matches": [], "rank": "0-10", "refs": [], "see_also": [], "text": ""},'
	
	+  '"book": {"annotations": [], "author": "", "imagedirpath": "./visual-search/indexedbooks/", "images": ["/media/book1/k1.jpg", "/media/book1/k1.jpg", "/media/book1/k1.jpg", "media/book1/k1.jpg"], "pages": [], "title": ""},' 
	+	'"column": {"annotations": [], "geometry": {"sizex": 300, "sizey": 300, "startx": 0, "starty": 0}, "sections": [], "title": ""},'
	+	'"line": {"annotations": [], "geometry": {"sizex": 300, "sizey": 300, "startx": 0, "starty": 0}, "phrases": [], "text": ""},'
	+	'"page": {"angle": 30.0, "annotations": [], "colspace": "10px", "columns": [], "linespace": "5px", "ncolumns": 2, "pagenum": 1, "templateimgpath": "", "wordspace": "2px"},' 
	+	' "phrase": {"annotations": [], "geometry": {"sizex": 300, "sizey": 300, "startx": 0, "starty": 0}},'
	+	'"section": {"annotations": [], "geometry": {"sizex": 300, "sizey": 300, "startx": 0, "starty": 0},"lines": [], "text": "", "title": "", "type": ["paragraph", "footnote", "pagenum", "notes"]}'
	+	'}';

var book2JSON = '{"annotation": {"author": "", "comment": "", "date": "", "matches": [], "rank": "0-10", "refs": [], "see_also": [], "text": ""},'

	+  '"book": {"annotations": [], "author": "", "imagedirpath": "./visual-search/indexedbooks/", "images": ["/media/book1/o1.jpg", "/media/book1/o2.jpg", "/media/book1/o3.jpg", "media/book1/o4.jpg"], "pages": [], "title": ""},' 
	+	'"column": {"annotations": [], "geometry": {"sizex": 300, "sizey": 300, "startx": 0, "starty": 0}, "sections": [], "title": ""},'
	+	'"line": {"annotations": [], "geometry": {"sizex": 300, "sizey": 300, "startx": 0, "starty": 0}, "phrases": [], "text": ""},'
	+	'"page": {"angle": 30.0, "annotations": [], "colspace": "10px", "columns": [], "linespace": "5px", "ncolumns": 2, "pagenum": 1, "templateimgpath": "", "wordspace": "2px"},' 
	+	' "phrase": {"annotations": [], "geometry": {"sizex": 300, "sizey": 300, "startx": 0, "starty": 0}},'
	+	'"section": {"annotations": [], "geometry": {"sizex": 300, "sizey": 300, "startx": 0, "starty": 0},"lines": [], "text": "", "title": "", "type": ["paragraph", "footnote", "pagenum", "notes"]}'
	+	'}';

var book3JSON = '{"annotation": {"author": "", "comment": "", "date": "", "matches": [], "rank": "0-10", "refs": [], "see_also": [], "text": ""},'

	+  '"book": {"annotations": [], "author": "", "imagedirpath": "./visual-search/indexedbooks/", "images": ["/media/book1/k1.jpg", "/media/book1/k1.jpg", "/media/book1/k1.jpg", "media/book1/k1.jpg"], "pages": [], "title": ""},' 
	+	'"column": {"annotations": [], "geometry": {"sizex": 300, "sizey": 300, "startx": 0, "starty": 0}, "sections": [], "title": ""},'
	+	'"line": {"annotations": [], "geometry": {"sizex": 300, "sizey": 300, "startx": 0, "starty": 0}, "phrases": [], "text": ""},'
	+	'"page": {"angle": 30.0, "annotations": [], "colspace": "10px", "columns": [], "linespace": "5px", "ncolumns": 2, "pagenum": 1, "templateimgpath": "", "wordspace": "2px"},' 
	+	' "phrase": {"annotations": [], "geometry": {"sizex": 300, "sizey": 300, "startx": 0, "starty": 0}},'
	+	'"section": {"annotations": [], "geometry": {"sizex": 300, "sizey": 300, "startx": 0, "starty": 0},"lines": [], "text": "", "title": "", "type": ["paragraph", "footnote", "pagenum", "notes"]}'
	+	'}';

var bookLstJSON = '[{"id":"1","name":"Bagavatha"},{"id":"2","name":"Ramayana"},{"id":"3","name":"Bharatha"}]';