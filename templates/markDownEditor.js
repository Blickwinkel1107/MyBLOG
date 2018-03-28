function showMdEditor(){
    let opened = document.getElementById('mdeditor').style.display;
    if(opened === 'none'){
        document.getElementById('mdeditor').style.display = 'block';
        editormd("test-editormd", {
        width   : "100%",
        height  : 640,
        syncScrolling : "both",
        //你的lib目录的路径，我这边用JSP做测试的
        path    : "static/editor.md-master/lib/",
        //这个配置在simple.html中并没有，但是为了能够提交表单，使用这个配置可以让构造出来的HTML代码直接在第二个隐藏的textarea域中，方便post提交表单。
        saveHTMLToTextarea : true
    });
    }
    else{
        document.getElementById('mdeditor').style.display = 'none';
        delete editormd("test-editormd");
    }
}