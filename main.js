/*const logBtn = document.getElementById('onSubmit');
logBtn.addEventListener('click', fetchData);

async function fetchData() {

    const response = await fetch('http://localhost:3000/users/');
    const data = await response.json();

    data.forEach(obj => {
        Object.entries(obj).forEach(([key, value]) => {
            console.log(`${key} ${value}`);
        });
        console.log('-------------------');
    });
}
*/
/*

var p1 = 'Naman';
async function fetchData() {

    const response = await fetch('http://localhost:3000/users/');
    const data = await response.json();
    console.log("hi");
    data.forEach(obj => {
            if(obj.username ==p1)
            console.log(obj.news);
        });
    
}

function validateForm() {
                var x = 'Naman';
                fetchData(x);
                console.log(x);        
            }
*/
//SHRUTI DEBUG
//document.getElementById('business').style.display = "block";
const logBtn = document.getElementById('onSubmit');
logBtn.addEventListener('click', fetchData);
    
async function fetchData() {

    let x = document.forms["myForm"]["fname"].value;
    let y = document.forms["myForm"]["password"].value;
    const response = await fetch('http://localhost:3000/users/');
    const data = await response.json();
    var flag =10;
    data.forEach(obj => {
        Object.entries(obj).forEach(([key, value]) => {
            if(obj.username == x&& obj.password == y)
            {
                flag = 0;
                var p= obj.news;
                        document.getElementById(p[0]).style.display = "block";
                        document.getElementById(p[1]).style.display = "block";
                        document.getElementById(p[2]).style.display = "block";
                        $('#myModal').modal('hide');
                        window.localStorage.setItem('profile', JSON.stringify(obj));
            }
        });
        
    });
    if(flag!=0)
        console.log('-------No password/id------------');
    else if(flag == 0||p!=null)
    {
            document.getElementById('logMod').style.display = "none";
            document.getElementById('accMod').style.display = "block"; 
            document.getElementById('name').innerHTML =p.username+" "+p.news+"</br>";
    }
}
    var p = window.localStorage.getItem('profile');
            p = JSON.parse(p);
            var p1 = p.news;
            console.log(p1);
            document.getElementById(p1[0]).style.display = "block";
            document.getElementById(p1[1]).style.display = "block";
            document.getElementById(p1[2]).style.display = "block";




    const item = localStorage.getItem('profile');

    if(item){
            document.getElementById('logMod').style.display = "none";
            document.getElementById('accMod').style.display = "block"; 
            document.getElementById('name').innerHTML ="News Interested: INDIA INTERNATIONAL SPORTS";
    }
    else
    {
        console.log('Name is not found');
    }

    if(window.localStorage())
    {
            console.log("printing?")
            document.getElementById('logMod').style.display = "none";
            document.getElementById('accMod').style.display = "block"; 
            document.getElementById('name').innerHTML ="News Interested: INDIA INTERNATIONAL SPORTS";
    }