---
layout: post
title:  "토스트 알림"
date:   2023-12-14 11:31:00 +0900
categories: Sample&nbsp;Codes&nbsp;(JavaScript)
---

<!-- toast alram -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/toastr.css" integrity="sha512-3pIirOrwegjM6erE5gPSwkUzO+3cTjpnV9lexlNZqvupR64iZBnOOTiiLPb9M36zpMScbmUNIcHUqKD47M719g==" crossorigin="anonymous" referrerpolicy="no-referrer" />
<script src="https://cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/toastr.min.js" integrity="sha512-VEd+nq25CkR676O+pLBnDW09R7VQX9Mdiij052gVCp5yVH3jGtH70Ho/UUv4mJDsEdTvqRCFZg0NKGiojGnUCw==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<style>
    #toastrList{
        width: 80%;
        height: 35px;
        display: flex;
        justify-content: space-around;
        align-items: center;
        margin: 0 auto;
    }
    #toastrList>button{
        width: 24%;
        height: 30px;
    }
    #toastrList>button#toast_succeess{
        background-color: #74B574;
    }
    #toastrList>button#toast_info{
        background-color: #59ABC3;
    }
    #toastrList>button#toast_warning{
        background-color: #F89406;
    }
    #toastrList>button#toast_error{
        background-color: #BC3932;
    }
</style>

### 환경 설정


{% highlight xml %}
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/toastr.css" 
integrity="sha512-3pIirOrwegjM6erE5gPSwkUzO+3cTjpnV9lexlNZqvupR64iZBnOOTiiLPb9M36zpMScbmUNIcHUqKD47M719g==" 
crossorigin="anonymous" referrerpolicy="no-referrer" />

<script src="https://cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/toastr.min.js" 
integrity="sha512-VEd+nq25CkR676O+pLBnDW09R7VQX9Mdiij052gVCp5yVH3jGtH70Ho/UUv4mJDsEdTvqRCFZg0NKGiojGnUCw==" 
crossorigin="anonymous" referrerpolicy="no-referrer"></script>
{% endhighlight %}

### 사용 방법

- 기본 형식 : toastr.메소드명(제목, 내용, 옵션);
- 제목 생략 후 내용만 입력할 수도 있다.

{% highlight javascript %}
function toast_succeess(){
    toastr.success('toast_succeess');
}
function toast_info(){
    toastr.info('toast_info');
}
function toast_warning(){
    toastr.warning('toast_warning');
}
function toast_error(){
    toastr.error('toast_error');
}
{% endhighlight %}

<div id="toastrList">
    <button id="toast_succeess" onclick="toast_succeess()">succeess</button>
    <button id="toast_info" onclick="toast_info()">info</button>
    <button id="toast_warning" onclick="toast_warning()">warning</button>
    <button id="toast_error" onclick="toast_error()">error</button>
</div>

### 옵션 설정

{% highlight javascript %}
toastr.options = {
    "closeButton": false,
    "debug": false,
    "newestOnTop": false,
    "progressBar": true,
    "positionClass": "toast-top-right",
    "preventDuplicates": false,
    "onclick": null,
    "showDuration": "100",
    "hideDuration": "1000",
    "timeOut": "1500",
    "extendedTimeOut": "1000",
    "showEasing": "swing",
    "hideEasing": "linear",
    "showMethod": "fadeIn",
    "hideMethod": "fadeOut"
}
{% endhighlight %}

<script>
    function toast_succeess(){
        toastr.success('toast_succeess');
    }
    function toast_info(){
        toastr.info('toast_info');
    }
    function toast_warning(){
        toastr.warning('toast_warning');
    }
    function toast_error(){
        toastr.error('toast_error');
    }

    toastr.options = {
        "closeButton": true,
        "debug": false,
        "newestOnTop": false,
        "progressBar": true,
        "positionClass": "toast-top-right",
        "preventDuplicates": false,
        "onclick": null,
        "showDuration": "100",
        "hideDuration": "1000",
        "timeOut": "1500",
        "extendedTimeOut": "1000",
        "showEasing": "swing",
        "hideEasing": "linear",
        "showMethod": "fadeIn",
        "hideMethod": "fadeOut"
    }
</script>