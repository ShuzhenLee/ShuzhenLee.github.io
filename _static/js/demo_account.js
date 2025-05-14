document.addEventListener('DOMContentLoaded', (function() {
    var newIndex = 0;
    var flexChart, fixChart;
    var flexCumuChart, fixCumuChart;
    var minPeriods, maxPeriods;

    // Function to get the current page based on the element's ID
    function getCurrentPage() {
        const url = window.location.pathname;
        if (url.includes("Decision_P1")) {
            return 'P1';
        } else if (url.includes("Decision_P2")) {
            return 'P2';
        } else if (url.includes("Decision_P3")) {
            return 'P3';
        } else if (url.includes("Decision_P4")) {
            return 'P4';
        } else if (url.includes("Decision_P5")) {
            return 'P5';
        } else {
            return null;
        }
    }

    const currentPage = getCurrentPage();
    if (currentPage === 'P1') {
        maxPeriods = 9;
        minPeriods = 1;
        // decision = parseFloat(document.getElementById('data-container').dataset.decision0);
    } else if (currentPage === 'P2') {
        maxPeriods = 18;
        minPeriods = 10;
        // decision = parseFloat(document.getElementById('data-container').dataset.decision1);
    } else if (currentPage === 'P3') {
        maxPeriods = 27;
        minPeriods = 19;
        // decision = parseFloat(document.getElementById('data-container').dataset.decision2);
    } else if (currentPage === 'P4') {
        maxPeriods = 36;
        minPeriods = 28;
        // decision = parseFloat(document.getElementById('data-container').dataset.decision3);
    } else if (currentPage === 'P5') {
        maxPeriods = 45;
        minPeriods = 37;
        // decision = parseFloat(document.getElementById('data-container').dataset.decision4);
    } else {
        return null;
    }

    // Function to initialize the new chart with Period 1 data
    function initializeNewChart() {
        newIndex = minPeriods - 1; // Start index from the minimum period
        flexChart = Highcharts.chart('newContainer', {
            credits: { enabled: false },
            exporting: { enabled: false },
            title: { text: 'Return by Period', align: 'left' },
            xAxis: {
                title: { text: 'Period' },
                type: 'linear',
                min: 0, // Start from Period 1
                max: 45,
                tickLength: 0,
                minorTickLength: 0,
                tickInterval: 1,
                labels: {
                    formatter: function() { return (this.value); },
                    rotation: 0,
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
                { name: 'Sustainable Fund', data: [], color: '#008000FF'},
                { name: 'Conventional Fund', data: [], color: '#808080' },
                { name: 'Initial Portfolio', data: [], color: '#0000FF' },

            ]
        });

        // Load previous data for the page
        for (let i = 0; i < minPeriods - 1; i++) {
            flexChart.series[0].addPoint({ x: i, y: chartData.susData[i] }, false, false);
            flexChart.series[1].addPoint({ x: i, y: chartData.conData[i] }, false, false);
            flexChart.series[2].addPoint({ x: i, y: chartData.fixportData[i] }, false, false);
        }
        flexChart.redraw();
    }

    function initializeFixNewChart() {
        fixChart = minPeriods - 1; // Start index from the minimum period
        fixChart = Highcharts.chart('fix_newContainer', {
            credits: { enabled: false },
            exporting: { enabled: false },
            title: { text: 'Return by Period', align: 'left' },
            xAxis: {
                title: { text: 'Period' },
                type: 'linear',
                min: 0, // Start from Period 1
                max: 45,
                tickLength: 0,
                minorTickLength: 0,
                tickInterval: 1,
                labels: {
                    formatter: function() { return (this.value); },
                    rotation: 0,
                    align: 'center',
                    step: 1
                }
            },
            yAxis: [{ title: { text: 'Return (%)' }, labels: { format: '{value:.2f}%' },
                  }],
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
                    label: { enabled: false },
                    dataLabels: { enabled: false, allowOverlap: false }
                }
            },
            series: [
                { name: 'Initial Portfolio', data: [], color: '#0000FF'  },
                { name: 'Adjusted Portfolio', data: [], color: '#007afe' }

            ]
        });

        // Load previous data for the page
        for (let i = 0; i < minPeriods - 1; i++) {
            fixChart.series[0].addPoint({ x: i, y: chartData.fixportData[i] }, false, false);
            fixChart.series[1].addPoint({ x: i, y: chartData.portData[i] }, false, false);
        }
        fixChart.redraw();
    }

    function updateUpDownTable(index) {
        // Get the returns for the current index
        const sustainableReturn = chartData.susData[index] + '%';
        const conventionalReturn = chartData.conData[index]+ '%';

        // Calculate "Your Portfolio" returns
        const portfolioReturn = (Math.round(chartData.portData[index] * 100) / 100).toFixed(2) + '%';
        const fixportfolioReturn = (Math.round(chartData.fixportData[index] * 100) / 100).toFixed(2) + '%';

        // Define the SVG icons for up and down indicators
        // const upTriangle = '<svg width="10" height="10" viewBox="0 0 24 24" fill="green" xmlns="http://www.w3.org/2000/svg"><path d="M12 2L22 22H2L12 2Z"/></svg>';
        // const downTriangle = '<svg width="10" height="10" viewBox="0 0 24 24" fill="red" xmlns="http://www.w3.org/2000/svg"><path d="M12 22L2 2H22L12 22Z"/></svg>';
        // const upTriangle = '<svg width="10" height="10" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 2L22 22H2L12 2Z"/></svg>';
        // const downTriangle = '<svg width="10" height="10" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 22L2 2H22L12 22Z"/></svg>';

        // Determine which triangle to display based on return values
        // const sustainableTriangle = chartData.susData[index] < 0 ? downTriangle : upTriangle;
        // const conventionalTriangle = chartData.conData[index] < 0 ? downTriangle : upTriangle;
        // const portfolioTriangle = chartData.portData[index] < 0 ? downTriangle : upTriangle;
        // const fixportfolioTriangle = chartData.fixportData[index] < 0 ? downTriangle : upTriangle;

        // Ensure the table container is visible
        document.getElementById('UpDownTable').style.display = 'block';

        // Update the table content dynamically
        document.getElementById('UpDownTable').innerHTML = `
        <table style="width: 100%; border-collapse: collapse; text-align: center; font-size: 14px;">
            <tr style="background-color: #f9f9f9;">
                <th style="padding: 5px; border: 1px solid #cecbcb; font-weight: bold;">&nbsp;</th>
                <th style="padding: 5px; border: 1px solid #cecbcb; font-weight: bold;">Conventional Fund</th>
                <th style="padding: 5px; border: 1px solid #cecbcb; font-weight: bold;">Sustainable Fund</th>
                <th style="padding: 5px; border: 1px solid #cecbcb; font-weight: bold;">Initial Portfolio</th>
            </tr>
            <tr style="background-color: #ffffff;">
                <td style="padding: 5px; border: 1px solid #cecbcb;">Period ${index} Returns</td>
                <td style="padding: 5px; border: 1px solid #cecbcb;};">
                    ${conventionalReturn}
                </td>
                <td style="padding: 5px; border: 1px solid #cecbcb;};">
                    ${sustainableReturn}
                </td>
                <td style="padding: 5px; border: 1px solid #cecbcb; };">
                    ${fixportfolioReturn}
                </td>

            </tr>
        </table>
        `;

        document.getElementById('fix_UpDownTable').style.display = 'block';

        // Update the table content dynamically
        document.getElementById('fix_UpDownTable').innerHTML = `
        <table style="width: 100%; border-collapse: collapse; text-align: center; font-size: 14px;">
            <tr style="background-color: #f9f9f9;">
                <th style="padding: 5px; border: 1px solid #cecbcb; font-weight: bold;">&nbsp;</th>
                <th style="padding: 5px; border: 1px solid #cecbcb; font-weight: bold;">Initial Portfolio</th>
                <th style="padding: 5px; border: 1px solid #cecbcb; font-weight: bold;">Adjusted Portfolio</th>
            </tr>
            <tr style="background-color: #ffffff;">
                <td style="padding: 5px; border: 1px solid #cecbcb;">Period ${index} Returns</td>

                <td style="padding: 5px; border: 1px solid #cecbcb; };">
                    ${fixportfolioReturn}
                </td>
                <td style="padding: 5px; border: 1px solid #cecbcb; };">
                    ${portfolioReturn}
                </td>
            </tr>
        </table>
        `;
    }
    // Function to add data for the current period and update data labels
    function addPeriodData() {
        if (newIndex < chartData.susData.length && newIndex <= maxPeriods) {
            flexChart.series[0].addPoint({ x: newIndex, y: chartData.susData[newIndex] }, false, false);
            flexChart.series[1].addPoint({ x: newIndex, y: chartData.conData[newIndex] }, false, false);
            flexChart.series[2].addPoint({ x: newIndex, y: chartData.portData[newIndex] }, false, false);
            // flexChart.series[3].addPoint({ x: newIndex, y: chartData.fixportData[newIndex] }, false, false);

            // fixChart.series[0].addPoint({ x: newIndex, y: chartData.susData[newIndex] }, false, false);
            // fixChart.series[1].addPoint({ x: newIndex, y: chartData.conData[newIndex] }, false, false);
            fixChart.series[0].addPoint({ x: newIndex, y: chartData.portData[newIndex] }, false, false);
            fixChart.series[1].addPoint({ x: newIndex, y: chartData.fixportData[newIndex] }, false, false);

            // Update the table for the current period
            updateUpDownTable(newIndex);
            updateDataLabels(flexChart);
            updateFixDataLabels(fixChart);
            newIndex++;
            flexChart.redraw();
            fixChart.redraw();
        }

        // add a stop line
        if (newIndex === maxPeriods+1) {
            flexChart.xAxis[0].addPlotLine({
                color: 'lightgray',
                width: 0.8,
                value: maxPeriods,
                zIndex: 5
            });
            fixChart.xAxis[0].addPlotLine({
                color: 'lightgray',
                width: 0.8,
                value: maxPeriods,
                zIndex: 5
            });
        }
        if (newIndex === maxPeriods+1) {
            allPeriodsRevealed = true;
            document.getElementById('next-button').disabled = false; // Enable the Next Page button
            document.getElementById('average-return').style.display = 'block'; // Enable the Next Page button
            document.getElementById('next-button').style.backgroundColor = ''; // Optional: Reset background
            const event = new Event('allPeriodsRevealed');
            window.dispatchEvent(event);
        }
    }
    initializeNewChart();
    initializeFixNewChart();

    function initializeCumulativeChart() {
        cumu_1_Chart = Highcharts.chart('cumu_1_Container', {
            credits: { enabled: false },
            exporting: { enabled: false },
            title: { text: 'Cumulative Return (Up to the current period)', align: 'left' },
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
                    label: { enabled: false },
                    dataLabels: { enabled: false, allowOverlap: false }
                }
            },
            series: [{
                name: 'Sustainable Fund',
                data: window.CumulativeDataEveryPeriod.TRSusData,
                color: '#008000FF'
            }, {
                name: 'Conventional Fund',
                data: window.CumulativeDataEveryPeriod.TRConData,
                color: '#808080'
            }, {
                name: 'Initial Portfolio',
                data: window.CumulativeDataEveryPeriod.TRFixPortData,
                color: '#0000FF'
            }, {
                name: 'Adjusted Portfolio',
                data: window.CumulativeDataEveryPeriod.TRPortData,
                color: '#007afe'
            }
            ]
        });
        // add a stop line
        cumu_1_Chart.xAxis[0].addPlotLine({
            color: 'lightgray',
            width: 0.8,
            value: maxPeriods,
            zIndex: 5
        });
        cumu_1_Chart.redraw();
    }


    // Function to render the summary table
    function renderSummaryTable() {
        const summaryData = window.summaryData[0];
        const isPageP5 = currentPage === 'P5';
        // Generate the table rows dynamically
        let tableHTML = `
            <table style="width: 100%; border-collapse: collapse; text-align: center; font-size: 12px; white-space: nowrap">
                <caption style="font-family: Arial; font-size: 18px; color: rgb(51, 51, 51); font-weight: bold; fill: rgb(51, 51, 51); text-align=left">
                    Summary of Fund Performance
                </caption>
                <tr>
                    <th></th>
                    <th>Conventional Fund</th>
                    <th>Sustainable Fund</th>
                    <th>Initial Portfolio</th>
                    <th>Adjusted Portfolio</th>
                </tr>
                <tr>
                    <td>Cumulative Return</td>
                    <td>${summaryData.cumulative.con}%</td>
                    <td>${summaryData.cumulative.sus}%</td>
                    <td>${summaryData.cumulative.fix_port}%</td>
                    <td>${summaryData.cumulative.port}%</td>
                </tr>
                <tr>
                    <td>Average Return Per Period</td>
                    <td>${summaryData.averageReturns.con}%</td>
                    <td>${summaryData.averageReturns.sus}%</td>
                    <td>${summaryData.averageReturns.fix_port}%</td>
                    <td>${summaryData.averageReturns.port}%</td>
                </tr>
                <tr>
                    <td>Volatility</td>
                    <td>${summaryData.volatilities.con}%</td>
                    <td>${summaryData.volatilities.sus}%</td>
                    <td>${summaryData.volatilities.fix_port}%</td>
                    <td>${summaryData.volatilities.port}%</td>
                </tr>
                <tr>
                    <td>Sharpe Ratio</td>
                    <td>${summaryData.sharpeRatios.con}</td>
                    <td>${summaryData.sharpeRatios.sus}</td>
                    <td>${summaryData.sharpeRatios.fix_port}</td>
                    <td>${summaryData.sharpeRatios.port}</td>
                </tr>
        `;
        // Close the table
        tableHTML += `
            </table>
        `;

        document.getElementById('summaryTableContainer').innerHTML = tableHTML;
    }


    function updateDataLabels(chartname) {

        var series1 = chartname.series[0];
        var series2 = chartname.series[1];
        var series3 = chartname.series[2];
        // var series4 = chartname.series[3];

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
            // var lastPoint4 = series4.data[series4.data.length - 1];

            // Calculate offsets to prevent overlap
            const offset1 = lastPoint1.plotY < lastPoint2.plotY ? -20 : 20;
            const offset2 = lastPoint1.plotY < lastPoint2.plotY ? 20 : -20;
            const offset3 = lastPoint3.plotY < lastPoint1.plotY && lastPoint3.plotY < lastPoint2.plotY ? 30 : 0;
            // const offset4 = lastPoint4.plotY < lastPoint1.plotY && lastPoint4.plotY < lastPoint2.plotY ? 30 : 0;

            lastPoint1.update({ dataLabels: { enabled: true, format: '{y:.2f}%', style: { fontWeight: 'bold' },
                    color: lastPoint1.color, y: offset1, x: 10, allowOverlap: false } }, false);
            lastPoint2.update({ dataLabels: { enabled: true, format: '{y:.2f}%', style: { fontWeight: 'bold' },
                    color: lastPoint2.color, y: offset2, x: 10, allowOverlap: false } }, false);
            lastPoint3.update({ dataLabels: { enabled: true, format: '{y:.2f}%', style: { fontWeight: 'bold' },
                    color: lastPoint3.color, y: offset3, x: 10, allowOverlap: false } }, false);
        //     lastPoint4.update({ dataLabels: { enabled: true, format: '{y:.2f}%', style: { fontWeight: 'bold' },
        //             color: lastPoint4.color, y: offset4, allowOverlap: false } }, false);
        }
        chartname.redraw();
    }

    function updateFixDataLabels(chartname) {
        var series1 = chartname.series[0]; // Initial Portfolio
        var series2 = chartname.series[1]; // Adjusted Portfolio

        // Disable data labels for all points in each series
        [series1, series2].forEach(series => {
            series.data.forEach(point => point.update({ dataLabels: { enabled: false } }, false));
        });
        chartname.redraw(); // Apply updates first

        // Only enable data labels for the last point if it exists
        if (series1.data.length > 0 && series2.data.length > 0) {
            var lastPoint1 = series1.data[series1.data.length - 1];
            var lastPoint2 = series2.data[series2.data.length - 1];

            // Ensure the higher value is placed above the lower one
            let higherPoint = lastPoint1.y > lastPoint2.y ? lastPoint1 : lastPoint2;
            let lowerPoint = lastPoint1.y > lastPoint2.y ? lastPoint2 : lastPoint1;

            // Dynamic label positioning to prevent overlap
            higherPoint.update({
                dataLabels: {
                    enabled: true,
                    format: '{y:.2f}%',
                    style: { fontWeight: 'bold' },
                    color: higherPoint.color,
                    y: -20, // Move higher value label up
                    x: 10,
                    allowOverlap: false
                }
            }, false);

            lowerPoint.update({
                dataLabels: {
                    enabled: true,
                    format: '{y:.2f}%',
                    style: { fontWeight: 'bold' },
                    color: lowerPoint.color,
                    y: 20, // Move lower value label down
                    x: 10,
                    allowOverlap: false
                }
            }, false);
        }

        chartname.redraw();
    }
    function updateFourLineDataLabels(chartname) {
        var series = chartname.series; // All 4 series

        // Disable data labels for all points in each series
        series.forEach(serie => {
            serie.data.forEach(point => point.update({ dataLabels: { enabled: false } }, false));
        });
        chartname.redraw(); // Apply updates first

        // Get the last data points of all 4 series
        let lastPoints = series.map(serie => serie.data[serie.data.length - 1]);

        // Sort points from highest to lowest based on y-value
        lastPoints.sort((a, b) => b.y - a.y);

        let labelOffsets = [-20, -10, 10, 20]; // Dynamic offsets to prevent overlap

        // Apply labels to each last point dynamically
        lastPoints.forEach((point, index) => {
            point.update({
                dataLabels: {
                    enabled: true,
                    format: '{y:.2f}%',
                    color: point.color,
                    y: labelOffsets[index], // Assign dynamic spacing to prevent overlap
                    x: 10, // Moves label to the right of the point
                    align: 'left',
                    allowOverlap: false
                }
            }, false);
        });

        chartname.redraw();
    }


    const intervalDuration = 500; // Interval duration in milliseconds (e.g., 2000ms = 2 seconds)
    const periodInterval = setInterval(addPeriodData, intervalDuration);


    if (currentPage !== 'P5') {
        document.getElementById('next-button').addEventListener('click', function (event) {
            event.preventDefault();
            initializeCumulativeChart();
            // updateDataLabels(cumu_1_Chart);
            updateFourLineDataLabels(cumu_1_Chart);

        });
    }
    if (currentPage === 'P5') {
        document.getElementById('next-button').addEventListener('click', function (event) {
            event.preventDefault();
            initializeCumulativeChart();
            // updateDataLabels(cumu_1_Chart);
            updateFourLineDataLabels(cumu_1_Chart);
            renderSummaryTable();

        });
    }

}),);



