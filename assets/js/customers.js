let profilepic = document.querySelectorAll(".profilepic");
const name = document.querySelectorAll(".dbname");
var i = 0;
profilepic.forEach((pic)=>{
    pic.innerText = name[i].innerText.slice(6, 7);
    i++;
})