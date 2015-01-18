
var state = true;

d3.select("#switch").on('click', function(){

		if (state == 1){
			d3.select("button").transition().style("background-color", "red");
			d3.select("#photo").selectAll("img").remove();
			d3.select("#photo").selectAll("img").data([0])
            .enter()
            .append("img")
            .attr("src", "data/angry.jpeg")
            .attr("width", "200")
            .attr("height", "200")
            .transition()
            .duration(500)
            .ease('sin')
            .style("margin-left", '100' + 'px');

		} else {
			d3.select("button").transition().style("background-color", "green");
			d3.select("#photo").selectAll("img").remove();
			d3.select("#photo").selectAll("img").data([0])
            .enter()
            .append("img")
            .attr("src", "data/happy.jpeg")
            .attr("width", "200")
            .attr("height", "200")
            .transition()
            .ease('linear')
            .duration(500)
            .style("margin-left", '100' + 'px');

		}
		state = !state;
	}
);
