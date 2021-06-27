function swal_fire(icon, title, text) {
    Swal.fire({
        "icon": icon,
        "title": title,
        "text": text,
    });
}

function error_swal(error_message) {
    swal_fire("error", "Error", error_message);
}

function success_swal(success_message) {
    swal_fire("success", "Success", success_message);
}

function please_wait_swal(please_wait_message) {
    swal_fire("info", "Please wait", please_wait_message);
}

function ajax_post(url, data, swal_close=false) {
    $.ajax({
        url: url,
        type: "post",
        data: data,
        success: function(result) {
            if(swal_close)
                window.swal.close();

            swal_fire(result.icon, result.title, result.text);
        }
    });
}