
function downloadProject() {
    $.get('/api/project',
    {
        api: $('#apis').children('option:selected').val(),
        client: $('#clients').children('option:selected').val(),
        server: $('#servers').children('option:selected').val(),
        platform: $('#platforms').children('option:selected').val()
    },
    function(data){
        let base64_string = data.data;

        const linkSource = `data:application/zip;base64,${base64_string}`;
        const downloadLink = document.createElement('a');
        document.body.appendChild(downloadLink);
    
        downloadLink.href = linkSource;
        downloadLink.target = '_self';
        downloadLink.download = `${data.name}.zip`;
        downloadLink.click();
    },
    'json')
}

function getData(){
    $.get('/api/data', function(data){
        data.apis.forEach(x=>{$('#apis').append(`<option value="${x}">${x}</option>`) });
        data.clients.forEach(x=>{$('#clients').append(`<option value="${x}">${x}</option>`) });
        data.servers.forEach(x=>{$('#servers').append(`<option value="${x}">${x}</option>`) });
        data.platforms.forEach(x=>{$('#platforms').append(`<option value="${x}">${x}</option>`) });
        data.databases.forEach(x=>{$('#databases').append(`<option value="${x}">${x}</option>`) });
    });
}

$(document).ready(getData);