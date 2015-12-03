// Validating Empty Field first and then start capture
function startcapture() 
{
    if (document.getElementById('wlname').value == "" ||
        document.getElementById('arrayname').value == ""||
        document.getElementById('ipaddr1').value == "" ||
        document.getElementById('ipaddr2').value == "") {
        alert("Fill All Fields !");
    } 
    else {
        $('#capture_popup').fadeOut("slow");
        var capture_parms = get_formparms("newwl");
        wload_process(capture_parms, "capture");
        /*
        $.getJSON('/workloads/capture?'+ serialize(capture_parms), function(data){
            $('#capture_popup').fadeOut("slow");
            $('#console').html(data);
            getwloads(true);
        });
        */
    }
}   

function startupload() 
{
    if (document.getElementById('uploadwlname').value == "" ||
        document.getElementById('arrname').value == "") {
        alert("Fill All Fields !");
    } 
    else {        
          doUpload();          
    }
}

function urlize(lpath, text, newwin)
{
    if (typeof text == "undefined")
        text = lpath;
    if (typeof newwin == "undefined")
        newwin = true
    if (newwin == true)
        newwin = "target=\"_blank\"";
    return '<a href="/workloads/getgraph/' + lpath + '" ' + newwin + '>' + text + '</a>'
}

function settext()
{
   var text = $('#ipaddr1').val();
   $('#ipaddr2').val(text);  
}

function getbooks(hglass)
{
    console.log(hglass);
    if (hglass == true)
        $(".hourglass").show();
    var $select = $('#booklist');
    var pattern=document.getElementById('book_filter').value;
    
    $.getJSON('/books/list?pattern='+pattern, function(data){
            // alert("Server response json:"+data);
               
        $select.append('<ul onclick="getjsonname(event);"> table class="booklist" id="wltable">'+
                        '</table>');
        var table= $select.children();
        table.empty();
        table.append('<tr>'+
                '<th>Select</th>'+
                '<th>Workload Path</th>'+
                '<th>Status</th>'+
                '<th>Controls</th>'+
                '</tr>');
        $.each(data, function(key, winfo) {
            //alert("name:" +winfo.name+ ":" + "running:" +winfo.running);
            var size = 0
            var total_size = 0
            $.each(winfo.dumpsizes, function(key,val){
                total_size += val;
            });
            var isparsed = (winfo['status'].length > 0);
            var wlinfo = '<tr>'+
            '<td>' +'<input type="checkbox" value=\"' + 
                winfo["name"] + '\"/>'+ '</td>'+
            '<td>' + 
            (isparsed 
                ?  urlize(winfo["name"] + "/allgraphs.html", winfo["name"]) 
                : winfo["name"])
                + '</td>'+
            '<td>' + winfo["status"] + '</td>'+
            '<td>'+'<button onclick="docmd(\'' +winfo["name"]+ '\',\'stop\');">Stop</button>'+
            '<button onclick="docmd(\'' +winfo["name"]+
            '\',\'parse\');">Parse</button>'+
            '<button onclick="docmd(\'' +winfo["name"]+
            '\',\'delete\');">Delete</button>'+
            (isparsed 
                ? 
                  '<button onclick="doexplore({\'wlnames\' : [\'' +
                    winfo["name"] + '\']}, \'customview\');">Custom Plot</button>' + 
                  '<button onclick="doexplore({\'wlnames\' : [\'' +
                    winfo["name"] + '\']}, \'splunkview\');">Splunk View</button>'
                : '')
                +'</td>'+
            '</tr>'
                table.append(wlinfo);
        });
        if (hglass == true)
            $(".hourglass").hide();
    });
}

function doexplore(wlparms, cmd)
{
    window.open('/workloads/' + cmd + '?' + serialize(wlparms), '_blank');
}

function docmd(wlname,cmd)
{
    wload_process({ "wlnames" : wlname }, cmd);   
  
}  

function wload_process(wlparms, cmd)
{
    $(".hourglass").show();
    console.log('cmd = ' + cmd + ', parms = ' + wlparms);
    var $consolediv = $('#console');
 //alert("Workload name:-> " +wlname +" " +"Running:->"+runstatus);
    $.getJSON('/workloads/'+cmd+'?' + serialize(wlparms), function(data){
        $('#wload_table').empty();
        var $resp = "Response for " + cmd + ":<p>\n";;
        $.each(data, function(ind, wload) {
            $resp += wload.wlname + ": " + wload.status + "<br>\n";
        });
        $consolediv.html($resp);
        $(".hourglass").hide();
        setTimeout(function(){
            getwloads(true)
        },1000)
    });
}

function get_selwloads()
{
    var selwloads = [];
    $('#wltable').find('input[type="checkbox"]:checked').each(function(){
        /*
        var row = $(this).parent().parent();
        var rowcells = row.find('td');
        var wlname = $(rowcells[1]).text();
        */
        var wlname = $(this).val();
        selwloads.push(wlname);
    });
    var wlparms = { "wlnames" : selwloads };
    console.log(wlparms);
    return wlparms;
}

/*function getfiles_csv()
{
    var $select = $('#files');
    var myform = document.forms["plot_parms"];
    var pattern = myform.elements['file_pattern'].value;
    // console.log("user");

    $.getJSON('/listfiles?pattern='+pattern, function(data){
        $select.html('');
        // console.log('list is ' + data);

        $.each(data, function(key, val){
            // console.log('element is ' + val);
            $select.append('<option id=' + key + '>'+ val +'</option>');
            })
    });
}*/
