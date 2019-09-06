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
                return data_obj(result)
            },
            error: function(error) {
                console.log(error)
            }
        })
    }
}
function createCharts(data_obj) {

}

///
/// Main Area
///
createBaseballStatsList()

var yearSelected = false
var statSelected = false
var measureSelected = false