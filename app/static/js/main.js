function createBaseballStatsList() {
    var current_stats = ['W', 'L', 'WinLossPercentage', 'ERA', 'G', 'GS', 'GF', 'CG', 'SHO', 'SV', 'IP', 'H', 'R', 'ER', 'HR', 'BB', 'IBB', 'SO', 'HBP', 'BK', 'WP', 'BF', 'ERAPLUS', 'FIP', 'WHIP', 'H9', 'HR9', 'BB9', 'SO9', 'StrikeoutsPerWalk']
    var listElement = $('#statList')

    for (var i = 0; i < current_stats.length; i++) {
        listElement.append('<button onclick="clickedElem(this)" class="dropdown-item" id="stats">' + current_stats[i] + '</button>')
    }
}

function clickedElem(element) {
    var dropdown_elem = $('#' + element.id + 'MenuButton')
    dropdown_elem.text(element.innerHTML)

    if (element.id == 'year') {
        yearSelected = true
    } else if (element.id == 'stats') {
        statSelected = true
    } else if (element.id == 'measure'){
        measureSelected = true
    } else {
        return Error("Invalid element was selected")
    }

    extractDataFormSql()
}

function extractDataFormSql() {
    if (yearSelected && statSelected && measureSelected) {
        var dataToSend = {
            Year: $('#yearMenuButton').html(),
            Stat: $('#statsMenuButton').html(),
            Measure: $('#measureMenuButton').html()
        }

        $.ajax({
            url: '/',
            type: 'POST',
            data: dataToSend,
            success: function(result) {
                return createCharts(result)
            },
            error: function(error) {
                console.log(error)
            }
        })
    }
}
function createCharts(data_str) {
    var data_obj = JSON.parse(data_str)
    var players = []
    var measurements = []
    var stats = []
    var final_data = []
    var keys = Object.keys(data_obj)
    for (var i = 0; i < keys.length; i++) {
        final_data.push({})
        final_data[final_data.length - 1]["name"] = keys[i]
        final_data[final_data.length - 1]["stat"] = data_obj[keys[i]]['Stat']
        final_data[final_data.length - 1]["measure"] = data_obj[keys[i]]['Measure']
    }

    var svg = d3.select('#bar_chart')
    var margin = 200
    var width = svg.attr("width")
    var height = svg.attr("height") - margin

    svg.append("text")
       .attr("transform", "translate(100,0")
       .attr("x", 120)
       .attr("y", 50)
       .attr("font-size", "24px")
       .text("Player's Measurements based on Statistic")
    var xScale = d3.scaleBand().range([0, width]).padding(0.5)
    var yScale = d3.scaleLinear().range([height, 0])

    var g = svg.append('g').attr("transform", "translate(" + 25 + ',' + 100 + ")")

    xScale.domain(final_data.map(function(d) {return d.name}))
    yScale.domain([50, d3.max(final_data.map(function(d) {return d.measure}))])

    g.append('g').attr("transform", "translate(0," + height + ")").call(d3.axisBottom(xScale)).selectAll("text").style("font-size", 7)
    g.append('g').call(d3.axisLeft(yScale).ticks(10)).append("text").attr("y", 6).attr("dy", "0.71em").attr("text-anchor", "end").text('value')

    g.selectAll(".bar")
     .data(final_data)
     .enter().append("rect")
     .attr("class", "bar")
     .on("mouseover", onMouseOver)
     .on("mouseout", onMouseOut)
     .attr("x", function(d) { return xScale(d.name)})
     .attr("y", function(d) { return yScale(d.measure)})
     .attr("width", xScale.bandwidth())
     .attr("height", function(d) { return height - yScale(d.measure)})

     function onMouseOver(d, i) {
         d3.select(this).attr('class', 'highlight')
         d3.select(this)
           .transition()
           .duration(400)
           .attr('width', xScale.bandwidth() + 5)
           .attr("y", function(d) { return yScale(d.measure) - 10})
           .attr("height", function(d) {return height - yScale(d.measure) + 10})

        g.append("text")
         .attr('class', 'val')
         .attr('x', function() {
             return xScale(d.name) + 8
         })
         .attr('y', function() {
             return yScale(d.measure) - 15
         })
         .text(function() {
             console.log(d.measure)
             return [d.measure]
         })
     }

     function onMouseOut(d, i) {
        d3.select(this).attr('class', 'bar')
        d3.select(this)
          .transition()
          .duration(400)
          .attr('width', xScale.bandwidth())
          .attr("y", function(d) {return yScale(d.measure)})
          .attr("height", function(d) { return height - yScale(d.measure)})

        d3.selectAll('.val').remove()
     }
}

///
/// Main Area
///
createBaseballStatsList()

var yearSelected = false
var statSelected = false
var measureSelected = false