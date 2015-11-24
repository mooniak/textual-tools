$(function () {
    var data=function(lables, vals){
        var out={
            labels: lables,
            series: [
                vals
            ]
        };
        return out;
    }

    var options=function(ledger){
        var out = {
            reverseData: true,
            horizontalBars: true,
            fullWidth: true,
            showArea:true,
            height:ledger.length*20+'px',
            axisY: {
                offset: 70
            }
        };
        return out
    }



    $('#single').css('height',ledgerSingleLables.length*20);
    $('#double').css('height',ledgerDoubleLables.length*20);
    $('#triple').css('height',ledgerTripleLables.length*20);
    new Chartist.Bar('#single', data(ledgerSingleLables,ledgerSingleVals), options(ledgerSingleLables));
    new Chartist.Bar('#double', data(ledgerDoubleLables,ledgerDoubleVals), options(ledgerDoubleLables));
    new Chartist.Bar('#triple', data(ledgerTripleLables,ledgerTripleVals), options(ledgerTripleLables));
});

function textReport(data){
    ledgerSingleLables=[]
    ledgerSingleVals=[]
    ledgerDoubleLables=[]
    ledgerDoubleVals=[]
    ledgerTripleLables=[]
    ledgerTripleVals=[]
    $.each(data.ledgerSingle, function(key, load){
        ledgerSingleVals.push(load);
        ledgerSingleLables.push(key);
    });
    $.each(data.ledgerDouble, function(key, load){
        ledgerDoubleVals.push(load);
        ledgerDoubleLables.push(key);
    });
    $.each(data.ledgerTriple, function(key, load){
        ledgerTripleVals.push(load);
        ledgerTripleLables.push(key);
    });
}