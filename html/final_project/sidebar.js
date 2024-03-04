const burger = document.querySelector(".burger");
const sidebar = document.querySelector(".sidebar");


const openMenu = () => {
    burger.classList.toggle("active");
    sidebar.classList.toggle("active");
};

burger.addEventListener("click", openMenu);