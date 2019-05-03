$(function() {
    // Bar chart
    new Chart(document.getElementById("chartjs-dashboard-bar-devices"), {
        type: "bar",
        data: {
            labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
            datasets: [{
                label: "Mobile",
                backgroundColor: window.theme.primary,
                borderColor: window.theme.primary,
                hoverBackgroundColor: window.theme.primary,
                hoverBorderColor: window.theme.primary,
                data: [54, 67, 41, 55, 62, 45, 55, 73, 60, 76, 48, 79]
            }, {
                label: "Desktop",
                backgroundColor: "#E8EAED",
                borderColor: "#E8EAED",
                hoverBackgroundColor: "#E8EAED",
                hoverBorderColor: "#E8EAED",
                data: [69, 66, 24, 48, 52, 51, 44, 53, 62, 79, 51, 68]
            }]
        },
        options: {
            maintainAspectRatio: false,
            legend: {
                display: false
            },
            scales: {
                yAxes: [{
                    gridLines: {
                        display: false
                    },
                    stacked: false,
                    ticks: {
                        stepSize: 20
                    }
                }],
                xAxes: [{
                    barPercentage: .75,
                    categoryPercentage: .5,
                    stacked: false,
                    gridLines: {
                        color: "transparent"
                    }
                }]
            }
        }
    });
});
$(function() {
    $("#world_map").vectorMap({
        map: "world_mill",
        normalizeFunction: "polynomial",
        hoverOpacity: .7,
        hoverColor: false,
        regionStyle: {
            initial: {
                fill: "#e3eaef"
            }
        },
        markerStyle: {
            initial: {
                "r": 9,
                "fill": window.theme.primary,
                "fill-opacity": .95,
                "stroke": "#fff",
                "stroke-width": 7,
                "stroke-opacity": .4
            },
            hover: {
                "stroke": "#fff",
                "fill-opacity": 1,
                "stroke-width": 1.5
            }
        },
        backgroundColor: "transparent",
        zoomOnScroll: false,
        markers: [{
            latLng: [31.230391, 121.473701],
            name: "Shanghai"
        },
            {
                latLng: [39.904202, 116.407394],
                name: "Beijing"
            },
            {
                latLng: [28.704060, 77.102493],
                name: "Delhi"
            },
            {
                latLng: [6.524379, 3.379206],
                name: "Lagos"
            },
            {
                latLng: [39.343357, 117.361649],
                name: "Tianjin"
            },
            {
                latLng: [24.860735, 67.001137],
                name: "Karachi"
            },
            {
                latLng: [41.008240, 28.978359],
                name: "Istanbul"
            },
            {
                latLng: [35.689487, 139.691711],
                name: "Tokyo"
            },
            {
                latLng: [23.129110, 113.264381],
                name: "Guangzhou"
            },
            {
                latLng: [19.075983, 72.877655],
                name: "Mumbai"
            },
            {
                latLng: [40.7127837, -74.0059413],
                name: "New York"
            },
            {
                latLng: [34.052235, -118.243683],
                name: "Los Angeles"
            },
            {
                latLng: [41.878113, -87.629799],
                name: "Chicago"
            },
            {
                latLng: [29.760427, -95.369804],
                name: "Houston"
            },
            {
                latLng: [33.448376, -112.074036],
                name: "Phoenix"
            },
            {
                latLng: [51.507351, -0.127758],
                name: "London"
            },
            {
                latLng: [48.856613, 2.352222],
                name: "Paris"
            },
            {
                latLng: [55.755825, 37.617298],
                name: "Moscow"
            },
            {
                latLng: [40.416775, -3.703790],
                name: "Madrid"
            }
        ]
    });
    setTimeout(function() {
        $(window).trigger('resize');
    }, 50)
});
$(function() {
    // Pie chart
    new Chart(document.getElementById("chartjs-dashboard-pie"), {
        type: "pie",
        data: {
            labels: ["Direct", "Affiliate", "E-mail", "Other"],
            datasets: [{
                data: [2602, 1253, 541, 1465],
                backgroundColor: [
                    window.theme.primary,
                    window.theme.warning,
                    window.theme.danger,
                    "#E8EAED"
                ],
                borderColor: "transparent"
            }]
        },
        options: {
            responsive: !window.MSInputMethodContext,
            maintainAspectRatio: false,
            legend: {
                display: false
            }
        }
    });
});
$(function() {
    // Radar chart
    new Chart(document.getElementById("chartjs-dashboard-radar"), {
        type: "radar",
        data: {
            labels: ["Technology", "Sports", "Media", "Gaming", "Arts"],
            datasets: [{
                label: "Interests",
                backgroundColor: "rgba(0, 123, 255, 0.2)",
                borderColor: "#2979ff",
                pointBackgroundColor: "#2979ff",
                pointBorderColor: "#fff",
                pointHoverBackgroundColor: "#fff",
                pointHoverBorderColor: "#2979ff",
                data: [70, 53, 82, 60, 33]
            }]
        },
        options: {
            maintainAspectRatio: false,
            legend: {
                display: false
            }
        }
    });
});
$(function() {
    $("#datatables-dashboard-traffic").DataTable({
        pageLength: 8,
        lengthChange: false,
        bFilter: false,
        autoWidth: false,
        order: [
            [1, "desc"]
        ]
    });
});