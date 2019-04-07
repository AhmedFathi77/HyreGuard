
let login_button = document.getElementById("login_button");
login_button.addEventListener('click',()=>{
    login_button.style.backgroundColor = '#ff5500';
    login_button.style.boxShadow = '0 2px 2px 0 rgba(255, 119, 68,.14),0 3px 1px -2px rgba(255, 119, 68,.2),0 1px 5px 0 rgba(0,0,0,.12)';
    login_button.style.border = '1px solid  #ff5500';
});
login_button.addEventListener('focus',()=>{
    login_button.style.backgroundColor = '#ff5500';
    login_button.style.boxShadow = '0 2px 2px 0 rgba(255, 119, 68,.14),0 3px 1px -2px rgba(255, 119, 68,.2),0 1px 5px 0 rgba(0,0,0,.12)';
    login_button.style.border = '1px solid  #ff5500';
});
console.log('Hello');