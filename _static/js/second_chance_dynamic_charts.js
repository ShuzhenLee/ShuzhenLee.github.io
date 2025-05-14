;(function() {
    var cumulativeChart;
    var maxPeriods = 45;
    var second_allocation = parseFloat(document.getElementById('data-container').dataset.second_allocation) || 0; // Retrieve initial decision for Period 1

    // Function to calculate cumulative returns for both funds and the portfolio
    function calculateCumulativeReturns() {
        let cumulativeSustainable = 100;
        let cumulativeConventional = 100;
        let cumulativePortfolio = 100;
        const cumulativeData = {
            sustainable: [['Period 0', 0]],
            conventional: [['Period 0', 0]],
            portfolio: [['Period 0', 0]]
        };

        for (let i = 0; i < maxPeriods; i++) {
            const period = `Period ${i + 1}`;
            const sustainableReturn = parseFloat(chartData[i]['Sustainable Fund']);
            const conventionalReturn = parseFloat(chartData[i]['Conventional Fund']);

            // Calculate cumulative for sustainable and conventional funds
            cumulativeSustainable *= (1 + sustainableReturn);
            cumulativeConventional *= (1 + conventionalReturn);
            cumulativeData.sustainable.push([period, cumulativeSustainable-100]);
            cumulativeData.conventional.push([period, cumulativeConventional-100]);

            // Calculate cumulative portfolio based on the decision applied to fund returns
            const portfolioReturn = (second_allocation / 100) * sustainableReturn + ((100 - second_allocation) / 100) * conventionalReturn;
            cumulativePortfolio *= (1 + portfolioReturn);
            cumulativeData.portfolio.push([period, cumulativePortfolio-100]);
        }
        return cumulativeData;
    }

    // Function to initialize the cumulative chart with all periods
    function initializeCumulativeChart() {
        const cumulativeData = calculateCumulativeReturns();

        cumulativeChart = Highcharts.chart('cumulativeContainer', {
            credits: { enabled: false },
            exporting: { enabled: false },
            title: { text: 'Cumulative Return (over 45 periods)', align: 'left' },
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
                    rotation: 0,
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
                        tooltipLines.push('<span style="color:' + point.color + '">●</span> ' + point.series.name + ': <b>' + point.y.toFixed(2) + '%</b><br/>');
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
                    label: { enabled: false },
                    dataLabels: { enabled: false, allowOverlap: false }
                }
            },
            series: [
                {
                    name: 'Sustainable Fund',
                    data: cumulativeData.sustainable.map(entry => entry[1]),
                    color: '#008000FF',
                    dataLabels: {
                        enabled: true,
                        formatter: function() {
                            if (this.point.index === this.series.data.length - 1) {
                                return this.y.toFixed(2);
                            }
                            return null;
                        },
                        style: { fontWeight: 'bold', fontSize: '12px', color: this.color },
                        align: 'right',
                        verticalAlign: 'middle'
                    }
                },
                {
                    name: 'Conventional Fund',
                    data: cumulativeData.conventional.map(entry => entry[1]),
                    color: '#808080',
                    dataLabels: {
                        enabled: true,
                        formatter: function() {
                            if (this.point.index === this.series.data.length - 1) {
                                return this.y.toFixed(2);
                            }
                            return null;
                        },
                        style: { fontWeight: 'bold', fontSize: '12px', color: this.color },
                        align: 'right',
                        verticalAlign: 'middle'
                    }
                },
                {
                    name: 'Your Portfolio',
                    data: cumulativeData.portfolio.map(entry => entry[1]),
                    color: '#0000FF',
                    dataLabels: {
                        enabled: true,
                        formatter: function() {
                            if (this.point.index === this.series.data.length - 1) {
                                return this.y.toFixed(2);
                            }
                            return null;
                        },
                        style: { fontWeight: 'bold', fontSize: '12px', color: this.color },
                        align: 'right',
                        verticalAlign: 'middle'
                    }
                }
            ]
        });
        // generateSummaryTable(cumulativeData);
    }

    // // Function to generate summary table
    // function generateSummaryTable(cumulativeData) {
    //     const sustainableReturns = chartData.map(d => parseFloat(d['Sustainable Fund']));
    //     const conventionalReturns = chartData.map(d => parseFloat(d['Conventional Fund']));
    //     const portfolioReturns = chartData.map(d => {
    //         const sustainableReturn = parseFloat(d['Sustainable Fund']);
    //         const conventionalReturn = parseFloat(d['Conventional Fund']);
    //         return (second_allocation / 100) * sustainableReturn + ((100 - second_allocation) / 100) * conventionalReturn;
    //     });
    //
    //     const cumulativeSustainableReturn = cumulativeData.sustainable[maxPeriods][1].toFixed(2);
    //     const cumulativeConventionalReturn = cumulativeData.conventional[maxPeriods][1].toFixed(2);
    //     const cumulativePortfolioReturn = cumulativeData.portfolio[maxPeriods][1].toFixed(2);
    //
    //     const avgSustainableReturn = (sustainableReturns.reduce((a, b) => a + b, 0) / maxPeriods * 100).toFixed(2);
    //     const avgConventionalReturn = (conventionalReturns.reduce((a, b) => a + b, 0) / maxPeriods * 100).toFixed(2);
    //     const avgPortfolioReturn = (portfolioReturns.reduce((a, b) => a + b, 0) / maxPeriods * 100).toFixed(2);
    //
    //     const stdDevSustainable = Math.sqrt(sustainableReturns.reduce((acc, val) => acc + Math.pow(val - avgSustainableReturn / 100, 2), 0) / (maxPeriods - 1) * 100).toFixed(2);
    //     const stdDevConventional = Math.sqrt(conventionalReturns.reduce((acc, val) => acc + Math.pow(val - avgConventionalReturn / 100, 2), 0) / (maxPeriods - 1) * 100).toFixed(2);
    //     const stdDevPortfolio = Math.sqrt(portfolioReturns.reduce((acc, val) => acc + Math.pow(val - avgPortfolioReturn / 100, 2), 0) / (maxPeriods - 1) * 100).toFixed(2);
    //
    //     document.getElementById('summaryTable').innerHTML = `
    //         <table style="width: 100%; border-collapse: collapse; text-align: center; font-size: 14px;">
    //             <caption style="font-weight: bold; font-size: 18px; text-align: center;">Summary of Cumulative Performance</caption>
    //             <tr>
    //                 <th></th>
    //                 <th>Conventional Fund</th>
    //                 <th>Sustainable Fund</th>
    //                 <th>Your Portfolio</th>
    //             </tr>
    //             <tr>
    //                 <td><b>Cumulative Return</b></td>
    //                 <td>${cumulativeConventionalReturn}</td>
    //                 <td>${cumulativeSustainableReturn}</td>
    //                 <td>${cumulativePortfolioReturn}</td>
    //             </tr>
    //             <tr>
    //                 <td><b>Average Return Per Period (%)</b></td>
    //                 <td>${avgConventionalReturn}%</td>
    //                 <td>${avgSustainableReturn}%</td>
    //                 <td>${avgPortfolioReturn}%</td>
    //             </tr>
    //             <tr>
    //                 <td><b>Volatility (%)</b></td>
    //                 <td>${stdDevConventional}%</td>
    //                 <td>${stdDevSustainable}%</td>
    //                 <td>${stdDevPortfolio}%</td>
    //             </tr>
    //         </table>
    //     `;
    // }
    function updateDataLabels(chartname) {

        var series1 = chartname.series[0];
        var series2 = chartname.series[1];
        var series3 = chartname.series[2];

            // Disable data labels for all points in each series
        [series1, series2, series3].forEach(series => {
            series.data.forEach(point => point.update({ dataLabels: { enabled: false } }, false));
        });
        chartname.redraw(); // Force Highcharts to apply these updates first

        // Only enable data labels for the last point if it exists
        if (series1.data.length > 0 && series2.data.length > 0 && series3.data.length > 0) {
            var lastPoint1 = series1.data[series1.data.length - 1];
            var lastPoint2 = series2.data[series2.data.length - 1];
            var lastPoint3 = series3.data[series3.data.length - 1];

            // Calculate offsets to prevent overlap
            const offset1 = lastPoint1.plotY < lastPoint2.plotY ? -20 : 20;
            const offset2 = lastPoint1.plotY < lastPoint2.plotY ? 20 : -20;
            const offset3 = lastPoint3.plotY < lastPoint1.plotY && lastPoint3.plotY < lastPoint2.plotY ? 30 : 0;

            lastPoint1.update({ dataLabels: { enabled: true, format: '{y:.2f}%', style: { fontWeight: 'bold' },
                    color: lastPoint1.color, y: offset1,  x: 10, allowOverlap: false } }, false);
            lastPoint2.update({ dataLabels: { enabled: true, format: '{y:.2f}%', style: { fontWeight: 'bold' },
                    color: lastPoint2.color, y: offset2,  x: 10, allowOverlap: false } }, false);
            lastPoint3.update({ dataLabels: { enabled: true, format: '{y:.2f}%', style: { fontWeight: 'bold' },
                    color: lastPoint3.color, y: offset3,  x: 10, allowOverlap: false } }, false);
        }
        chartname.redraw();
    }

    // Load data and initialize chart and table on page load
    document.addEventListener('DOMContentLoaded', function() {
        Papa.parse(csvDataUrl, {
            download: true,
            header: true,
            dynamicTyping: true,
            complete: function(results) {
                window.chartData = results.data;
                initializeCumulativeChart();
                updateDataLabels(cumulativeChart);
            }
        });
    });
})();
