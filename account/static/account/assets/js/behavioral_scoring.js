// variable that keeps all the filter information

var send_data = {};

$(document).ready(function () {
    // reset all parameters on page load

    resetFilters();
    // bring all the data without any filters

    getAPIData();
    // get all business loans from database via AJAX call into loan select options

    getBusiness();
    // get all mortage loans from database via AJAX call into mortage select options

    getmortage();

    // on selecting the business option

    $('#business').on('change', function () {
        // since school and funeral is dependent 

        // on business select, emty all the options from select input

        $("#school").val("all");
        $("#funeral").val("all");
        send_data['school'] = '';
        send_data['funeral'] = '';

        // update the selected business

        if (this.value == "all")
            send_data['business'] = "";
        else
            send_data['business'] = this.value;

        //get school of selected business

        getschool(this.value);
        // get api data of updated filters

        getAPIData();
    });

    // on filtering the mortage input

    $('#mortage').on('change', function () {
        // get the api data of updated mortage

        if (this.value == "all")
            send_data['mortage'] = "";
        else
            send_data['mortage'] = this.value;
        getAPIData();
    });

    // on filtering the school input

    $('#school').on('change', function () {
        // clear the funeral input 

        // since it is dependent on school input

        send_data['funeral'] = "";
        $('#funeral').val("all");
        if (this.value == "all")
            send_data['school'] = "";
        else
            send_data['school'] = this.value;
        getfuneral(this.value);
        getAPIData();
    });

    // on filtering the funeral input

    $('#funeral').on('change', function () {
        if (this.value == "all")
            send_data['funeral'] = "";
        else
            send_data['funeral'] = this.value;
        getAPIData();
    });

    // sort the data according to price/points

    $('#sort_by').on('change', function () {
        send_data['sort_by'] = this.value;
        getAPIData();
    });

    // display the results after reseting the filters

    $("#display_all").click(function () {
        resetFilters();
        getAPIData();
    })
})


/**
    Function that resets all the filters   
**/
function resetFilters() {
    $("#business").val("all");
    $("#school").val("all");
    $("#funeral").val("all");
    $("#mortage").val("all");
    $("#sort_by").val("none");

    //clearing up the school and funeral select box

    getschool("all");
    getfuneral("all");

    send_data['business'] = '';
    send_data['school'] = '';
    send_data['funeral'] = '';
    send_data['mortage'] = '';
    send_data["sort_by"] = '',
        send_data['format'] = 'json';
}

/**.
    Utility function to showcase the api data 
    we got from backend to the table content

**/




function putTableData(result) {
    // creating table row for each result and
    // pushing to the html cntent of table body of listing table
    let row;
    if (result["results"].length > 0) {
        $("#no_results").hide();
        $("#behavioral_list_data").show();
        $("#behavioral_listing").html("");
        // populate application scoring_listing data

        // populate behaviora_listing data
        $.each(result["results"], function (a, b) {
            console.log("behavioral_classifier_data " + JSON.stringify(b))
            console.log("probability " + b.income_probability)
            var client_profile = b.client_id
            var officer_profile = "{% url 'companies:profile' " + b.officer_id + " %}"
            var report = "{% url 'companies:profile' " + b.loan_id + " %}"
            var csv = "{% url 'companies:profile' " + b.loan_id + " %}"
            client_url_id = 'client'
            officer_url_id = 'officer_' + b.officer_id
            report_url_id = 'report_' + b.loan_id
            csv_url_id = 'csv_' + b.loan_id

            console.log("URLSSSSS" + client_profile)
            row = `<tr> <td><a href="/companies/client_profile/?client_id=${b.client_id}">${b.loan_id}</a></td><td><a href="/companies/client_profile/?client_id=${b.client_id}" id="${client_url_id}" >${b.client_id}</a></td><td>${b.loan_amount}</td><td>${b.loan_amount}</td><td>${b.loan_amount}</td><td style='background-color:${b.income_color}'>${b.income_probability}</td><td style='background-color:${b.income_color}'>${b.income_text}</td><td>${b.behavioral_time_to_default}</td><td>${b.behavioral_contact_channel}</td><td>${b.behavioral_contact_schedule}</td><td>${b.behavioral_message}</td>${`<td class='text-center'>
                    <ul class='icons-list'>
                        <li class='dropdown'>
                            <a class='dropdown-toggle' data-toggle='dropdown'>
                                <i class='icon-menu9'></i>
                            </a>

                            <ul class='dropdown-menu dropdown-menu-right'>
                            <li><a href="/companies/client_profile/?=${b.client_id}" ><i class='icon-person'></i>
                            View
                            Client</a></li>
                    <li><a href="/companies/application_report/?=${b.loan_id}"  ><i
                                class='icon-book'></i> View
                            Report</a></li>
                    <li><a href="/companies/application_report_export_csv/?=${b.loan_id}"><i
                                class='icon-file-excel'></i> Export to .csv</a></li>
                            </ul>
                        </li>
                    </ul>
                </td></tr>`}`
            $("#behavioral_listing").append(row);


        });
    }
    else {
        // if no result found for the given filter, then display no result
        console.log("no data behavioral")
        $("#no_results h5").html("No behavioral results found");
        $("#behavioral_listing").hide();
        $("#no_results").show();
    }


    // setting previous and next page url for the given result

    let prev_url = result["previous"];
    let next_url = result["next"];
    // disabling-enabling button depending on existence of next/prev page. 

    if (prev_url === null) {
        $("#previous").addClass("disabled");
        $("#previous").prop('disabled', true);
    } else {
        $("#previous").removeClass("disabled");
        $("#previous").prop('disabled', false);
    }
    if (next_url === null) {
        $("#next").addClass("disabled");
        $("#next").prop('disabled', true);
    } else {
        $("#next").removeClass("disabled");
        $("#next").prop('disabled', false);
    }
    // setting the url

    $("#previous").attr("url", result["previous"]);
    $("#next").attr("url", result["next"]);
    // displaying result count

    $("#result-count span").html(result["count"]);
}

function clientUrl(data) {
    console.log("dound dta" + data)
    id = "#" + data
    console.log(id)
    let url = "/companies/profile/" + data
    // let url = $(id).attr("url")
    // let url = '{% url companies:behavioral_scoring_view %}'
    console.log("bhv url" + url)
    $.ajax({
        method: 'GET',
        url: url,
        data: data,
        success: function (result) {
            console.log("API RES" + JSON.stringify(result))
            // putTableData(result);]]]
            window.location.href = ""
        },
        error: function (response) {
            console.log('no client data')
        }
    });
}

function getAPIData() {
    let url = $('#behavioral_list_data').attr("url")
    // let url = '{% url companies:behavioral_scoring_view %}'
    console.log("bhv url" + url)
    $.ajax({
        method: 'GET',
        url: url,
        data: send_data,
        beforeSend: function () {
            $("#no_results").html("Loading data...");
        },
        success: function (result) {
            console.log("API RES" + JSON.stringify(result))
            putTableData(result);
        },
        error: function (response) {
            $("#no_results").html("Something went wrong");
            $("#behavioral_list_data").hide();
        }
    });
}

$("#next").click(function () {
    // load the next page data and 

    // put the result to the table body

    // by making ajax call to next available url

    let url = $(this).attr("url");
    if (!url)
        $(this).prop('all', true);

    $(this).prop('all', false);
    $.ajax({
        method: 'GET',
        url: url,
        success: function (result) {
            putTableData(result);
        },
        error: function (response) {
            console.log(response)
        }
    });
})

$("#previous").click(function () {
    // load the previous page data and 

    // put the result to the table body 

    // by making ajax call to previous available url

    let url = $(this).attr("url");
    if (!url)
        $(this).prop('all', true);

    $(this).prop('all', false);
    $.ajax({
        method: 'GET',
        url: url,
        success: function (result) {
            putTableData(result);
        },
        error: function (response) {
            console.log(response)
        }
    });
})

function getBusiness() {
    // fill the options of businesses by making ajax call

    // obtain the url from the businesses select input attribute

    let url = $("#business").attr("url");

    // makes request to getBusiness(request) method in views

    $.ajax({
        method: 'GET',
        url: url,
        data: {},
        success: function (result) {

            businesses_option = "<option value='all' selected>All loan officers</option>";
            $.each(result["businesses"], function (a, b) {
                businesses_option += "<option>" + b + "</option>"
            });
            $("#business").html(businesses_option)
        },
        error: function (response) {
            console.log(response)
        }
    });
}

function getmortage() {
    // fill the options of varities by making ajax call

    // obtain the url from the mortage select input attribute

    let url = $("#mortage").attr("url");
    // makes request to getmortage(request) method in views

    $.ajax({
        method: 'GET',
        url: url,
        data: {},
        success: function (result) {
            mortage_options = "<option value='all' selected>Clients</option>";
            $.each(result["mortage"], function (a, b) {
                mortage_options += "<option>" + b + "</option>"
            });
            $("#mortage").html(mortage_options)
        },
        error: function (response) {
            console.log(response)
        }
    });
}

function getschool(business) {
    // fill the options of schools by making ajax call

    // obtain the url from the schools select input attribute

    let url = $("#school").attr("url");
    // makes request to getschool(request) method in views

    let school_option = "<option value='all' selected>All schools</option>";
    $.ajax({
        method: 'GET',
        url: url,
        data: {
            "business": business
        },
        success: function (result) {
            $.each(result["school"], function (a, b) {
                school_option += "<option>" + b + "</option>"
            });
            $("#school").html(school_option)
        },
        error: function (response) {
            console.log(response)
        }
    });
}

function getfuneral(school) {
    // fill the options of funeral by making ajax call

    // obtain the url from the funeral select input attribute

    let url = $("#funeral").attr("url");
    // makes request to getfuneral(request) method in views

    let funeral_option = "<option value='all' selected>All risk levels</option>";
    $.ajax({
        method: 'GET',
        url: url,
        data: {
            "school": school
        },
        success: function (response) {
            $.each(response["funeral"], function (a, b) {
                funeral_option += "<option>" + b + "</option>"
            });
            $("#funeral").html(funeral_option);
        },
        error: function (response) {
            console.log(response)
        }
    });
}