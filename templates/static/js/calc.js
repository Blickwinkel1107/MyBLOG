function getId(id_str) {
    return document.getElementById(id_str);
}
function int(id_str) {
    return parseInt(getId(id_str).value);
}
function add(id1, id2) {
    if(getId(id1).value == null) {
        getId(id1).value = 0
    }
    if(getId(id2).value == null) {
        getId(id2).value = 0
    }
    let a = int(id1), b = int(id2);
    let res;
    switch(getId("ops").value) {
        case "+": res = a + b; break;
        case "-": res = a - b; break;
        case "*": res = a * b; break;
        case "/": res = a / b; break;
        default: res = 0;
    }
    getId("res").value = res;
}
