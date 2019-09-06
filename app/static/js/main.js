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

    var keys = Object.keys(data_obj)
    for (var i = 0; i < keys.length; i++) {
        players.push(keys[i])
        measurements.push(data_obj[keys[i]]['Measure'])
        stats.push(data_obj[keys[i]]['Stat'])
    }

    var svg = d3.select('#bar_chart')
    var margin = 50
    var width = svg.attr("width")
    var height = svg.attr("height") - margin

    var xScale = d3.scaleBand().range([0, width]).padding(0.1)
    var yScale = d3.scaleLinear().range([height, 0])

    var g = svg.append('g')

    xScale.domain(players)
    yScale.domain([0, d3.max(0, measurements)])

    g.append('g').attr("transform", "translate(0," + (height - 50) + ")").call(d3.axisBottom(xScale).ticks(10)).selectAll("text").attr('transform', 'rotate(45)').attr('dx', '2.5em')
    g.append('g').call(d3.axisLeft(yScale).ticks(10)).append("text").attr("y", 6).attr("dy", "0.71em").attr('transform', 'rotate(90)').attr("text-anchor", "end")

}

///
/// Main Area
///
createBaseballStatsList()

var yearSelected = false
var statSelected = false
var measureSelected = false