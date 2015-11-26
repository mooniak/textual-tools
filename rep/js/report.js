$(function () {
    var data = function (lables, vals) {
        var out = {
            labels: lables,
            series: [
                vals
            ]
        };
        return out;
    };

    var options = function (ledger) {
        var out = {
            reverseData: true,
            horizontalBars: true,
            fullWidth: true,
            height: ledger.length * 30 + 'px',
            axisX: {
                position: 'start'
            },
            axisY: {
                offset: 70
            }, 
            chartPadding: {
                right: 40
            },
            labelInterpolationFnc: function(value) {
      return value + ' CHF'
    },
        };
        return out
    };

    $('#charachters').html("Charachters : " + charCount);
    $('#charachters_s').html("Charachters without white spaces : " + charCountNoWhiteSpace);
    $('#words').html("words : " + wordCount);
    $('#range').html("range : " + unicodeRange);
    $('#source').html("source : <a href=" + source + "'>" + source + "</a>");
    $('#files').html("files :  <a href=" + name + "'>" + name + "</a>");
    $('#single').css('height', ledgerSingleLables.length * 30);
    $('#double').css('height', ledgerDoubleLables.length * 30);
    $('#triple').css('height', ledgerTripleLables.length * 30);
    new Chartist.Bar('#single', data(ledgerSingleLables, ledgerSingleVals), options(ledgerSingleLables));
    new Chartist.Bar('#double', data(ledgerDoubleLables, ledgerDoubleVals), options(ledgerDoubleLables));
    new Chartist.Bar('#triple', data(ledgerTripleLables, ledgerTripleVals), options(ledgerTripleLables));
});

function textReport(data) {
    ledgerSingleLables = [];
    ledgerSingleVals = [];
    ledgerDoubleLables = [];
    ledgerDoubleVals = [];
    ledgerTripleLables = [];
    ledgerTripleVals = [];
    $.each(data.ledgerSingle, function (key, load) {
        ledgerSingleVals.push(load.count);
        ledgerSingleLables.push(load.character);
    });
    $.each(data.ledgerDouble, function (key, load) {
        ledgerDoubleVals.push(load.count);
        ledgerDoubleLables.push(load.character);
    });
    $.each(data.ledgerTriple, function (key, load) {
        ledgerTripleVals.push(load.count);
        ledgerTripleLables.push(load.character);
    });
    charCount = data.charCount;
    charCountNoWhiteSpace = data.charCountNoWhiteSpace;
    wordCount = data.wordCount;
    unicodeRange = data.unicodeRange;
    name = data.name;
    source = data.source;
}