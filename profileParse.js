var p = window.localStorage.getItem('profile');
            p = JSON.parse(p);
            var p1 = p.news;
            console.log(p1);
            document.getElementById(p1[0]).style.display = "block";
            document.getElementById(p1[1]).style.display = "block";
            document.getElementById(p1[2]).style.display = "block";

    var butt = document.getElementById('alert');

    function alerting(){
const item = localStorage.getItem('profile');

    if(item){
        console.log(item);
        var item1 = JSON.parse(item);
        console.log(item1.username);
        window.alert("Logged in as: "+item1.username+" "+item1.news+"</br>");
    }
    else
    {
        window.alert('Name is not found');
    }

}