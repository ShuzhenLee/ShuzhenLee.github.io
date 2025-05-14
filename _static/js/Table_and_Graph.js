document.addEventListener('DOMContentLoaded', (function() {
    var newChart;
    var cumu_1_Chart;

    // Function to initialize the new chart with Period 1 data
    function initializeNewChart() {
        newChart = Highcharts.chart('newContainer', {
            credits: { enabled: false },
            exporting: { enabled: false },
            title: { text: 'Return by Period', align: 'left' },
            subtitle: { enabled: false },
            xAxis: {
                title: { text: 'Period' },
                type: 'linear',
                min: 0, // Start from Period 0
                max: 45,
                tickLength: 0,
                minorTickLength: 0,
                tickInterval: 1,
                labels: {
                    formatter: function() { return (this.value); }, // Display Period 1, Period 2, etc.
                    align: 'center',
                    step: 1
                }
            },
            yAxis: [{ title: { text: 'Return (%)' }, labels: { format: '{value:.2f}%' } }],
            legend: { align: 'left', verticalAlign: 'top', borderWidth: 0 },
            tooltip: {
                formatter: function() {
                    var points = this.points,
                        tooltipLines = [];
                    points.sort(function(a, b) { return b.y - a.y; });
                    points.forEach(function(point) {
                        tooltipLines.push('<span style="color:' + point.color + '">●</span> ' + point.series.name + ': <b>' + point.y + '%</b><br/>');
                    });
                    var periodNumber = parseInt(this.x, 10) ;
                    tooltipLines.unshift('<b>Period ' + periodNumber + '</b><br/>');
                    return tooltipLines.join('');
                },
                shared: true,
                crosshairs: true
            },
            plotOptions: {
                series: {
                    label: { enabled: false },
                    dataLabels: { enabled: false }
                }
            },
            series: [
                { name: 'Conventional Fund', data: [], color: '#808080' },
                { name: 'Sustainable Fund', data: [], color: '#008000FF' },
            ]
        });

        // Add a plot line
        newChart.xAxis[0].addPlotLine({
            color: 'lightgray',
            width: 0.8,
            value: 45,
            zIndex: 5
        });

        // Prepend a starting point of 0 to the data
        let susData = [{ x: 0, y: 0 }].concat(chartData.susData.map((value, index) => ({ x: index + 1, y: value })));
        let conData = [{ x: 0, y: 0 }].concat(chartData.conData.map((value, index) => ({ x: index + 1, y: value })));

        // Set the data for the chart
        newChart.series[0].setData(conData, false);
        newChart.series[1].setData(susData, false); // Add all Sustainable Fund data

        newChart.redraw();
    }


    function initializeCumulativeChart() {
        cumu_1_Chart = Highcharts.chart('cumu_1_Container', {
            credits: { enabled: false },
            exporting: { enabled: false },
            title: { text: 'Cumulative Return (over the past 45 periods)', align: 'left' },
            // subtitle: { text: 'Source: Fund websites', align: 'left' },
            xAxis: {
                title: { text: 'Period' },
                type: 'linear',
                min: 0, // Start from Period 0
                max: 45,
                tickLength: 0,
                minorTickLength: 0,
                tickInterval: 1,
                labels: {
                    formatter: function() {
                        return this.value === 0 ? '0' : this.value;},
                    // rotation: -45,
                    align: 'center',
                    step: 1
                }
            },
            yAxis: [{ title: { text: 'Cumulative Return (%)' }, labels: { format: '{value:.2f}%' } }],
            legend: { align: 'left', verticalAlign: 'top', borderWidth: 0 },
            tooltip: {
                formatter: function() {
                    var points = this.points,
                        tooltipLines = [];
                    points.sort(function(a, b) { return b.y - a.y; });
                    points.forEach(function(point) {
                        tooltipLines.push('<span style="color:' + point.color + '">●</span> ' + point.series.name + ': <b>' + point.y + '%</b><br/>');
                    });
                    var periodNumber = parseInt(this.x, 10);
                    tooltipLines.unshift('<b>Period ' + periodNumber + '</b><br/>');
                    return tooltipLines.join('');
                },
                shared: true,
                crosshairs: true
            },
            plotOptions: {
                series: {
                    label: { enabled: false, },
                    dataLabels: { enabled: false, allowOverlap: false }
                }
            },
            series: [{
                name: 'Conventional Fund',
                data: window.CumulativeDataEveryPeriod.TRConData,
                color: '#808080'
            }, {
                name: 'Sustainable Fund',
                data: window.CumulativeDataEveryPeriod.TRSusData,
                color: '#008000FF'
            }, ]
        });
        // add a stop line
        cumu_1_Chart.xAxis[0].addPlotLine({
            color: 'lightgray',
            width: 0.8,
            value: 45,
            zIndex: 5
        });
        cumu_1_Chart.redraw();
    }

        // Function to render the summary table
    function renderSummaryTable() {
        const summaryData = window.summaryData[0];
        let tableHTML = `
            <table style="width: 100%; border-collapse: collapse; text-align: center; font-size: 12px; white-space: nowrap">
                <caption style="font-family: Arial; font-size: 18px; color: rgb(51, 51, 51); font-weight: bold; fill: rgb(51, 51, 51); text-align=left">
                    Summary of Fund Performance (over the past 45 periods)
                </caption>
                <tr>
                    <th></th>
                   <th>Conventional Fund</th>
                   <th>Sustainable Fund</th>
                </tr>
                <tr>
                    <td>Cumulative Return</td>
                    <td>${summaryData.cumulative.con}%</td>
                    <td>${summaryData.cumulative.sus}%</td>
                </tr>
                <tr>
                    <td>Average Return Per Period</td>
                    <td>${summaryData.averageReturns.con}%</td>
                    <td>${summaryData.averageReturns.sus}%</td>
                </tr>
                <tr>
                    <td>Volatility</td>
                    <td>${summaryData.volatilities.con}%</td>
                    <td>${summaryData.volatilities.sus}%</td>
                </tr>
                <tr>
                    <td>Sharpe Ratio</td>
                    <td>${summaryData.sharpeRatios.con}</td>
                    <td>${summaryData.sharpeRatios.sus}</td>
                </tr>
        `;
        // Close the table
        tableHTML += `
            </table>
        `;

        document.getElementById('summaryTableContainer').innerHTML = tableHTML;
    }

    renderSummaryTable();

    function updateDataLabels(chartname) {
        var series1 = chartname.series[0];
        var series2 = chartname.series[1];

            // Disable data labels for all points in each series
        [series1, series2].forEach(series => {
            series.data.forEach(point => point.update({ dataLabels: { enabled: false } }, false));
        });
        chartname.redraw(); // Force Highcharts to apply these updates first

        // Only enable data labels for the last point if it exists
        if (series1.data.length > 0 && series2.data.length > 0) {
            var lastPoint1 = series1.data[series1.data.length - 1];
            var lastPoint2 = series2.data[series2.data.length - 1];

            // Calculate offsets to prevent overlap
            const offset1 = lastPoint1.plotY < lastPoint2.plotY ? -20 : 20;
            const offset2 = lastPoint1.plotY < lastPoint2.plotY ? 20 : -20;

            lastPoint1.update({ dataLabels: { enabled: true, format: '{y:.2f}%', style: { fontWeight: 'bold' },
                    color: lastPoint1.color, y: offset1, x: 10, allowOverlap: false } }, false);
            lastPoint2.update({ dataLabels: { enabled: true, format: '{y:.2f}%', style: { fontWeight: 'bold' },
                    color: lastPoint2.color, y: offset2, x: 10, allowOverlap: false } }, false);
        }
        chartname.redraw();
    }
    initializeNewChart();
    updateDataLabels(newChart);

    document.getElementById('next-button').addEventListener('click', function (event) {
        event.preventDefault();
            initializeCumulativeChart();
            updateDataLabels(cumu_1_Chart);
    });

}),);
