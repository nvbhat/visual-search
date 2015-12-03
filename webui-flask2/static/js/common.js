function serialize(obj){
    var k = Object.keys(obj);
    var s = "";
    for(var i=0;i<k.length;i++) {
        s += k[i] + "=" + encodeURIComponent(obj[k[i]]);
        if (i != k.length -1) s += "&";
    }
    return s;
};

function get_formparms(formname)
{
    var form_parms = {};
    var myform = document.forms[formname];

    for (i=0; i < myform.elements.length; i++) {
        if (myform.elements[i].type == 'select-multiple') {
            var name = myform.elements[i].name;
            var $select = $('#' + name);
            form_parms[name] = $select.val();
        }
        else if (myform.elements[i].type != 'button')
            form_parms[myform.elements[i].name] = myform.elements[i].value;
    }
    return form_parms;
}
