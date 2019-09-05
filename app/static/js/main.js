function createBaseballStatsList() {
    var current_stats = ['W', 'L', 'WinLossPercentage', 'ERA', 'G', 'GS', 'GF', 'CG', 'SHO', 'SV', 'IP', 'H', 'R', 'ER', 'HR', 'BB', 'IBB', 'SO', 'HBP', 'BK', 'WP', 'BF', 'ERAPLUS', 'FIP', 'WHIP', 'H9', 'HR9', 'BB9', 'SO9', 'StrikeoutsPerWalk']
    var listElement = $('#statList')

    for (var i = 0; i < current_stats.length; i++) {
        listElement.append('<a class="dropdown-item" href="#">' + current_stats[i] + '</a>')
    }
}

createBaseballStatsList()