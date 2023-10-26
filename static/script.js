
        // const usersData = [
        //     { username: "Manhani", password: "nanami" },
        //     { username: "LEHpex", password: "felipe" },
        //     { username: "wiu", password: "wiu" }
        // ];

        // document.getElementById("login-button").addEventListener("click", function() {
        //     logar();
        // });

        // document.getElementById("password").addEventListener("keydown", function(event) {
        //     if (event.key === "Enter") {
        //         logar();
        //     }
        // });

        // function logar() {
        //     const username = document.getElementById("username").value;
        //     const password = document.getElementById("password").value;

        //     const user = usersData.find(user => user.username === username && user.password === password);

        //     if (user) {
        //         alert("Login bem-sucedido!");
        //         window.location.href = "dashboardhome";
        //     } else {
        //         alert("Usuário ou senha incorretos. Tente novamente.");
        //     }
        // }


            const menuMobile = document.querySelector('.menu-mobile')
            const body = document.querySelector('body')
            const header = document.querySelector('.header-div')

            menuMobile.addEventListener('click', () => {
                menuMobile.classList.contains("bi-list")
                ? menuMobile.classList.replace("bi-list", "bi-x")
                : menuMobile.classList.replace("bi-x", "bi-list");
                body.classList.toggle("menu-nav-active")
                /*header.classList.contains("header-div")
                ? header.classList.replace("header-div", "header-div2")
                : header.classList.replace("header-div2", "header-div"); */
            })
