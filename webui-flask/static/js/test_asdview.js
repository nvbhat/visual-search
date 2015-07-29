


            var svg = d3.select("body")

                .append("svg")

                .attr("width","100%")

                .attr("height","100%")

                .style("border", "1px solid black")

 .append('svg:g')

    .call(d3.behavior.zoom().on("zoom", redraw))

  .append('svg:g');
//.attr("preserveAspectRatio","none") ;



var tip = d3.tip()

  .attr('class', 'd3-tip')

  .offset([-10, 0])

  .html(function(d) {

    return "<strong>name:</strong> <span style='color:red'>" + d.text + "</span>";});

svg.call(tip);

console.log('hello');

d3.json("./visual-search/segmented-books/Kandanu1_coordinates.json",function(error,test) {

        console.log(test.imagepath);

        var imgs = svg.selectAll("image").data([0])

                .enter()

 		.append("svg:image")

                .attr('image-rendering','optimizeQuality')

                .attr("xlink:href", test.imagepath)

                .attr("x", "0")

                .attr("y", "0");

var img = new Image();

img.src=test.imagepath;

img.onload=function(){

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
                        .on('mouseover',tip.show)
                        .on('mouseout',tip.hide)
	.on("click",function goToURL() {
		  window.open("form.html");
});

});

function redraw() {

//console.log("here", d3.event.translate, d3.event.scale);

svg.attr("transform", "translate(" + d3.event.translate + ")scale(" + d3.event.scale + ")");

}
