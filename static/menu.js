/*$(document).ready(function() {
  $.get("/menu/menu.html", function(data) {
    $("#menu").html(data);
  });
});
*/
const menuMobile = document.querySelector('.menu-mobile')
const body = document.querySelector('body')

menuMobile.addEventListener('click', () => {
    menuMobile.classList.contains("bi-list")
    ? menuMobile.classList.replace("bi-list", "bi-x")
    : menuMobile.classList.replace("bi-x", "bi-list")
})




function checaCookie()
{
      alert("Cookies permitidos")
}

document.onload = checaCookie();