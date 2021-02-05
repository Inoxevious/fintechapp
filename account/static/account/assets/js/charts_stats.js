$(document).ready(function () {
    let url = $("#c3chart").attr("url");
    console.log("URL" + url)
    $.ajax({
        // type: "POST",
        url: url,

        // data: "{}",
        // contentType: "application/json",
        // dataType: "json",
        // async: "true",
        // cache: "false",
        success: function (result) {
            console.log("Acc data" + result)
            OnSuccess(result);
        },
        error: function (xhr, status, error) {
            alert(error);
        }
    });

    function OnSuccess(data) {
        var jsonData = data;
        console.log("Acc data" + JSON.stringify(jsonData))
        chart_data = JSON.stringify(jsonData.data)
        chart_labels = JSON.stringify(jsonData.labels)
        console.log(chart_labels, chart_data)
        var data = {};
        var labels = [];
        // $.each(jsonData['data'], function (a, b) {
        //     console.log("label: " + a + ' dta: ' + b)
        //     labels.push(a);
        //     data[a] = b;

        // })
        // jsonData.forEach(function (data) {
        //     projects.push(data.labels);
        //     data[e.job] = data.labesl;
        // })

        chart = c3.generate({
            bindto: '#chart-var-project',
            // colums: jsonData.data,
            data: {
                colums: [jsonData.data],
            },
            donut: {
                title: "Projects",
                width: 60,
                label: {
                    format: function (value, ratio, id) {
                        return value;
                    }
                }
            },
            color: {
                pattern: ["#F06292", "#8892d6", "#78c350", "#45bbe0", "#ff9800", "#f7531f"]
            }
        });
    }
});

