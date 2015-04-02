/**
 * 
 */

var MstrMngr = function () {};
$(MstrMngr.registerMstrListEvents);


var comments = $( "#comments" ),
remarks = $( "#remarks" ),
allFields = $( [] ).add( comments ).add( remarks ),
tips = $( ".validateTips" );

MstrMngr.registerMstrListEvents = function() {
	$("#bookList ol li").on('click', MstrMngr.onClickBook);
	$(".add-new-book").on("click", MstrMngr.addNewBook);
	$(".tn3-in-image").on("click", MstrMngr.onClickInlineZoom);
	$("#zoomImage").on('click', alert);

	$("#inlineZoom").on("click", MstrMngr.onClickInlineZoom);
	$("#topPositionMap,#leftPositionMap,#rightPositionMap,#bottomPositionMap").on("click", MstrMngr.moveButtonClickHandler);
	$("#zoomInButton,#zoomOutButton").on("click", MstrMngr.zoomButtonClickHandler);
	
};

MstrMngr.addNewBook = function() {
	alert();
};

MstrMngr.onClickBook = function() {
	
	$("#mygallery-book1").css("display", "block");
	
	$("#mygallery-book1").owlCarousel({
 
		autoPlay: 3000, //Set AutoPlay to 3 seconds
 
		items : 4,
		itemsDesktop : [1199,3],
		itemsDesktopSmall : [979,3]
		
	});
	
/*	var tixOptions = {autoplayInterval:9999999999,
			nav:'thumbnails',
			navIcons:false,
			loader:'/static/img/ajax-loader.gif'
		};
	var GALLERY_ID = "#mygallery-" + this.id;

	switch(this.id) {
	    case 'book1':
	    	$("#mygallery-book2").css("display", "none");
			$("#mygallery-book3").css("display", "none");
	        break;
	    case 'book2':
	    	$("#mygallery-book1").css("display", "none");
			$("#mygallery-book3").css("display", "none");
	        break;
	    case 'book3':
	    	$("#mygallery-book1").css("display", "none");
			$("#mygallery-book2").css("display", "none");
	        break;
	}
	$(GALLERY_ID).css("display", "block");
	$(GALLERY_ID).tiksluscarousel(tixOptions);

	$('.tslider').smartZoom({'containerClass':'zoomableContainer'});*/
//	$('.zoom').zoom();
};

MstrMngr.showBooks = function () {
	$(".demo-wrapper").css('display', 'block');
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
	$("#slctdPageInfo").text($this.attr('pageid'));
	$("#slctdPage").html($this.html());


var scaleX =  1391 / $("#slctdPage img").width(),
	scaleY =  1851 / $("#slctdPage img").height(),
	vwPortWidth = $("#slctdPage img").width() * scaleX,
	vwPortHeight = $("#slctdPage img").height() * scaleY;


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


	d3.json("/static/json/Kandanu1_coordinates.json", function(error,test) {


		var imgs = svg.selectAll("image").data([0])
						.enter()
						.append("svg:image")
						.attr('image-rendering','optimizeQuality')
						.attr("x", "0")
						.attr("y", "0");

		var img = new Image();

		img.src=test.imagepath;

		img.onload=function(){
			alert(this.width + "  &  " + this.height);
			var width=this.width;
			var height=this.height;
			imgs.attr("width", width)
				.attr("height",height);
		}





	//Draw the Rectangle

		var rectangle = svg.selectAll("rect").data(test.segments)
							.enter()
							.append("svg:rect")
							.attr("class","overlay")
							.attr("pointer-events", "all")
							.attr("x", function (d) { return d.geometry.x; } )
							.attr("y", function (d) { return d.geometry.y; } )
							.attr("width", function (d) { return d.geometry.height; } )
							.attr("height", function (d) { return d.geometry.width; } )
							.style("fill-opacity",0.2)
							.attr('fill',function (d) { return "blue"; } )
//							.on('mouseover',tip.show)
//							.on('mouseout',tip.hide)
							.on("click",function goToURL() {
								MstrMngr.showAnnotaionDailog($(this));
							});
	});
	
//	$("#slctdPage").Jcrop({});
};


function redraw() {
	svg.attr("transform", "translate(" + d3.event.translate + ")scale(" + d3.event.scale + ")");
}


MstrMngr.showAnnotaionDailog = function (compref) {
		
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

	dialog = $( "#annotaion_dialog_form" ).dialog({
//		autoOpen: false,
		height: 200,
		width: 350,
		modal: true,
		buttons: {
			"Add an annotation": MstrMngr.addAnnotation,
			Cancel: function() {
				dialog.dialog( "close" );
			}
		},
		close: function() {
			allFields.removeClass( "ui-state-error" );
		}
	});

	
};

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

function checkLength( o, n, min, max ) {
    if ( o.val().length > max || o.val().length < min ) {
      o.addClass( "ui-state-error" );
      updateTips( "Length of " + n + " must be between " +
        min + " and " + max + "." );
      return false;
    } else {
      return true;
    }
  }