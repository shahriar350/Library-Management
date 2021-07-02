feather.replace();

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// function updateOptions(options) {
//     const update = {...options};
//     update.headers = {
//         ...update.headers,
//         "X-CSRFToken": getCookie("csrftoken"),
//         "X-Requested-With": "XMLHttpRequest",
//         "Accept": "application/json",
//         "Content-Type": "application/json",
//     };
//     return update;
// }
//
// export default function fetcher(url, options) {
//     return fetch(url, updateOptions(options));
// }


function capfirst(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}