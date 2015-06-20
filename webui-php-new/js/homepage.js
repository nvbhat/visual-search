/**
 * 
 */

var MstrMngr = function () {};
$(MstrMngr.registerMstrListEvents);

MstrMngr.registerMstrListEvents = function() {
	//$("#bookList ol li").on('click', MstrMngr.onClickBook);
	$(".add-new-book").on("click", MstrMngr.addNewBook);
	//$(".tn3-in-image").on("click", MstrMngr.inlineZoom);
	//$("#zoomImage").on('click', alert);
	
};

MstrMngr.addNewBook = function() {
var importbook="multiupload.php";
//var importbook="importbook.html";
window.location.href=importbook;
};

MstrMngr.onClickBook = function() {
alert("jeee");
	var tixOptions = {autoplayInterval:9999999999,
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


                case 'booktest':

                               //var imgfile="gg.png";
                               //processImg(imgfile);
                             var book="visualsearch/indexedbooks/Kan.json";
                              processBook(book);
       		 $("#mygallery-book4").css("display", "none");
		       $("#mygallery-book3").css("display", "none");
			break;

	}
	$(GALLERY_ID).css("display", "block");
	$(GALLERY_ID).tiksluscarousel(tixOptions);
	
	$('.zoom').zoom();
};

MstrMngr.showBooks = function () {
	$(".demo-wrapper").css('display', 'block');
};

MstrMngr.onSelectPage = function() {
	$('#gallery-container').sGallery({
		fullScreenEnabled: true
	});
};

MstrMngr.inlineZoom = function() {
	$(this).zoomTarget();
};

MstrMngr.zoomImage = function (event) {
	$("#o1").zoomTarget();
};
