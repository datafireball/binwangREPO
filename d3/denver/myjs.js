var chartsvg = d3.select('#chart')
	.append('svg')
		.attr('width', 400)
		.attr('height', 60)
		.style('background', '#93A1A1');

var populate = function(j){
	d3.select('#photo'+j).on('mouseover', function(){
		// find the photo tag and remove all the img tags inside
		d3.select('#photo').selectAll('img').remove();
		// create new img tag and populate an image based on its id
    	d3.select('#photo').append("img")
            .attr("src","images/" + j + ".jpeg" )
            .attr("x", -8)
            .attr("y", -8)
            .attr("width","500px")                  
            .attr("height","500px"); 
	});
}

// Note: for loop in javascript is really tricky and pay attention to the lexical scope and closure
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Closures
for (i = 0; i < 16; i++) { 
	// create a new rectangular and set its ip to be photo_n
	chartsvg.append('rect')
			.attr('x', i * 25)
			.attr('y', 20)
			.attr('width', 20)
			.attr('height', 20)
			.attr('fill', '#'+ Math.floor(Math.random()*16777215).toString(16))
			.attr('id', 'photo' + i);
	populate(i);
}


